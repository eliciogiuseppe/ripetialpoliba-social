from brand import *
from render import render

W, H = 1080, 1350


def hl(t):
    return f'<span class="hl">{t}</span>'


def swipe(bg="#fff", fg=BLUE, label="Scorri"):
    return f'<div class="swipe" style="background:{bg};color:{fg}">{label} {ARROW}</div>'


def icon_dot(name, bg=BLUE, fg="#fff", d=88, s=46):
    return f'<div style="width:{d}px;height:{d}px;border-radius:50%;background:{bg};display:flex;align-items:center;justify-content:center;flex:none">{icon(name, s, fg, 2.2)}</div>'


def link_card(theme="blue"):
    return f"""<div class="card" style="padding:34px 44px;display:flex;align-items:center;gap:28px">
  {icon_dot('link', BLUE, '#fff', 96, 50)}
  <div>
    <div style="font-weight:800;font-size:54px;color:{BLUE};letter-spacing:-0.01em">ripetialpoliba.it</div>
    <div style="font-weight:600;font-size:30px;color:{MUTED};margin-top:6px">Prenota online in pochi passaggi</div>
  </div>
</div>"""


# ---------------------------------------------------------------- C1 lancio
def c1_s1():
    card = f"""<div class="card" style="position:absolute;right:90px;bottom:84px;width:460px;padding:32px 38px;transform:rotate(-3deg);color:{INK}">
  <div style="width:84px;height:84px;border-radius:24px;background:{BLUE};display:flex;align-items:center;justify-content:center">{icon('book', 46, '#fff', 2.2)}</div>
  <div style="font-weight:800;font-size:46px;margin-top:22px">Analisi 1</div>
  <div style="font-weight:500;font-size:26px;color:{MUTED};margin-top:8px;line-height:1.35">Limiti, derivate, studio di funzione, integrali</div>
  <div style="height:2px;background:#EEF2F6;margin:22px 0 18px"></div>
  <div style="font-weight:800;font-size:30px;color:{BLUE};text-align:right">Scegli →</div>
</div>"""
    inner = f"""{top_bar('1/6', 'blue')}
<div style="position:absolute;left:80px;right:80px;top:200px">
  <span class="pill on-blue">Ripetizioni tra studenti</span>
  <div class="display" style="font-size:116px;margin-top:36px">Chi l'ha<br>già {hl('passato')}<br>te lo spiega.</div>
  <div class="body" style="margin-top:32px;max-width:900px;color:rgba(255,255,255,.88)">Ripetizioni per gli esami del Poliba, con studenti che li hanno già superati.</div>
</div>
{card}
<div style="position:absolute;left:80px;bottom:110px">{swipe()}</div>"""
    return page(inner, W, H, "blue-grid")


def bubble(text, offset):
    return f"""<div style="margin-left:{offset}px;display:inline-block;align-self:flex-start;position:relative">
  <div class="card" style="padding:30px 40px;border-radius:40px 40px 40px 12px;font-weight:700;font-size:42px;line-height:1.25;color:{INK}">{text}</div>
</div>"""


def c1_s2():
    inner = f"""{top_bar('2/6', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Il problema</span>
  <div class="display" style="font-size:104px;margin-top:40px">Lo conosci<br>questo {hl('momento')}?</div>
  <div style="display:flex;flex-direction:column;gap:30px;margin-top:70px">
    {bubble('«Mancano tre settimane all\'appello.»', 0)}
    {bubble('«Gli esercizi non tornano.»', 90)}
    {bubble('«E adesso a chi lo chiedo?»', 30)}
  </div>
  <div style="margin-top:64px;font-weight:600;font-size:36px;color:{MUTED}">Ci siamo passati anche noi.</div>
</div>"""
    return page(inner, W, H, "paper")


def feature(ic, title, sub=None):
    s = f'<div style="font-weight:500;font-size:30px;color:{MUTED};margin-top:6px">{sub}</div>' if sub else ""
    return f"""<div style="display:flex;align-items:center;gap:30px">
  {icon_dot(ic)}
  <div><div style="font-weight:700;font-size:40px;color:{INK}">{title}</div>{s}</div>
</div>"""


