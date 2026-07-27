#!/usr/bin/env python3
"""
Assemble assets/terminal-card.svg.

    python3 tools/ascii_portrait.py --image photo.jpg --cols 88 --rows 46 > tools/portrait.json
    python3 tools/build_card.py

Edit CONTENT / LEFT_META below and re-run. Dotted leaders are computed, so
labels stay aligned however you edit them.
"""

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "assets" / "terminal-card.svg"

# ---------------------------------------------------------------- content ---
# ("+"|" ", label, value)  key/value row      ("#", label, "")  group header
# ("", "", "")             blank spacer       (">", text, "")   plain indented

CONTENT = [
    ("+", "Subject", "Reagent Sandra"),
    (" ", "Handle", "R21 / Octopuzzz"),
    (" ", "Role", "Software Developer · Data Streaming & Backend"),
    (" ", "Origin", "Jakarta, Indonesia"),
    (" ", "Education", "B.CS — Bina Nusantara University · GPA 3.59"),
    (" ", "Status", "Building ETL pipelines @ Bank Indonesia"),
    (" ", "ToolChain", "VS Code, Git, Docker, Postman"),
    ("", "", ""),
    ("+", "Core Lang", "Go, TypeScript, JavaScript, Java, Ruby"),
    (" ", "Core Backend", "Gin, Gorm, Spring Boot, Express.js, Node.js"),
    (" ", "Core Frontend", "Next.js, React.js, Vue.js, Flutter"),
    (" ", "Core Data", "Confluent, Kafka, ElasticSearch, MongoDB"),
    (" ", "Core Infra", "Docker, Kubernetes, Jenkins, GCP, Nginx"),
    ("", "", ""),
    ("#", "Mission Log", ""),
    (" ", "ACTIVE", "Confluent ETL streaming & transformation — Bank Indonesia"),
    (" ", "SHIPPED", "irennieart.com — Next.js studio site & class booking"),
    (" ", "PRIOR", "Microservices — BNI core system integration"),
    (" ", "PRIOR", "Super Apps platform — Next.js + Google Maps API"),
    ("", "", ""),
    ("#", "Certifications", ""),
    (" ", "IBM", "Certified App Connect Enterprise"),
    (" ", "MongoDB", "SI Associate"),
    (" ", "Kominfo", "Digitalent Bootcamp — Go · React · Ruby on Rails"),
    ("", "", ""),
    ("#", "Contact", ""),
    (" ", "Grid LinkedIn", "reagent-sandra"),
    (" ", "Grid GitHub", "Octopuzzz"),
    (" ", "Grid Mail", "████████ classified"),
    (" ", "Grid Portfolio", "████████ classified"),
    ("", "", ""),
    ("#", "Live Stats", ""),
    (">", "See live GitHub telemetry below ↓", ""),
]

LEFT_META = [
    ("#", "ACHIEVEMENTS", ""),
    (">", "Pull Shark", ""),
    (">", "Pair Extraordinaire", ""),
    ("", "", ""),
    ("+", "Repos", "37"),
    (" ", "Stars", "8"),
]

# ----------------------------------------------------------------- layout ---
W, H = 900, 540
PANEL_TOP, PANEL_BOTTOM, SPLIT_X = 62, 518, 332

ART_X, ART_Y = 44, 104
ART_CW = 3.09                 # character advance; 88 cols -> 272px panel width
ART_FS = ART_CW / 0.6         # monospace advance is ~0.6em
ART_LH = ART_CW * 1.92

# The handle used to sit at y=78 and collide with the SYSTEM.INFO label at
# y=84. It now has its own line, and the body starts lower to make room —
# line-height tightened from 13 to 12 so the block still clears the panel.
INFO_X, INFO_Y = 352, 140
INFO_FS = 10
INFO_LH = 12
INFO_GAP = 7
LEADER_W = 19


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def portrait_rows() -> list[str]:
    cached = HERE / "portrait.json"
    if cached.exists():
        return json.loads(cached.read_text())
    proc = subprocess.run(
        [sys.executable, str(HERE / "ascii_portrait.py"), "--cols", "88", "--rows", "46"],
        capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)


