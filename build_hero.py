#!/usr/bin/env python3
"""
Assemble assets/hero.svg.

    python3 tools/ascii_portrait.py --image photo.jpg > tools/portrait.json
    python3 tools/build_hero.py

Edit IDENTITY / CHIPS / STAGES below and re-run.
"""

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "assets" / "hero.svg"

# ---------------------------------------------------------------- content ---
EYEBROW = "SOFTWARE DEVELOPER · DATA STREAMING"
NAME = "Reagent Sandra"
ROLE = ["Backend and streaming data — Go, Kafka,",
        "and the pipelines that run between them."]
CHIPS = ["Jakarta, ID", "Bank Indonesia", "BINUS · CS 3.59"]
STAGES = [("CDC", "#FF4D8D"), ("Kafka", "#7C5CFF"),
          ("ksqlDB", "#38E8C8"), ("Analytics", "#FFA23E")]

# ----------------------------------------------------------------- layout ---
W, H = 900, 480

ART_X, ART_Y = 48, 122
ART_CW = 3.18                     # character advance width
ART_FS = ART_CW / 0.6             # monospace advance is ~0.6em
ART_LH = ART_CW * 1.92

COL_X, COL_R = 372, 856           # right column left edge / right limit
NODE_X = [406, 550, 694, 838]
TRACK_Y = 382


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def portrait_rows() -> list[str]:
    cached = HERE / "portrait.json"
    if cached.exists():
        return json.loads(cached.read_text())
    proc = subprocess.run([sys.executable, str(HERE / "ascii_portrait.py")],
                          capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)


def build_art(rows: list[str]) -> tuple[str, float]:
    out = []
    for i, row in enumerate(rows):
        if not row.strip():
            continue
        y = ART_Y + i * ART_LH
        out.append(f'<text class="art" x="{ART_X}" y="{y:.2f}" '
                   f'textLength="{len(row) * ART_CW:.1f}" lengthAdjust="spacing" '
                   f'xml:space="preserve">{esc(row)}</text>')
    return "\n      ".join(out), len(rows) * ART_LH


def build_chips() -> str:
    out, x = [], COL_X
    for label in CHIPS:
        w = len(label) * 7.2 + 26
        out.append(
            f'<rect x="{x:.0f}" y="254" width="{w:.0f}" height="28" rx="14" '
            f'fill="#FFFFFF" fill-opacity="0.06" stroke="#FFFFFF" stroke-opacity="0.13"/>'
            f'<text class="mono chip" x="{x + w / 2:.0f}" y="272" '
            f'text-anchor="middle">{esc(label)}</text>')
        x += w + 10
    return "\n      ".join(out)


def build_pipeline() -> str:
    out = []
    for i, ((label, colour), x) in enumerate(zip(STAGES, NODE_X)):
        delay = f' n{i + 1}' if i else ''
        out.append(
            f'<g class="node{delay}"><circle cx="{x}" cy="{TRACK_Y}" r="14" '
            f'fill="none" stroke="{colour}" stroke-width="1.5"/></g>'
            f'<circle cx="{x}" cy="{TRACK_Y}" r="6" fill="{colour}"/>'
            f'<text class="mono stage" x="{x}" y="{TRACK_Y + 30}" '
            f'text-anchor="middle">{esc(label)}</text>')
    return "\n      ".join(out)


