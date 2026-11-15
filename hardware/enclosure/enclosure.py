"""SecondBrain Tab: Stage 0 prototype enclosure (parametric, CadQuery).

Run:  pip install cadquery && python3 enclosure.py
Writes STL and STEP files for the two shell halves into ./out

Axes: X across the face, Y up the face, Z through the thickness.
Origin at the centre of the body. Front face is +Z, top edge is +Y.
All dimensions in millimetres.

Values marked MEASURE are estimates. Check them against the real parts
before printing more than one test shell.
"""
import cadquery as cq
from cadquery import exporters

# ---- Outer form (same face as the target design) ----
W = 28.0            # face width
H = 45.3            # face height, W x golden ratio
T = 12.0            # thickness of the prototype (target design is 9.0)
R_CORNER = 4.1      # face corner radius
R_EDGE = 2.5        # front and back edge radius
WALL = 1.5

# ---- Parts ----
BOARD_W, BOARD_L = 17.8, 21.0   # XIAO nRF52840 Sense
PCB_Z = 0.0                     # underside of the board sits on the split plane
USB_W, USB_H = 9.4, 3.6         # USB-C opening, MEASURE
USB_Z = 2.6                     # centre of the USB-C connector above the split, MEASURE
CELL_W, CELL_L, CELL_T = 20.0, 30.0, 4.0   # 402030 LiPo
MIC_X, MIC_Y = 0.0, 12.0        # mic hole on the front face, MEASURE against the board
LED_X, LED_Y = 5.5, 17.5        # LED window on the front face, MEASURE against the board
SW_Y = -8.0                     # slide switch centre on the right edge
SW_SLOT_L, SW_SLOT_H = 6.5, 2.4 # lever slot, MEASURE against SS12D00-G3
MAGNET_D, MAGNET_T = 8.2, 1.0   # pocket for an 8 x 1 mm disc magnet
CORD_D = 2.0                    # cord holes through the top corners
CORD_INSET = 3.2
LIP_T, LIP_H, FIT = 0.8, 1.8, 0.12

# Golden layout: the lower 28 x 28 square carries the mark button
BTN_Y = -H / 2 + W / 2
BTN_DISH_D = W / 1.618
BTN_HOLE_D = 3.6

IN_W, IN_H, IN_T = W - 2 * WALL, H - 2 * WALL, T - 2 * WALL
R_IN = R_CORNER - WALL


def rbox(w, h, t, r_vert, r_face=0.0):
    b = cq.Workplane("XY").box(w, h, t).edges("|Z").fillet(r_vert)
    if r_face > 0:
        b = b.faces(">Z or <Z").edges().fillet(r_face)
    return b


def ring(z0, height, outer_off, thick):
    """Ring that follows the inside of the wall, from z0 upward."""
    o = rbox(IN_W - 2 * outer_off, IN_H - 2 * outer_off, height, R_IN - outer_off)
    i = rbox(IN_W - 2 * (outer_off + thick), IN_H - 2 * (outer_off + thick),
             height + 1, max(R_IN - outer_off - thick, 0.4))
    return o.cut(i).translate((0, 0, z0 + height / 2))


outer = rbox(W, H, T, R_CORNER, R_EDGE)
cavity = rbox(IN_W, IN_H, IN_T, R_IN, 1.0)
shell = outer.cut(cavity)

# Cord pillars in the two top corners, full height, with through holes
px, py = W / 2 - CORD_INSET, H / 2 - CORD_INSET
for sx in (-1, 1):
    pillar = cq.Workplane("XY").circle(1.8).extrude(IN_T).translate((sx * px, py, -IN_T / 2))
    shell = shell.union(pillar.intersect(outer))
for sx in (-1, 1):
    hole = cq.Workplane("XY").circle(CORD_D / 2).extrude(T + 2).translate((sx * px, py, -T / 2 - 1))
    shell = shell.cut(hole)

# Openings
usb = (cq.Workplane("XY").box(USB_W, 4.0, USB_H).edges("|Y").fillet(1.2)
       .translate((0, H / 2 - 2.0 + 0.5, USB_Z)))
sw_slot = cq.Workplane("XY").box(3.5, SW_SLOT_L, SW_SLOT_H).translate((W / 2 - 1.2, SW_Y, 0))
mic = cq.Workplane("XY").circle(0.75).extrude(WALL + 1).translate((MIC_X, MIC_Y, T / 2 - WALL - 0.5))
led = cq.Workplane("XY").circle(1.0).extrude(WALL + 1).translate((LED_X, LED_Y, T / 2 - WALL - 0.5))
dish = cq.Workplane("XY").circle(BTN_DISH_D / 2).extrude(1.0).translate((0, BTN_Y, T / 2 - 0.5))
btn = cq.Workplane("XY").circle(BTN_HOLE_D / 2).extrude(WALL + 1).translate((0, BTN_Y, T / 2 - WALL - 0.5))
magnet = (cq.Workplane("XY").circle(MAGNET_D / 2).extrude(MAGNET_T)
          .translate((0, BTN_Y, -T / 2 + WALL - MAGNET_T)))
for c in (usb, sw_slot, mic, led, dish, btn, magnet):
    shell = shell.cut(c)

# Split into back (tub) and front (lid)
half = cq.Workplane("XY").box(W + 2, H + 2, T).translate((0, 0, T / 2))
front = shell.intersect(half)
back = shell.cut(half)

# Locating lip on the back half, matching relief in the front half
sw_body = cq.Workplane("XY").box(5.0, 9.6, 6.0).translate((W / 2 - WALL - 2.5, SW_Y, 0))
lip = ring(0, LIP_H, FIT, LIP_T).cut(usb).cut(sw_slot).cut(sw_body)
back = back.union(lip)
front = front.cut(ring(-0.01, LIP_H + 0.25, 0, LIP_T + 2 * FIT))

# Rib on the back half that locates the cell and walls off the switch bay
cell_x0 = -IN_W / 2 + 0.2
rib = (cq.Workplane("XY").box(0.8, 22.0, 3.0)
       .translate((cell_x0 + CELL_W + 0.25 + 0.4, -H / 2 + WALL + 12.0, -T / 2 + WALL + 1.5)))
back = back.union(rib)

if __name__ == "__main__":
    import os
    os.makedirs("out", exist_ok=True)
    for name, part in (("tab-proto-front", front), ("tab-proto-back", back)):
        exporters.export(part, f"out/{name}.stl", tolerance=0.02, angularTolerance=0.1)
        exporters.export(part, f"out/{name}.step")
        bb = part.val().BoundingBox()
        print(name, "valid" if part.val().isValid() else "INVALID",
              "solids", part.solids().size(),
              "bbox %.2f x %.2f x %.2f" % (bb.xlen, bb.ylen, bb.zlen),
              "volume %.0f mm3" % part.val().Volume(),
              "mass %.1f g at 1.2 g/cc" % (part.val().Volume() * 1.2 / 1000))
    asm = front.translate((0, 0, 9)).union(back.translate((0, 0, -9)), clean=False)
    for name, d in (("iso", (1.2, -1.6, 1.0)), ("iso-back", (1.2, -1.6, -1.0))):
        exporters.export(asm, f"out/preview-{name}.svg",
                         opt={"width": 700, "height": 700, "marginLeft": 40, "marginTop": 40,
                              "showAxes": False, "projectionDir": d, "strokeWidth": 0.15,
                              "strokeColor": (30, 32, 36), "hiddenColor": (190, 194, 200),
                              "showHidden": False})