def build_art(rows: list[str]) -> tuple[str, float]:
    out = []
    n = len(rows)
    for i, row in enumerate(rows):
        if not row.strip():
            continue
        y = ART_Y + i * ART_LH
        # Gentle falloff top and bottom so the scan reads as a fading capture.
        op = 0.42 + 0.30 * (1 - abs(i - n / 2) / (n / 2))
        out.append(
            f'<text class="art" x="{ART_X}" y="{y:.2f}" opacity="{op:.2f}" '
            f'textLength="{len(row) * ART_CW:.1f}" lengthAdjust="spacing" '
            f'xml:space="preserve">{esc(row)}</text>')
    return "\n    ".join(out), n * ART_LH


def build_rows(content, x, y0, leader=LEADER_W, fs=INFO_FS) -> tuple[str, float]:
    out, y = [], float(y0)
    for marker, label, value in content:
        if marker == "":
            y += INFO_GAP
            continue
        if marker == "#":
            out.append(
                f'<text x="{x}" y="{y:.1f}" xml:space="preserve">'
                f'<tspan class="mark">+ </tspan>'
                f'<tspan class="grp">{esc(label)}</tspan></text>')
        elif marker == ">":
            out.append(f'<text class="note" x="{x + 2 * fs * 0.6:.1f}" '
                       f'y="{y:.1f}">{esc(label)}</text>')
        else:
            head = f"{marker} {label} "
            dots = "." * max(1, leader - len(head))
            out.append(
                f'<text x="{x}" y="{y:.1f}" xml:space="preserve">'
                f'<tspan class="{"mark" if marker == "+" else "key"}">{marker} </tspan>'
                f'<tspan class="key">{esc(label)} </tspan>'
                f'<tspan class="dots">{dots}</tspan>'
                f'<tspan class="val"> {esc(value)}</tspan></text>')
        y += INFO_LH
    return "\n    ".join(out), y - INFO_LH