def main() -> None:
    rows = portrait_rows()
    art, art_h = build_art(rows)
    travel = NODE_X[-1] - NODE_X[0]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"
     role="img" aria-label="{esc(NAME)} — backend and streaming data engineer, Jakarta, Indonesia">
  <title>{esc(NAME)} — backend &amp; streaming data</title>

  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1A1147"/>
      <stop offset="55%" stop-color="#130D33"/>
      <stop offset="100%" stop-color="#0C0822"/>
    </linearGradient>

    <radialGradient id="auroraA" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF4D8D" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#FF4D8D" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="auroraB" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38E8C8" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#38E8C8" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="auroraC" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7C5CFF" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#7C5CFF" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="spectrum" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FF4D8D"/>
      <stop offset="38%" stop-color="#7C5CFF"/>
      <stop offset="72%" stop-color="#38E8C8"/>
      <stop offset="100%" stop-color="#FFA23E"/>
    </linearGradient>

    <!-- userSpaceOnUse so the wash runs across the whole portrait, not per row -->
    <linearGradient id="portrait" gradientUnits="userSpaceOnUse"
                    x1="0" y1="{ART_Y}" x2="0" y2="{ART_Y + art_h:.0f}">
      <stop offset="0%" stop-color="#FF9BC4"/>
      <stop offset="42%" stop-color="#BCA6FF"/>
      <stop offset="100%" stop-color="#7BFFE4"/>
    </linearGradient>

    <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>

    <filter id="haze" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="46"/>
    </filter>
    <filter id="spark" x="-160%" y="-160%" width="420%" height="420%">
      <feGaussianBlur stdDeviation="3.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <clipPath id="card"><rect width="{W}" height="{H}" rx="24"/></clipPath>
    <clipPath id="artclip">
      <rect x="{ART_X - 10}" y="{ART_Y - 12}" width="304" height="{art_h + 20:.0f}"/>
    </clipPath>
  </defs>

  <style>
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter,
                          Roboto, "Helvetica Neue", Arial, sans-serif; }}
    .mono {{ font-family: ui-monospace, "SF Mono", "JetBrains Mono", Menlo,
                          Consolas, "Liberation Mono", monospace; }}
    .eyebrow {{ font-size: 11px; letter-spacing: 2.6px; fill: #38E8C8; }}
    .name    {{ font-size: 42px; font-weight: 800; fill: #F7F5FF; letter-spacing: -0.5px; }}
    .role    {{ font-size: 15.5px; fill: #B5ADE0; }}
    .chip    {{ font-size: 12px; fill: #DAD5F7; }}
    .stage   {{ font-size: 11.5px; fill: #CFC9F0; }}
    .quiet   {{ font-size: 10px; letter-spacing: 2.4px; fill: #8A80C2; }}
    .art     {{ font-size: {ART_FS:.2f}px; fill: url(#portrait); opacity: 1;
                white-space: pre; }}

    .packet {{ animation: flow 3.6s linear infinite; }}
    .p2 {{ animation-delay: 0.9s; }}
    .p3 {{ animation-delay: 1.8s; }}
    .p4 {{ animation-delay: 2.7s; }}
    .node {{ animation: breathe 3.6s ease-in-out infinite; }}
    .n1 {{ animation-delay: 0.9s; }}
    .n2 {{ animation-delay: 1.8s; }}
    .n3 {{ animation-delay: 2.7s; }}
    #sweep {{ animation: scan 5s ease-in-out infinite; }}

    @keyframes flow {{
      0%   {{ transform: translateX(0px); opacity: 0; }}
      6%   {{ opacity: 1; }}
      94%  {{ opacity: 1; }}
      100% {{ transform: translateX({travel}px); opacity: 0; }}
    }}
    @keyframes breathe {{
      0%, 100% {{ opacity: 0.30; }}
      12%      {{ opacity: 0.85; }}
      40%      {{ opacity: 0.30; }}
    }}
    @keyframes scan {{
      0%   {{ transform: translateY(0px); }}
      100% {{ transform: translateY({art_h:.0f}px); }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      .packet {{ animation: none; opacity: 0.9; }}
      .node   {{ animation: none; opacity: 0.5; }}
      #sweep  {{ animation: none; opacity: 0; }}
    }}
  </style>

  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>

    <g filter="url(#haze)">
      <ellipse cx="742" cy="10" rx="250" ry="170" fill="url(#auroraA)"/>
      <ellipse cx="898" cy="250" rx="200" ry="180" fill="url(#auroraC)"/>
      <ellipse cx="150" cy="470" rx="250" ry="170" fill="url(#auroraB)"/>
    </g>

    <!-- portrait -->
    <rect x="{ART_X - 20}" y="{ART_Y - 24}" width="324" height="{art_h + 46:.0f}" rx="18"
          fill="#FFFFFF" fill-opacity="0.035" stroke="#FFFFFF" stroke-opacity="0.09"/>
    <g clip-path="url(#artclip)">
      {art}
      <rect id="sweep" x="{ART_X - 10}" y="{ART_Y - 12}" width="304" height="26" fill="url(#beam)"/>
    </g>

    <!-- identity -->
    <text class="mono eyebrow" x="{COL_X}" y="100">{esc(EYEBROW)}</text>
    <text class="sans name" x="{COL_X}" y="150">{esc(NAME)}</text>
    <rect x="{COL_X}" y="168" width="66" height="4" rx="2" fill="url(#spectrum)"/>
    <text class="sans role" x="{COL_X}" y="206">{esc(ROLE[0])}</text>
    <text class="sans role" x="{COL_X}" y="228">{esc(ROLE[1])}</text>

    <g>
      {build_chips()}
    </g>

    <line x1="{COL_X}" y1="316" x2="{COL_R}" y2="316" stroke="url(#rule)" stroke-width="1"/>
    <text class="mono quiet" x="{COL_X}" y="342">PIPELINE</text>

    <!-- signature: the stream -->
    <g>
      <line x1="{NODE_X[0]}" y1="{TRACK_Y}" x2="{NODE_X[-1]}" y2="{TRACK_Y}"
            stroke="url(#spectrum)" stroke-width="2" stroke-linecap="round" opacity="0.30"/>
      {build_pipeline()}
      <g filter="url(#spark)">
        <circle class="packet" cx="{NODE_X[0]}" cy="{TRACK_Y}" r="4" fill="#FFE9F2"/>
        <circle class="packet p2" cx="{NODE_X[0]}" cy="{TRACK_Y}" r="4" fill="#E4DBFF"/>
        <circle class="packet p3" cx="{NODE_X[0]}" cy="{TRACK_Y}" r="4" fill="#D6FFF5"/>
        <circle class="packet p4" cx="{NODE_X[0]}" cy="{TRACK_Y}" r="4" fill="#FFEFD9"/>
      </g>
    </g>
  </g>

  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="24"
        fill="none" stroke="#FFFFFF" stroke-opacity="0.10"/>
</svg>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(svg):,} bytes, {len(rows)} art rows)")


if __name__ == "__main__":
    main()
