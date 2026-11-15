# Plan

The project runs in seven phases. Each phase has a goal, deliverables and an exit test. Current progress lives in [STATUS.md](../STATUS.md), which is updated whenever something changes.

This is a hobby project, so there are no dates. Phases 0 to 4 cost little and answer the main question: is this worth building properly?

## Phases at a glance

| Phase | Name | Goal | Exit test |
| --- | --- | --- | --- |
| 0 | Direction and concept | Agree what we are building and what it looks like | Direction doc and concept sheets accepted |
| 1 | Prototype design | Have a buildable design for four units | Parts list final, shell fits a real board |
| 2 | Product and platform spec | Know what every part of the system must do | Spec reviewed by all four of us |
| 3 | Build four units | Four working Tabs | Each unit records a conversation into the Omi app |
| 4 | Field trial | Learn whether we use it | Two weeks of wear, then a go or no-go |
| 5 | Our own software | Replace borrowed software with our own | A day of conversations becomes a daily summary in our app |
| 6 | Product hardware | Storage on the Tab, then a custom board | ODM brief ready, or the project stops |

## Phase 0: Direction and concept

| Deliverable | Where |
| --- | --- |
| Direction and prototype plan | [01-direction-and-prototype-plan.md](01-direction-and-prototype-plan.md) |
| Concept sheets for the target design | [design/concept-sheets](../design/concept-sheets/) |

## Phase 1: Prototype design

| Deliverable | Where |
| --- | --- |
| Component stack and parts list | [02-prototype-component-stack.md](02-prototype-component-stack.md) |
| Printable enclosure, first pass | [hardware/enclosure](../hardware/enclosure/) |
| Measurements from a real board and switch | To do, once parts arrive |
| Enclosure revised to those measurements | To do |
| One test print checked for fit | To do |

## Phase 2: Product and platform spec

| Deliverable | Where |
| --- | --- |
| Product and platform spec | [03-product-and-platform-spec.md](03-product-and-platform-spec.md) |
| Review by all four co-founders | To do |
| Open questions in the spec answered or parked | To do |

## Phase 3: Build four units

| Deliverable | Notes |
| --- | --- |
| Parts ordered | Boards first. They are the long-lead item. |
| Five shell sets printed | After the test print passes |
| Four units soldered and assembled | One spare set of parts |
| Firmware flashed | Pre-built DevKit 1 release |
| Each unit paired with the Omi app | Records and transcribes one test conversation |
| Battery life measured | One full working day per unit |

## Phase 4: Field trial

| Deliverable | Notes |
| --- | --- |
| Two weeks of daily wear by all four | Lanyard, clip and pendant each tried |
| Twenty recordings kept for the speech-to-text test | Car, café, office, under a fan |
| Speech-to-text comparison | Sarvam Saaras against Deepgram Nova-3 on those recordings |
| Trial notes | What we used, what we ignored, what annoyed us |
| Go or no-go decision | Written down, with reasons |

## Phase 5: Our own software

Only if Phase 4 is a go. Order follows section 10 of the spec.

| Deliverable | Notes |
| --- | --- |
| Cloud pipeline | Ingest, transcribe, summarise, daily and weekly roll-ups |
| Phone app | Sync, Today, Conversation, summaries, search |
| Desktop capture app | macOS first |
| Web app | Read-only |

## Phase 6: Product hardware

Only if Phase 5 produces something we rely on.

| Deliverable | Notes |
| --- | --- |
| Storage on the Tab | Add-on storage and store-and-forward firmware on a prototype |
| Carriers | Pendant frame, magnetic clip, lanyard mount, printed and tested |
| Custom board requirements | Two mics, storage, haptics, magnetic charging |
| ODM brief | Design, spec and volumes, ready to send |
| Legal review | Consent and recording, before any unit reaches an outside user |

## How we track

- [STATUS.md](../STATUS.md) holds the state of every deliverable: done, in progress, blocked or not started.
- When a deliverable changes state, STATUS.md changes in the same commit.
- Decisions that change the plan are added to the decision log at the bottom of STATUS.md.
