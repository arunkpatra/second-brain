# SecondBrain: agreed direction and prototype plan

15 Nov 2026

## Context

SecondBrain is a hobby project for now, with four prototype units for the four Rensaar co-founders. It becomes a real product only if those units prove useful.

- **First users:** the four of us. We travel often, sell in person, and spend some days in back-to-back meetings, video calls and Slack.
- **Target user later:** professionals in meetings all day, sales people first.
- **Undecided on purpose:** price band and subscription.
- **Benchmark:** NeoSapien Neo 1 (20 g, chain-worn, up to 16 hours, not water-resistant, about ₹12,999).
- **Name:** "SecondBrain" is a working title, because NeoSapien already markets a "Second Brain" operating system.

## Decisions agreed

| Topic | Decision | Why |
| --- | --- | --- |
| Form | Slim Tab capsule with three carriers: pendant, magnetic clip, lanyard badge mount | The neck is often taken, and pendants slip under clothing. A lanyard is invisible in Indian offices. |
| Capture | Always-on, gated by voice activity | Full-day battery without the user managing sessions |
| Controls | Mute slider, one "mark this" button, recording LED, haptic | A slider has a state you can feel. A press toggle does not. |
| Prototype electronics | Open-source Omi design, not a custom board | Four units do not justify custom hardware or an ODM |
| ODM | Deferred until the prototypes prove out | An ODM needs a validated design and a real spec |

## Capture behaviour

The device is always-on, with three conditions.

1. **Gated by voice activity.** The mic stays awake, but audio is stored and sent only while someone is speaking.
2. **A slider for mute, a button for marking.** The slider tells you by touch whether it is recording, in a pocket or under a table.
3. **Discreet controls, not covert recording.** A small LED is on while capturing. Being caught with a hidden recorder in a sales meeting costs more than the notes are worth.

**The video-call gap:** on headphones, the device hears only your side of a call. Calls and Slack huddles need a small desktop capture app, which belongs in the spec from day one.

## Prototyping

The four units reuse open-source electronics, with our own enclosure, app and backend. Custom boards and an ODM come only after that works.

**Stage 0: four units**

- **Electronics:** the Omi DevKit design, built on the Seeed XIAO nRF52840 Sense board with a small rechargeable cell. Hardware files and firmware are open on GitHub.
- **Change from the earlier suggestion:** Omi no longer sells DevKit 2. Its docs point to building a DevKit 1 from parts or buying the consumer Omi pendant. Building from parts fits us better, because we control the enclosure.
- **Enclosure:** 3D-printed in resin or nylon through an Indian print service.
- **Software:** our own phone app and backend, which is where the product is decided.

**Stage 1: only if Stage 0 proves out**

- Take the validated design and a written spec to an ODM.

**What the four units must test:** mixed Hindi-English sales conversations in noisy places, where existing devices are weakest.

## Two designs

We draw two designs in the same shape language. All figures are starting estimates to be tested.

|  | Target design | Prototype enclosure |
| --- | --- | --- |
| Purpose | The product we would ship | A printable shell for the four units |
| Size | 45.3 × 28 × 9 mm, a golden-rectangle face with 4.1 mm corners and 2.5 mm edges | Thicker, sized around the off-the-shelf board and cell |
| Weight | Under 18 g | Not constrained |
| Sealing | IP54 or better, for sweat and monsoon | None |
| Charging | Magnetic pogo-pin cradle | The board's USB-C port |
| Microphones | Two or three, for fan and traffic noise | The board's single mic |
| Storage | On-device, so a killed phone app loses nothing | Depends on the board build |
| Battery | A full 16-hour day | Measured, then reported |
| Materials | Matte polymer core, metal or fabric carriers | Printed resin or nylon |

The concept sheets for the target design are in [design/concept-sheets](../design/concept-sheets/).

## Plan

1. **Concept sheets for the target design.** Views, dimensions, interface callouts, the three carriers, and wear ergonomics. Done, first pass.
2. **Component stack for the prototype.** Board, cell, button, slider and LED, with a parts list that can be bought in India. Done, see [02-prototype-component-stack.md](02-prototype-component-stack.md).
3. **Prototype enclosure.** Printable 3D model sized around that stack, in the Tab shape. First pass done, see [hardware/enclosure](../hardware/enclosure/). Dimensions are provisional until a board is measured.
4. **Product and platform spec.** Device, phone app, device-to-phone sync, cloud backend, and the desktop capture app.
5. **Build four units.** Print, assemble, flash the open firmware.
6. **Two weeks of real use.** The four of us wear them in meetings and travel, then decide whether to continue.

## Open questions and risks

- **Does the single-mic board hear well enough on a lanyard or clip?** If not, Stage 0 needs a different board.
- **Does the open firmware support store-and-forward?** Without on-device storage, a killed phone app loses audio.
- **Who assembles the units?** Soldering a board, cell and switch is light work, but someone has to do it.
- **Bystander consent.** India's DPDP rules phase in consent obligations over 18 months from November 2025, and ambient audio of other people is unsettled. This needs a lawyer before any sale.
- **Speech quality for mixed Hindi-English.** Untested, and the main reason to build.

## Sources

- [NeoSapien Neo 1](https://neosapien.ai/)
- [Omi DevKit 2 documentation](https://docs.omi.me/onboarding/omi-devkit-2)
- [Omi DevKit 1 documentation](https://docs.omi.me/doc/hardware/DevKit1)
- [Chambers: India's DPDP regime takes effect](https://chambers.com/articles/s-r-data-india-s-digital-personal-data-protection-regime-takes-effect)
