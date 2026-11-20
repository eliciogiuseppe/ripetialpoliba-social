"""Reel a testo cinetico (stile C4), 1080x1920, 30 fps, con la musica originale.

Uso: python3 build_reel_cinetico.py C7|C10
Uscita: png/<NOME>_reel.mp4 e png/<NOME>_reel_copertina.png (+ fermi immagine per il controllo).
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


def hl(t):
    return f'<span class="hl">{t}</span>'


REELS = {
    # 25/11 · I 5 tipi di studenti in aula studio
    "C7": dict(
        pill="Aula studio", titolo=f"I 5 tipi di<br>studenti in<br>{hl('aula studio')}", titolo_size=124,
        etichetta_size=104, meter="CONCENTRAZIONE",
        voci=[
            ("L'evidenziatore", "«Importante. Anche questo. Pure questo.»", 40),
            ("Il ritardatario", "Arriva alle 9, apre il libro alle 11.", 10),
            ("Il pianificatore", "Terzo piano di studio della settimana.", 25),
            ("Quello della pausa", "«Solo cinque minuti.» Un'ora dopo è ancora al bar.", 15),
            ("Quello che spiega", "Spiega il programma a tutto il tavolo. E all'esame vola.", 95),
        ],
        fine_pill="E tu?", fine=f"Tu quale<br>{hl('sei')}?", fine_size=150,
        fine_sotto="Scrivilo nei commenti.", offset="3",
    ),
    # 28/11 · Diario di sessione: il sabato dello studente
    "C10": dict(
        pill="Diario di sessione", titolo=f"Il sabato<br>dello<br>{hl('studente')}", titolo_size=140,
        etichetta_size=150, meter="MOTIVAZIONE",
        voci=[
            ("9:00", "«Oggi studio tutto il giorno.»", 100),
            ("10:30", "«Prima sistemo la scrivania.»", 85),
            ("13:00", "«Pausa pranzo. Me la sono meritata.»", 60),
            ("16:00", "«Ok, adesso si inizia sul serio.»", 75),
            ("21:00", "«Domani recupero.»", 20),
        ],
        fine_pill="Consiglio da collega", fine=f"Meglio 3 ore<br>vere che 12<br>{hl('promesse')}.", fine_size=118,
        fine_sotto=None, offset="40",
    ),
}

HOOK, VOCE, END = 2.8, 2.5, 3.8


def html(c):
    n = len(c["voci"])
    voci = ""
    for i, (lab, frase, _) in enumerate(c["voci"]):
        voci += f"""<div class="stage" id="st{i}" style="position:absolute;left:80px;right:120px;top:600px;opacity:0">
  <div class="lab" style="font-family:'InterD';font-weight:900;font-size:{c['etichetta_size']}px;letter-spacing:-0.03em;color:{HL};line-height:1">{lab}</div>
  <div class="quote card" style="margin-top:52px;padding:46px 52px;border-radius:48px 48px 48px 14px;font-weight:800;font-size:62px;line-height:1.18;color:{INK}">{frase}</div>
