from brand import *
from render import render

W, H = 1080, 1920


def hl(t):
    return f'<span class="hl">{t}</span>'


CUE_ARROW = '<svg width="70" height="90" viewBox="0 0 70 90" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"><path d="M14 8 C 40 20, 50 45, 36 78"/><path d="M22 66 L36 80 L50 64"/></svg>'


def cue(text, color):
    return f'<div style="display:flex;align-items:flex-end;gap:16px;color:{color};font-weight:800;font-size:40px">{text} {CUE_ARROW}</div>'


def story_top(theme):
    color = INK if theme == "paper" else "#fff"
    bg = NIGHT1 if theme == "blue" else BLUE
    # sits just below Instagram's top UI (progress bar + account row)
    return f'<div style="position:absolute;left:80px;top:260px;display:flex;align-items:center;gap:18px;color:{color}">{symbol_cap(bg=bg, size=60)}<span style="font-weight:800;font-size:30px">Ripeti al Poliba</span></div>'


def s1():
    inner = f"""{story_top('blue')}
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">Novità al Poli</span>
  <div class="display" style="font-size:128px;margin-top:44px">Ripeti al Poliba<br>è {hl('online')}</div>
  <div class="body" style="margin-top:48px;font-size:46px;color:rgba(255,255,255,.92)">Ripetizioni per gli esami del Poliba, con studenti che li hanno già passati.</div>
</div>
<div style="position:absolute;left:50%;top:1150px;transform:translateX(-50%) rotate(-6deg)">{symbol_cap(bg=NIGHT1, size=300)}</div>
<div style="position:absolute;left:80px;right:80px;bottom:380px;display:flex;justify-content:center"><div style="font-weight:700;font-size:36px;color:rgba(255,255,255,.85)">Tocca per scoprire come funziona →</div></div>"""
    return page(inner, W, H, "blue-grid")


def s2():
    inner = f"""{story_top('paper')}
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">La domanda della settimana</span>
  <div class="display" style="font-size:112px;margin-top:44px">Qual è l'esame<br>che ti fa più<br>{hl('paura')}?</div>
  <div class="body" style="margin-top:40px;font-size:42px;color:{MUTED}">Vota, poi ti diciamo i risultati.</div>
</div>
<div style="position:absolute;right:120px;top:1110px">{cue('Vota qui', BLUE)}</div>"""
    return page(inner, W, H, "paper")


def s3():
    inner = f"""{story_top('paper')}
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Quiz lampo · Analisi 1</span>
  <div class="display" style="font-size:100px;margin-top:44px">Qual è la<br>{hl('derivata')} di</div>
  <div class="card" style="margin-top:50px;padding:46px 0;text-align:center;font-family:'InterD';font-weight:800;font-size:110px;letter-spacing:-0.01em;color:{INK}">f(x) = x · e<sup style="font-size:64px;vertical-align:52px">x</sup>?</div>
</div>
<div style="position:absolute;right:120px;top:1150px">{cue('Rispondi qui', BLUE)}</div>"""
    return page(inner, W, H, "paper")


def s4():
    inner = f"""{story_top('blue')}
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">Prima dell'appello</span>
  <div class="display" style="font-size:130px;margin-top:44px">Ti serve<br>una {hl('mano')}?</div>
  <div class="body" style="margin-top:48px;font-size:46px;color:rgba(255,255,255,.92)">Prenota una lezione con chi l'ha già passato. Online o in presenza, scegli tu.</div>
</div>
<div style="position:absolute;right:120px;top:1170px">{cue('Tocca il link', HL)}</div>"""
    return page(inner, W, H, "blue-grid")


if __name__ == "__main__":
    jobs = [(f"C5_stories_{i}", f(), W, H) for i, f in enumerate([s1, s2, s3, s4], 1)]
    render(jobs)
    print("done")
