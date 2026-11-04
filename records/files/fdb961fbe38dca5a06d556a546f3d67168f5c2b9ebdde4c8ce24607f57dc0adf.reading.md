# The figure: the model with its forms inside it

Drawn at D6b from `fractal-forms-D6.jsonl` by `_analysis/d6b_figure.py`. It is the stage C5 figure (`figure-C5.md`, drawing 1: 21 boxes, 20 arrows, each arrow with the proposition that carries it) with the six room forms drawn into its boxes and arrows, at the level where they differ: the element or arrow. Each box and arrow names the forms that specify it (add detail that holds in their rooms) or restrict it (it holds there only under a condition). A box with no form named is held by every form as the model states it. Four elements outside the C5 drawing are added because a form changes them (P19, P23, P27, P32); the claim C01 stands beside the figure, as at C5. No form replaces any element. The unvalidated proposals (`proposals-D6.jsonl`) are not drawn.

## The forms

- **A, Border terms and the announced plan**: changes 11 of the 66 units (elements and arrows) read.
- **B, Behind the thread: chat, scripts, raids**: changes 7 of the 66 units (elements and arrows) read.
- **C, The design reopened**: changes 10 of the 66 units (elements and arrows) read.
- **D, Keeping, with help or carrying on**: changes 17 of the 66 units (elements and arrows) read.
- **E, The sub's play, run as work**: changes 13 of the 66 units (elements and arrows) read.
- **F, Moving for the spot**: changes 14 of the 66 units (elements and arrows) read.

Units read: 66 (each with six form lines, 396 lines in all); lines that specify 37, restrict 35, replace 0, leave untouched 324.

## Drawing 1, the model with the forms in its boxes and arrows

```mermaid
flowchart LR
  classDef changed fill:#fff4d6,stroke:#8a6d00
  classDef plain fill:#f4f4f4,stroke:#999
  subgraph conditions["Conditions"]
    K01["K01: the April Fools play, beside the work<br/>specified by D E F"]:::changed
    K02["K02: the room judges it has too few hands"]:::plain
  end
  subgraph mediators["Mediators, named for what the room and its members do"]
    R01["R01: the starter"]:::plain
    P01["P01: the room's calls for hands<br/>specified by C D F"]:::changed
    P02["P02: settling what the mark will show<br/>specified by C E"]:::changed
    P03["P03: building the mark, members posting its state<br/>specified by F"]:::changed
    P04["P04: templates and coordinates<br/>specified by A C F"]:::changed
    P05["P05: upkeep<br/>specified by A D F<br/>restricted by C"]:::changed
    P07["P07: sparing a neighbour's work<br/>specified by A B C D"]:::changed
    P08["P08: border talk and deals<br/>specified by A B C"]:::changed
    P09["P09: attack calls"]:::plain
    P10["P10: the move"]:::plain
    P14["P14: scripts and spare accounts<br/>specified by B E F<br/>restricted by A D"]:::changed
    P15["P15: the bare answer"]:::plain
    P16["P16: help between rooms<br/>specified by C D"]:::changed
    P17["P17: coalitions"]:::plain
    P18["P18: contest in talk"]:::plain
    P20["P20: the host sub's line<br/>specified by D"]:::changed
    P19["P19: a guest's work on a host's mark, under the host's rule<br/>restricted by D F"]:::changed
    P23["P23: the chat: planning moved off the thread<br/>specified by A B<br/>restricted by E"]:::changed
    P27["P27: choosing the spot before any loss<br/>restricted by F"]:::changed
    P32["P32: members stepping away under strain<br/>restricted by B"]:::changed
  end
  subgraph follows["What follows"]
    P11["P11: celebration<br/>specified by A D"]:::changed
    P12["P12: records (after hour 73, curation of the record)<br/>specified by A F"]:::changed
    P13["P13: what the room keeps<br/>specified by D<br/>restricted by E"]:::changed
  end
  C01note["C01, beside the figure: a decided element of order<br/>restricted by A C"]:::changed
  H73(["hour 73: placement stops for every room"])
  P11 --- H73
  H73 --- P12
  P01 -->|"A01 N01; restricted by D E"| P03
  R01 -->|"A02 N01; restricted by D E"| P01
  P03 -->|"A03 N01"| P05
  P05 -->|"A04 N02; restricted by F"| P08
  P08 -->|"A05 N09; specified by B D; restricted by A"| P07
  P05 -->|"A06 N06; restricted by D F"| P14
  P03 -->|"A07 N04; restricted by E F"| P11
  P11 -->|"A08 N04; restricted by E"| P12
  P12 -->|"A09 N04; restricted by D E"| P13
  K02 -->|"A10 N08; restricted by E F"| P10
  P02 -->|"A11 N07; restricted by C"| P04
  P01 -->|"A12 N07; restricted by F"| P15
  P05 -->|"A13 N02; restricted by C D"| P16
  P08 -->|"A14 N09; restricted by A"| P16
  P01 -->|"A15 N03; restricted by B E"| P09
  P09 -->|"A16 N03; restricted by E"| P07
  P09 -->|"A17 N03"| P08
  P09 -->|"A18 N03"| P18
  P05 -->|"A19 N02"| P17
  P01 -->|"A20 N05; restricted by D"| P20
```

