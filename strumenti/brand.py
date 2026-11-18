"""Ripeti al Poliba – brand primitives for Instagram graphics."""

BLUE = "#155DFC"
NIGHT1 = "#1C398E"
NIGHT2 = "#312C85"
HL = "#FFD84D"
INK = "#101828"
PAPER = "#F6F8FC"
GRID = "#DCE6FA"
SKY = "#DBEAFE"
MUTED = "#62748E"

FONT_DIR = "file:///usr/share/fonts/opentype/inter"


def symbol_cap(bg=BLUE, rounded=True, size=512, bg_on=True):
    """Option A – 'Tocco': geometric graduation cap with yellow tassel."""
    rx = 116 if rounded else 0
    bgrect = f'<rect width="512" height="512" rx="{rx}" fill="{bg}"/>' if bg_on else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}">
{bgrect}
<path d="M150 236 V320 C150 354 200 378 256 378 C312 378 362 354 362 320 V236 L256 286 Z" fill="#FFFFFF"/>
<polygon points="256,118 446,206 256,294 66,206" fill="#FFFFFF" stroke="{bg}" stroke-width="14" stroke-linejoin="round"/>
<path d="M256 206 L404 226" fill="none" stroke="{NIGHT1}" stroke-width="13" stroke-linecap="round"/>
<path d="M404 226 V318" fill="none" stroke="{HL}" stroke-width="13" stroke-linecap="round"/>
<rect x="386" y="306" width="36" height="74" rx="13" fill="{HL}"/>
<circle cx="256" cy="206" r="17" fill="{NIGHT1}"/>
</svg>'''


def symbol_bubble(bg=BLUE, rounded=True, size=512, bg_on=True):
    """Option B – 'Fumetto': a speech bubble with highlighted notes (someone explains it to you)."""
    rx = 116 if rounded else 0
    bgrect = f'<rect width="512" height="512" rx="{rx}" fill="{bg}"/>' if bg_on else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}">
{bgrect}
<path d="M150 96 H362 C400 96 428 124 428 162 V300 C428 338 400 366 362 366 H230 L150 430 L162 366 H150 C112 366 84 338 84 300 V162 C84 124 112 96 150 96 Z" fill="#FFFFFF"/>
<rect x="136" y="160" width="236" height="56" rx="12" fill="{HL}" transform="rotate(-3 254 188)"/>
<rect x="136" y="244" width="236" height="26" rx="13" fill="{NIGHT1}"/>
<rect x="136" y="292" width="150" height="26" rx="13" fill="{NIGHT1}" opacity="0.55"/>
</svg>'''


