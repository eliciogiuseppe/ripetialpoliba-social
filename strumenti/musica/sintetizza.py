# Musica originale per stories e Reel di Ripeti al Poliba (lo-fi, 92 BPM, La minore).
# Tutto sintetizzato qui: nessun campione o brano di terzi.
import numpy as np, sys
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 44100
BPM = 92
BEAT = 60 / BPM
BAR = 4 * BEAT
rng = np.random.default_rng(7)

def nota(m):  # MIDI -> Hz
    return 440.0 * 2 ** ((m - 69) / 12)

def env(n, a=0.01, d=0.0, s=1.0, r=0.2, dur=None):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4))
    if dur is None: dur = n / SR
    e = e * np.where(t < dur, 1.0, np.exp(-(t - dur) / max(r, 1e-3)))
    return e

def rhodes(f, dur, vel=0.5):
    n = int((dur + 1.2) * SR); t = np.arange(n) / SR
    trem = 1 + 0.06 * np.sin(2 * np.pi * 4.5 * t)
    s = (np.sin(2*np.pi*f*t) * np.exp(-t*1.6)
         + 0.35*np.sin(2*np.pi*2*f*t) * np.exp(-t*3.5)
         + 0.12*np.sin(2*np.pi*3*f*t + 0.3) * np.exp(-t*6)
         + 0.05*np.sin(2*np.pi*7*f*t) * np.exp(-t*25))
    return vel * s * trem * env(n, a=0.006, dur=dur, r=0.35)

def campanella(f, vel=0.25):
    n = int(1.6 * SR); t = np.arange(n) / SR
    s = np.sin(2*np.pi*f*t) * np.exp(-t*3) + 0.3*np.sin(2*np.pi*4.01*f*t) * np.exp(-t*9)
    return vel * s * env(n, a=0.002)

def basso(f, dur, vel=0.38):
    n = int((dur + 0.3) * SR); t = np.arange(n) / SR
    s = np.sin(2*np.pi*f*t) + 0.25*np.sin(2*np.pi*2*f*t)
    return vel * np.tanh(1.4*s) * env(n, a=0.01, dur=dur, r=0.08)

def cassa(vel=0.6):
    n = int(0.45 * SR); t = np.arange(n) / SR
    f = 45 + 75 * np.exp(-t * 28)
    ph = 2*np.pi*np.cumsum(f)/SR
    return vel * np.sin(ph) * np.exp(-t * 7.5)

def rullante(vel=0.35):
    n = int(0.3 * SR); t = np.arange(n) / SR
    rum = sosfilt(butter(2, [1500, 7000], 'bandpass', fs=SR, output='sos'), rng.standard_normal(n))
    return vel * (0.8*rum*np.exp(-t*18) + 0.4*np.sin(2*np.pi*190*t)*np.exp(-t*25))

def charleston(vel=0.12):
    n = int(0.08 * SR); t = np.arange(n) / SR
    rum = sosfilt(butter(2, 7500, 'highpass', fs=SR, output='sos'), rng.standard_normal(n))
    return vel * rum * np.exp(-t * 60)

def metti(buf, x, t0):
    i = int(t0 * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(x)); buf[i:j] += x[:j - i]

ACCORDI = [  # La-9, Famaj7, Do(add9), Sol6
    [57, 60, 64, 67, 71], [53, 57, 60, 64, 67], [48, 55, 60, 62, 64], [55, 59, 62, 64, 67]]
BASSI = [45, 41, 48, 43]
MELODIA = [  # (battito nella frase di 2 battute, nota) – pentatonica di La minore
    (0.0, 76), (1.0, 74), (1.5, 72), (2.5, 69), (4.0, 72), (5.0, 74), (5.5, 76), (6.5, 79)]

def brano(durata):
    n = int((durata + 2) * SR)
    L = {k: np.zeros(n) for k in ('keys', 'bass', 'drums', 'mel')}
    battute = int(np.ceil(durata / BAR)) + 1
    for b in range(battute):
        t0 = b * BAR; c = ACCORDI[b % 4]
        for k, m in enumerate(c):  # accordo arpeggiato morbido, ripetuto a metà battuta
            metti(L['keys'], rhodes(nota(m), BAR*0.48, 0.30), t0 + k*0.018)
            metti(L['keys'], rhodes(nota(m), BAR*0.45, 0.20), t0 + 2*BEAT + 0.12 + k*0.015)
        r = BASSI[b % 4]
        metti(L['bass'], basso(nota(r), BEAT*1.4), t0)
        metti(L['bass'], basso(nota(r), BEAT*0.6, 0.4), t0 + 2.5*BEAT)
        metti(L['bass'], basso(nota(r + 7), BEAT*0.8, 0.4), t0 + 3*BEAT)
        if b >= 1:  # batteria dalla seconda battuta
            metti(L['drums'], cassa(), t0); metti(L['drums'], cassa(0.6), t0 + 2.5*BEAT)
            metti(L['drums'], rullante(), t0 + BEAT); metti(L['drums'], rullante(), t0 + 3*BEAT)
            for e in range(8):  # ottavi con swing
                metti(L['drums'], charleston(0.10 if e % 2 else 0.14), t0 + e*BEAT/2 + (0.06 if e % 2 else 0))
        if b >= 2 and b % 2 == 0:
            for bt, m in MELODIA:
                metti(L['mel'], campanella(nota(m), 0.22), t0 + bt*BEAT)
    # mix stereo
    keys = sosfilt(butter(2, 5200, 'lowpass', fs=SR, output='sos'), L['keys'])
    mel = L['mel']; bass = L['bass']; dr = L['drums']
    eco = lambda x, d, g: np.concatenate([np.zeros(int(d*SR)), x[:-int(d*SR)]]) * g
    sx = keys + 0.9*mel + bass + dr + eco(keys, 0.011, 0.5) + eco(mel, BEAT*0.75, 0.35)
    dx = keys + 0.9*mel + bass + dr + eco(keys, 0.017, 0.5) + eco(mel, BEAT*0.5, 0.35)
    crepitio = (rng.random(n) < 0.0006) * rng.standard_normal(n) * 0.05
    st = np.stack([sx + crepitio, dx + crepitio], 1)[:int(durata*SR)]
    st = np.tanh(st * 0.8) / 0.8
    st /= np.max(np.abs(st)) / 0.89
    return st

if __name__ == '__main__':
    durata = float(sys.argv[1]) if len(sys.argv) > 1 else 64
    s = brano(durata)
    f = int(1.0 * SR); s[:f] *= np.linspace(0, 1, f)[:, None]
    g = int(2.0 * SR); s[-g:] *= np.linspace(1, 0, g)[:, None]
    wavfile.write(str(__import__('pathlib').Path(__file__).resolve().parent / 'lofi.wav'), SR, (s * 32767).astype(np.int16))
    print('ok', s.shape[0] / SR, 's')
