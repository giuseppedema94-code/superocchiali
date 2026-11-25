#!/usr/bin/env python3
"""Genera le pagine statiche di superocchiali.it. Nessuna AI: solo template.
Uso: python3 scripts/build.py  (dalla radice del repo)"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://superocchiali.it"
CSP = ("default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
       "font-src 'self'; img-src 'self' data: https:; connect-src 'self'; "
       "base-uri 'self'; form-action 'self'")

LOGO = ('<svg width="58" height="28" viewBox="0 0 58 28" aria-hidden="true">'
        '<circle cx="14" cy="14" r="11" fill="#FFD23F" stroke="#141414" stroke-width="3"/>'
        '<circle cx="44" cy="14" r="11" fill="#FFD23F" stroke="#141414" stroke-width="3"/>'
        '<path d="M25 12 Q29 8 33 12" fill="none" stroke="#141414" stroke-width="3"/>'
        '<circle cx="16" cy="13" r="4" fill="#141414"/><circle cx="46" cy="13" r="4" fill="#141414"/></svg>')

NAV = [("/sole/", "Sole"), ("/vista/", "Vista"), ("/#test", "Che faccia hai?")]


def page(path, title, desc, body, current=""):
    nav = "".join(
        f'<a class="pill" href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>'
        for h, t in NAV)
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-adsense-account" content="ca-pub-1199141407956658">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="superocchiali.it">
<meta name="theme-color" content="#FFD23F">
<link rel="icon" href="/img/logo.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/bricolage.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/style.css">
<script src="/js/app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Vai al contenuto</a>
<header class="wrap top">
<a class="logo" href="/">{LOGO}<span>super<b>occhiali</b>.it</span></a>
<nav class="nav" aria-label="Menu principale">{nav}</nav>
</header>
<main id="main">
{body}
</main>
<footer class="wrap foot">
<p>superocchiali.it confronta i prezzi dei negozi online. Alcuni link sono di affiliazione: se compri, il negozio ci riconosce una piccola commissione. Il prezzo per te non cambia.</p>
<nav aria-label="Pie di pagina"><a href="/privacy/">Privacy</a><a href="/sole/">Sole</a><a href="/vista/">Vista</a></nav>
</footer>
</body>
</html>
"""


def face_svg(d):
    return f'<svg viewBox="0 0 44 52" aria-hidden="true"><path d="{d}" fill="#fff" stroke="#141414" stroke-width="3"/></svg>'


FACES = [
    ("tondo", "tondo", "M22 4 C38 4 40 20 40 28 C40 40 32 48 22 48 C12 48 4 40 4 28 C4 20 6 4 22 4 Z"),
    ("ovale", "ovale", "M22 3 C35 3 38 16 38 26 C38 40 30 49 22 49 C14 49 6 40 6 26 C6 16 9 3 22 3 Z"),
    ("quadrato", "quadrato", "M8 5 L36 5 Q40 5 40 10 L40 40 Q40 48 32 48 L12 48 Q4 48 4 40 L4 10 Q4 5 8 5 Z"),
    ("cuore", "a cuore", "M4 8 Q22 0 40 8 Q40 30 22 49 Q4 30 4 8 Z"),
    ("allungato", "allungato", "M22 2 C33 2 35 14 35 26 C35 40 30 50 22 50 C14 50 9 40 9 26 C9 14 11 2 22 2 Z"),
]


def eyes(n):
    return "".join(
        f'<svg width="26" height="18" viewBox="0 0 26 18" aria-hidden="true"><ellipse cx="13" cy="9" rx="11" ry="7" fill="{"#FFD23F" if i < n else "#fff"}" stroke="#141414" stroke-width="2.5"/><circle cx="13" cy="9" r="3.5" fill="#141414"/></svg>'
        for i in range(5))


def offerte(reparto="", light=False):
    cls = "empty light" if light else "empty"
    return (f'<div id="offerte" data-reparto="{reparto}">'
            f'<div class="{cls}"><p>Stiamo collegando i primi negozi. Appena arrivano i loro listini, qui trovi le offerte del giorno con i prezzi a confronto.</p></div></div>')