</div>"""
    dots = "".join(f'<div id="d{i}" style="flex:1;height:14px;border-radius:7px;background:rgba(255,255,255,.22)"></div>' for i in range(n))
    sotto = f'<div class="body" style="margin-top:36px;font-size:48px;color:rgba(255,255,255,.92)">{c["fine_sotto"]}</div>' if c["fine_sotto"] else ""
    total = HOOK + VOCE * n + END
    return total, f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{base_css()}
.gridbg{{background-image:linear-gradient(rgba(255,255,255,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.05) 2px,transparent 2px);background-size:54px 54px}}
</style></head><body>
<div class="frame night" style="width:{W}px;height:{H}px">
  <div class="gridbg" style="position:absolute;inset:0"></div>
  <div style="position:absolute;left:80px;top:250px;display:flex;align-items:center;gap:18px;color:#fff">{symbol_cap(bg=BLUE, size=60)}<span style="font-weight:800;font-size:30px">Ripeti al Poliba</span></div>
  <div id="hook" style="position:absolute;left:80px;right:120px;top:560px">
    <span class="pill on-night">{c['pill']}</span>
    <div class="display" style="font-size:{c['titolo_size']}px;margin-top:44px;color:#fff">{c['titolo']}</div>
  </div>
  <div id="dots" style="position:absolute;left:80px;right:120px;top:470px;display:flex;gap:16px;opacity:0">{dots}</div>
  {voci}
  <div id="meter" style="position:absolute;left:80px;right:120px;top:1360px;opacity:0">
    <div style="display:flex;justify-content:space-between;font-weight:800;font-size:34px;color:#fff;letter-spacing:.04em"><span>{c['meter']}</span><span id="pct">0%</span></div>
    <div style="margin-top:20px;height:40px;border-radius:20px;background:rgba(255,255,255,.18);overflow:hidden">
      <div id="bar" style="height:100%;width:0%;border-radius:20px;background:{HL}"></div>
    </div>
  </div>
  <div id="end" style="position:absolute;left:80px;right:120px;top:520px;opacity:0">
    <span class="pill on-night">{c['fine_pill']}</span>
    <div class="display" style="font-size:{c['fine_size']}px;margin-top:44px;color:#fff">{c['fine']}</div>
    {sotto}
    <div class="card" style="margin-top:64px;padding:36px 44px;display:flex;align-items:center;gap:30px">
      {symbol_cap(bg=BLUE, size=110)}
      <div><div style="font-family:'InterD';font-weight:900;font-size:56px;color:{INK};letter-spacing:-0.02em">Ripeti al Poliba</div>
      <div style="font-weight:700;font-size:32px;color:{BLUE};margin-top:8px">prenota su ripetialpoliba.it · link in bio</div></div>
    </div>
  </div>
</div>
<script>
const HOOK={HOOK}, STAGE={VOCE}, LEVELS={[v[2] for v in c['voci']]};
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
const clamp=x=>Math.min(Math.max(x,0),1);
function setT(t){{
  const hook=document.getElementById('hook');
  const hIn=ease(t/0.5), hOut=clamp((t-(HOOK-0.3))/0.3);
  hook.style.opacity=Math.min(hIn,1-hOut);
  hook.style.transform=`translateY(${{(1-hIn)*60 - hOut*40}}px)`;
  const endStart=HOOK+STAGE*LEVELS.length;
  const inStages=t>=HOOK-0.1 && t<endStart;
  document.getElementById('dots').style.opacity=inStages?1:0;
  document.getElementById('meter').style.opacity=inStages?1:0;
  let level=0;
  for(let i=0;i<LEVELS.length;i++){{
    const s=HOOK+i*STAGE, lt=t-s, el=document.getElementById('st'+i);
    const inn=ease(lt/0.4), out=clamp((lt-(STAGE-0.25))/0.25);
    el.style.opacity=(lt>=0 && lt<STAGE)?Math.min(inn,1-out):0;
    el.querySelector('.lab').style.transform=`translateY(${{(1-inn)*50}}px)`;
    const q=ease((lt-0.2)/0.4);
    el.querySelector('.quote').style.transform=`scale(${{0.92+0.08*q}})`;
    el.querySelector('.quote').style.opacity=lt>=0?q:0;
    document.getElementById('d'+i).style.background=(t>=s)?'{HL}':'rgba(255,255,255,.22)';
    if(lt>=0){{ const prev=i?LEVELS[i-1]:0; level=prev+(LEVELS[i]-prev)*ease(lt/0.7); }}
  }}
  document.getElementById('bar').style.width=level+'%';
  document.getElementById('pct').textContent=Math.round(level)+'%';
  const end=document.getElementById('end'), eIn=ease((t-endStart)/0.5);
  end.style.opacity=t>=endStart?eIn:0;
  end.style.transform=`translateY(${{(1-eIn)*60}}px)`;
}}
setT(0);
</script></body></html>"""


async def frames(nome, doc, total, out, n_voci):
    hp = ROOT / "html" / f"{nome}_reel.html"
    hp.write_text(doc, encoding="utf-8")
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(device_scale_factor=1, viewport={"width": W, "height": H})
        await pg.goto(hp.as_uri())
        await pg.evaluate("document.fonts.ready")
        n = int(total * FPS)
        for k in range(n):
            await pg.evaluate(f"setT({k / FPS})")
            await pg.screenshot(path=str(out / f"f_{k:04d}.png"), type="png")
        fermi = [("copertina", 1.4)] + [(f"voce{i + 1}", HOOK + i * VOCE + 1.6) for i in range(n_voci)] + [("fine", total - 0.5)]
        for f, t in fermi:
            await pg.evaluate(f"setT({t})")
            await pg.screenshot(path=str(ROOT / "png" / f"{nome}_reel_{f}.png"))
        await b.close()
    return n


def main(nome):
    c = REELS[nome]
    total, doc = html(c)
    with tempfile.TemporaryDirectory() as d:
        out = pathlib.Path(d)
        n = asyncio.run(frames(nome, doc, total, out, len(c["voci"])))
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(out / "f_%04d.png"),
            "-ss", c["offset"], "-t", f"{total:.2f}", "-i", str(ROOT / "musica" / "lofi-norm.flac"),
            "-filter_complex", f"[1:a]afade=t=in:st=0:d=0.5,afade=t=out:st={total - 1.0:.2f}:d=1.0[a]",
            "-map", "0:v", "-map", "[a]", "-t", f"{total:.2f}",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high",
            "-r", str(FPS), "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
            str(ROOT / "png" / f"{nome}_reel.mp4"),
        ], check=True)
    print(nome, "frames", n, "secondi", round(total, 2))


if __name__ == "__main__":
    for nome in sys.argv[1:] or REELS:
        main(nome)
