# Stories del 20, 21 e 22/11 (3 al giorno), senza adesivi interattivi.
from brand import *
from render import render
from build_stories import W, H, hl, story_top
from build_stories_g1 import passo


def blu(pill, titolo_html, testo, extra='', size=120):
    return page(f"""{story_top('blue')}
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">{pill}</span>
  <div class="display" style="font-size:{size}px;margin-top:44px">{titolo_html}</div>
  <div class="body" style="margin-top:48px;font-size:46px;color:rgba(255,255,255,.92)">{testo}</div>
</div>{extra}""", W, H, "blue-grid")


def carta(pill, titolo_html, corpo, size=108):
    return page(f"""{story_top('paper')}
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">{pill}</span>
  <div class="display" style="font-size:{size}px;margin-top:44px;color:{INK}">{titolo_html}</div>
  {corpo}
</div>""", W, H, "paper")


def cappello(top=1120):
    return f'<div style="position:absolute;left:50%;top:{top}px;transform:translateX(-50%) rotate(-6deg)">{symbol_cap(bg=NIGHT1, size=300)}</div>'


def url_pill(top=1180, sotto='link in bio'):
    return f"""<div style="position:absolute;left:80px;right:80px;top:{top}px;display:flex;flex-direction:column;align-items:center;gap:26px">
  <div style="background:#fff;color:{BLUE};border-radius:999px;padding:34px 64px;font-family:'InterD';font-weight:900;font-size:58px;letter-spacing:-0.01em">ripetialpoliba.it</div>
  <div style="font-weight:700;font-size:36px;color:rgba(255,255,255,.85)">{sotto}</div>
</div>"""


def scheda(testo, top=36):
    return f'<div class="card" style="margin-top:{top}px;padding:44px 48px"><div class="body" style="font-size:42px;color:{INK}"><b style="color:{BLUE}">Fai così:</b> {testo}</div></div>'


def riga_stadio(n, testo):
    return f"""<div style="display:flex;align-items:center;gap:30px;margin-top:26px">
  <div style="flex:none;width:84px;height:84px;border-radius:26px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font-family:'InterD';font-weight:900;font-size:46px">{n}</div>
  <div class="body" style="font-size:42px;color:{INK};font-weight:600">{testo}</div></div>"""


STORIES = {
    # 20/11 · C2 Diventa tutor
    'G2_story_1': lambda: blu('Cerchiamo tutor', f"Quell'esame<br>l'hai {hl('passato')}?", "Ora puoi spiegarlo a chi lo deve ancora dare.", cappello(), size=118),
    'G2_story_2': lambda: carta('Diventa tutor', f"Su Ripeti al Poliba<br>scegli {hl('tu')}", f"""<div style="margin-top:36px">
      {passo(1, 'Le materie', 'Proponi quelle che conosci')}
      {passo(2, 'Gli orari', 'Quando ti è comodo')}
      {passo(3, 'Il luogo', 'Online o in presenza')}</div>""", size=100),
    'G2_story_3': lambda: blu('Iscrizione gratuita', f"Candidati<br>{hl('oggi')}", "Su ripetialpoliba.it clicca «Registrati come Tutor». Ogni profilo viene approvato prima di andare online.", url_pill(1250)),
    # 21/11 · C3 Metodo Poli
    'G3_story_1': lambda: carta('Metodo Poli', f"5 errori che<br>allungano la<br>tua {hl('sessione')}", f'<div class="body" style="margin-top:44px;font-size:44px;color:{MUTED}">Il terzo lo facciamo quasi tutti. Li trovi nel nuovo post.</div>', size=112),
    'G3_story_2': lambda: carta('Errore n. 1', f"Rileggere invece<br>di {hl('ripetere')}", scheda("chiudi il quaderno e riscrivi a memoria definizioni e passaggi, poi controlla cosa ti manca.", 56), size=104),
    'G3_story_3': lambda: blu('Prima dell\'appello', f"Salvalo per<br>la {hl('sessione')}", "E se un esame proprio non torna, prenota un tutor che l'ha già passato.", url_pill(1210), size=120),
    # 22/11 · C4 Reel I 5 stadi
    'G4_story_1': lambda: blu('Diario di sessione', f"I 5 stadi dello<br>studente prima<br>dell'{hl('appello')}", "Il nuovo Reel è sul profilo.", cappello(1160), size=108),
    'G4_story_2': lambda: carta('Sii sincero', f"A che stadio<br>{hl('sei')}?", f"""<div style="margin-top:30px">
      {riga_stadio(1, '«Ho tutto il tempo del mondo»')}
      {riga_stadio(2, '«Inizio domani. Sul serio.»')}
      {riga_stadio(3, '«Quanti esercizi ci sono?!»')}
      {riga_stadio(4, '«Mi serve chi me lo spieghi»')}
      {riga_stadio(5, '«Ce la posso fare»')}</div>
      <div class="body" style="margin-top:40px;font-size:38px;color:{MUTED}">Scrivilo nei commenti del Reel.</div>""", size=112),
    'G4_story_3': lambda: blu('Consiglio da collega', f"Salta lo<br>{hl('stadio 4')}", "Prenota prima, con chi l'esame l'ha già passato.", url_pill(1180), size=130),
}

if __name__ == '__main__':
    render([(k, f(), W, H) for k, f in STORIES.items()])
    from PIL import Image
    for g in (2, 3, 4):
        ims = [Image.open(f'png/G{g}_story_{i}.png').convert('RGB') for i in (1, 2, 3)]
        s = Image.new('RGB', (W * 3, H), 'white')
        for k, im in enumerate(ims):
            s.paste(im, (k * W, 0))
        s.resize((W, H // 3)).save(f'png/_s_g{g}.png')
    print('ok')