def c1_s3():
    inner = f"""{top_bar('3/6', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">La soluzione</span>
  <div class="display" style="font-size:104px;margin-top:40px">Ecco<br>{hl('Ripeti al Poliba')}</div>
  <div class="body" style="margin-top:40px">Una piattaforma per prenotare lezioni con studenti del Poliba che quell'esame l'hanno già superato.</div>
  <div class="card" style="margin-top:56px;padding:48px;display:flex;flex-direction:column;gap:40px">
    {feature('user', 'Tutor che studiano al Poliba')}
    {feature('cap', 'Approvati uno per uno', 'prima di comparire sulla piattaforma')}
    {feature('calendar', 'Prenoti online', 'scegli materia, giorno e orario')}
  </div>
</div>"""
    return page(inner, W, H, "paper")


def step(n, text):
    return f"""<div class="card" style="padding:38px 44px;display:flex;align-items:center;gap:36px">
  <div class="display" style="width:110px;height:110px;border-radius:32px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font-size:72px;flex:none">{n}</div>
  <div style="font-weight:800;font-size:46px;color:{INK};line-height:1.15">{text}</div>
</div>"""


def c1_s4():
    inner = f"""{top_bar('4/6', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Come funziona</span>
  <div class="display" style="font-size:104px;margin-top:40px">Prenoti in<br>{hl('3 passaggi')}</div>
  <div style="display:flex;flex-direction:column;gap:28px;margin-top:60px">
    {step(1, 'Scegli la materia')}
    {step(2, 'Scegli giorno e orario')}
    {step(3, 'Conferma con la tua email')}
  </div>
  <div style="margin-top:40px;font-weight:600;font-size:32px;line-height:1.4;color:{MUTED}">Non serve registrarti prima: basta la tua email.</div>
</div>"""
    return page(inner, W, H, "paper")


MATERIE = [("Analisi 1", "15"), ("Analisi 2", "15"), ("Fisica 1", "15"), ("Fisica 2", "15"),
           ("Informatica per l'ingegneria", "15"), ("Scienza delle costruzioni", "20"), ("SEIMAFI", "20")]


def c1_s5():
    rows = ""
    for i, (m, p) in enumerate(MATERIE):
        border = "" if i == len(MATERIE) - 1 else "border-bottom:2px solid #EEF2F6;"
        rows += f"""<div style="display:flex;align-items:center;justify-content:space-between;padding:19px 0;{border}">
  <div style="font-weight:700;font-size:38px;color:{INK}">{m}</div>
  <div style="font-weight:800;font-size:38px;color:{BLUE};white-space:nowrap">{p} €/h</div>
</div>"""
    inner = f"""{top_bar('5/7', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Le materie di oggi</span>
  <div class="display" style="font-size:96px;margin-top:36px">Cosa puoi<br>{hl('prenotare')}</div>
  <div class="card" style="margin-top:40px;padding:12px 48px">{rows}</div>
  <div style="margin-top:30px;font-weight:600;font-size:32px;color:{MUTED}">Nuove materie arrivano quando i tutor le propongono.</div>
</div>"""
    return page(inner, W, H, "paper")


def info_row(ic, title, sub=None, last=False):
    s = f'<div style="font-weight:500;font-size:30px;color:{MUTED};margin-top:4px">{sub}</div>' if sub else ""
    border = "" if last else "border-bottom:2px solid #EEF2F6;"
    return f"""<div style="display:flex;align-items:center;gap:30px;padding:21px 0;{border}">
  {icon_dot(ic, SKY, BLUE, 84, 44)}
  <div><div style="font-weight:700;font-size:39px;color:{INK}">{title}</div>{s}</div>
</div>"""


def c1_s6():
    inner = f"""{top_bar('5/6', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Le info che contano</span>
  <div class="display" style="font-size:92px;margin-top:36px">Tutto chiaro prima<br>di {hl('iniziare')}</div>
  <div class="card" style="margin-top:42px;padding:8px 48px">
    {info_row('pin', 'Online o in presenza', 'il luogo lo indica il tutor')}
    {info_row('cash', 'Pagamento in contanti')}
    {info_row('move', 'Lezione spostabile', 'dalla tua area personale')}
    {info_row('user', 'Stesso tutor per tutta la materia')}
    {info_row('chat', 'Chat diretta con il tutor', 'anche per mandare file', last=True)}
  </div>
</div>"""
    return page(inner, W, H, "paper")


