"""Reel C5 'Prenoti una lezione in 3 passaggi' – animazione grafica, 1080x1920, 30 fps.

I passaggi seguono il sito: materia → giorno e orario → nome, email e «Conferma prenotazione».
Uso: python3 build_reel_c5.py [OFFSET_MUSICA]
Uscita: png/C5_reel.mp4 (con musica originale) e png/C5_reel_copertina.png
"""
import asyncio
import pathlib
import subprocess
import sys
import tempfile
from playwright.async_api import async_playwright
from brand import *

ROOT = pathlib.Path(__file__).resolve().parent
FPS = 30
W, H = 1080, 1920
HOOK = 2.8
STEP = 3.0
END = 3.8
TOTAL = HOOK + STEP * 3 + END
OFFSET = sys.argv[1] if len(sys.argv) > 1 else "21"

CHECK_W = CHECK.format(s=44, c="#fff")


def riga_materia(i, nome):
    return f"""<div class="mat" id="m{i}" style="display:flex;align-items:center;gap:28px;padding:30px 34px;border-radius:30px;background:#F1F5FD;margin-top:{0 if i == 0 else 22}px;transition:none">
  <div class="mi" style="flex:none;width:76px;height:76px;border-radius:22px;background:{SKY};display:flex;align-items:center;justify-content:center">{icon('book', 44, BLUE, 2.2)}</div>
  <div class="mn" style="font-weight:800;font-size:46px;color:{INK};letter-spacing:-0.01em">{nome}</div>
  <div class="mc" style="margin-left:auto;width:64px;height:64px;border-radius:50%;background:{BLUE};display:flex;align-items:center;justify-content:center;opacity:0">{CHECK_W}</div>
</div>"""


def chip(id_, testo, w):
    return f'<div class="chip" id="{id_}" style="width:{w}px;height:104px;border-radius:26px;background:#F1F5FD;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:40px;color:{INK}">{testo}</div>'


def campo(id_, etichetta, valore):
    return f"""<div style="margin-top:22px">
  <div style="font-weight:700;font-size:30px;color:{MUTED}">{etichetta}</div>
  <div style="margin-top:12px;height:100px;border-radius:24px;border:4px solid #DCE6FA;background:#F8FAFF;display:flex;align-items:center;padding:0 30px;font-weight:700;font-size:40px;color:{INK}"><span id="{id_}" data-full="{valore}"></span><span class="caret" id="{id_}c" style="display:inline-block;width:4px;height:46px;background:{BLUE};margin-left:4px;opacity:0"></span></div>
</div>"""


GIORNI = ["Lun", "Mar", "Mer", "Gio", "Ven"]
ORARI = ["15:00", "16:00", "17:00"]

card1 = "".join(riga_materia(i, n) for i, n in enumerate(["Analisi 1", "Fisica 1", "Scienza delle costruzioni"]))
card2 = f"""<div style="font-weight:700;font-size:30px;color:{MUTED}">Giorno</div>
<div style="display:flex;gap:16px;margin-top:14px">{''.join(chip(f'g{i}', g, 140) for i, g in enumerate(GIORNI))}</div>
<div style="font-weight:700;font-size:30px;color:{MUTED};margin-top:40px">Orario</div>
<div style="display:flex;gap:16px;margin-top:14px">{''.join(chip(f'o{i}', o, 240) for i, o in enumerate(ORARI))}</div>"""
card3 = f"""{campo('nome', 'Nome e cognome', 'Il tuo nome')}
{campo('mail', 'Email', 'la.tua@email.it')}
<div id="btn" style="margin-top:38px;height:112px;border-radius:28px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;gap:18px;font-weight:800;font-size:42px">
  <span id="btnok" style="display:none">{CHECK_W}</span><span>Conferma prenotazione</span></div>"""

PASSI = [
    ("Scegli la<br>{hl}", "materia", card1),
    ("Scegli giorno<br>e {hl}", "orario", card2),
    ("Nome, email<br>e {hl}", "conferma", card3),
]