def main() -> None:
    rows = portrait_rows()
    art, art_h = build_art(rows)
    info, last_y = build_rows(CONTENT, INFO_X, INFO_Y)
    meta, _ = build_rows(LEFT_META, ART_X, ART_Y + art_h + 38, leader=13)

    cur_x = INFO_X + (len(CONTENT[-1][1]) + 3) * INFO_FS * 0.6

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"
     role="img" aria-label="Terminal dossier for Reagent Sandra, software developer, Jakarta">
  <title>Octopuzzz/README.md — system dossier</title>

  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.6" y2="1">
      <stop offset="0%" stop-color="#05060d"/>
      <stop offset="100%" stop-color="#0a0e1a"/>
    </linearGradient>

    <!-- userSpaceOnUse so one wash spans the whole portrait, not each row -->
    <linearGradient id="scanTone" gradientUnits="userSpaceOnUse"
                    x1="0" y1="{ART_Y}" x2="0" y2="{ART_Y + art_h:.0f}">
      <stop offset="0%" stop-color="#7dd3fc"/>
      <stop offset="55%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#22d3ee"/>
    </linearGradient>

    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>
      <stop offset="50%" stop-color="#67e8f9" stop-opacity="0.38"/>
      <stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/>
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="1.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <clipPath id="artclip">
      <rect x="{ART_X - 8}" y="{ART_Y - 12}" width="290" height="{art_h + 18:.0f}"/>
    </clipPath>
  </defs>

  <style>
    text {{
      font-family: "JetBrains Mono", "SFMono-Regular", "SF Mono", Menlo,
                   Consolas, "Liberation Mono", "Courier New", monospace;
      dominant-baseline: middle;
    }}
    .chrome {{ font-size: 11px; fill: #64748b; letter-spacing: 0.4px; }}
    .panel  {{ font-size: 9px;  fill: #22d3ee; letter-spacing: 2.2px; opacity: 0.75; }}
    .handle {{ font-size: 18px; fill: #22d3ee; font-weight: 700; letter-spacing: 1px; }}
    .art    {{ font-size: {ART_FS:.2f}px; fill: url(#scanTone); white-space: pre; }}
    .key    {{ font-size: {INFO_FS}px; fill: #7dd3fc; }}
    .dots   {{ font-size: {INFO_FS}px; fill: #1e3a5f; }}
    .val    {{ font-size: {INFO_FS}px; fill: #e2e8f0; }}
    .mark   {{ font-size: {INFO_FS}px; fill: #fbbf24; font-weight: 700; }}
    .grp    {{ font-size: {INFO_FS}px; fill: #fbbf24; letter-spacing: 1.4px; }}
    .note   {{ font-size: {INFO_FS}px; fill: #94a3b8; }}

    #frame  {{ animation: pulse 5s ease-in-out infinite; }}
    #beam   {{ animation: sweep 4.5s linear infinite; }}
    #cursor {{ animation: blink 1s steps(1, end) infinite; }}

    @keyframes pulse {{ 0%, 100% {{ opacity: 0.85; }} 50% {{ opacity: 1; }} }}
    @keyframes sweep {{ 0% {{ transform: translateY(0px); }}
                        100% {{ transform: translateY({art_h:.0f}px); }} }}
    @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}

    @media (prefers-reduced-motion: reduce) {{
      #frame, #beam, #cursor {{ animation: none; }}
      #beam {{ opacity: 0; }}
    }}
  </style>

  <rect width="{W}" height="{H}" rx="14" fill="url(#bg)"/>

  <g id="frame" filter="url(#glow)">
    <rect x="12" y="12" width="{W - 24}" height="{H - 24}" rx="12"
          fill="none" stroke="#22d3ee" stroke-width="1"/>
  </g>
  <rect x="22" y="22" width="{W - 44}" height="{H - 44}" rx="8"
        fill="none" stroke="#22d3ee" stroke-width="1" opacity="0.18"/>

  <circle cx="44" cy="42" r="4.5" fill="#ff5f57"/>
  <circle cx="60" cy="42" r="4.5" fill="#febc2e"/>
  <circle cx="76" cy="42" r="4.5" fill="#28c840"/>
  <text class="chrome" x="98" y="43">Octopuzzz/README.md</text>

  <line x1="22" y1="{PANEL_TOP}" x2="{W - 22}" y2="{PANEL_TOP}"
        stroke="#22d3ee" stroke-width="1" opacity="0.2"/>
  <line x1="{SPLIT_X}" y1="{PANEL_TOP}" x2="{SPLIT_X}" y2="{PANEL_BOTTOM}"
        stroke="#22d3ee" stroke-width="1" opacity="0.15"/>

  <!-- left: visual map -->
  <text class="panel" x="{ART_X}" y="84">VISUAL.MAP</text>
  <g clip-path="url(#artclip)">
    {art}
    <rect id="beam" x="{ART_X - 8}" y="{ART_Y - 12}" width="290" height="14" fill="url(#scan)"/>
  </g>
  <line x1="{ART_X}" y1="{ART_Y + art_h + 18:.0f}" x2="{SPLIT_X - 16}"
        y2="{ART_Y + art_h + 18:.0f}" stroke="#22d3ee" stroke-width="1" opacity="0.2"/>

    {meta}

  <!-- right: system info -->
  <text class="panel" x="{INFO_X}" y="84">SYSTEM.INFO</text>
  <text class="handle" x="{INFO_X}" y="108" filter="url(#softglow)">Octopuzzz</text>
  <line x1="{INFO_X}" y1="122" x2="{W - 34}" y2="122"
        stroke="#22d3ee" stroke-width="1" opacity="0.35"/>

    {info}

  <rect id="cursor" x="{cur_x:.1f}" y="{last_y - 5:.1f}" width="6" height="11" fill="#22d3ee"/>
</svg>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(svg):,} bytes, {len(rows)} art rows, "
          f"body ends y={last_y:.0f})")


if __name__ == "__main__":
    main()