def c1_s7():
    inner = f"""{top_bar('6/6', 'blue')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">Il prossimo passo</span>
  <div class="display" style="font-size:120px;margin-top:40px">Prenota la tua<br>{hl('prima lezione')}</div>
  <div class="body" style="margin-top:40px;color:rgba(255,255,255,.9)">Scegli la materia, trova il tutor, al resto pensiamo noi.</div>
  <div style="margin-top:60px">{link_card()}</div>
</div>
<div style="position:absolute;right:-90px;bottom:-110px;opacity:.13;transform:rotate(-12deg)">{SYMBOLS['tocco'](bg='#FFFFFF', size=620, bg_on=False)}</div>
<div style="position:absolute;left:80px;bottom:100px;display:inline-flex;align-items:center;gap:14px;border:3px solid rgba(255,255,255,.55);color:#fff;font-weight:700;font-size:30px;padding:18px 30px;border-radius:999px">Mandalo al tuo gruppo di corso</div>"""
    return page(inner, W, H, "blue-grid")


# ---------------------------------------------------------------- C2 diventa tutor
def check_row(text, last=False):
    border = "" if last else "border-bottom:2px solid #EEF2F6;"
    return f"""<div style="display:flex;align-items:center;gap:28px;padding:22px 0;{border}">
  <div style="width:62px;height:62px;border-radius:50%;background:{HL};display:flex;align-items:center;justify-content:center;flex:none">{CHECK.format(s=36, c=INK)}</div>
  <div style="font-weight:700;font-size:38px;color:{INK};line-height:1.2">{text}</div>
</div>"""


def c2():
    inner = f"""{top_bar(None, 'blue')}
<div style="position:absolute;left:80px;right:80px;top:200px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">Cerchiamo tutor</span>
  <div class="display" style="font-size:100px;margin-top:34px">Quell'esame<br>l'hai passato?<br>Ora {hl('spiegalo')}.</div>
  <div class="card" style="margin-top:44px;padding:8px 48px">
    {check_row('Iscrizione gratuita')}
    {check_row('Scegli tu materie e orari')}
    {check_row('Online o in presenza, decidi tu dove')}
    {check_row('Gli studenti ti prenotano online', last=True)}
  </div>
</div>
<div style="position:absolute;left:80px;right:80px;bottom:80px;display:flex;flex-direction:column;gap:20px">
  <div style="align-self:flex-start;display:inline-flex;align-items:center;gap:18px;background:{HL};color:{INK};font-weight:800;font-size:36px;padding:24px 38px;border-radius:999px">Candidati su ripetialpoliba.it {ARROW}</div>
  <div style="font-weight:500;font-size:25px;color:rgba(255,255,255,.8)">Clicca «Registrati come Tutor» · ogni profilo viene approvato</div>
</div>"""
    return page(inner, W, H, "blue-grid")


# ---------------------------------------------------------------- C3 metodo
ERRORI = [
    ("Rileggere invece di", "ripetere", "Rileggere appunti e libro dà l'impressione di sapere, ma non ti allena a ricordare da solo.",
     "Chiudi il quaderno e riscrivi a memoria definizioni e passaggi. Poi controlla cosa ti manca."),
    ("Guardare subito la", "soluzione", "Capire una soluzione mentre la leggi non vuol dire saperla trovare all'esame.",
     "Prova finché sei davvero bloccato. Poi guarda la soluzione e rifai l'esercizio da zero il giorno dopo."),
    ("Ridursi agli", "ultimi giorni", "Quello che studi in poche maratone si dimentica in fretta.",
     "Ripassa lo stesso argomento più volte a distanza di giorni: per esempio dopo 1, 3 e 7 giorni."),
    ("Non provare mai una", "simulazione", "All'esame contano anche tempo e tensione, e si allenano solo con prove vere.",
     "Prima dell'appello fai almeno una prova completa e cronometrata, con un vecchio testo d'esame se è disponibile."),
    ("Restare", "bloccati da soli", "Ogni giorno perso su un argomento è un giorno tolto al resto del programma.",
     "Dopo due tentativi a vuoto chiedi: a un collega, al docente durante il ricevimento o a un tutor."),
]


