# Stories del 19/11 (giorno del lancio): senza adesivi interattivi, perché
# vengono pubblicate via API (Windsor.ai), che non li supporta.
from brand import *
from render import render
from build_stories import W, H, hl, story_top, s1


def passo(n, titolo, testo):
    return f"""<div class="card" style="display:flex;align-items:center;gap:40px;padding:44px 48px;margin-top:34px">
  <div style="flex:none;width:110px;height:110px;border-radius:32px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font-family:'InterD';font-weight:900;font-size:64px">{n}</div>
  <div><div style="font-family:'InterD';font-weight:900;font-size:52px;color:{INK};letter-spacing:-0.02em">{titolo}</div>
  <div class="body" style="font-size:36px;color:{MUTED};margin-top:6px">{testo}</div></div>
</div>"""


def come_funziona():
    inner = f"""{story_top('paper')}
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Come funziona</span>
  <div class="display" style="font-size:112px;margin-top:44px;color:{INK}">Prenoti in<br>{hl('3 passaggi')}</div>
  <div style="margin-top:36px">
    {passo(1, 'La materia', 'Scegli l\'esame da preparare')}
    {passo(2, 'Giorno e orario', 'Scegli quando ti è comodo')}
    {passo(3, 'Conferma', 'Basta la tua email')}
  </div>
  <div class="body" style="margin-top:44px;font-size:38px;color:{MUTED}">Online o in presenza · pagamento in contanti</div>
</div>"""
    return page(inner, W, H, "paper")


def prenota():
    inner = f"""{story_top('blue')}
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">Prima dell'appello</span>
  <div class="display" style="font-size:130px;margin-top:44px">Ti serve<br>una {hl('mano')}?</div>
  <div class="body" style="margin-top:48px;font-size:46px;color:rgba(255,255,255,.92)">Prenota una lezione con chi l'ha già passato. Online o in presenza, scegli tu.</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:1150px;display:flex;justify-content:center">
  <div style="background:#fff;color:{BLUE};border-radius:999px;padding:34px 64px;font-family:'InterD';font-weight:900;font-size:58px;letter-spacing:-0.01em">ripetialpoliba.it</div>
</div>"""
    return page(inner, W, H, "blue-grid")


if __name__ == "__main__":
    render([("G1_story_1", s1(), W, H), ("G1_story_2", come_funziona(), W, H), ("G1_story_3", prenota(), W, H)])
    from PIL import Image
    ims = [Image.open(f"png/G1_story_{i}.png") for i in (1, 2, 3)]
    s = Image.new("RGB", (W * 3, H), "white")
    for k, im in enumerate(ims):
        s.paste(im.convert("RGB"), (k * W, 0))
    s.resize((W * 3 // 3, H // 3)).save("png/_s_g1.png")
    print("ok")
