<div align="center">

# Pokopia Controller Icons <br>

[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
![pokopia](https://img.shields.io/badge/Pokopia-2.0.1a-292929)
![zip](https://img.shields.io/badge/ZIP-menos%20de%201%20MB-blue) <br>
![documentation](https://img.shields.io/badge/Documentation-gray)
[![english](https://img.shields.io/badge/-English-blue)](README.md)
[![português](https://img.shields.io/badge/-Português%20Brasileiro-blue)](README.br.md)

Troque os ícones do Switch pelos de PlayStation, Xbox, Steam Deck ou teclado no Pokémon Pokopia! <br>
O mod modifica apenas a textura necessária, sem recomprimir e mantendo a qualidade original <br>
São 27 ícones nos menus e avisos, desenhados no estilo do próprio jogo :)

<img src="icons/playstation/b.png" width="48" alt="Cruz">
<img src="icons/playstation/a.png" width="48" alt="Círculo">
<img src="icons/playstation/y.png" width="48" alt="Quadrado">
<img src="icons/playstation/x.png" width="48" alt="Triângulo">
<img src="icons/xbox/b.png" width="48" alt="A">
<img src="icons/xbox/a.png" width="48" alt="B">
<img src="icons/xbox/y.png" width="48" alt="X">
<img src="icons/xbox/x.png" width="48" alt="Y">
<img src="icons/keyboard/b.png" width="48" alt="X">
<img src="icons/keyboard/a.png" width="48" alt="C">
<img src="icons/keyboard/y.png" width="48" alt="Z">
<img src="icons/keyboard/x.png" width="48" alt="V">

</div>
<br>

## Instalação (ou troca de layout)

### ZIP (recomendado)

1. Baixe o ZIP do seu controle, ou o de teclado (não precisa extrair)

   | Controle | ZIP |
   | --- | --- |
   | DualSense, DualSense Edge, DualShock 4 | [PlayStation](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-playstation-icons.zip) |
   | Xbox, ROG Ally e outros com o A embaixo | [Xbox](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-xbox-icons.zip) |
   | Steam Deck | [Steam Deck](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-steam-deck-icons.zip) |
   | Teclado | [Teclado](https://github.com/dumpsabfuck/pokopia-controller-icons/releases/latest/download/pokopia-keyboard-icons.zip) |

2. No emulador, clique com o botão direito no jogo e depois em `Configure Game`
3. Na aba `Add-Ons`, clique em `Import Mod from ZIP`, escolha o arquivo e dê `OK` no nome que aparecer
4. Agora é só abrir o jogo :)

<details>
    <summary>
        <strong>Não encontrei um botão que você citou</strong>
    </summary>

Na página inicial do emulador, onde tem os jogos, clique com o botão direito no jogo, depois em `Open Mod Data Location`, e arraste a pasta `Controller Icons` de dentro do ZIP que você baixou pra pasta que abrir.

</details>

### Manual

<details>
    <summary>
        <strong>Ver o passo a passo</strong>
    </summary>

1. Instale o [Python 3.9](https://www.python.org/downloads/) ou mais novo (se o instalador perguntar, marque `Add python.exe to PATH`)
2. Baixe [este repositório em ZIP](https://github.com/dumpsabfuck/pokopia-controller-icons/archive/refs/heads/main.zip) e extraia os arquivos
3. Feche o jogo
4. Ache a pasta `KIDS_PLATFORM_OUNCE` do update 2.0.1a (onde ficam o `root.rdb` e o `0x00011c54.fdata`)
5. Na pasta onde está o `apply.py`, clique na barra de endereço, digite `cmd` e aperte Enter
6. Rode o `apply.py` com o seu layout (`playstation`, `xbox`, `steam-deck` ou `keyboard`):

   ```bash
   python apply.py playstation "{GAME_FOLDER_PATH}\updates\655360\romfs\motor_asset_re\KIDS_PLATFORM_OUNCE" "{MODS_FOLDER_PATH}\Controller Icons"
   ```

   `{GAME_FOLDER_PATH}` é a pasta do jogo, e `{MODS_FOLDER_PATH}` é a pasta que abre no `Open Mod Data Location`.

   A estrutura deve ficar parecida com isso:

   ```
   📂 load
   └── 📂 0400A3A01EE4C000
       └── 📂 Controller Icons
           ├── 📂 romfs
           └── 📂 romfs_ext
   ```

7. Agora é só abrir o jogo :)

</details>

## Desinstalação

Clique com o botão direito no jogo, depois em `Open Mod Data Location`, e apague a pasta `Controller Icons`.

## Ícones

<details>
    <summary>
        <strong>Ver os ícones de PlayStation</strong>
    </summary>

| Botão do Switch | Ícone | Botão do controle |
| --- | --- | --- |
| A, B, X, Y | <img src="icons/playstation/a.png" width="48" alt="Círculo"> <img src="icons/playstation/b.png" width="48" alt="Cruz"> <img src="icons/playstation/x.png" width="48" alt="Triângulo"> <img src="icons/playstation/y.png" width="48" alt="Quadrado"> | Círculo, cruz, triângulo, quadrado |
| L, R | <img src="icons/playstation/l.png" width="48" alt="L1"> <img src="icons/playstation/r.png" width="48" alt="R1"> | L1, R1 |
| ZL, ZR | <img src="icons/playstation/zl.png" width="48" alt="L2"> <img src="icons/playstation/zr.png" width="48" alt="R2"> | L2, R2 |
| Analógico esquerdo, analógico direito | <img src="icons/playstation/ls.png" width="48" alt="L"> <img src="icons/playstation/rs.png" width="48" alt="R"> | L, R |
| Clique dos analógicos | <img src="icons/playstation/pushls.png" width="48" alt="L3"> <img src="icons/playstation/pushrs.png" width="48" alt="R3"> | L3, R3 |
| + | <img src="icons/playstation/plus.png" width="48" alt="Options"> | Options |
| − | <img src="icons/playstation/minus.png" width="48" alt="Create"> | Create |
| Capture | <img src="icons/playstation/capture.png" width="48" alt="Microfone"> | Microfone |
| Home | <img src="icons/playstation/home.png" width="48" alt="PS"> | PS |
| Direcional | <img src="icons/playstation/dpad.png" width="48" alt="Direcional"> <img src="icons/playstation/dpad_up.png" width="48" alt="Cima"> <img src="icons/playstation/dpad_right.png" width="48" alt="Direita"> <img src="icons/playstation/dpad_down.png" width="48" alt="Baixo"> <img src="icons/playstation/dpad_left.png" width="48" alt="Esquerda"> <img src="icons/playstation/dpad_h.png" width="48" alt="Esquerda e direita"> <img src="icons/playstation/dpad_v.png" width="48" alt="Cima e baixo"> | Direcional |
| Setas | <img src="icons/playstation/up.png" width="48" alt="Seta para cima"> <img src="icons/playstation/right.png" width="48" alt="Seta para a direita"> <img src="icons/playstation/down.png" width="48" alt="Seta para baixo"> <img src="icons/playstation/left.png" width="48" alt="Seta para a esquerda"> | Setas do direcional |

</details>

<details>
    <summary>
        <strong>Ver os ícones de Xbox</strong>
    </summary>

| Botão do Switch | Ícone | Botão do controle |
| --- | --- | --- |
| A, B, X, Y | <img src="icons/xbox/a.png" width="48" alt="B"> <img src="icons/xbox/b.png" width="48" alt="A"> <img src="icons/xbox/x.png" width="48" alt="Y"> <img src="icons/xbox/y.png" width="48" alt="X"> | B, A, Y, X |
| L, R | <img src="icons/xbox/l.png" width="48" alt="LB"> <img src="icons/xbox/r.png" width="48" alt="RB"> | LB, RB |
| ZL, ZR | <img src="icons/xbox/zl.png" width="48" alt="LT"> <img src="icons/xbox/zr.png" width="48" alt="RT"> | LT, RT |
| Analógico esquerdo, analógico direito | <img src="icons/xbox/ls.png" width="48" alt="L"> <img src="icons/xbox/rs.png" width="48" alt="R"> | L, R |
| Clique dos analógicos | <img src="icons/xbox/pushls.png" width="48" alt="LS"> <img src="icons/xbox/pushrs.png" width="48" alt="RS"> | LS, RS |
| + | <img src="icons/xbox/plus.png" width="48" alt="Menu"> | Menu |
| − | <img src="icons/xbox/minus.png" width="48" alt="View"> | View |
| Capture | <img src="icons/xbox/capture.png" width="48" alt="Share"> | Share |
| Home | <img src="icons/xbox/home.png" width="48" alt="Casa"> | Botão Xbox |
| Direcional | <img src="icons/xbox/dpad.png" width="48" alt="Direcional"> <img src="icons/xbox/dpad_up.png" width="48" alt="Cima"> <img src="icons/xbox/dpad_right.png" width="48" alt="Direita"> <img src="icons/xbox/dpad_down.png" width="48" alt="Baixo"> <img src="icons/xbox/dpad_left.png" width="48" alt="Esquerda"> <img src="icons/xbox/dpad_h.png" width="48" alt="Esquerda e direita"> <img src="icons/xbox/dpad_v.png" width="48" alt="Cima e baixo"> | Direcional |
| Setas | <img src="icons/xbox/up.png" width="48" alt="Seta para cima"> <img src="icons/xbox/right.png" width="48" alt="Seta para a direita"> <img src="icons/xbox/down.png" width="48" alt="Seta para baixo"> <img src="icons/xbox/left.png" width="48" alt="Seta para a esquerda"> | Setas do direcional |

</details>

<details>
    <summary>
        <strong>Ver os ícones de Steam Deck</strong>
    </summary>

| Botão do Switch | Ícone | Botão do controle |
| --- | --- | --- |
| A, B, X, Y | <img src="icons/steam-deck/a.png" width="48" alt="B"> <img src="icons/steam-deck/b.png" width="48" alt="A"> <img src="icons/steam-deck/x.png" width="48" alt="Y"> <img src="icons/steam-deck/y.png" width="48" alt="X"> | B, A, Y, X |
| L, R | <img src="icons/steam-deck/l.png" width="48" alt="L1"> <img src="icons/steam-deck/r.png" width="48" alt="R1"> | L1, R1 |
| ZL, ZR | <img src="icons/steam-deck/zl.png" width="48" alt="L2"> <img src="icons/steam-deck/zr.png" width="48" alt="R2"> | L2, R2 |
| Analógico esquerdo, analógico direito | <img src="icons/steam-deck/ls.png" width="48" alt="L"> <img src="icons/steam-deck/rs.png" width="48" alt="R"> | L, R |
| Clique dos analógicos | <img src="icons/steam-deck/pushls.png" width="48" alt="L3"> <img src="icons/steam-deck/pushrs.png" width="48" alt="R3"> | L3, R3 |
| + | <img src="icons/steam-deck/plus.png" width="48" alt="Menu"> | Menu |
| − | <img src="icons/steam-deck/minus.png" width="48" alt="View"> | View |
| Capture | <img src="icons/steam-deck/capture.png" width="48" alt="Três pontos"> | `...` |
| Home | <img src="icons/steam-deck/home.png" width="48" alt="Casa"> | Botão Steam |
| Direcional | <img src="icons/steam-deck/dpad.png" width="48" alt="Direcional"> <img src="icons/steam-deck/dpad_up.png" width="48" alt="Cima"> <img src="icons/steam-deck/dpad_right.png" width="48" alt="Direita"> <img src="icons/steam-deck/dpad_down.png" width="48" alt="Baixo"> <img src="icons/steam-deck/dpad_left.png" width="48" alt="Esquerda"> <img src="icons/steam-deck/dpad_h.png" width="48" alt="Esquerda e direita"> <img src="icons/steam-deck/dpad_v.png" width="48" alt="Cima e baixo"> | Direcional |
| Setas | <img src="icons/steam-deck/up.png" width="48" alt="Seta para cima"> <img src="icons/steam-deck/right.png" width="48" alt="Seta para a direita"> <img src="icons/steam-deck/down.png" width="48" alt="Seta para baixo"> <img src="icons/steam-deck/left.png" width="48" alt="Seta para a esquerda"> | Setas do direcional |

</details>

<details>
    <summary>
        <strong>Ver os ícones de teclado</strong>
    </summary>

| Botão do Switch | Ícone | Tecla |
| --- | --- | --- |
| A, B, X, Y | <img src="icons/keyboard/a.png" width="48" alt="C"> <img src="icons/keyboard/b.png" width="48" alt="X"> <img src="icons/keyboard/x.png" width="48" alt="V"> <img src="icons/keyboard/y.png" width="48" alt="Z"> | C, X, V, Z |
| L, R | <img src="icons/keyboard/l.png" width="48" alt="Q"> <img src="icons/keyboard/r.png" width="48" alt="E"> | Q, E |
| ZL, ZR | <img src="icons/keyboard/zl.png" width="48" alt="R"> <img src="icons/keyboard/zr.png" width="48" alt="T"> | R, T |
| Analógico esquerdo, analógico direito | <img src="icons/keyboard/ls.png" width="48" alt="WASD"> <img src="icons/keyboard/rs.png" width="48" alt="IJKL"> | WASD, IJKL |
| Clique dos analógicos | <img src="icons/keyboard/pushls.png" width="48" alt="F"> <img src="icons/keyboard/pushrs.png" width="48" alt="G"> | F, G |
| + | <img src="icons/keyboard/plus.png" width="48" alt="M"> | M |
| − | <img src="icons/keyboard/minus.png" width="48" alt="N"> | N |
| Capture | <img src="icons/keyboard/capture.png" width="48" alt="Câmera"> | Sem tecla padrão |
| Home | <img src="icons/keyboard/home.png" width="48" alt="Casa"> | Sem tecla padrão |
| Direcional | <img src="icons/keyboard/dpad.png" width="48" alt="Setas"> <img src="icons/keyboard/dpad_up.png" width="48" alt="Cima"> <img src="icons/keyboard/dpad_right.png" width="48" alt="Direita"> <img src="icons/keyboard/dpad_down.png" width="48" alt="Baixo"> <img src="icons/keyboard/dpad_left.png" width="48" alt="Esquerda"> <img src="icons/keyboard/dpad_h.png" width="48" alt="Esquerda e direita"> <img src="icons/keyboard/dpad_v.png" width="48" alt="Cima e baixo"> | Setas do teclado |
| Setas | <img src="icons/keyboard/up.png" width="48" alt="Seta para cima"> <img src="icons/keyboard/right.png" width="48" alt="Seta para a direita"> <img src="icons/keyboard/down.png" width="48" alt="Seta para baixo"> <img src="icons/keyboard/left.png" width="48" alt="Seta para a esquerda"> | Setas do teclado |

</details>

## Dúvidas

<details>
    <summary>
        <strong>Por que o botão A da tela de título não mudou?</strong>
    </summary>

Essa é uma textura que o mod não troca.

</details>

<details>
    <summary>
        <strong>Funciona junto com a tradução PT-BR?</strong>
    </summary>

Funciona. Testei com a [tradução 2.5.4](https://github.com/LucianoNeo/pokemon-pokopia-pt-br) e sem ela também.

</details>

<details>
    <summary>
        <strong>Mudei os botões no emulador e alguns ícones não batem</strong>
    </summary>

Os ícones seguem o mapeamento padrão do emulador, então não vão bater se você mudar os botões ou as teclas.

</details>

<details>
    <summary>
        <strong>Como eu troco um ícone?</strong>
    </summary>

Todos os ícones estão na pasta `icons`. Cada ícone é um PNG de 84x84. Edite o que quiser e gere os patches de novo.

Pra gerar os patches de novo, você precisa do Python 3.11 ou mais novo:

```bash
pip install -r requirements.txt
python build.py
```

Depois rode o `apply.py` como na [instalação manual](#manual).

</details>

<details>
    <summary>
        <strong>Como isso funciona por dentro?</strong>
    </summary>

O `root.rdb` diz onde cada recurso está: em qual `.fdata` (pela posição dele no `root.rdx`) e em que ponto dele. Os ícones estão na textura 18 do G1T `0xBC2C37F5`, dentro do `0x00011c54.fdata`. Cada arquivo em `patches/` guarda só os blocos BC7 dos ícones novos, nada do jogo. Só os blocos embaixo dos ícones mudam, e eles continuam em BC7, como no original.

O `apply.py` lê o G1T da sua cópia, confere o SHA-256 e grava esses blocos por cima. Depois salva o resultado num `.fdata` novo, o `0x0d5e1c05.fdata`, inclui esse arquivo numa cópia do `root.rdx` e grava um patch IPS de 23 bytes que faz o `root.rdb` apontar pra lá. O G1T tem 62 texturas e só o atlas dos botões muda, então o `.fdata` novo leva as outras 61 junto.

Se você quer aprender sobre esse tipo de mod, pode usar o projeto como material de estudo: o `apply.py` e o `build.py` são curtos e explicam no topo os formatos que usam. O `flip_gobs`, no `build.py`, mostra também a diferença entre o layout de textura do Switch 1 e o do Switch 2.

</details>

## Agradecimentos

- [RDBExplorer](https://github.com/MrIkso/RDBExplorer), pelos formatos RDB e `.fdata`.
- [gust_tools](https://github.com/VitaSmith/gust_tools), pelo formato G1T.
- ns2-assets, pelas anotações sobre texturas do Switch 2.
- [Inter](https://github.com/rsms/inter), a fonte dos textos dos botões.
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:PlayStation_logo.svg), pelo vetor do logo PS.

## Aviso

Esse é um projeto independente, sem nenhuma ligação com a Nintendo, a The Pokémon Company, a Koei Tecmo, a Sony, a Microsoft, a Valve ou a ASUS, e nenhuma delas apoia ou patrocina o projeto. O código deste repositório não tem nenhum arquivo do jogo, mas o mod pronto traz cópias modificadas de um arquivo de texturas e do `root.rdx` do jogo, e a arte do jogo que está nele pertence aos seus donos. Pokémon e Pokopia são marcas dos seus donos. PlayStation, DualSense, DualShock e o logo PS são marcas da Sony Interactive Entertainment; Xbox, da Microsoft; Steam Deck, da Valve; e ROG Ally, da ASUS. A [licença MIT](LICENSE) vale pro código e pros ícones, não pras marcas citadas aqui nem pros arquivos do jogo.