faces_html = "".join(
    f'<button type="button" class="face" data-face="{k}" data-label="{l}" aria-pressed="{"true" if k == "tondo" else "false"}">{face_svg(d)}<span>{l}</span></button>'
    for k, l, d in FACES)

HOME = f"""<section id="test" class="wrap hero">
<div class="hero-txt">
<p class="badge">Il comparatore che ti guarda in faccia</p>
<h1>Che faccia hai?</h1>
<p class="lead">Scegli la forma del tuo viso: ti diciamo quali montature ti stanno bene e ti mostriamo i prezzi dei negozi a confronto.</p>
<div class="faces" role="group" aria-label="Forma del viso">{faces_html}</div>
<div class="tip" aria-live="polite">
<p>Viso <span id="tip-label">tondo</span>: <span id="tip-text">montature squadrate o rettangolari, che aggiungono angoli.</span></p>
<a href="/vista/">Vedi le montature →</a>
</div>
</div>
<div class="hero-art"><img src="/img/mascotte.svg" width="380" height="380" alt="La mascotte di superocchiali: un paio di occhiali con gli occhi che saluta"></div>
</section>

<section class="dark" aria-labelledby="lenti">
<div class="wrap">
<div class="sec-head"><h2 id="lenti">Le Lenti del Giorno</h2><p>Prezzi presi ogni giorno dai negozi</p></div>
{offerte()}
</div>
</section>

<section class="wrap depts" aria-label="Reparti">
<a class="dept sun" href="/sole/"><h2>Sole</h2><p>Per chi strizza gli occhi da aprile a ottobre.</p>
<span class="tags"><span class="tag">Polarizzati</span><span class="tag">Sportivi</span><span class="tag">A specchio</span><span class="tag">Vintage</span><span class="tag">Bambini</span></span></a>
<a class="dept coral" href="/vista/"><h2>Vista</h2><p>Per chi legge il menu a un braccio di distanza.</p>
<span class="tags"><span class="tag">Montature economiche</span><span class="tag">Luce blu</span><span class="tag">Da lettura</span><span class="tag">Titanio</span></span></a>
</section>

<section class="wrap split" aria-labelledby="occhiometro">
<div><h2 id="occhiometro">L'Occhiometro</h2>
<p>Ogni offerta prende da 1 a 5 occhi. Contano solo dati veri: prezzo, spese di spedizione, giorni per il reso. Niente recensioni inventate.</p></div>
<div class="meter" aria-label="Esempio di Occhiometro">
<div class="meter-row"><span>Prezzo più basso</span><span class="eyes">{eyes(5)}</span></div>
<div class="meter-row"><span>Spedizione gratis</span><span class="eyes">{eyes(4)}</span></div>
<div class="meter-row"><span>Reso entro 30 giorni</span><span class="eyes">{eyes(3)}</span></div>
</div>
</section>

<section class="band" aria-labelledby="vicino">
<div class="wrap">
<h2 id="vicino">Visto da Vicino</h2>
<p>Le guide in arrivo.</p>
<div class="grid">
<div class="note"><p class="kind">Guida</p><h3>Aviator: sì, anche se non piloti</h3></div>
<div class="note"><p class="kind">Domande sceme (ma non troppo)</p><h3>Le lenti per la luce blu servono davvero?</h3></div>
<div class="note"><p class="kind">Sotto i 50€</p><h3>Polarizzati che non piangono al primo graffio</h3></div>
</div>
</div>
</section>"""


def reparto(nome, slug, lead, cats, faccia):
    cats_html = "".join(f'<div class="cat"><h2>{t}</h2><p>{d}</p></div>' for t, d in cats)
    return f"""<section class="wrap page-hero">
<p class="badge">Reparto {nome}</p>
<h1>Occhiali {"da sole" if slug == "sole" else "da vista"}</h1>
<p class="lead">{lead}</p>
</section>
<section class="wrap cats" aria-label="Tipi">{cats_html}</section>
<section class="dark" aria-labelledby="lenti">
<div class="wrap">
<div class="sec-head"><h2 id="lenti">Offerte {nome.lower()}</h2><p>Prezzi presi ogni giorno dai negozi</p></div>
{offerte(slug)}
</div>
</section>
<section class="wrap prose">
<h2>Quale forma per il tuo viso</h2>
<p>{faccia} Non sai che faccia hai? <a href="/#test">Fai il test</a>.</p>
</section>"""


