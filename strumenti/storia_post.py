# Story che "condivide" il post appena pubblicato: la copertina del post su
# sfondo Ripeti al Poliba, con l'invito ad aprirlo sul profilo.
# L'API non permette la condivisione nativa (adesivo del post), quindi
# questa è una story normale, in video con la musica originale.
#
# Uso: python3 storia_post.py COPERTINA.jpg USCITA.mp4 [OFFSET_MUSICA] [ETICHETTA]
#   COPERTINA: prima immagine del carosello, immagine del post o copertina del Reel.
import pathlib, subprocess, sys
from PIL import Image
from brand import *
from render import render
from build_stories import W, H, hl, story_top

ROOT = pathlib.Path(__file__).resolve().parent


def storia(copertina, etichetta):
    larg, alt = Image.open(copertina).size
    # la copertina sta in un riquadro di 760 × 1000 px al massimo
    scala = min(760 / larg, 1000 / alt)
    w, h = round(larg * scala), round(alt * scala)
    uri = pathlib.Path(copertina).resolve().as_uri()
    inner = f"""{story_top('blue')}
<div style="position:absolute;left:80px;top:390px"><span class="pill on-blue">{etichetta}</span></div>
<div style="position:absolute;left:50%;top:{500 + (1000 - h) // 2}px;transform:translateX(-50%) rotate(-2deg);width:{w}px;height:{h}px;border-radius:34px;overflow:hidden;border:10px solid #fff;box-shadow:0 30px 70px rgba(10,20,60,.45)">
  <img src="{uri}" style="width:100%;height:100%;display:block;object-fit:cover">
</div>
<div style="position:absolute;left:80px;right:80px;top:1560px;text-align:center">
  <div class="display" style="font-size:72px">Lo trovi sul {hl('profilo')}</div>
</div>"""
    return page(inner, W, H, "blue-grid")


if __name__ == '__main__':
    copertina, uscita = sys.argv[1], sys.argv[2]
    offset = sys.argv[3] if len(sys.argv) > 3 else '0'
    etichetta = sys.argv[4] if len(sys.argv) > 4 else 'Nuovo post'
    nome = 'storia_post_' + pathlib.Path(uscita).stem.replace('-', '_')
    render([(nome, storia(copertina, etichetta), W, H)])
    png = ROOT / 'png' / f'{nome}.png'
    subprocess.run(['sh', str(ROOT / 'storia_video.sh'), str(png), uscita, offset], check=True)
    print(png, '->', uscita)
