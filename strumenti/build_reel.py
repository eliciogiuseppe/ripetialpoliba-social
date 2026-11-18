"""Reel 'I 5 stadi dello studente prima dell'appello' – kinetic text, 1080x1920, 30 fps."""
import asyncio
import pathlib
import subprocess
from playwright.async_api import async_playwright
from brand import *

ROOT = pathlib.Path(__file__).resolve().parent
FPS = 30
W, H = 1080, 1920

STAGES = [
    ("−30 giorni", "«Ho tutto il tempo del mondo.»", 8),
    ("−14 giorni", "«Inizio domani. Stavolta sul serio.»", 30),
    ("−7 giorni", "«Ma quanti esercizi ci sono nel programma?!»", 65),
    ("−2 giorni", "«Ok, mi serve qualcuno che me lo spieghi.»", 100),
    ("Giorno X", "«Ce la posso fare.»", 55),
]
HOOK = 2.8
STAGE = 2.3
END = 3.8
TOTAL = HOOK + STAGE * len(STAGES) + END

stage_html = ""
for i, (lab, quote, _) in enumerate(STAGES):
    stage_html += f"""<div class="stage" id="st{i}" style="position:absolute;left:80px;right:110px;top:640px;opacity:0">
  <div class="lab" style="display:inline-block;font-family:'InterD';font-weight:900;font-size:150px;letter-spacing:-0.03em;color:{HL};line-height:1">{lab}</div>
  <div class="quote card" style="margin-top:56px;padding:48px 52px;border-radius:48px 48px 48px 14px;font-weight:800;font-size:66px;line-height:1.18;color:{INK}">{quote}</div>
</div>"""

dots = "".join(f'<div class="dot" id="d{i}" style="width:120px;height:14px;border-radius:7px;background:rgba(255,255,255,.22)"></div>' for i in range(5))

HTML = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{base_css()}
.gridbg{{background-image:linear-gradient(rgba(255,255,255,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.05) 2px,transparent 2px);background-size:54px 54px}}
</style></head><body>
<div class="frame night" style="width:{W}px;height:{H}px">
  <div class="gridbg" style="position:absolute;inset:0"></div>
  <div style="position:absolute;left:80px;top:250px;display:flex;align-items:center;gap:18px;color:#fff">{symbol_cap(bg=BLUE, size=60)}<span style="font-weight:800;font-size:30px">Ripeti al Poliba</span></div>

  <div id="hook" style="position:absolute;left:80px;right:110px;top:560px">
    <span class="pill on-night">Diario di sessione</span>
    <div class="display" style="font-size:132px;margin-top:44px;color:#fff">I {'<span class="hl">5 stadi</span>'}<br>dello studente<br>prima<br>dell'appello</div>
  </div>

  <div id="dots" style="position:absolute;left:80px;top:470px;display:flex;gap:16px;opacity:0">{dots}</div>
  {stage_html}

  <div id="meter" style="position:absolute;left:80px;right:110px;top:1330px;opacity:0">
    <div style="display:flex;justify-content:space-between;font-weight:800;font-size:34px;color:#fff;letter-spacing:.04em"><span>LIVELLO DI PANICO</span><span id="pct">0%</span></div>
    <div style="margin-top:20px;height:40px;border-radius:20px;background:rgba(255,255,255,.18);overflow:hidden">
      <div id="bar" style="height:100%;width:0%;border-radius:20px;background:{HL}"></div>
    </div>
  </div>

  <div id="end" style="position:absolute;left:80px;right:110px;top:520px;opacity:0">
    <span class="pill on-night">Consiglio da collega</span>
    <div class="display" style="font-size:118px;margin-top:44px;color:#fff">Salta lo<br>stadio 4:<br>{'<span class="hl">prenota prima</span>'}.</div>
    <div class="card" style="margin-top:70px;padding:36px 44px;display:flex;align-items:center;gap:30px">
      {symbol_cap(bg=BLUE, size=110)}
      <div><div style="font-family:'InterD';font-weight:900;font-size:58px;color:{INK};letter-spacing:-0.02em">Ripeti al Poliba</div>
      <div style="font-weight:700;font-size:32px;color:{BLUE};margin-top:8px">prenota su ripetialpoliba.it</div></div>
    </div>
  </div>
</div>
<script>
const HOOK={HOOK}, STAGE={STAGE}, TOTAL={TOTAL};
const LEVELS={[s[2] for s in STAGES]};
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
const clamp=x=>Math.min(Math.max(x,0),1);
function setT(t){{
  const hook=document.getElementById('hook');
  const hIn=ease(t/0.5), hOut=clamp((t-(HOOK-0.3))/0.3);
  hook.style.opacity=Math.min(hIn,1-hOut);
  hook.style.transform=`translateY(${{(1-hIn)*60 - hOut*40}}px)`;
  const endStart=HOOK+STAGE*LEVELS.length;
  const inStages=t>=HOOK-0.1 && t<endStart;
  const dots=document.getElementById('dots'); dots.style.opacity=inStages?1:0;
  const meter=document.getElementById('meter'); meter.style.opacity=inStages?1:0;
  let level=0;
  for(let i=0;i<LEVELS.length;i++){{
    const s=HOOK+i*STAGE, lt=t-s;
    const el=document.getElementById('st'+i);
    const inn=ease(lt/0.4), out=clamp((lt-(STAGE-0.25))/0.25);
    const vis=(lt>=0 && lt<STAGE)?Math.min(inn,1-out):0;
    el.style.opacity=vis;
    el.querySelector('.lab').style.transform=`translateY(${{(1-inn)*50}}px)`;
    const q=ease((lt-0.2)/0.4);
    el.querySelector('.quote').style.transform=`scale(${{0.92+0.08*q}})`;
    el.querySelector('.quote').style.opacity=lt>=0?q:0;
    document.getElementById('d'+i).style.background = (t>=s)?'{HL}':'rgba(255,255,255,.22)';
    if(lt>=0){{ const prev=i?LEVELS[i-1]:0; level=prev+(LEVELS[i]-prev)*ease(lt/0.7); }}
  }}
  document.getElementById('bar').style.width=level+'%';
  document.getElementById('pct').textContent=Math.round(level)+'%';
  const end=document.getElementById('end');
  const eIn=ease((t-endStart)/0.5);
  end.style.opacity=t>=endStart?eIn:0;
  end.style.transform=`translateY(${{(1-eIn)*60}}px)`;
}}
setT(0);
</script></body></html>"""


async def main():
    out = ROOT / "reel"
    for f in out.glob("f_*.png"):
        f.unlink()
    (ROOT / "html" / "C4_reel.html").write_text(HTML, encoding="utf-8")
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(device_scale_factor=1, viewport={"width": W, "height": H})
        await pg.goto((ROOT / "html" / "C4_reel.html").as_uri())
        await pg.evaluate("document.fonts.ready")
        n = int(TOTAL * FPS)
        for k in range(n):
            await pg.evaluate(f"setT({k / FPS})")
            await pg.screenshot(path=str(out / f"f_{k:04d}.png"), type="png")
        # cover = a still of the hook
        await pg.evaluate("setT(1.4)")
        await pg.screenshot(path=str(ROOT / "png" / "C4_reel_copertina.png"))
        await b.close()
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(out / "f_%04d.png"),
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-shortest", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-r", str(FPS), "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
        str(ROOT / "png" / "C4_reel.mp4"),
    ], check=True)
    print("frames", n, "seconds", TOTAL)


asyncio.run(main())
