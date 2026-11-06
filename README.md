<div align="center">

# Pokopia Controller Icons <br>

[![license](https://img.shields.io/badge/license-MIT-EE1515?labelColor=222224)](LICENSE)
![pokopia](https://img.shields.io/badge/Pokopia-2.0.1a-EE1515?labelColor=222224)
![zip](https://img.shields.io/badge/ZIP-under%201%20MB-EE1515?labelColor=222224) <br>
![documentation](https://img.shields.io/badge/Documentation-222224)
[![english](https://img.shields.io/badge/-English-F0F0F0)](README.md)
[![português](https://img.shields.io/badge/-Português%20Brasileiro-F0F0F0)](README.br.md)

PlayStation, Xbox, Steam Deck and keyboard icons for Pokémon Pokopia! <br>
The mod only changes the texture it needs, doesn't recompress it and keeps the original quality <br>
It swaps 27 Switch icons in the menus and prompts, drawn in the game's own style :)

<img src="icons/playstation/b.png" width="48" alt="Cross">
<img src="icons/playstation/a.png" width="48" alt="Circle">
<img src="icons/playstation/y.png" width="48" alt="Square">
<img src="icons/playstation/x.png" width="48" alt="Triangle">
<img src="icons/xbox/b.png" width="48" alt="A">
<img src="icons/xbox/a.png" width="48" alt="B">
<img src="icons/xbox/y.png" width="48" alt="X">
<img src="icons/xbox/x.png" width="48" alt="Y">
<img src="icons/keyboard/b.png" width="48" alt="X">
<img src="icons/keyboard/a.png" width="48" alt="C">
<img src="icons/keyboard/y.png" width="48" alt="Z">
<img src="icons/keyboard/x.png" width="48" alt="V">
<img src="icons/keyboard-mouse/rs.png" width="48" alt="Mouse">

</div>
<br>

## Installation (or switching layouts)

### ZIP (recommended)

1. Download the ZIP for your controller, or the keyboard one (no need to extract it)

   | Controller | ZIP |
   | --- | --- |
   | DualSense, DualSense Edge, DualShock 4 | [PlayStation](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-playstation-icons.zip) |
   | Xbox, ROG Ally and others with A at the bottom | [Xbox](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-xbox-icons.zip) |
   | Steam Deck | [Steam Deck](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-steam-deck-icons.zip) |
   | Keyboard | [Keyboard](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-keyboard-icons.zip) |
   | Keyboard and mouse | [Keyboard and mouse](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-keyboard-mouse-icons.zip) |

2. In the emulator, right-click the game and click `Configure Game`
3. In the `Add-Ons` tab, click `Import Mod from ZIP`, pick the file and click `OK` on the name it suggests
4. That's it, start the game :)

<details>
    <summary>
        <strong>I can't find a button you mentioned</strong>
    </summary>

On the emulator's main page, where your games are, right-click the game, click `Open Mod Data Location` and drag the `Controller Icons` folder from inside the ZIP you downloaded into the folder that opens.

</details>

### Manual

<details>
    <summary>
        <strong>See the steps</strong>
    </summary>

1. Get [Python 3.9](https://www.python.org/downloads/) or newer (if the installer asks, tick `Add python.exe to PATH`)
2. Download [this repo as a ZIP](https://github.com/dumpsabfuck/pokopia-controller-icons/archive/refs/heads/main.zip) and extract it
3. Close the game
4. Find the `KIDS_PLATFORM_OUNCE` folder from update 2.0.1a (the one with `root.rdb` and `0x00011c54.fdata`)
5. In the folder with `apply.py`, click the address bar, type `cmd` and press Enter
6. Run `apply.py` with your layout (`playstation`, `xbox`, `steam-deck`, `keyboard` or `keyboard-mouse`):

   ```bash
   python apply.py playstation "{GAME_FOLDER_PATH}\updates\655360\romfs\motor_asset_re\KIDS_PLATFORM_OUNCE" "{MODS_FOLDER_PATH}\Controller Icons"
   ```

   `{GAME_FOLDER_PATH}` is the game's folder, and `{MODS_FOLDER_PATH}` is the folder that opens with `Open Mod Data Location`.

   The structure should look something like this:

   ```
   📂 load
   └── 📂 0400A3A01EE4C000
       └── 📂 Controller Icons
           ├── 📂 romfs
           └── 📂 romfs_ext
   ```

7. That's it, start the game :)

</details>

## Uninstall

Right-click the game, click `Open Mod Data Location` and delete the `Controller Icons` folder.

## Icons

<details>
    <summary>
        <strong>See the PlayStation icons</strong>
    </summary>

| Switch button | Icon | Controller button |
| --- | --- | --- |
| A, B, X, Y | <img src="icons/playstation/a.png" width="48" alt="Circle"> <img src="icons/playstation/b.png" width="48" alt="Cross"> <img src="icons/playstation/x.png" width="48" alt="Triangle"> <img src="icons/playstation/y.png" width="48" alt="Square"> | Circle, cross, triangle, square |
| L, R | <img src="icons/playstation/l.png" width="48" alt="L1"> <img src="icons/playstation/r.png" width="48" alt="R1"> | L1, R1 |
| ZL, ZR | <img src="icons/playstation/zl.png" width="48" alt="L2"> <img src="icons/playstation/zr.png" width="48" alt="R2"> | L2, R2 |
| Left stick, right stick | <img src="icons/playstation/ls.png" width="48" alt="L"> <img src="icons/playstation/rs.png" width="48" alt="R"> | L, R |
| Stick clicks | <img src="icons/playstation/pushls.png" width="48" alt="L3"> <img src="icons/playstation/pushrs.png" width="48" alt="R3"> | L3, R3 |
| + | <img src="icons/playstation/plus.png" width="48" alt="Options"> | Options |
| − | <img src="icons/playstation/minus.png" width="48" alt="Create"> | Create |
| Capture | <img src="icons/playstation/capture.png" width="48" alt="Microphone"> | Microphone |
| Home | <img src="icons/playstation/home.png" width="48" alt="PS"> | PS |
| D-pad | <img src="icons/playstation/dpad.png" width="48" alt="D-pad"> <img src="icons/playstation/dpad_up.png" width="48" alt="Up"> <img src="icons/playstation/dpad_right.png" width="48" alt="Right"> <img src="icons/playstation/dpad_down.png" width="48" alt="Down"> <img src="icons/playstation/dpad_left.png" width="48" alt="Left"> <img src="icons/playstation/dpad_h.png" width="48" alt="Left and right"> <img src="icons/playstation/dpad_v.png" width="48" alt="Up and down"> | D-pad |
| Arrows | <img src="icons/playstation/up.png" width="48" alt="Up arrow"> <img src="icons/playstation/right.png" width="48" alt="Right arrow"> <img src="icons/playstation/down.png" width="48" alt="Down arrow"> <img src="icons/playstation/left.png" width="48" alt="Left arrow"> | D-pad arrows |

</details>

<details>
    <summary>
        <strong>See the Xbox icons</strong>
    </summary>

| Switch button | Icon | Controller button |
| --- | --- | --- |
| A, B, X, Y | <img src="icons/xbox/a.png" width="48" alt="B"> <img src="icons/xbox/b.png" width="48" alt="A"> <img src="icons/xbox/x.png" width="48" alt="Y"> <img src="icons/xbox/y.png" width="48" alt="X"> | B, A, Y, X |
| L, R | <img src="icons/xbox/l.png" width="48" alt="LB"> <img src="icons/xbox/r.png" width="48" alt="RB"> | LB, RB |
| ZL, ZR | <img src="icons/xbox/zl.png" width="48" alt="LT"> <img src="icons/xbox/zr.png" width="48" alt="RT"> | LT, RT |
| Left stick, right stick | <img src="icons/xbox/ls.png" width="48" alt="L"> <img src="icons/xbox/rs.png" width="48" alt="R"> | L, R |
| Stick clicks | <img src="icons/xbox/pushls.png" width="48" alt="LS"> <img src="icons/xbox/pushrs.png" width="48" alt="RS"> | LS, RS |
| + | <img src="icons/xbox/plus.png" width="48" alt="Menu"> | Menu |
| − | <img src="icons/xbox/minus.png" width="48" alt="View"> | View |
| Capture | <img src="icons/xbox/capture.png" width="48" alt="Share"> | Share |
| Home | <img src="icons/xbox/home.png" width="48" alt="House"> | Xbox button |
| D-pad | <img src="icons/xbox/dpad.png" width="48" alt="D-pad"> <img src="icons/xbox/dpad_up.png" width="48" alt="Up"> <img src="icons/xbox/dpad_right.png" width="48" alt="Right"> <img src="icons/xbox/dpad_down.png" width="48" alt="Down"> <img src="icons/xbox/dpad_left.png" width="48" alt="Left"> <img src="icons/xbox/dpad_h.png" width="48" alt="Left and right"> <img src="icons/xbox/dpad_v.png" width="48" alt="Up and down"> | D-pad |
| Arrows | <img src="icons/xbox/up.png" width="48" alt="Up arrow"> <img src="icons/xbox/right.png" width="48" alt="Right arrow"> <img src="icons/xbox/down.png" width="48" alt="Down arrow"> <img src="icons/xbox/left.png" width="48" alt="Left arrow"> | D-pad arrows |

</details>

<details>
    <summary>
        <strong>See the Steam Deck icons</strong>
    </summary>

| Switch button | Icon | Controller button |
| --- | --- | --- |
| A, B, X, Y | <img src="icons/steam-deck/a.png" width="48" alt="B"> <img src="icons/steam-deck/b.png" width="48" alt="A"> <img src="icons/steam-deck/x.png" width="48" alt="Y"> <img src="icons/steam-deck/y.png" width="48" alt="X"> | B, A, Y, X |
| L, R | <img src="icons/steam-deck/l.png" width="48" alt="L1"> <img src="icons/steam-deck/r.png" width="48" alt="R1"> | L1, R1 |
| ZL, ZR | <img src="icons/steam-deck/zl.png" width="48" alt="L2"> <img src="icons/steam-deck/zr.png" width="48" alt="R2"> | L2, R2 |
| Left stick, right stick | <img src="icons/steam-deck/ls.png" width="48" alt="L"> <img src="icons/steam-deck/rs.png" width="48" alt="R"> | L, R |
| Stick clicks | <img src="icons/steam-deck/pushls.png" width="48" alt="L3"> <img src="icons/steam-deck/pushrs.png" width="48" alt="R3"> | L3, R3 |
| + | <img src="icons/steam-deck/plus.png" width="48" alt="Menu"> | Menu |
| − | <img src="icons/steam-deck/minus.png" width="48" alt="View"> | View |
| Capture | <img src="icons/steam-deck/capture.png" width="48" alt="Three dots"> | `...` |
| Home | <img src="icons/steam-deck/home.png" width="48" alt="House"> | Steam button |
| D-pad | <img src="icons/steam-deck/dpad.png" width="48" alt="D-pad"> <img src="icons/steam-deck/dpad_up.png" width="48" alt="Up"> <img src="icons/steam-deck/dpad_right.png" width="48" alt="Right"> <img src="icons/steam-deck/dpad_down.png" width="48" alt="Down"> <img src="icons/steam-deck/dpad_left.png" width="48" alt="Left"> <img src="icons/steam-deck/dpad_h.png" width="48" alt="Left and right"> <img src="icons/steam-deck/dpad_v.png" width="48" alt="Up and down"> | D-pad |
| Arrows | <img src="icons/steam-deck/up.png" width="48" alt="Up arrow"> <img src="icons/steam-deck/right.png" width="48" alt="Right arrow"> <img src="icons/steam-deck/down.png" width="48" alt="Down arrow"> <img src="icons/steam-deck/left.png" width="48" alt="Left arrow"> | D-pad arrows |

</details>

<details>
    <summary>
        <strong>See the keyboard icons</strong>
    </summary>

| Switch button | Icon | Key |
| --- | --- | --- |
| A, B, X, Y | <img src="icons/keyboard/a.png" width="48" alt="C"> <img src="icons/keyboard/b.png" width="48" alt="X"> <img src="icons/keyboard/x.png" width="48" alt="V"> <img src="icons/keyboard/y.png" width="48" alt="Z"> | C, X, V, Z |
| L, R | <img src="icons/keyboard/l.png" width="48" alt="Q"> <img src="icons/keyboard/r.png" width="48" alt="E"> | Q, E |
| ZL, ZR | <img src="icons/keyboard/zl.png" width="48" alt="R"> <img src="icons/keyboard/zr.png" width="48" alt="T"> | R, T |
| Left stick, right stick | <img src="icons/keyboard/ls.png" width="48" alt="WASD"> <img src="icons/keyboard/rs.png" width="48" alt="IJKL"> | WASD, IJKL |
| Stick clicks | <img src="icons/keyboard/pushls.png" width="48" alt="F"> <img src="icons/keyboard/pushrs.png" width="48" alt="G"> | F, G |
| + | <img src="icons/keyboard/plus.png" width="48" alt="M"> | M |
| − | <img src="icons/keyboard/minus.png" width="48" alt="N"> | N |
| Capture | <img src="icons/keyboard/capture.png" width="48" alt="Camera"> | No default key |
| Home | <img src="icons/keyboard/home.png" width="48" alt="House"> | No default key |
| D-pad | <img src="icons/keyboard/dpad.png" width="48" alt="Arrow keys"> <img src="icons/keyboard/dpad_up.png" width="48" alt="Up"> <img src="icons/keyboard/dpad_right.png" width="48" alt="Right"> <img src="icons/keyboard/dpad_down.png" width="48" alt="Down"> <img src="icons/keyboard/dpad_left.png" width="48" alt="Left"> <img src="icons/keyboard/dpad_h.png" width="48" alt="Left and right"> <img src="icons/keyboard/dpad_v.png" width="48" alt="Up and down"> | Arrow keys |
| Arrows | <img src="icons/keyboard/up.png" width="48" alt="Up arrow"> <img src="icons/keyboard/right.png" width="48" alt="Right arrow"> <img src="icons/keyboard/down.png" width="48" alt="Down arrow"> <img src="icons/keyboard/left.png" width="48" alt="Left arrow"> | Arrow keys |

</details>

<details>
    <summary>
        <strong>See the keyboard and mouse icons</strong>
    </summary>

Same as the keyboard, but the right stick becomes the mouse: <img src="icons/keyboard-mouse/rs.png" width="48" alt="Mouse">

</details>

## FAQ

<details>
    <summary>
        <strong>Why didn't the A button on the title screen change?</strong>
    </summary>

That's a texture this mod doesn't change.

</details>

<details>
    <summary>
        <strong>Does it work with the PT-BR translation?</strong>
    </summary>

Yes. I tested it with [translation 2.5.4](https://github.com/LucianoNeo/pokemon-pokopia-pt-br), and without it too.

</details>

<details>
    <summary>
        <strong>I rebound my buttons and some icons don't match</strong>
    </summary>

The icons follow the emulator's default binding, so they won't match if you rebind your buttons or keys.

</details>

<details>
    <summary>
        <strong>How do I change an icon?</strong>
    </summary>

All the icons are in the `icons` folder. Every icon is an 84x84 PNG. Edit what you want and rebuild the patches.

To rebuild the patches, you'll need Python 3.11 or newer:

```bash
pip install -r requirements.txt
python build.py
```

Then run `apply.py` as in the [manual installation](#manual).

</details>

<details>
    <summary>
        <strong>What's going on under the hood?</strong>
    </summary>

`root.rdb` says where each asset is: which `.fdata` (by its position in `root.rdx`) and where in it. The icons are in texture 18 of the G1T `0xBC2C37F5`, inside `0x00011c54.fdata`. Each file in `patches/` only has the BC7 blocks of the new icons, nothing from the game. Only the blocks under the icons change, and they stay in BC7, like the original.

`apply.py` reads the G1T from your copy, checks its SHA-256 and writes those blocks over it. Then it saves the result in a new `.fdata`, `0x0d5e1c05.fdata`, adds that file to a copy of `root.rdx` and writes a 23-byte IPS patch that points `root.rdb` there. The G1T has 62 textures and only the button atlas changes, so the new `.fdata` carries the other 61 along.

If you want to learn about this kind of mod, feel free to use this project as study material: `apply.py` and `build.py` are short, and each one explains the formats it uses at the top. `flip_gobs`, in `build.py`, also shows how Switch 2's texture layout differs from Switch 1's.

</details>

## Thanks

- [RDBExplorer](https://github.com/MrIkso/RDBExplorer), for the RDB and `.fdata` formats.
- [gust_tools](https://github.com/VitaSmith/gust_tools), for the G1T format.
- ns2-assets, for its notes on Switch 2 textures.
- [Inter](https://github.com/rsms/inter), the font of the button labels.
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:PlayStation_logo.svg), for the vector of the PS logo.

## Disclaimer

This is an independent project, with no ties to Nintendo, The Pokémon Company, Koei Tecmo, Sony, Microsoft, Valve or ASUS, and none of them back or sponsor it. The code in this repo has no game files, but the finished mod has modified copies of one game texture file and the game's `root.rdx`, and the game's art in it belongs to its rights holders. Pokémon and Pokopia are trademarks of their owners. PlayStation, DualSense, DualShock and the PS logo are trademarks of Sony Interactive Entertainment; Xbox of Microsoft; Steam Deck of Valve; and ROG Ally of ASUS. The [MIT license](LICENSE) covers the code and the icons, not those trademarks or the game's files.
