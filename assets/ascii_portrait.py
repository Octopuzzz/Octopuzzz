#!/usr/bin/env python3
"""
Generate the ASCII portrait grid for assets/terminal-card.svg.

Two modes:

  1. Real avatar (recommended):
         python3 tools/ascii_portrait.py --image avatar.png
     Download your avatar first:
         curl -L "https://avatars.githubusercontent.com/u/71009747?v=4&s=400" -o avatar.png

  2. Procedural placeholder (no input file needed):
         python3 tools/ascii_portrait.py

Output is a JSON list of rows, sized to the SVG's VISUAL.MAP panel
(54 columns x 44 rows). Paste it into build_card.py, or pipe it:
         python3 tools/ascii_portrait.py --image avatar.png > tools/portrait.json
"""

import argparse
import json
import sys

from PIL import Image, ImageDraw, ImageFilter

COLS, ROWS = 54, 30

# Cell aspect in the SVG is 5.03w x 9.09h. At 54x30 cells that makes the source
# frame near-square, which is what a head-and-shoulders crop actually wants —
# a taller frame forces the crop narrower than the shoulders, and the
# silhouette then runs off both edges with no visible outline.
SRC_W, SRC_H = COLS * 5, int(ROWS * 9.09)

# Density ramp, darkest -> lightest. Space last so background drops out.
RAMP = "@%#*+=-:. "


def procedural_bust() -> Image.Image:
    """Formal head-and-shoulders portrait — tuxedo, wing collar, bow tie."""
    img = Image.new("L", (SRC_W, SRC_H), 0)
    d = ImageDraw.Draw(img)

    W, H = SRC_W, SRC_H
    cx = W / 2

    # Painted back to front: jacket, shirt, lapels, neck, collar, tie, head.

    # --- jacket -----------------------------------------------------------
    # Shoulders sweep in from off-canvas so the bust fills the frame edge.
    d.polygon(
        [(cx - W * 0.66, H * 1.10), (cx - W * 0.48, H * 0.68),
         (cx - W * 0.17, H * 0.585), (cx + W * 0.17, H * 0.585),
         (cx + W * 0.48, H * 0.68), (cx + W * 0.66, H * 1.10)],
        fill=120,
    )

    # --- shirt ------------------------------------------------------------
    # Bright panel so the chest reads as white dress shirt against dark cloth.
    d.polygon(
        [(cx - W * 0.10, H * 0.585), (cx + W * 0.10, H * 0.585),
         (cx + W * 0.062, H * 0.98), (cx - W * 0.062, H * 0.98)],
        fill=248,
    )

    # --- lapels -----------------------------------------------------------
    # Darker than the jacket so the satin edge reads as a hard diagonal.
    for side in (-1, 1):
        d.polygon(
            [(cx + side * W * 0.105, H * 0.60),
             (cx + side * W * 0.275, H * 0.655),
             (cx + side * W * 0.215, H * 0.86),
             (cx + side * W * 0.078, H * 0.98),
             (cx + side * W * 0.072, H * 0.75)],
            fill=64,
        )
        # Notch where lapel meets collar.
        d.polygon(
            [(cx + side * W * 0.185, H * 0.635), (cx + side * W * 0.275, H * 0.655),
             (cx + side * W * 0.205, H * 0.700)],
            fill=150,
        )

    # --- neck -------------------------------------------------------------
    d.rounded_rectangle(
        [cx - W * 0.082, H * 0.42, cx + W * 0.082, H * 0.615],
        radius=int(W * 0.035), fill=168,
    )
    d.ellipse([cx - W * 0.10, H * 0.415, cx + W * 0.10, H * 0.475], fill=124)

    # --- wing collar ------------------------------------------------------
    for side in (-1, 1):
        d.polygon(
            [(cx + side * W * 0.045, H * 0.560), (cx + side * W * 0.135, H * 0.588),
             (cx + side * W * 0.062, H * 0.650)],
            fill=238,
        )

    # --- bow tie ----------------------------------------------------------
    for side in (-1, 1):
        d.polygon(
            [(cx + side * W * 0.018, H * 0.612), (cx + side * W * 0.125, H * 0.582),
             (cx + side * W * 0.125, H * 0.665), (cx + side * W * 0.018, H * 0.640)],
            fill=92,
        )
    d.rounded_rectangle(
        [cx - W * 0.026, H * 0.606, cx + W * 0.026, H * 0.646],
        radius=int(W * 0.010), fill=66,
    )

    # --- head -------------------------------------------------------------
    d.ellipse([cx - W * 0.200, H * 0.120, cx + W * 0.200, H * 0.470], fill=208)
    for side in (-1, 1):
        d.ellipse(
            [cx + side * W * 0.200 - W * 0.033, H * 0.262,
             cx + side * W * 0.200 + W * 0.033, H * 0.338],
            fill=186,
        )
    # Hair: swept cap sitting slightly proud of the skull.
    d.ellipse([cx - W * 0.222, H * 0.098, cx + W * 0.222, H * 0.300], fill=96)
    d.polygon(
        [(cx - W * 0.222, H * 0.215), (cx + W * 0.222, H * 0.190),
         (cx + W * 0.150, H * 0.155), (cx - W * 0.150, H * 0.160)],
        fill=96,
    )

    # --- features ---------------------------------------------------------
    for side in (-1, 1):
        d.ellipse(
            [cx + side * W * 0.148 - W * 0.072, H * 0.252,
             cx + side * W * 0.148 + W * 0.072, H * 0.280],
            fill=112,
        )
        d.ellipse(
            [cx + side * W * 0.112 - W * 0.042, H * 0.288,
             cx + side * W * 0.112 + W * 0.042, H * 0.314],
            fill=62,
        )
    d.polygon([(cx, H * 0.298), (cx + W * 0.042, H * 0.370), (cx - W * 0.042, H * 0.370)], fill=236)
    d.ellipse([cx - W * 0.080, H * 0.392, cx + W * 0.080, H * 0.416], fill=106)

    img = img.filter(ImageFilter.GaussianBlur(W * 0.009))

    # Blend the filled mass with its own edges -> contour-heavy "scan" look.
    edges = img.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(1.1))
    return Image.blend(img.point(lambda p: int(p * 0.64)), edges.point(lambda p: min(255, p * 3)), 0.40)