stage_html = ""
for i, (tit, parola, card) in enumerate(PASSI):
    titolo = tit.format(hl=f'<span class="hl">{parola}</span>')
    stage_html += f"""<div class="stage" id="st{i}" style="position:absolute;left:80px;right:120px;top:500px;opacity:0">
  <div class="lab" style="font-weight:800;font-size:34px;letter-spacing:.14em;color:{HL}">PASSO {i + 1} DI 3</div>
  <div class="tit display" style="font-size:104px;margin-top:26px;color:#fff">{titolo}</div>
  <div class="card cardx" style="margin-top:56px;padding:40px 40px">{card}</div>
</div>"""

dots = "".join(f'<div id="d{i}" style="flex:1;height:14px;border-radius:7px;background:rgba(255,255,255,.25)"></div>' for i in range(3))

HTML = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{base_css()}</style></head><body>
<div class="frame blue-grid" style="width:{W}px;height:{H}px">
  <div style="position:absolute;left:80px;top:250px;display:flex;align-items:center;gap:18px;color:#fff">{symbol_cap(bg=NIGHT1, size=60)}<span style="font-weight:800;font-size:30px">Ripeti al Poliba</span></div>

  <div id="hook" style="position:absolute;left:80px;right:120px;top:560px">
    <span class="pill on-blue">Come funziona</span>
    <div class="display" style="font-size:124px;margin-top:44px;color:#fff">Prenoti una<br>lezione in<br><span class="hl">3 passaggi</span></div>
    <div class="body" style="margin-top:50px;font-size:46px;color:rgba(255,255,255,.92)">Con studenti che quell'esame l'hanno già passato.</div>
  </div>
  <div id="hookcap" style="position:absolute;left:50%;top:1290px;transform:translateX(-50%) rotate(-6deg)">{symbol_cap(bg=NIGHT1, size=240)}</div>

  <div id="dots" style="position:absolute;left:80px;right:120px;top:410px;display:flex;gap:16px;opacity:0">{dots}</div>
  {stage_html}

  <div id="end" style="position:absolute;left:80px;right:120px;top:520px;opacity:0">
    <span class="pill on-blue">Tutto qui</span>
    <div class="display" style="font-size:118px;margin-top:44px;color:#fff">Il prossimo<br>esame parte<br>da <span class="hl">qui</span>.</div>
    <div class="body" style="margin-top:44px;font-size:44px;color:rgba(255,255,255,.92)">Online o in presenza.<br>Pagamento in contanti.</div>
    <div class="card" style="margin-top:60px;padding:36px 44px;display:flex;align-items:center;gap:30px">
      {symbol_cap(bg=BLUE, size=110)}
      <div><div style="font-family:'InterD';font-weight:900;font-size:56px;color:{INK};letter-spacing:-0.02em">Ripeti al Poliba</div>
      <div style="font-weight:700;font-size:32px;color:{BLUE};margin-top:8px">prenota su ripetialpoliba.it · link in bio</div></div>
    </div>
  </div>
