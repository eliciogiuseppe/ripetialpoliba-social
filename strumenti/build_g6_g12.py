# Post e stories dal 24 al 30/11/2026 (C6–C12, G6–G12).
# I Reel C7 e C10 sono in build_reel_cinetico.py.
# Solo fatti verificati sul sito: lezioni individuali, online o in presenza (luogo scelto
# dal tutor), pagamento in contanti, lezione spostabile dall'area personale, chat con il tutor.
from brand import *
from render import render
import build_posts as P
from build_posts import top_bar, swipe, icon_dot, link_card, bubble, step
import build_stories as S
from build_stories_g2_g4 import blu, carta, url_pill, scheda, riga_stadio, cappello

PW, PH = P.W, P.H          # post 1080x1350
SW, SH = S.W, S.H          # story 1080x1920
hl = P.hl

LENTE = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg>'


def nota(testo, colore=MUTED, top=36):
    return f'<div style="margin-top:{top}px;font-weight:600;font-size:31px;line-height:1.4;color:{colore}">{testo}</div>'


def riga(ic, titolo, sub=None, last=False, pad=20):
    s = f'<div style="font-weight:500;font-size:29px;color:{MUTED};margin-top:4px">{sub}</div>' if sub else ""
    border = "" if last else "border-bottom:2px solid #EEF2F6;"
    return f"""<div style="display:flex;align-items:center;gap:30px;padding:{pad}px 0;{border}">
  {icon_dot(ic, SKY, BLUE, 80, 42)}
  <div><div style="font-weight:700;font-size:38px;color:{INK}">{titolo}</div>{s}</div>
</div>"""


def fai_cosi(testo, top=56, etichetta="FAI COSÌ"):
    return f"""<div class="card" style="margin-top:{top}px;padding:46px 50px">
  <span style="display:inline-block;background:{HL};color:{INK};font-weight:800;font-size:26px;letter-spacing:.14em;padding:12px 24px;border-radius:999px">{etichetta}</span>
  <div style="font-weight:700;font-size:41px;line-height:1.32;color:{INK};margin-top:24px">{testo}</div>
</div>"""


def cta_blu(pag, pill, titolo_html, testo, invito):
    inner = f"""{top_bar(pag, 'blue')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">{pill}</span>
  <div class="display" style="font-size:118px;margin-top:40px">{titolo_html}</div>
  <div class="body" style="margin-top:40px;color:rgba(255,255,255,.9)">{testo}</div>
  <div style="margin-top:60px">{link_card()}</div>
</div>
<div style="position:absolute;right:-90px;bottom:-110px;opacity:.13;transform:rotate(-12deg)">{SYMBOLS['tocco'](bg='#FFFFFF', size=620, bg_on=False)}</div>
<div style="position:absolute;left:80px;bottom:100px;display:inline-flex;align-items:center;gap:14px;border:3px solid rgba(255,255,255,.55);color:#fff;font-weight:700;font-size:30px;padding:18px 30px;border-radius:999px">{invito}</div>"""
    return page(inner, PW, PH, "blue-grid")


# ------------------------------------------------ «Materia sotto la lente» (C6 Analisi 1, C12 Fisica 1)
def lente_cover(materia, sotto):
    inner = f"""{top_bar('1/6', 'blue')}
<div style="position:absolute;right:-60px;bottom:-90px;opacity:.14;transform:rotate(-8deg)">{LENTE.format(s=640)}</div>
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">Materia sotto la lente</span>
  <div class="display" style="font-size:168px;margin-top:50px">{hl(materia)}</div>
  <div class="body" style="margin-top:56px;max-width:860px;color:rgba(255,255,255,.92)">{sotto}</div>
  <div style="margin-top:34px;display:flex;flex-direction:column;gap:18px;font-weight:800;font-size:42px;color:#fff">
    <div>→ Gli argomenti chiave</div><div>→ Dove ci si blocca</div><div>→ Come prepararla</div></div>
</div>
<div style="position:absolute;left:80px;bottom:110px">{swipe()}</div>"""
    return page(inner, PW, PH, "blue-grid")


