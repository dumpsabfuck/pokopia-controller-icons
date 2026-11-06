"""Write the controller icons mod from your own copy of Pokopia 2.0.1a.

The game folder is only read. The output folder is a LayeredFS mod with three files: a new fdata holding the patched
G1T, a root.rdx that also lists it, and an IPS patch that makes root.rdb point at it.

RDB: root.rdb, the index of the game's assets. Each entry holds an asset's KTID and where its data is.
RDX: root.rdx, the list of the game's fdata files, which the RDB refers to by position.
fdata: a 16-byte header, then many assets, each stored as one record.
IDRK: the record format: a header, parameters, then the asset's data, here in compressed chunks.
G1T: the texture file inside the record. The layout's patch overwrites some of its blocks.
"""

import argparse
import hashlib
import struct
import zlib
from pathlib import Path

KTID = 0xBC2C37F5
ORIGINAL_SHA256 = "c61d33d92ec280fd9eae4d70fbc27510a2120089fdf6c9a8df1b10c880d0a608"
FDATA = "0x00011c54.fdata"
FDATA_HEADER_SIZE = 16
RDX = "root.rdx"
ASSETS = Path("motor_asset_re", "KIDS_PLATFORM_OUNCE")
LAYOUTS = ("playstation", "xbox", "steam-deck", "keyboard")
PATCHES_DIR = Path(__file__).parent / "patches"
PATCH_ENTRY = struct.Struct("<I16s")
NOT_ORIGINAL = f"{FDATA}: texture {KTID:#x} is not the original from Pokopia 2.0.1a; restore the game's original files"

# Not used by the game. The name of the new fdata comes from it.
MOD_FDATA_ID = 0x0D5E1C05
MOD_FDATA = f"{MOD_FDATA_ID:#010x}.fdata"

ENTRY_KTID_OFFSET = 36
ENTRY_SIZES = struct.Struct("<8xqq")
LOCATION_RECORD_OFFSET = 2
# Where a record is: its offset, its size, and the position in root.rdx of its fdata.
LOCATION_RECORD = struct.Struct("<IIH")

# RDX entry: position, mount point (255 is the main folder), a byte that is always 255, and the ID that names the file.
RDX_ENTRY = struct.Struct("<HBBI")
RDX_MAIN_FOLDER = 255
RDX_RESERVED = 255

# IDRK header, 56 bytes: 0 magic, 8 record size, 16 stored size, 24 raw size, 32 param size, 44 flags, 48 CRC32 of the
# stored data, 52 param count.
RECORD_HEADER = struct.Struct("<24xqi16xi")
RECORD_SIZES_OFFSET = 8
RECORD_FLAGS_OFFSET = 44
RECORD_CRC_OFFSET = 48
COMPRESSION_MASK = 0x3F << 20
PARAM_ENTRY_SIZE = 12
CHUNK_PREFIX_SIZE = 10


def read_record(game_dir: Path) -> tuple[int, bytes]:
    """Return the offset in root.rdb of the texture's location block, and the record it points at."""

    rdb = (game_dir / "root.rdb").read_bytes()

    # A false hit only reads the wrong bytes, and those fail the hash check before anything is written.
    entry = rdb.index(KTID.to_bytes(4, "little")) - ENTRY_KTID_OFFSET
    entry_size, location_size = ENTRY_SIZES.unpack_from(rdb, entry)
    location = entry + entry_size - location_size
    record_offset, record_size, _ = LOCATION_RECORD.unpack_from(rdb, location + LOCATION_RECORD_OFFSET)
    with (game_dir / FDATA).open("rb") as file:
        file.seek(record_offset)
        return location, file.read(record_size)


def decompress_chunks(packed: bytes, raw_size: int) -> bytearray:
    """Decompress zlib chunks, each after a 10-byte prefix starting with its size."""

    result = bytearray()
    position = 0
    while len(result) < raw_size:
        chunk_size = struct.unpack_from("<H", packed, position)[0]
        chunk_start = position + CHUNK_PREFIX_SIZE
        result += zlib.decompress(packed[chunk_start : chunk_start + chunk_size])
        position = chunk_start + chunk_size

    return result