SOLE = reparto(
    "Sole", "sole",
    "Polarizzati, sportivi, vintage: confronta i prezzi dei negozi online e scegli quello che costa meno, spedizione compresa.",
    [("Polarizzati", "Tagliano i riflessi di acqua, neve e asfalto. Utili alla guida e al mare."),
     ("Sportivi", "Avvolgenti e leggeri, restano su anche quando corri."),
     ("A specchio", "Lente riflettente: si vede poco dentro, si vede bene fuori."),
     ("Vintage", "Tondi, aviator, wayfarer: le forme che tornano ogni estate."),
     ("Bambini", "Lenti con filtro UV e montature che resistono alle cadute.")],
    "Viso tondo: forme squadrate. Viso quadrato: forme tonde. Viso ovale: quasi tutto, aviator compresi.")

VISTA = reparto(
    "Vista", "vista",
    "Montature economiche, in titanio, con filtro luce blu: confronta i prezzi e porta la ricetta del tuo ottico.",
    [("Montature economiche", "Il necessario per vedere bene, senza pagare il marchio."),
     ("Luce blu", "Lenti con filtro per chi passa la giornata davanti a uno schermo."),
     ("Da lettura", "Graduazione fissa, da tenere in borsa o sul comodino."),
     ("Titanio", "Leggere e resistenti, non lasciano segni sul naso.")],
    "Viso a cuore: cat-eye leggeri o montature senza bordo sotto. Viso allungato: montature alte o oversize.")

PRIVACY = """<section class="wrap prose page-hero">
<h1>Privacy</h1>
<p>superocchiali.it non usa cookie e non raccoglie dati personali. Non ci sono moduli, registrazioni o strumenti di tracciamento.</p>
<h2>Link ai negozi</h2>
<p>Quando clicchi un'offerta vai sul sito del negozio, che tratta i tuoi dati secondo la propria informativa. Il link può contenere un codice di affiliazione: serve al negozio per riconoscere che arrivi da qui.</p>
<h2>Font e hosting</h2>
<p>I caratteri sono ospitati sul sito stesso, senza chiamate a servizi esterni. Il sito è ospitato su GitHub Pages, che può registrare l'indirizzo IP dei visitatori per motivi di sicurezza.</p>
</section>"""

NOTFOUND = """<section class="wrap page-hero">
<h1>Qui non si vede niente</h1>
<p class="lead">Questa pagina non esiste. Forse servono un paio di occhiali nuovi?</p>
<p><a class="pill is-sun" href="/">Torna alla home</a></p>
</section>"""

PAGES = [
    ("/", "index.html", "superocchiali.it: occhiali da sole e da vista, prezzi a confronto",
     "Confronta i prezzi di occhiali da sole e da vista nei negozi online. Scopri le montature giuste per la forma del tuo viso.", HOME, ""),
    ("/sole/", "sole/index.html", "Occhiali da sole: prezzi a confronto | superocchiali.it",
     "Occhiali da sole polarizzati, sportivi e vintage: confronta i prezzi dei negozi online.", SOLE, "/sole/"),
    ("/vista/", "vista/index.html", "Occhiali da vista e montature: prezzi a confronto | superocchiali.it",
     "Montature da vista economiche, in titanio e con filtro luce blu: confronta i prezzi dei negozi online.", VISTA, "/vista/"),
    ("/privacy/", "privacy/index.html", "Privacy | superocchiali.it",
     "Informativa privacy di superocchiali.it: niente cookie, niente dati personali.", PRIVACY, ""),
    ("/404.html", "404.html", "Pagina non trovata | superocchiali.it",
     "Pagina non trovata.", NOTFOUND, ""),
]

for path, out, title, desc, body, cur in PAGES:
    f = ROOT / out
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(page(path, title, desc, body, cur), encoding="utf-8")

(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"<url><loc>{SITE}{p}</loc></url>\n" for p, *_ in PAGES if p.endswith("/"))
    + "</urlset>\n", encoding="utf-8")
print("ok")