def lente_argomenti(materia, argomenti):
    righe = "".join(riga('book', a, last=(i == len(argomenti) - 1)) for i, a in enumerate(argomenti))
    inner = f"""{top_bar('2/6', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Gli argomenti chiave</span>
  <div class="display" style="font-size:96px;margin-top:36px">Cosa c'è in<br>{hl(materia)}</div>
  <div class="card" style="margin-top:44px;padding:8px 48px">{righe}</div>
  {nota("Il programma esatto cambia da corso a corso: controlla quello del tuo docente.")}
</div>"""
    return page(inner, PW, PH, "paper")


def fumetto(testo, offset):
    return f'<div class="card" style="margin-left:{offset}px;align-self:flex-start;padding:30px 40px;border-radius:40px 40px 40px 12px;font-weight:700;font-size:42px;line-height:1.25;color:{INK};white-space:nowrap">{testo}</div>'


def lente_blocchi(frasi):
    inner = f"""{top_bar('3/6', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Dove ci si blocca</span>
  <div class="display" style="font-size:104px;margin-top:40px">I punti che<br>fanno {hl('sudare')}</div>
  <div style="display:flex;flex-direction:column;gap:30px;margin-top:70px">
    {fumetto(frasi[0], 0)}
    {fumetto(frasi[1], 70)}
    {fumetto(frasi[2], 30)}
  </div>
  {nota("Capita a tutti. Si sbloccano con metodo e con qualcuno che te li spiega.", top=64)}
</div>"""
    return page(inner, PW, PH, "paper")


def lente_metodo(consigli):
    inner = f"""{top_bar('4/6', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Come prepararla</span>
  <div class="display" style="font-size:104px;margin-top:40px">3 regole<br>da {hl('collega')}</div>
  <div style="display:flex;flex-direction:column;gap:28px;margin-top:60px">
    {step(1, consigli[0])}
    {step(2, consigli[1])}
    {step(3, consigli[2])}
  </div>
</div>"""
    return page(inner, PW, PH, "paper")


def lente_esercizio(pre, chiave, perche, testo):
    inner = f"""{top_bar('5/6', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Da fare ogni giorno</span>
  <div class="display" style="font-size:100px;margin-top:40px">{pre}<br>{hl(chiave)}</div>
  <div class="body" style="margin-top:40px;font-size:40px;color:#344054">{perche}</div>
  {fai_cosi(testo, 60)}
</div>"""
    return page(inner, PW, PH, "paper")


ANALISI1 = dict(
    materia="Analisi 1",
    sotto="Nel post:",
    argomenti=["Limiti", "Derivate", "Studio di funzione", "Integrali"],
    frasi=["«È una forma indeterminata?»", "«Lo studio di funzione è infinito.»", "«Per parti o per sostituzione?»"],
    consigli=["Parti dai limiti: tornano in tutto il corso", "Fai studi di funzione completi, dall'inizio alla fine", "Allenati sui vecchi testi d'esame, cronometrati"],
    esercizio=("La pagina delle", "formule", "Derivate e integrali fondamentali devono uscirti senza pensarci, così all'esame ragioni sul resto.",
               "Scrivi a memoria su una pagina le derivate e gli integrali fondamentali. Controlla, correggi e rifalla ogni giorno per una settimana."),
)

FISICA1 = dict(
    materia="Fisica 1",
    sotto="Nel post:",
    argomenti=["Cinematica", "Dinamica e leggi di Newton", "Lavoro ed energia", "Quantità di moto e urti", "Corpo rigido"],
    frasi=["«Che sistema di riferimento scelgo?»", "«Quali forze agiscono qui?»", "«Ma l'energia si conserva o no?»"],
    consigli=["Disegna sempre il diagramma delle forze", "Risolvi in lettere, i numeri solo alla fine", "Alla fine, controlla<br>le unità di misura"],
    esercizio=("Prima delle equazioni,", "ragiona", "Tanti errori nascono da un'equazione scritta prima di aver capito cosa succede.",
               "Per ogni esercizio scrivi in una riga cosa si conserva (energia, quantità di moto) e perché. Solo dopo imposta le equazioni."),
)