def read_texture(game_dir: Path) -> tuple[int, bytes, bytearray]:
    """Return the location offset, the record's header and params, and the G1T; refuse anything but the original."""

    try:
        location, record = read_record(game_dir)
        raw_size, param_size, param_count = RECORD_HEADER.unpack_from(record)
        params_end = RECORD_HEADER.size + param_count * PARAM_ENTRY_SIZE + param_size
        g1t = decompress_chunks(record[params_end:], raw_size)
    except (struct.error, zlib.error, ValueError, OverflowError) as error:
        raise ValueError(NOT_ORIGINAL) from error

    if hashlib.sha256(g1t).hexdigest() != ORIGINAL_SHA256:
        raise ValueError(NOT_ORIGINAL)

    return location, record[:params_end], g1t


def apply_patch(g1t: bytearray, layout: str) -> None:
    patch = zlib.decompress((PATCHES_DIR / f"{layout}.patch").read_bytes())
    for offset, block in PATCH_ENTRY.iter_unpack(patch):
        g1t[offset : offset + len(block)] = block


def build_record(header_and_params: bytes, g1t: bytearray) -> bytearray:
    # Stored uncompressed: type 4 can't be written back, because the other 8 bytes of each chunk prefix are unknown.
    # The game accepts type 0 for this record.
    record = bytearray(header_and_params) + g1t
    struct.pack_into("<qqq", record, RECORD_SIZES_OFFSET, len(record), len(g1t), len(g1t))
    flags = struct.unpack_from("<I", record, RECORD_FLAGS_OFFSET)[0]
    struct.pack_into("<I", record, RECORD_FLAGS_OFFSET, flags & ~COMPRESSION_MASK)
    struct.pack_into("<I", record, RECORD_CRC_OFFSET, zlib.crc32(g1t))
    return record


def build_ips(offset: int, data: bytes) -> bytes:
    """Return an IPS patch with one record writing `data` at `offset`."""

    return b"PATCH" + offset.to_bytes(3, "big") + len(data).to_bytes(2, "big") + data + b"EOF"


def write_mod(game_dir: Path, out_dir: Path, location: int, record: bytes) -> None:
    with (game_dir / FDATA).open("rb") as file:
        fdata_header = file.read(FDATA_HEADER_SIZE)

    rdx = (game_dir / RDX).read_bytes()
    mod_fdata_position = len(rdx) // RDX_ENTRY.size

    assets_dir = out_dir / "romfs" / ASSETS
    assets_dir.mkdir(parents=True, exist_ok=True)
    (assets_dir / MOD_FDATA).write_bytes(fdata_header + record)
    mod_entry = RDX_ENTRY.pack(mod_fdata_position, RDX_MAIN_FOLDER, RDX_RESERVED, MOD_FDATA_ID)
    (assets_dir / RDX).write_bytes(rdx + mod_entry)

    # Patched, not replaced, so the mod works alongside a translation that changes root.rdb.
    ips_path = out_dir / "romfs_ext" / ASSETS / "root.rdb.ips"
    ips_path.parent.mkdir(parents=True, exist_ok=True)
    location_record = LOCATION_RECORD.pack(FDATA_HEADER_SIZE, len(record), mod_fdata_position)
    ips_path.write_bytes(build_ips(location + LOCATION_RECORD_OFFSET, location_record))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("layout", choices=LAYOUTS, help="the controller layout to install")
    parser.add_argument("game_dir", type=Path, help="the KIDS_PLATFORM_OUNCE folder of update 2.0.1a")
    parser.add_argument("out_dir", type=Path, help="the folder to write the mod in")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        location, header_and_params, g1t = read_texture(args.game_dir)
        apply_patch(g1t, args.layout)
        write_mod(args.game_dir, args.out_dir, location, build_record(header_and_params, g1t))
    except (OSError, ValueError, zlib.error) as error:
        raise SystemExit(f"apply: {error}") from error

    print(f"wrote {args.out_dir.resolve()}")


if __name__ == "__main__":
    main()
