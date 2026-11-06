"""Build each layout's patch from its sprites in icons/, without reading any game file.

A patch is zlib over (offset, block) pairs: every block under a sprite, at its place in the game's G1T.

G1T: the game's texture file. The button atlas is its texture 18, stored swizzled.
BC7: the atlas's compression, which stores each 4x4 block of pixels in 16 bytes.
GOB: the 512-byte unit of Switch memory that swizzling arranges a texture into.
"""

import zlib
from pathlib import Path

from bc7enc import pack_dds
from PIL import Image
from pyswizzle import nsw_swizzle

from apply import LAYOUTS, PATCH_ENTRY, PATCHES_DIR

ICONS_DIR = Path(__file__).parent / "icons"

# Fixed, because apply.py only accepts one exact G1T.
ATLAS_START = 4451984
ATLAS_SIZE = (1024, 1024)
SPRITE_SIZE = 84
BLOCK_PIXELS = 4
BLOCK_BYTES = 16
SWIZZLE_MODE = 4
GOB_RUN_BYTES = 32

ATLAS_BLOCKS_PER_ROW = ATLAS_SIZE[0] // BLOCK_PIXELS
ATLAS_BYTES = ATLAS_SIZE[1] // BLOCK_PIXELS * ATLAS_BLOCKS_PER_ROW * BLOCK_BYTES
SPRITE_BLOCKS = SPRITE_SIZE // BLOCK_PIXELS

# Top-left corner of each sprite in the atlas, from the game's texinfo 0x987344AA.
# fmt: off
POSITIONS = {
    "a": (240, 336), "b": (928, 408), "x": (704, 596), "y": (0, 600),
    "l": (264, 508), "r": (528, 512), "zl": (88, 600), "zr": (176, 600),
    "ls": (440, 508), "rs": (856, 584), "pushls": (88, 512), "pushrs": (176, 512),
    "plus": (0, 512), "minus": (768, 508), "capture": (328, 420), "home": (884, 496),
    "dpad": (504, 420), "dpad_up": (592, 424), "dpad_down": (796, 420),
    "dpad_left": (88, 424), "dpad_right": (176, 424), "dpad_h": (0, 424), "dpad_v": (680, 424),
    "up": (440, 596), "down": (416, 420), "left": (352, 508), "right": (616, 512),
}
# fmt: on


def flip_gobs(data: bytes) -> bytes:
    """Swap the middle two of every four 32-byte runs, the Switch 2 change to the Switch 1 GOB layout."""

    flipped = bytearray(data)
    for start in range(0, len(data), 4 * GOB_RUN_BYTES):
        second = start + GOB_RUN_BYTES
        third = second + GOB_RUN_BYTES
        flipped[second:third] = data[third : third + GOB_RUN_BYTES]
        flipped[third : third + GOB_RUN_BYTES] = data[second:third]

    return bytes(flipped)


def swizzle(blocks: bytes) -> bytes:
    """Return the atlas's blocks in the order the G1T stores them."""

    return flip_gobs(nsw_swizzle(blocks, ATLAS_SIZE, (BLOCK_PIXELS, BLOCK_PIXELS), BLOCK_BYTES, SWIZZLE_MODE))


def encode_atlas(icons_dir: Path) -> bytes:
    atlas = Image.new("RGBA", ATLAS_SIZE)
    for name, position in POSITIONS.items():
        atlas.paste(Image.open(icons_dir / f"{name}.png"), position)

    return pack_dds(atlas.tobytes(), *ATLAS_SIZE, "BC7")


def sprite_mask() -> bytes:
    """Return an atlas-sized buffer set only on the blocks under the sprites."""

    mask = bytearray(ATLAS_BYTES)
    row_bytes = SPRITE_BLOCKS * BLOCK_BYTES
    for x, y in POSITIONS.values():
        first_row = y // BLOCK_PIXELS
        first_column = x // BLOCK_PIXELS
        for row in range(first_row, first_row + SPRITE_BLOCKS):
            start = (row * ATLAS_BLOCKS_PER_ROW + first_column) * BLOCK_BYTES
            mask[start : start + row_bytes] = b"\xff" * row_bytes

    return bytes(mask)


def build_patch(layout: str, mask: bytes) -> None:
    blocks = swizzle(encode_atlas(ICONS_DIR / layout))
    entries = [
        PATCH_ENTRY.pack(ATLAS_START + offset, blocks[offset : offset + BLOCK_BYTES])
        for offset in range(0, ATLAS_BYTES, BLOCK_BYTES)
        if mask[offset]
    ]
    patch_path = PATCHES_DIR / f"{layout}.patch"
    patch_path.write_bytes(zlib.compress(b"".join(entries), zlib.Z_BEST_COMPRESSION))
    print(f"{patch_path.name}: {len(entries)} blocks")


def main() -> None:
    PATCHES_DIR.mkdir(exist_ok=True)
    mask = swizzle(sprite_mask())
    for layout in LAYOUTS:
        build_patch(layout, mask)


if __name__ == "__main__":
    main()