def lente(prefisso, d):
    return [
        (f"{prefisso}_1", lente_cover(d["materia"], d["sotto"])),
        (f"{prefisso}_2", lente_argomenti(d["materia"], d["argomenti"])),
        (f"{prefisso}_3", lente_blocchi(d["frasi"])),
        (f"{prefisso}_4", lente_metodo(d["consigli"])),
        (f"{prefisso}_5", lente_esercizio(*d["esercizio"])),
        (f"{prefisso}_6", cta_blu('6/6', 'Prima dell\'appello', f"{d['materia']}<br>non {hl('torna')}?",
                                  "Prenota un tutor che l'ha già passata. Lezioni individuali, online o in presenza.",
                                  "Mandalo a chi la deve dare")),
    ]


# ------------------------------------------------ C8 · Il richiamo attivo in un'immagine
def mossa(n, titolo, sub, ic):
    return f"""<div class="card" style="padding:30px 34px;display:flex;flex-direction:column;gap:12px">
  <div style="display:flex;align-items:center;justify-content:space-between">
    <div class="display" style="width:92px;height:92px;border-radius:28px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font-size:58px">{n}</div>
    {icon(ic, 56, BLUE, 2.1)}
  </div>
  <div style="font-family:'InterD';font-weight:900;font-size:50px;color:{INK};letter-spacing:-0.02em;margin-top:6px">{titolo}</div>
  <div style="font-weight:600;font-size:30px;color:{MUTED};line-height:1.3">{sub}</div>
</div>"""


def c8():
    inner = f"""{top_bar(None, 'paper')}
<div style="position:absolute;left:80px;right:80px;top:200px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Metodo Poli</span>
  <div class="display" style="font-size:92px;margin-top:30px">Il richiamo attivo<br>in {hl('4 mosse')}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:40px">
    {mossa(1, 'Studia', 'un argomento alla volta', 'book')}
    {mossa(2, 'Chiudi tutto', 'libro e appunti', 'laptop')}
    {mossa(3, 'Ricorda', 'scrivi o spiega a voce quello che sai', 'chat')}
    {mossa(4, 'Controlla', 'cosa manca, e correggi', 'help')}
  </div>
  <div style="margin-top:24px;display:flex;align-items:center;gap:22px;background:{BLUE};color:#fff;border-radius:30px;padding:24px 36px">
    {icon('move', 50, HL, 2.4)}
    <div style="font-weight:800;font-size:36px">Poi ripeti dopo qualche giorno</div>
  </div>
</div>"""
    return page(inner, PW, PH, "paper")


# ------------------------------------------------ C9 · Piano di studio in 4 settimane
SETTIMANE = [
    ("Mappa e", "basi", "Prima di correre, sai dove stai andando.",
     "Raccogli programma, appunti e vecchi testi d'esame. Dividi il programma in argomenti e ripassa le basi che tornano ovunque."),
    ("Teoria ed", "esercizi", "Un argomento alla volta, senza saltare da un capitolo all'altro.",
     "Teoria e subito esercizi sullo stesso argomento. La sera, richiamo attivo: scrivi a memoria quello che hai fatto."),
    ("Testi", "d'esame", "Gli esercizi del libro non bastano: all'esame le domande sono di un altro tipo.",
     "Passa ai vecchi testi d'esame. Segna gli argomenti in cui sbagli e riprendili dopo due giorni."),
    ("Simulazioni e", "ripasso", "Arrivi all'appello allenato a tempo e tensione.",
     "Almeno una simulazione completa e cronometrata. Negli ultimi giorni solo ripasso: niente argomenti nuovi."),
]


def c9_cover():
    inner = f"""{top_bar('1/7', 'paper')}
<div class="display" style="position:absolute;right:30px;bottom:-60px;font-size:760px;color:transparent;-webkit-text-stroke:6px {SKY};line-height:1">4</div>
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Metodo Poli</span>
  <div class="display" style="font-size:118px;margin-top:40px">La sessione<br>in {hl('4 settimane')}</div>
  <div class="body" style="margin-top:40px;color:{MUTED}">Un piano semplice per arrivare all'appello senza maratone.</div>
</div>
<div style="position:absolute;left:80px;bottom:110px">{swipe(BLUE, '#fff')}</div>"""
    return page(inner, PW, PH, "paper")


