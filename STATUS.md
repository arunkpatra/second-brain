# Status

Last updated: 15 Nov 2026

**Where we are:** design and spec first passes are done. Nothing is built yet. The next move is to order boards.

## Phase summary

| Phase | Name | Status |
| --- | --- | --- |
| 0 | Direction and concept | Done |
| 1 | Prototype design | In progress, waiting on parts |
| 2 | Product and platform spec | In progress, waiting on review |
| 3 | Build four units | Not started |
| 4 | Field trial | Not started |
| 5 | Our own software | Not started |
| 6 | Product hardware | Not started |

Phase definitions and exit tests are in [docs/PLAN.md](docs/PLAN.md).

## Next actions

| Action | Owner | Blocks |
| --- | --- | --- |
| Order five XIAO nRF52840 Sense boards, five 402030 cells, switches, wire and magnets | Arun | Phases 1 and 3 |
| Order one test print of the shell | Arun | Phase 1 |
| Review the product and platform spec | All four | Phase 2 |
| Measure the first board and switch, then send the numbers | Arun | Phase 1 |

## Phase 0: Direction and concept

- [x] Direction and prototype plan
- [x] Concept sheets: overview, views and interfaces, carriers, wear ergonomics
- [x] Form revised to a golden-rectangle face with 4.1 mm corners and 2.5 mm edges

## Phase 1: Prototype design

- [x] Component stack and parts list
- [x] Printable enclosure, first pass, with STL and STEP files
- [ ] Measurements from a real board and switch
- [ ] Enclosure revised to those measurements
- [ ] One test print checked for fit

## Phase 2: Product and platform spec

- [x] Product and platform spec, version 0.1
- [ ] Review by all four co-founders
- [ ] Open questions answered or parked

## Phase 3: Build four units

- [ ] Parts ordered
- [ ] Five shell sets printed
- [ ] Four units soldered and assembled
- [ ] Firmware flashed
- [ ] Each unit paired with the Omi app and tested
- [ ] Battery life measured

## Phase 4: Field trial

- [ ] Two weeks of daily wear by all four
- [ ] Twenty recordings kept for the speech-to-text test
- [ ] Speech-to-text comparison
- [ ] Trial notes
- [ ] Go or no-go decision

## Phase 5: Our own software

- [ ] Cloud pipeline
- [ ] Phone app
- [ ] Desktop capture app
- [ ] Web app

## Phase 6: Product hardware

- [ ] Storage on the Tab
- [ ] Carriers printed and tested
- [ ] Custom board requirements
- [ ] ODM brief
- [ ] Legal review

## Known risks

| Risk | Phase it bites | What we do about it |
| --- | --- | --- |
| The first build has no on-device storage, so a killed phone app loses audio | 4 | Accept for the trial. Fix in Phase 6. |
| One chest-worn mic may not hear well on a lanyard | 4 | The trial compares all three wear positions. |
| Shell openings were modelled without a board in hand | 1 | Measure, revise, test print before printing five. |
| The Sense board is short on stock in India | 3 | Order early from a seller showing stock. |
| Recording bystanders is legally unsettled | 6 | Legal review before any outside user. |

## Decision log

| Date | Decision |
| --- | --- |
| 15 Nov 2026 | Tab form with three carriers: pendant, magnetic clip, lanyard mount |
| 15 Nov 2026 | Always-on capture gated by voice activity, with a mute slider, mark button and recording LED |
| 15 Nov 2026 | Prototypes use open-source Omi electronics. No ODM until the prototypes prove out. |
| 15 Nov 2026 | Face is a golden rectangle, 28 × 45.3 mm, with 4.1 mm corners and 2.5 mm edges |
| 15 Nov 2026 | Stage 0 is an Omi DevKit 1 build, since DevKit 2 cannot be built from parts |
| 15 Nov 2026 | Arun orders the parts and solders the units |
| 15 Nov 2026 | Repository is public |