def c3_cover():
    inner = f"""{top_bar('1/7', 'paper')}
<div class="display" style="position:absolute;right:40px;bottom:-60px;font-size:760px;color:transparent;-webkit-text-stroke:6px {SKY};line-height:1">5</div>
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-paper" style="align-self:flex-start">Metodo Poli</span>
  <div class="display" style="font-size:122px;margin-top:40px">5 errori che<br>{hl('allungano')}<br>la tua sessione</div>
  <div class="body" style="margin-top:40px;color:{MUTED}">Il terzo lo facciamo quasi tutti.</div>
</div>
<div style="position:absolute;left:80px;bottom:110px">{swipe(BLUE, '#fff')}</div>"""
    return page(inner, W, H, "paper")


def c3_err(i):
    pre, key, why, fix = ERRORI[i]
    inner = f"""{top_bar(f'{i + 2}/7', 'paper')}
<div style="position:absolute;left:80px;right:80px;top:210px;display:flex;flex-direction:column">
  <div style="display:flex;align-items:flex-end;justify-content:space-between">
    <span class="pill on-paper">Errore {i + 1} di 5</span>
    <div class="display" style="font-size:190px;color:{BLUE};line-height:.8">0{i + 1}</div>
  </div>
  <div class="display" style="font-size:96px;margin-top:48px">{pre}<br>{hl(key)}</div>
  <div class="body" style="margin-top:44px;font-size:40px;color:#344054">{why}</div>
  <div class="card" style="margin-top:64px;padding:50px 52px">
    <span style="display:inline-block;background:{HL};color:{INK};font-weight:800;font-size:26px;letter-spacing:.14em;padding:12px 24px;border-radius:999px">FAI COSÌ</span>
    <div style="font-weight:700;font-size:42px;line-height:1.32;color:{INK};margin-top:26px">{fix}</div>
  </div>
</div>"""
    return page(inner, W, H, "paper")


def c3_cta():
    inner = f"""{top_bar('7/7', 'blue')}
<div style="position:absolute;left:80px;right:80px;top:220px;display:flex;flex-direction:column">
  <span class="pill on-blue" style="align-self:flex-start">Prima dell'appello</span>
  <div class="display" style="font-size:120px;margin-top:40px">Salvalo per<br>la {hl('sessione')}</div>
  <div class="body" style="margin-top:40px;color:rgba(255,255,255,.9)">E se un esame proprio non torna, prenota un tutor che l'ha già passato.</div>
  <div style="margin-top:60px">{link_card()}</div>
</div>
<div style="position:absolute;right:-90px;bottom:-110px;opacity:.13;transform:rotate(-12deg)">{SYMBOLS['tocco'](bg='#FFFFFF', size=620, bg_on=False)}</div>
<div style="position:absolute;left:80px;bottom:100px;display:inline-flex;align-items:center;gap:14px;border:3px solid rgba(255,255,255,.55);color:#fff;font-weight:700;font-size:30px;padding:18px 30px;border-radius:999px">Mandalo a chi è in sessione</div>"""
    return page(inner, W, H, "blue-grid")


if __name__ == "__main__":
    jobs = []
    for i, f in enumerate([c1_s1, c1_s2, c1_s3, c1_s4, c1_s6, c1_s7], 1):
        jobs.append((f"C1_lancio_{i}", f(), W, H))
    jobs.append(("C2_diventa_tutor", c2(), W, H))
    jobs.append(("C3_metodo_1", c3_cover(), W, H))
    for i in range(5):
        jobs.append((f"C3_metodo_{i + 2}", c3_err(i), W, H))
    jobs.append(("C3_metodo_7", c3_cta(), W, H))
    render(jobs)
    print("done", len(jobs))