def c9_sett(i):
    pre, key, perche, cosa = SETTIMANE[i]
    inner = f"""{top_bar(f'{i + 2}/7', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:210px;display:flex;flex-direction:column">
  <div style="display:flex;align-items:flex-end;justify-content:space-between">
    <span class="pill on-paper">Settimana {i + 1} di 4</span>
    <div class="display" style="font-size:190px;color:{BLUE};line-height:.8">0{i + 1}</div>
  </div>
  <div class="display" style="font-size:100px;margin-top:48px">{pre}<br>{hl(key)}</div>
  <div class="body" style="margin-top:44px;font-size:40px;color:#344054">{perche}</div>
  {fai_cosi(cosa, 64, 'QUESTA SETTIMANA')}
</div>"""
    return page(inner, PW, PH, "paper")


def c9_errore():
    inner = f"""{top_bar('6/7', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">L'errore da evitare</span>
  <div class="display" style="font-size:100px;margin-top:40px">Fare il piano<br>e {hl('dimenticarlo')}</div>
  <div class="body" style="margin-top:40px;font-size:40px;color:#344054">Un piano che non guardi più diventa solo un foglio.</div>
  {fai_cosi("Ogni domenica controlla dove sei arrivato e sistema la settimana dopo. Sei indietro? Togli qualcosa, non le ore di sonno.", 60)}
</div>"""
    return page(inner, PW, PH, "paper")


# ------------------------------------------------ C11 · Online o in presenza
def modo(ic, titolo, sub):
    return f"""<div class="card" style="flex:1;padding:32px 34px">
  <div style="width:84px;height:84px;border-radius:26px;background:{BLUE};display:flex;align-items:center;justify-content:center">{icon(ic, 48, '#fff', 2.1)}</div>
  <div style="font-family:'InterD';font-weight:900;font-size:52px;color:{INK};letter-spacing:-0.02em;margin-top:20px">{titolo}</div>
  <div style="font-weight:600;font-size:30px;color:{MUTED};margin-top:8px;line-height:1.3">{sub}</div>
</div>"""


def c11():
    inner = f"""{top_bar(None, 'paper')}
<div style="position:absolute;left:80px;right:80px;top:180px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Come funzionano le lezioni</span>
  <div class="display" style="font-size:92px;margin-top:28px">Online o in<br>{hl('presenza')}?</div>
  <div style="display:flex;gap:24px;margin-top:36px">
    {modo('laptop', 'Online', 'ti colleghi da dove vuoi')}
    {modo('pin', 'In presenza', 'il luogo lo sceglie il tutor')}
  </div>
  <div class="card" style="margin-top:26px;padding:4px 44px">
    {riga('user', 'Lezioni individuali', pad=13)}
    {riga('cash', 'Pagamento in contanti', pad=13)}
    {riga('chat', 'Chat diretta con il tutor', pad=13)}
    {riga('move', 'Lezione spostabile', 'dalla tua area personale', last=True, pad=13)}
  </div>
</div>"""
    return page(inner, PW, PH, "paper")


# ------------------------------------------------ stories (1080x1920)
def nuovo_reel(titolo_html, size=112):
    return blu('Nuovo Reel', titolo_html, "Lo trovi sul profilo.", cappello(1160), size=size)


def elenco(righe, dopo=None, top=30):
    corpo = "".join(riga_stadio(i + 1, r) for i, r in enumerate(righe))
    d = f'<div class="body" style="margin-top:40px;font-size:38px;color:{MUTED}">{dopo}</div>' if dopo else ""
    return f'<div style="margin-top:{top}px">{corpo}</div>{d}'


def testo_muto(t, top=44):
    return f'<div class="body" style="margin-top:{top}px;font-size:44px;color:{MUTED}">{t}</div>'


def tessera(contenuto, top=100):
    return f'''<div style="margin-top:{top}px;display:flex;justify-content:center"><div style="transform:rotate(-5deg);width:300px;height:300px;border-radius:78px;background:{BLUE};display:flex;align-items:center;justify-content:center;box-shadow:0 24px 60px rgba(21,93,252,.28)">{contenuto}</div></div>'''


