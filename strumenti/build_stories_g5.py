# Stories del 23/11 · Domande frequenti (3 stories), senza adesivi interattivi.
# Fatti dal sito: lezioni online o in presenza (luogo scelto dal tutor),
# pagamento in contanti, lezione spostabile dall'area personale.
from brand import *
from render import render
from build_stories import W, H, hl
from build_stories_g2_g4 import blu, carta, url_pill


def due_modi(top=1180):
    def box(ic, testo):
        return f"""<div class="card" style="flex:1;padding:44px 30px;display:flex;flex-direction:column;align-items:center;gap:22px">
  <div style="width:120px;height:120px;border-radius:34px;background:{SKY};display:flex;align-items:center;justify-content:center">{icon(ic, 68, BLUE, 2.1)}</div>
  <div style="font-family:'InterD';font-weight:900;font-size:50px;color:{INK};letter-spacing:-0.02em">{testo}</div></div>"""
    return f'<div style="position:absolute;left:80px;right:80px;top:{top}px;display:flex;gap:30px">{box("laptop", "Online")}{box("pin", "In presenza")}</div>'


def contanti():
    return f"""<div class="card" style="margin-top:60px;padding:50px 48px;display:flex;align-items:center;gap:40px">
  <div style="flex:none;width:150px;height:150px;border-radius:42px;background:{BLUE};display:flex;align-items:center;justify-content:center">{icon('cash', 88, '#fff', 2.0)}</div>
  <div><div class="body" style="font-size:36px;color:{MUTED}">Pagamento delle lezioni</div>
  <div style="font-family:'InterD';font-weight:900;font-size:76px;color:{INK};letter-spacing:-0.02em;margin-top:6px">In contanti</div></div>
</div>
<div class="body" style="margin-top:50px;font-size:40px;color:{MUTED}">Lezioni individuali, online o in presenza.</div>
<div style="margin-top:110px;display:flex;justify-content:center"><div style="transform:rotate(-6deg)">{symbol_cap(bg=BLUE, size=260)}</div></div>"""


STORIES = {
    'G5_story_1': lambda: blu('Domande frequenti', f"Online o in<br>{hl('presenza')}?", "Come preferisci. In presenza, il luogo lo sceglie il tutor.", due_modi(), size=118),
    'G5_story_2': lambda: carta('Domande frequenti', f"Come si<br>{hl('paga')}?", contanti(), size=124),
    'G5_story_3': lambda: blu('Domande frequenti', f"Hai un<br>{hl('imprevisto')}?", "Se cambi programma, sposti la lezione dalla tua area personale.", url_pill(1230), size=124),
}

if __name__ == '__main__':
    render([(k, f(), W, H) for k, f in STORIES.items()])
    from PIL import Image
    ims = [Image.open(f'png/G5_story_{i}.png').convert('RGB') for i in (1, 2, 3)]
    s = Image.new('RGB', (W * 3, H), 'white')
    for k, im in enumerate(ims):
        s.paste(im, (k * W, 0))
    s.resize((W * 3 // 2, H // 2)).save('png/_s_g5.png')
    print('ok')