## Legend

- **Boxes.** Left, the conditions; middle, what the room and its members do; right, what follows the work. The bar at hour 73 marks the close. Shaded boxes are changed by at least one form; grey boxes by none.
- **specified by X**: in form X, add-step, add-condition or link lines on the unit lean (held by at least the larger of 5 and a tenth of X's defining rooms, at 1.2 times the 558 defining rooms' share or more). **restricted by X**: restrict lines lean and outnumber the other leaning ops. The rule was logged at D6a-01 before it ran (`_analysis/d6_fractal.py`).
- **Arrows.** Each keeps its C5 label: its id and the proposition (N01 to N09) that carries it, then the forms that specify or restrict it. Of the 20 arrows, one is specified by a form (A05, by B and D), and 16 are restricted by one or more. A restriction says the order holds in that form only under a condition, or that the record there cannot show it.
- **Forms.** A to F are the six room forms of D4a-08c, by their final names (`room-forms-names.md`). B is a grouping, not one shared change. The 35 branches are the level below and are not drawn; the table names the branches that explain each form's changes (`fractal-D6.jsonl`).

## Where each form differs, with the branches that explain it

| form | specifies | restricts | branches with a line in this form (`fractal-D6.jsonl`) |
|---|---|---|---|
| A, Border terms and the announced plan | P04, P05, P07, P08, P11, P12, P23 | A05, A14, C01, P14 | F10, F15, F17, F18, F19, F26, F28, F30, F31, F32 |
| B, Behind the thread: chat, scripts, raids | A05, P07, P08, P14, P23 | A15, P32 | F08, F16, F20, F29 |
| C, The design reopened | P01, P02, P04, P07, P08, P16 | A11, A13, C01, P05 | F07, F33, F34 |
| D, Keeping, with help or carrying on | A05, K01, P01, P05, P07, P11, P13, P16, P20 | A01, A02, A06, A09, A13, A20, P14, P19 | F04, F11, F12, F13, F14, F18, F22, F23, F24, F27 |
| E, The sub's play, run as work | K01, P02, P14 | A01, A02, A07, A08, A09, A10, A15, A16, P13, P23 | F01, F02, F03, F04, F05, F06, F21, F25, F34, F35 |
| F, Moving for the spot | K01, P01, P03, P04, P05, P12, P14 | A04, A06, A07, A10, A12, P19, P27 | F04, F08, F09 |

**Held by every form as the model states it (31 units):** A03, A17, A18, A19, A21, C02, K02, K03, K04, K05, K06, K07, P06, P09, P10, P15, P17, P18, P21, P22, P24, P25, P26, P28, P29, P30, P31, P33, P34, R01, R02.

## What the figure leaves out

It leaves out what the C5 figure left out (its last section), the eleven unvalidated proposals, the two held proposals (QD4-001; stated in full in `retelling-D6.md`), and the rates at which the forms hold an element without changing it, which the rule does not test (told in the retelling under D05 and D08). It does not draw the branches, the splits of form D, or the survival reading by form, which the retelling gives in words.