GRAFICO = f'''<svg width="210" height="210" viewBox="0 0 100 100" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="M12 86 H92 M18 92 V10" stroke="rgba(255,255,255,.55)" stroke-width="4"/>
<path d="M22 78 C34 20, 44 18, 52 46 S 70 84, 88 22" stroke="#fff" stroke-width="6"/>
<circle cx="39" cy="31" r="5.5" fill="{HL}"/><circle cx="64" cy="66" r="5.5" fill="{HL}"/></svg>'''

FORZE = f'''<svg width="220" height="220" viewBox="0 0 100 100" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="M8 74 H92" stroke="rgba(255,255,255,.55)" stroke-width="4"/>
<rect x="34" y="46" width="30" height="28" rx="4" fill="#fff"/>
<path d="M49 46 V14 M43 21 L49 14 L55 21" stroke="{HL}" stroke-width="5"/>
<path d="M49 74 V94 M43 87 L49 94 L55 87" stroke="{HL}" stroke-width="5"/>
<path d="M64 60 H92 M85 54 L92 60 L85 66" stroke="{HL}" stroke-width="5"/>
<text x="56" y="22" fill="#fff" font-family="InterD" font-weight="900" font-size="12">N</text>
<text x="56" y="96" fill="#fff" font-family="InterD" font-weight="900" font-size="12">P</text>
<text x="80" y="50" fill="#fff" font-family="InterD" font-weight="900" font-size="12">F</text></svg>'''


