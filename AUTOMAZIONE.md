# Pubblicazione automatica di @ripetialpoliba

Procedura seguita ogni giorno dall'attività programmata delle 12:00 (Europe/Rome).

## Regole del titolare (Giuseppe)
- Il nome del brand è sempre "Ripeti al Poliba".
- Il ritmo è **1 post o Reel al giorno alle 12:00, più almeno 3 stories**.
- Si pubblica direttamente, senza chiedere conferma: autorizzazione del 18/11/2026.
- Stories e Reel hanno la **musica**. Le stories sono video MP4 di 7 s con il brano originale in `strumenti/musica/`.
- **Niente stories con sondaggi o quiz** per ora. Niente adesivi o link cliccabili: l'API non li supporta.
- Non vanno pubblicati:
  - prezzi;
  - numeri o recensioni inventati;
  - funzionalità che il sito non ha;
  - loghi o immagini del Politecnico;
  - foto di persone;
  - musica di terzi.
- Non si risponde ai commenti, non si mandano DM e non si prendono impegni a nome di Ripeti al Poliba.
- Fatti verificati:
  - lezioni online o in presenza, con il luogo scelto dal tutor;
  - pagamento in contanti;
  - la lezione si può spostare dall'area personale;
  - i tutor si iscrivono gratis e vengono approvati dall'admin, le materie le propongono i tutor;
  - lezioni individuali;
  - materie: Analisi 1, Analisi 2, Fisica 1, Fisica 2, Informatica per l'ingegneria, Scienza delle costruzioni, SEIMAFI;
  - su richiesta: simulazioni d'esame, revisione tesi, laboratori pratici.
- Il link in bio è impostato: nelle caption si può scrivere "link in bio".

## Pubblicare il giorno X
Ogni giorno lavorano due attività programmate (Europe/Rome):
- **11:57 · post + storia del post.**
  1. Leggi `piano.json` (https://eliciogiuseppe.github.io/ripetialpoliba-social/piano.json) e prendi la voce con `data` = oggi.
  2. Con Windsor.ai (connettore `instagram`, account `17841456358250108`) controlla i media pubblicati oggi, così non pubblichi due volte.
  3. Pubblica il post:
     - `carosello` → `create_carousel_post` (`image_urls`, `caption`);
     - `foto` → `create_image_post`;
     - `reel` → `create_video_post` (`video_url`, `cover_url`, `share_to_feed`).
  4. **Subito dopo** pubblica `storia_post` con `create_story` (`video_url`). È la story che rilancia il post appena uscito: copertina del post, etichetta "Nuovo post" o "Nuovo Reel", "Lo trovi sul profilo".
- **13:17 · le 3 stories del giorno**, in ordine, con `create_story` (`video_url`). Prima controlla con Windsor quante stories sono già uscite oggi, così non le ripubblichi.

Tutti gli URL sono `base_url` + il percorso indicato in `piano.json`.

## Produrre nuovi contenuti
1. Le idee sono nel calendario editoriale: https://claude.ai/artifact/EsXwqCFHaZyTdaYXAMj5nH. Ogni giorno ha un post o Reel alle 12:00 e una riga di stories.
2. Le grafiche si fanno con `strumenti/` (Playwright + Chrome, font Inter in /usr/share/fonts/opentype/inter):
   - formati: post 1080×1350, stories e Reel 1080×1920;
   - stile e marchio "Tocco" come in `build_posts.py` e `build_stories_*.py`.
3. Controlla ogni immagine a vista prima di pubblicarla: testo leggibile, niente testo tagliato.
4. Story in video: `sh strumenti/storia_video.sh input.png output.mp4 OFFSET`. Usa offset diversi, tra 0 e 57 secondi.
   Storia del post: `python3 strumenti/storia_post.py COPERTINA.jpg AAAA-MM/gN-post.mp4 OFFSET "Nuovo post"` (per i Reel usa "Nuovo Reel" e la copertina del Reel). Va nel campo `storia_post` della voce del giorno.
5. Reel: video 1080×1920 con la musica di `strumenti/musica/lofi-norm.flac`, mixata con `ffmpeg`.
6. Metti i file in `AAAA-MM/`, aggiungi le voci in `piano.json`, poi commit e push su `main`. Verifica che gli URL su GitHub Pages rispondano 200.
7. Tieni `piano.json` sempre avanti di almeno 3 giorni.
8. Aggiorna lo stato nel calendario: PROGRAMMATO, poi PUBBLICATO con il link.