def load_avatar(path: str, floor: int = 56, gain: float = 0.5, gamma: float = 2.4) -> Image.Image:
    """Fit a real photo into the portrait frame.

    Handles the common studio-headshot case: dark subject cut out on a white
    background. The backdrop is detected and dropped to zero (so it renders as
    empty space, not a solid block of glyphs), and the subject is lifted to a
    tonal `floor` so dark clothing still reads as a silhouette instead of
    vanishing. `gain` controls local-contrast enhancement, which is what pulls
    detail out of a black shirt.
    """
    import numpy as np

    rgb = Image.open(path).convert("RGB")
    gray = rgb.convert("L")
    a = np.asarray(gray).astype(np.float32)

    # --- separate subject from backdrop -----------------------------------
    border = np.concatenate([a[:8, :].ravel(), a[-8:, :].ravel(),
                             a[:, :8].ravel(), a[:, -8:].ravel()])
    bg_light = border.mean() > 127
    cut = 35
    subject = (a < border.mean() - cut) if bg_light else (a > border.mean() + cut)
    # Drop speckle so JPEG noise in the backdrop can't define the head's top edge.
    subject = np.asarray(
        Image.fromarray((subject * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(5))
    ) > 127

    # Fill interior holes. Bright specular highlights — glasses lenses, a watch
    # face, a glossy button — otherwise read as "backdrop" and punch voids
    # through the subject. Flood the true backdrop inward from the corners;
    # whatever the flood cannot reach is an interior hole.
    # Done at reduced resolution (flood fill is pure Python and slow), and on a
    # copied image, because PIL's floodfill silently no-ops on array-backed ones.
    small = (
        Image.fromarray(((~subject) * 255).astype(np.uint8))
        .resize((subject.shape[1] // 4, subject.shape[0] // 4), Image.BOX)
        .point(lambda p: 255 if p > 127 else 0)
        .copy()
    )
    for corner in ((0, 0), (small.width - 1, 0),
                   (0, small.height - 1), (small.width - 1, small.height - 1)):
        if small.getpixel(corner) == 255:
            ImageDraw.floodfill(small, corner, 0)
    holes = np.asarray(
        small.resize((subject.shape[1], subject.shape[0]), Image.BILINEAR)
    ) > 127
    subject = subject | holes

    ys, xs = np.where(subject)
    if len(ys) == 0:
        raise SystemExit("could not separate subject from background")

    # --- frame on the head, then open out to a half-bust ------------------
    top = ys.min()
    head_band = subject[top:top + int(0.22 * (ys.max() - top)), :]
    hx = np.where(head_band.any(axis=0))[0]
    head_w = max(hx.max() - hx.min(), 1)
    head_cx = (hx.max() + hx.min()) / 2

    crop_w = head_w * 2.7
    crop_h = crop_w * (SRC_H / SRC_W)
    left = head_cx - crop_w / 2
    upper = top - crop_h * 0.055

    box = (int(left), int(upper), int(left + crop_w), int(upper + crop_h))
    canvas = Image.new("L", (rgb.width, rgb.height), 0)
    canvas.paste(gray, (0, 0), Image.fromarray((subject * 255).astype(np.uint8)))
    img = canvas.crop(box).resize((SRC_W, SRC_H), Image.LANCZOS)
    mask = (
        Image.fromarray((subject * 255).astype(np.uint8))
        .crop(box)
        .resize((SRC_W, SRC_H), Image.LANCZOS)
    )

    v = np.asarray(img).astype(np.float32)
    m = np.asarray(mask).astype(np.float32) / 255.0

    # --- tone-map the subject --------------------------------------------
    # Take the black/white points from the HEAD only. Measured over the whole
    # subject, a large dark garment drags the black point down and pushes every
    # skin tone to the ceiling, flattening the face into one solid glyph. Scoped
    # to the head, the face spans the full ramp and the clothing falls to the
    # floor as a silhouette — which is what you want at this resolution.
    head_zone = np.zeros_like(m, dtype=bool)
    head_zone[: int(SRC_H * 0.60)] = True
    inside = v[(m > 0.5) & head_zone]
    if inside.size:
        lo, hi = np.percentile(inside, [4, 96])
        if hi > lo:
            # Map the head's black point to SHADOW rather than 0. Hard-clipping
            # here would flatten the garment to a single tone before local
            # contrast ever runs, costing the placket, seams and shoulder line.
            shadow = 34.0
            v = np.clip(shadow + (v - lo) * (255.0 - shadow) / (hi - lo), 0, 255)

    # Local contrast: subtract a wide blur to recover folds, buttons, collar.
    # The blur is mask-normalized, otherwise the black backdrop drags down the
    # average near every silhouette edge and haloes the whole subject bright.
    r = SRC_W * 0.07

    def blur(arr: np.ndarray) -> np.ndarray:
        return np.asarray(
            Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).filter(
                ImageFilter.GaussianBlur(r)
            )
        ).astype(np.float32)

    norm = np.maximum(blur(m * 255.0) / 255.0, 1e-3)
    wide = np.clip(blur(v * m) / norm, 0, 255)
    detail = v - wide

    # Adaptive strength: flat areas (a black shirt) get the full gain, areas that
    # already have contrast (the face) get less, so neither ends up clipped.
    local_var = np.maximum(blur((detail ** 2) * m) / norm, 0.0)
    local_sd = np.sqrt(local_var)
    v = np.clip(v + detail * gain * (28.0 / (local_sd + 28.0)) * 2.4, 0, 255)

    # Compress highlights so the face doesn't clip to a solid block of glyphs.
    v = 255.0 * np.power(np.clip(v, 0, 255) / 255.0, gamma)

    # A black shirt carries almost no tonal detail that survives a 54-column
    # downsample, so it would render as a featureless slab. Trace the silhouette
    # edge and the strong internal boundaries (collar, shoulder seam, sleeve)
    # and lay them over the top — the body then reads as a contoured shape
    # rather than a fill pattern, which also suits the scan-line conceit.
    mimg = Image.fromarray((m * 255).astype(np.uint8))
    rim = (
        np.asarray(mimg.filter(ImageFilter.MaxFilter(5))).astype(np.float32)
        - np.asarray(mimg.filter(ImageFilter.MinFilter(5))).astype(np.float32)
    ) / 255.0

    seams = np.asarray(
        Image.fromarray(np.clip(v * m, 0, 255).astype(np.uint8))
        .filter(ImageFilter.FIND_EDGES)
        .filter(ImageFilter.GaussianBlur(0.7))
    ).astype(np.float32)
    seams = np.clip(seams * 2.6, 0, 255) * m

    v = np.maximum(v, rim * 210.0)
    v = np.maximum(v, seams * 0.85)

    # Lift the subject off the floor, leave the backdrop at zero.
    v = floor + v * (255 - floor) / 255.0
    v = v * m

    return Image.fromarray(v.astype(np.uint8)).filter(ImageFilter.SMOOTH)


def normalize(img: Image.Image) -> Image.Image:
    """Stretch to the full 0-255 range so the ramp uses all ten characters."""
    lo, hi = img.getextrema()
    if hi <= lo:
        return img
    return img.point(lambda p: int((p - lo) * 255 / (hi - lo)))


def to_ascii(img: Image.Image) -> list[str]:
    # BOX (area average) rather than LANCZOS: Lanczos' negative lobes undershoot
    # at hard edges, punching black holes through eyes and glasses frames.
    grid = normalize(img.resize((COLS, ROWS), Image.BOX))
    px = grid.load()
    span = len(RAMP) - 1

    rows = []
    for y in range(ROWS):
        line = []
        for x in range(COLS):
            # Invert: bright pixels -> dense glyphs, dark background -> space.
            line.append(RAMP[span - min(span, px[x, y] * len(RAMP) // 256)])
        rows.append("".join(line).rstrip())
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--image", help="path to an avatar image; omit for the procedural placeholder")
    ap.add_argument("--preview", action="store_true", help="print the art to stderr instead of JSON")
    ap.add_argument("--floor", type=int, default=56,
                    help="tonal floor for the subject; raise it if dark clothing disappears")
    ap.add_argument("--gamma", type=float, default=2.4,
                    help="highlight compression; raise it if the face clips to a solid block")
    ap.add_argument("--gain", type=float, default=0.5,
                    help="local-contrast strength; raise it to pull more detail from flat areas")
    args = ap.parse_args()

    img = load_avatar(args.image, args.floor, args.gain, args.gamma) if args.image else procedural_bust()
    rows = to_ascii(img)

    if args.preview:
        print("\n".join(rows), file=sys.stderr)
    else:
        print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