STORIES = {
    # 24/11 · C6 Analisi 1
    'G6_story_1': lambda: carta('Materia sotto la lente', f"Analisi 1:<br>lo studio di<br>{hl('funzione')}", testo_muto("È l'esercizio che mette insieme limiti, derivate e grafico. Nel nuovo post trovi come prepararla.") + tessera(GRAFICO), size=110),
    'G6_story_2': lambda: carta('Consiglio pratico', f"Segui sempre<br>lo {hl('stesso ordine')}", elenco(['Dominio', 'Segno e intersezioni con gli assi', 'Limiti agli estremi e asintoti', 'Derivata prima: crescenza, massimi e minimi', 'Grafico'], "Con una scaletta fissa non salti passaggi."), size=104),
    'G6_story_3': lambda: blu("Prima dell'appello", f"Analisi 1<br>non {hl('torna')}?", "Prenota un tutor che l'ha già passata.", url_pill(1180), size=130),
    # 25/11 · C7 Reel tipi di studenti
    'G7_story_1': lambda: nuovo_reel(f"I 5 tipi di<br>studenti in<br>aula {hl('studio')}", 112),
    'G7_story_2': lambda: carta('Sii sincero', f"Tu quale<br>{hl('sei')}?", elenco(['L\'evidenziatore', 'Il ritardatario', 'Il pianificatore', 'Quello della pausa', 'Quello che spiega'], "Scrivilo nei commenti del Reel."), size=112),
    'G7_story_3': lambda: blu('Consiglio da collega', f"Qualunque tipo<br>tu {hl('sia')}", "Se un esame non torna, prenota un tutor che l'ha già passato.", url_pill(1180), size=120),
    # 26/11 · C8 richiamo attivo
    'G8_story_1': lambda: carta('Metodo Poli', f"Prova<br>{hl('adesso')}", scheda("pensa all'ultimo argomento che hai studiato. Chiudi tutto e scrivi in due minuti quello che ricordi.", 56) + tessera(icon('book', 150, '#fff', 1.8)), size=130),
    'G8_story_2': lambda: carta('La regola dei due tentativi', f"Due tentativi,<br>poi {hl('controlla')}", scheda("se un passaggio non ti viene, riprova una seconda volta. Al secondo vuoto riapri gli appunti e segna il punto: è lì che devi ripassare.", 56), size=104),
    'G8_story_3': lambda: blu('Metodo Poli', f"Salva il post<br>sul {hl('richiamo')}", "Le 4 mosse in un'immagine, da riprendere quando inizi a ripassare.", cappello(1160), size=116),
    # 27/11 · C9 piano in 4 settimane
    'G9_story_1': lambda: carta('Piano in 4 settimane', f"La settimana 1<br>in {hl('breve')}", elenco(['Raccogli programma, appunti e vecchi testi', 'Dividi il programma in argomenti', 'Ripassa le basi che tornano ovunque'], "Il piano completo è nel nuovo post."), size=110),
    'G9_story_2': lambda: carta("L'errore da evitare", f"Fare il piano<br>e {hl('dimenticarlo')}", scheda("ogni domenica controlla dove sei arrivato e sistema la settimana dopo.", 56) + tessera(icon('calendar', 150, '#fff', 1.8)), size=104),
    'G9_story_3': lambda: blu("Prima dell'appello", f"Sei<br>{hl('indietro')}?", "Prenota un tutor che quell'esame l'ha già passato e riparti da lì.", url_pill(1180), size=136),
    # 28/11 · C10 Reel sabato dello studente
    'G10_story_1': lambda: nuovo_reel(f"Il sabato<br>dello {hl('studente')}", 124),
    'G10_story_2': lambda: carta('Weekend di studio', f"Pause che<br>{hl('aiutano')}", elenco(['Una pausa breve ogni ora circa', 'Lontano dal telefono', 'In piedi: due passi o un bicchiere d\'acqua'], "Poi torni sul libro con la testa più libera."), size=112),
    'G10_story_3': lambda: blu('Lunedì si riparte', f"Organizza la<br>{hl('settimana')}", "Prenota la lezione per i prossimi giorni, con chi l'esame l'ha già passato.", url_pill(1180), size=118),
    # 29/11 · C11 online o in presenza
    'G11_story_1': lambda: carta('Lezioni in presenza', f"Chi sceglie<br>il {hl('luogo')}?", testo_muto("Il tutor. E se preferisci restare a casa, la lezione si può fare online.") + tessera(icon('pin', 150, '#fff', 1.8)), size=118),
    'G11_story_2': lambda: carta('Sulla piattaforma', f"Chat con<br>il {hl('tutor')}", testo_muto("Scrivi al tutor dalla chat diretta, anche per mandare file.") + tessera(icon('chat', 150, '#fff', 1.8)), size=124),
    'G11_story_3': lambda: blu('Tutto chiaro', f"Prenota la<br>tua {hl('lezione')}", "Lezioni individuali, pagamento in contanti, lezione spostabile dall'area personale.", url_pill(1250), size=124),
    # 30/11 · C12 Fisica 1
    'G12_story_1': lambda: carta('Materia sotto la lente', f"Fisica 1:<br>il diagramma<br>delle {hl('forze')}", testo_muto("È il primo passo di quasi ogni esercizio di dinamica. Nel nuovo post trovi come prepararla.") + tessera(FORZE), size=110),
    'G12_story_2': lambda: carta('Errore tipico', f"I numeri<br>{hl('troppo presto')}", scheda("risolvi in lettere e sostituisci i numeri solo alla fine: così vedi subito se le unità di misura tornano.", 56), size=116),
    'G12_story_3': lambda: blu("Prima dell'appello", f"Fisica 1<br>non {hl('torna')}?", "Prenota un tutor che l'ha già passata.", url_pill(1180), size=130),
}


def posts():
    jobs = lente('C6_analisi1', ANALISI1)
    jobs.append(("C8_richiamo", c8()))
    jobs += [("C9_piano_1", c9_cover())] + [(f"C9_piano_{i + 2}", c9_sett(i)) for i in range(4)]
    jobs += [("C9_piano_6", c9_errore()),
             ("C9_piano_7", cta_blu('7/7', "Prima dell'appello", f"Sei<br>{hl('indietro')}?",
                                    "Un tutor che quell'esame l'ha già passato ti aiuta a capire da dove ripartire.",
                                    "Mandalo a chi è in sessione"))]
    jobs.append(("C11_lezioni", c11()))
    jobs += lente('C12_fisica1', FISICA1)
    return [(n, h, PW, PH) for n, h in jobs]


if __name__ == '__main__':
    import sys
    cosa = sys.argv[1] if len(sys.argv) > 1 else 'tutto'
    jobs = []
    if cosa in ('tutto', 'post'):
        jobs += posts()
    if cosa in ('tutto', 'stories'):
        jobs += [(k, f(), SW, SH) for k, f in STORIES.items()]
    render(jobs)
    print('ok', len(jobs))