def symbol_sheet(bg=BLUE, rounded=True, size=512, bg_on=True):
    """Option C – 'Quadretto': a grid-paper sheet with a highlighter stroke and a check."""
    rx = 116 if rounded else 0
    bgrect = f'<rect width="512" height="512" rx="{rx}" fill="{bg}"/>' if bg_on else ""
    lines = "".join(
        f'<line x1="{x}" y1="104" x2="{x}" y2="408" stroke="{GRID}" stroke-width="4"/>' for x in range(150, 380, 38)
    ) + "".join(
        f'<line x1="120" y1="{y}" x2="392" y2="{y}" stroke="{GRID}" stroke-width="4"/>' for y in range(136, 400, 38)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}">
{bgrect}
<g transform="rotate(-6 256 256)">
<rect x="112" y="96" width="288" height="320" rx="34" fill="#FFFFFF"/>
<clipPath id="sheetclip"><rect x="112" y="96" width="288" height="320" rx="34"/></clipPath>
<g clip-path="url(#sheetclip)">{lines}</g>
<rect x="150" y="226" width="214" height="62" rx="14" fill="{HL}" transform="rotate(-4 257 257)"/>
<path d="M176 258 L232 312 L346 188" fill="none" stroke="{BLUE if bg != BLUE else NIGHT1}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
</g>
</svg>'''


SYMBOLS = {"tocco": symbol_cap, "fumetto": symbol_bubble, "quadretto": symbol_sheet}


def base_css():
    weights = {
        100: "Thin", 200: "ExtraLight", 300: "Light", 400: "Regular", 500: "Medium",
        600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black",
    }
    faces = []
    for w, n in weights.items():
        faces.append(f"@font-face{{font-family:'InterX';font-weight:{w};src:url('{FONT_DIR}/Inter-{n}.otf');}}")
        faces.append(f"@font-face{{font-family:'InterD';font-weight:{w};src:url('{FONT_DIR}/InterDisplay-{n}.otf');}}")
    return "\n".join(faces) + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#000}}
body{{font-family:'InterX',sans-serif;color:{INK};-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;font-feature-settings:'ss01' 0}}
.frame{{position:relative;overflow:hidden}}
.paper{{background-color:{PAPER};background-image:linear-gradient({GRID} 2px,transparent 2px),linear-gradient(90deg,{GRID} 2px,transparent 2px);background-size:54px 54px;background-position:-1px -1px}}
.blue{{background:{BLUE};color:#fff}}
.blue-grid{{background-color:{BLUE};background-image:linear-gradient(rgba(255,255,255,.07) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.07) 2px,transparent 2px);background-size:54px 54px;background-position:-1px -1px;color:#fff}}
.night{{background:linear-gradient(160deg,{NIGHT1} 0%,{NIGHT2} 100%);color:#fff}}
.sky{{background:{SKY}}}
.display{{font-family:'InterD';font-weight:900;letter-spacing:-0.025em;line-height:1.02}}
.hl{{position:relative;z-index:0;white-space:nowrap;color:{INK}}}
.hl::before{{content:'';position:absolute;left:-0.10em;right:-0.10em;top:0.14em;bottom:0.00em;background:{HL};transform:skew(-9deg) rotate(-1.2deg);border-radius:0.10em;z-index:-1}}
.hl-soft::before{{opacity:1}}
.pill{{display:inline-flex;align-items:center;gap:14px;font-family:'InterX';font-weight:800;font-size:27px;letter-spacing:0.14em;text-transform:uppercase;padding:16px 30px;border-radius:999px}}
.pill.on-blue{{background:rgba(255,255,255,.16);color:#fff}}
.pill.on-paper{{background:{SKY};color:{BLUE}}}
.pill.on-night{{background:rgba(255,216,77,.16);color:{HL}}}
.top{{position:absolute;left:80px;right:80px;top:70px;display:flex;align-items:center;gap:20px;height:64px}}
.top .brand{{font-family:'InterX';font-weight:800;font-size:30px;letter-spacing:-0.01em}}
.top .page{{margin-left:auto;font-family:'InterX';font-weight:700;font-size:26px;letter-spacing:0.06em;opacity:.75}}
.card{{background:#fff;border-radius:44px;box-shadow:0 18px 50px rgba(16,24,40,.10),0 2px 6px rgba(16,24,40,.06)}}
.body{{font-family:'InterX';font-weight:500;font-size:40px;line-height:1.36}}
.small{{font-family:'InterX';font-weight:500;font-size:28px;line-height:1.4}}
.swipe{{display:inline-flex;align-items:center;gap:16px;font-weight:800;font-size:30px;padding:20px 34px;border-radius:999px}}
"""


def top_bar(page=None, theme="blue", symbol="tocco"):
    sym = SYMBOLS[symbol]
    if theme == "paper":
        logo = sym(bg=BLUE, size=64)
        color = INK
    elif theme == "night":
        logo = sym(bg=BLUE, size=64)
        color = "#fff"
    else:
        logo = sym(bg=NIGHT1, size=64)
        color = "#fff"
    pg = f'<span class="page">{page}</span>' if page else ""
    return f'<div class="top" style="color:{color}">{logo}<span class="brand">Ripeti al Poliba</span>{pg}</div>'


def page(inner, w, h, cls="", extra_css=""):
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8">
<style>{base_css()}
{extra_css}</style></head>
<body><div class="frame {cls}" style="width:{w}px;height:{h}px">{inner}</div></body></html>"""


ARROW = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg>'
CHECK = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 12.5l5 5L19.5 7"/></svg>'


def icon(name, size=56, color="#fff", sw=2.2):
    paths = {
        "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="M8 14h3"/>',
        "book": '<path d="M2.5 5.8c3-1.3 6.2-1.1 9.5 1 3.3-2.1 6.5-2.3 9.5-1v12.9c-3-1.3-6.2-1.1-9.5 1-3.3-2.1-6.5-2.3-9.5-1z"/><path d="M12 6.8v13"/>',
        "cap": '<path d="M12 4 2.5 8.5 12 13l9.5-4.5z"/><path d="M6.5 10.6V15c0 1.4 2.5 3 5.5 3s5.5-1.6 5.5-3v-4.4"/><path d="M21.5 8.5V14"/>',
        "help": '<circle cx="12" cy="12" r="9"/><path d="M9.3 9.3a2.8 2.8 0 1 1 3.9 2.6c-.8.4-1.2 1-1.2 1.8v.6"/><path d="M12 17.2h.01"/>',
        "pin": '<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>',
        "cash": '<rect x="2.5" y="6" width="19" height="12" rx="2.5"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9.5v5M18 9.5v5"/>',
        "move": '<path d="M4 12a8 8 0 0 1 13.7-5.6L20 8.7"/><path d="M20 4v4.7h-4.7"/><path d="M20 12a8 8 0 0 1-13.7 5.6L4 15.3"/><path d="M4 20v-4.7h4.7"/>',
        "user": '<circle cx="12" cy="8" r="3.8"/><path d="M4.5 20c.8-3.6 3.8-5.6 7.5-5.6s6.7 2 7.5 5.6"/>',
        "chat": '<path d="M20 15.5a2.5 2.5 0 0 1-2.5 2.5H9l-4.5 3.5V6.5A2.5 2.5 0 0 1 7 4h10.5A2.5 2.5 0 0 1 20 6.5z"/>',
        "link": '<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1 1"/><path d="M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1-1"/>',
        "laptop": '<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 19h20"/>',
    }
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>'