</div>
<script>
const HOOK={HOOK}, STEP={STEP}, TOTAL={TOTAL};
const BLUE='{BLUE}', HL='{HL}', INK='{INK}';
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
const clamp=x=>Math.min(Math.max(x,0),1);
const $=id=>document.getElementById(id);
function pick(el,on){{ el.style.background=on?BLUE:'#F1F5FD'; el.style.color=on?'#fff':INK; el.style.transform=on?'scale(1.04)':'none'; }}
function type(id,lt,start,dur){{
  const el=$(id), full=el.dataset.full, k=Math.round(full.length*clamp((lt-start)/dur));
  el.textContent=full.slice(0,k);
  $(id+'c').style.opacity=(lt>=start && lt<start+dur+0.15)?1:0;
}}
function setT(t){{
  const hook=$('hook'), cap=$('hookcap');
  const hIn=ease(t/0.5), hOut=clamp((t-(HOOK-0.3))/0.3);
  const hv=Math.min(hIn,1-hOut);
  hook.style.opacity=hv; cap.style.opacity=hv;
  hook.style.transform=`translateY(${{(1-hIn)*60 - hOut*40}}px)`;
  const endStart=HOOK+STEP*3;
  $('dots').style.opacity=(t>=HOOK-0.1 && t<endStart)?1:0;
  for(let i=0;i<3;i++){{
    const s=HOOK+i*STEP, lt=t-s, el=$('st'+i);
    const inn=ease(lt/0.4), out=clamp((lt-(STEP-0.25))/0.25);
    el.style.opacity=(lt>=0 && lt<STEP)?Math.min(inn,1-out):0;
    el.querySelector('.tit').style.transform=`translateY(${{(1-inn)*50}}px)`;
    const c=ease((lt-0.15)/0.45);
    el.querySelector('.cardx').style.transform=`translateY(${{(1-c)*80}}px)`;
    el.querySelector('.cardx').style.opacity=lt>=0?c:0;
    $('d'+i).style.background=(t>=s)?HL:'rgba(255,255,255,.25)';
  }}
  // passo 1: si seleziona Analisi 1
  const l1=t-HOOK;
  const on1=l1>=1.0;
  const m0=$('m0'); m0.style.background=on1?BLUE:'#F1F5FD'; m0.style.transform=on1?'scale(1.03)':'none';
  m0.querySelector('.mn').style.color=on1?'#fff':INK;
  m0.querySelector('.mi').style.background=on1?'rgba(255,255,255,.2)':'{SKY}';
  m0.querySelector('.mi svg').setAttribute('stroke',on1?'#fff':BLUE);
  const mc=m0.querySelector('.mc'); mc.style.opacity=on1?1:0; mc.style.background=on1?'{NIGHT1}':BLUE;
  // passo 2: mercoledì, poi le 16:00
  const l2=t-HOOK-STEP;
  for(let i=0;i<5;i++) pick($('g'+i), i===2 && l2>=0.9);
  for(let i=0;i<3;i++) pick($('o'+i), i===1 && l2>=1.6);
  // passo 3: nome, email, conferma
  const l3=t-HOOK-2*STEP;
  type('nome',l3,0.55,0.55);
  type('mail',l3,1.15,0.7);
  const pressed=l3>=2.05;
  $('btn').style.transform=(l3>=2.0 && l3<2.2)?'scale(.96)':'none';
  $('btn').style.background=pressed?'{NIGHT1}':BLUE;
  $('btnok').style.display=pressed?'inline-flex':'none';
  const end=$('end'), eIn=ease((t-endStart)/0.5);
  end.style.opacity=t>=endStart?eIn:0;
  end.style.transform=`translateY(${{(1-eIn)*60}}px)`;
}}
setT(0);
</script></body></html>"""


async def frames(out):
    (ROOT / "html" / "C5_reel.html").write_text(HTML, encoding="utf-8")
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(device_scale_factor=1, viewport={"width": W, "height": H})
        await pg.goto((ROOT / "html" / "C5_reel.html").as_uri())
        await pg.evaluate("document.fonts.ready")
        n = int(TOTAL * FPS)
        for k in range(n):
            await pg.evaluate(f"setT({k / FPS})")
            await pg.screenshot(path=str(out / f"f_{k:04d}.png"), type="png")
        # fermi immagine per il controllo a vista e la copertina
        for nome, t in [("copertina", 1.4), ("passo1", HOOK + 2.2), ("passo2", HOOK + STEP + 2.3), ("passo3", HOOK + 2 * STEP + 2.4), ("fine", TOTAL - 0.5)]:
            await pg.evaluate(f"setT({t})")
            await pg.screenshot(path=str(ROOT / "png" / f"C5_reel_{nome}.png"))
        await b.close()
    return n


def main():
    with tempfile.TemporaryDirectory() as d:
        out = pathlib.Path(d)
        n = asyncio.run(frames(out))
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(out / "f_%04d.png"),
            "-ss", OFFSET, "-t", f"{TOTAL:.2f}", "-i", str(ROOT / "musica" / "lofi-norm.flac"),
            "-filter_complex", f"[1:a]afade=t=in:st=0:d=0.5,afade=t=out:st={TOTAL - 1.0:.2f}:d=1.0[a]",
            "-map", "0:v", "-map", "[a]", "-t", f"{TOTAL:.2f}",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high",
            "-r", str(FPS), "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
            str(ROOT / "png" / "C5_reel.mp4"),
        ], check=True)
    print("frames", n, "seconds", TOTAL)


if __name__ == "__main__":
    main()
