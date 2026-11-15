# Prototype component stack and parts list

15 Nov 2026 · Stage 0, four units

The four prototypes are an Omi DevKit 1 build inside our own Tab-shaped shell: one Seeed XIAO nRF52840 Sense board, one LiPo cell, one slide switch. That build needs no firmware work, so the first unit can be recording within a day of the parts arriving.

## What the research changed

| Finding | Consequence |
| --- | --- |
| Only DevKit 1 can be built from parts. DevKit 2 and the consumer Omi use custom boards. | Stage 0 is a DevKit 1 build. |
| DevKit 1 streams audio to the phone over Bluetooth. Offline recording to a microSD card arrived with DevKit 2. | The first build has no on-device storage. If the phone app is killed, audio is lost. This is the biggest gap against the target design. |
| The DevKit 1 slide switch sits in line with the battery ground wire. | On the prototype the slider is a power switch. Off means certainly not recording, which is an honest stand-in for mute. |
| The XIAO Sense has one microphone and one RGB LED on the board. | One mic instead of two. The shell needs a mic hole and an LED window. |
| The DevKit 1 guide is marked legacy, community-maintained and unsupported. | Expect to read the firmware source. Help is on the Omi Discord. |

## Two builds

| | Build A: stock | Build B: with mark button |
| --- | --- | --- |
| Parts | Board, cell, slide switch | Build A plus a tactile button on a spare pin |
| Firmware | Pre-built DevKit 1 release, flashed by drag and drop | Compiled from source with a button handler |
| Phone app | The open-source Omi app, until ours exists | Same |
| Effort | Three solder joints per unit | Firmware work in nRF Connect SDK |
| Recommendation | Build all four this way first | Convert one unit once Build A works |

The shell is designed with the button position in place from the start, so Build B needs no new print.

## Stack inside the shell

Front to back, with the face kept at the target 28 × 45.3 mm.

| Layer | Part | Thickness, mm |
| --- | --- | --- |
| 1 | Front shell, with mic hole and LED window | 1.5 |
| 2 | XIAO nRF52840 Sense, 21 × 17.8 mm, mic side facing front | 4.5 |
| 3 | Air gap and wiring | 0.5 |
| 4 | LiPo cell 402030, 20 × 30 mm | 4.0 |
| 5 | Back shell, with magnet pocket | 1.5 |
| | **Total** | **12.0** |

- The prototype is 12 mm thick against the 9 mm target. A 502030 cell (5 mm, about 250 mAh) makes it 13 mm.
- The board sits at the bottom of the face with its USB-C port in the bottom edge, for charging and flashing.
- The slide switch sits on the right edge, where the target design has the mute slider.
- Board thickness with the USB-C connector is my estimate. Measure the real board before finalising the shell.

## Parts list

Quantities cover four units plus one spare set. Prices marked "est." are my estimates for commodity parts and need checking at order time.

| Part | Spec | Qty | Unit price, ₹ | Where |
| --- | --- | --- | --- | --- |
| Board | Seeed Studio XIAO nRF52840 Sense | 5 | 1,382 to 2,100 | [element14 India](https://in.element14.com/seeed-studio/102010469/xiao-board-arm-arduino-board/dp/4060352), [techiesms](https://techiesms.com/product/seeed-studio-xiao-nrf52840-sense/), [Robocraze 3-pack](https://robocraze.com/products/seeed-studio-xiao-nrf52840-sense-board-3-pack) |
| Cell | 1S LiPo 3.7 V, 402030, about 200 mAh, with protection circuit | 5 | 150 to 300 est. | Robu.in or similar |
| Slide switch | SS12D00-G3, 3 mm | 10 | 10 to 20 est. | Any component store |
| Tactile button | 6 × 6 mm, low profile, for Build B | 5 | 5 to 10 est. | Any component store |
| Wire | 28 AWG silicone, red and black | 1 m each | 50 est. | Any component store |
| Magnets | Neodymium disc 8 × 1.5 mm, for the carrier mount | 10 | 10 to 20 est. | Any component store |
| Shell | Resin or nylon print, two halves | 5 sets | 300 to 800 est. | Print service |

**Budget:** about ₹15,000 to ₹18,000 for everything, most of it the boards. This is an estimate.

**Stock warning:** the Sense variant was out of stock at one Indian seller when checked, and element14 showed deliveries starting 1 December 2026. Order boards first. Make sure the listing says "Sense": the plain XIAO nRF52840 has no microphone.

**Tools:** fine-tip soldering iron, wire stripper with a 28 AWG notch, tweezers, USB-C cable.

## Assembly, from the DevKit 1 guide

1. Cut the cell's black wire and strip both ends.
2. Solder the cell to the board's battery pads, with the slide switch in line on the black wire.
3. Seat the board, cell and switch in the shell and snap it shut.
4. Double-press the board's reset button, then drag the firmware file onto the drive that appears.

The device charges only while switched on, and a charge takes about one to two hours.

## What Stage 0 will and will not tell us

| Question | Answered by Build A? |
| --- | --- |
| Is the Tab shape comfortable on a lanyard, clip and pendant? | Yes |
| Does one chest-worn mic capture mixed Hindi-English speech well enough? | Yes |
| How long does a 200 mAh cell last in real use? | Yes |
| Do we actually use the notes? | Yes, using the Omi app first |
| Does two-mic pickup help? | No, needs a custom board |
| Does store-and-forward survive a killed phone app? | No, needs storage added |

## Open decisions

- **Storage.** The DevKit 2 firmware shows how microSD recording works, but its wiring targets a custom board. Adding a microSD breakout to the XIAO is possible and is firmware work. Decide after Build A is running.
- **Who solders.** Three joints per unit. A local electronics repair shop can do it if none of us wants to.
- **Our own app.** The Omi app is enough to judge the hardware. Our own app is only worth starting once the hardware has earned it.

## Sources

- [Omi DevKit 1](https://docs.omi.me/doc/hardware/DevKit1)
- [Omi buying guide](https://docs.omi.me/doc/assembly/Buying_Guide.md)
- [Omi build guide](https://docs.omi.me/doc/assembly/Build_the_device.md)
- [Omi DevKit 2 testing notes](https://docs.omi.me/doc/developer/DevKit2Testing)
- [Omi build introduction](https://docs.omi.me/doc/assembly/introduction.md)
- [element14 India listing](https://in.element14.com/seeed-studio/102010469/xiao-board-arm-arduino-board/dp/4060352)
- [techiesms listing](https://techiesms.com/product/seeed-studio-xiao-nrf52840-sense/)
- [Think Robotics listing](https://thinkrobotics.com/products/seeed-studio-xiao-nrf52840-sense)
