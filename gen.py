import os, re, json, html, shutil, importlib.util, datetime, sys
from pathlib import Path
from urllib.parse import quote_plus
from css import CSS
import assets

ROOT=Path(__file__).parent
SITE=ROOT/'site'
DOMAIN='https://marinadelreywaterdamagepros.com'
BRAND='Marina Del Rey Water Damage Pros'
CITY='Marina Del Rey'
PHONE_E164='+14245505662'; PHONE='(424) 550-5662'; TEL='tel:+14245505662'
EMAIL='contact@marinadelreywaterdamagepros.com'
ADDR_STREET='4025 Lincoln Blvd'; ADDR_CITY='Marina del Rey'; ADDR_ST='CA'; ADDR_ZIP='90292'
ADDR_LINE=f'{ADDR_STREET}, {ADDR_CITY}, {ADDR_ST} {ADDR_ZIP}'
TODAY='2026-10-27'
YEAR=2026

SERVICES=[ # slug, nav label, short
 ('water-damage-repair','Water Damage Repair'),
 ('water-mitigation','Water Mitigation'),
 ('water-damage-cleanup','Water Damage Cleanup'),
 ('emergency-water-removal','Emergency Water Removal'),
 ('flood-damage-restoration','Flood Damage Restoration'),
 ('mold-remediation','Mold Remediation'),
]
NEW_SERVICES=[ # slug, label, group
 ('burst-pipe-water-damage','Burst Pipe Water Damage','By cause'),
 ('roof-leak-water-damage','Roof Leak Water Damage','By cause'),
 ('water-heater-leak-cleanup','Water Heater Leak Cleanup','By cause'),
 ('appliance-leak-water-damage','Appliance Leak Water Damage','By cause'),
 ('ac-leak-water-damage','AC Leak Water Damage Repair','By cause'),
 ('slab-leak-water-damage','Slab Leak Water Damage','By cause'),
 ('sewage-backup-cleanup','Sewage Backup Cleanup','By cause'),
 ('kitchen-water-damage','Kitchen Water Damage','By place'),
 ('crawl-space-water-damage','Crawl Space Water Damage','By place'),
 ('commercial-water-damage','Commercial Water Damage','By place'),
 ('carpet-water-damage','Carpet Water Damage','By material'),
 ('drywall-water-damage-repair','Wall and Drywall Water Damage Repair','By material'),
 ('storm-water-damage','Storm Water Damage Cleanup','By storm and structure'),
 ('structural-drying','Structural Drying and Dehumidification','By storm and structure'),
]
HOODS=[('venice-canals-ca','Venice Canals'),('marina-peninsula-ca','Marina Peninsula'),('oxford-triangle-ca','Oxford Triangle')]
AREAS=[('venice-ca','Venice'),('playa-vista-ca','Playa Vista'),('playa-del-rey-ca','Playa del Rey'),('culver-city-ca','Culver City'),('santa-monica-ca','Santa Monica')]
BLOG_PHOTO={'repair':'water-damage-repair','mold':'mold-remediation','flood':'flood-damage-restoration','pipe':'emergency-water-removal','drying':'water-mitigation','general':'water-damage-cleanup'}
BLOG_IMG={'ceiling-water-damage-causes-and-signs':'blog/ceiling-causes','ceiling-water-damage-repair':'blog/ceiling-repair','does-home-insurance-cover-water-damage':'blog/insurance','ground-floor-garage-water-cleanup':'blog/garage','how-to-fix-water-damaged-wood-floors':'blog/wood-floors-fix','is-mold-on-ceiling-dangerous':'blog/mold-ceiling','mold-in-bathroom-and-closet-how-to-remove':'blog/mold-bathroom','mold-in-condo-walls-how-to-remove':'blog/mold-condo','mold-removal-cost-factors':'blog/mold-cost','mold-removal-services-what-to-expect':'blog/mold-expect','water-damage-drying-company-how-to-choose':'blog/drying-company','water-damaged-hardwood-floors-cupping-buckling':'blog/hardwood-cupping','what-is-water-damage-restoration':'blog/what-is-restoration','what-kills-black-mold':'blog/black-mold','what-kills-mold':'blog/kills-mold'}
def blog_img(slug):
    k=slug.split('/')[-1].replace('-marina-del-rey-ca','')
    return BLOG_IMG.get(k)
APPROVED_HOOD=['Scope and price explained before work starts','Serving Marina Del Rey and nearby towns']
APPROVED=['Scope and price explained before work starts','Same-day response when available','Serving Marina Del Rey and nearby towns','Licensed and insured']

KNOWS=("water damage restoration|water mitigation|water damage cleanup|water damage repair|flood damage restoration|emergency water removal|water extraction|structural drying|slab leak water damage|crawl space water damage|kitchen water damage|commercial water damage|appliance leak water damage|"
"mold remediation|mold removal|mold testing|mold clearance testing|black mold|burst pipe water damage|sewage backup cleanup|ceiling water damage|wall water damage|hardwood floor water damage|"
"ANSI/IICRC S500|ANSI/IICRC S520|moisture meters|thermal imaging|air movers|LGR dehumidifiers|extraction units|moisture mapping|drying logs|containment barriers|HEPA air filtration|antimicrobial treatment|"
"Category 1 water|Category 2 water|Category 3 water|water damage insurance documentation|supply line leaks|washing machine hose leak|water heater leak|dishwasher leak|toilet overflow|roof leak|AC condensate line leak|"
"condo water damage|apartment water damage|HOA water damage|ground floor flooding|parking garage flooding|storm drain backup|Marina del Rey|Marina del Rey harbor|Fisherman's Village|Burton Chace Park|Yvonne B. Burke Park|Aubrey E. Austin Park|"
"Mother's Beach|Marina del Rey Wetland Park|Harold L. Edgington Memorial Park|Oxford Basin|Ballona Lagoon Marine Preserve|Ballona Creek|Admiralty Way|Washington Boulevard|Lincoln Boulevard|Marina Freeway|Admiralty High-Rise|"
"Venice|Venice Canals|Abbot Kinney Boulevard|Ocean Front Walk|Marina Peninsula|Playa Vista|Bluff Creek|Playa del Rey|Del Rey Lagoon|Culver City|Fox Hills|Blair Hills|Downtown Culver City|Santa Monica|Ocean Park|Pico neighborhood|"
"Westchester|Del Rey|Palms|El Segundo|Los Angeles County|Los Angeles County Public Works Building and Safety|LADBS|LADWP|Los Angeles County Department of Beaches and Harbors|FEMA Flood Map Service Center|ZIP 90292|ZIP 90291|ZIP 90094|ZIP 90293|ZIP 90230|ZIP 90232|ZIP 90401|"
"ZIP 90402|ZIP 90403|ZIP 90404|ZIP 90405|24/7 emergency dispatch|same-day water damage response|carpet drying|drywall removal|insulation removal|flood cut|subfloor drying|odor removal|content pack-out|dehumidification|water category classification").split('|')

# ---------- helpers ----------
LINK_RE=re.compile(r'\[([^\]]+)\]\((/[^)]*)\)')
def md(s):
    s=html.escape(s,quote=False)
    return LINK_RE.sub(lambda m:f'<a href="{m.group(2)}">{m.group(1)}</a>',s)
def plain(s): return LINK_RE.sub(r'\1',s)
def esc(s): return html.escape(s,quote=True)
def url(slug): return '/' if slug in ('','/') else f'/{slug.strip("/")}/'
def absu(slug): return DOMAIN+url(slug)
def tel_btn(text=None,cls='btn',extra=''):
    return f'<a class="{cls}" href="{TEL}">{text or "Call "+PHONE}</a>'
def hero_image(name):
    for ext in ('webp',):
        p=ROOT/'images'/f'{name}.{ext}'
        if p.exists():
            from PIL import Image
            w,h=Image.open(p).size
            return f'/images/{name}.{ext}',w,h
    return None
ALTS=json.load(open(ROOT/'images'/'alt.json')) if (ROOT/'images'/'alt.json').exists() else {}

def apply_patches(pages):
    from content_patches import PATCHES
    for pg in pages:
        pt=PATCHES.get(pg['slug'])
        if not pt: continue
        if 'faq' in pt:
            pg['faqs']=list(pg['faqs'][:-1])+[pt['faq']]+[pg['faqs'][-1]]
        if 'addlink' in pt:
            seen=0
            for b in pg['body']:
                if b['t']=='h2': seen+=1
                if seen>=2 and b['t']=='p' and len(b['text'].split())>=40:
                    b['text']=b['text'].rstrip()+' '+pt['addlink']; break
        if 'blocks' in pt:
            body=pg['body']; idx=len(body)
            if pt.get('before'):
                for i in range(len(body)-1,-1,-1):
                    if body[i]['t']==pt['before']: idx=i; break
            if pt.get('after_h2'):
                for i,b in enumerate(body):
                    if b['t']=='h2' and b['text']==pt['after_h2']:
                        j=i+1
                        while j<len(body) and body[j]['t'] not in ('h2','callout','localnote','cta'): j+=1
                        idx=j; break
            pg['body']=body[:idx]+pt['blocks']+body[idx:]
    return pages

def load(name):
    p=ROOT/'content'/f'{name}.py'
    if not p.exists(): return []
    spec=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.PAGES

# ---------- chrome ----------
def head(pg):
    slug=pg['slug']; canon=absu(slug)
    img_pre=''
    hi=pg.get('_hero')
    if hi: img_pre=f'<link rel="preload" as="image" href="{hi[0]}" fetchpriority="high">\n'
    og_img=DOMAIN+(hi[0] if hi else '/og-image.png')
    robots='<meta name="robots" content="noindex,follow">\n' if pg.get('noindex') else ''
    canon_tag='' if pg.get('noindex') else f'<link rel="canonical" href="{canon}">\n'
    blocks=pg.get('_schema',[])
    if blocks:
        graph=[{k:v for k,v in b.items() if k!='@context'} for b in blocks]
        schema='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+'</script>\n'
    else: schema=''
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(pg['title'])}</title>
<meta name="description" content="{esc(pg['meta'])}">
{robots}{canon_tag}<meta name="theme-color" content="#5C1627">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="{'article' if pg.get('type')=='blog' else 'website'}"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{esc(pg['title'])}"><meta property="og:description" content="{esc(pg['meta'])}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(pg['title'])}"><meta name="twitter:description" content="{esc(pg['meta'])}"><meta name="twitter:image" content="{og_img}">
{img_pre}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@700&family=Sora:wght@600;700;800&family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/main.css">
{schema}</head>'''

def header():
    svc_dd=''.join(f'<li><a href="{url(s)}">{n}</a></li>' for s,n in SERVICES[:3])+'<li><a href="/services/">All Services</a></li>'
    area_dd=''.join(f'<li><a href="{url("service-area/"+s)}">{n}</a></li>' for s,n in AREAS)+'<li><a href="/service-area/">All Service Areas</a></li>'
    drawer_svc=''.join(f'<li><a href="{url(s)}">{n}</a></li>' for s,n in SERVICES[:3])
    drawer_area=''.join(f'<li><a href="{url("service-area/"+s)}">{n}</a></li>' for s,n in AREAS)
    return f'''<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="site-header" role="banner">
<div class="topbar"><div class="container topbar-inner"><span class="topbar-loc">Marina Del Rey, CA and nearby towns</span><span>24/7 Dispatch: <a href="{TEL}">{PHONE}</a></span></div></div>
<nav id="site-nav" aria-label="Main navigation"><div class="container nav-inner">
<a class="logo" href="/" aria-label="{BRAND} home"><img src="/logo.svg" alt="{BRAND}" width="234" height="56"></a>
<ul class="nav-links">
<li><a href="/">Home</a></li>
<li class="has-dropdown"><a href="/services/" aria-haspopup="true">Services <span class="dd-arrow" aria-hidden="true">&#9662;</span></a><ul class="dropdown">{svc_dd}</ul></li>
<li class="has-dropdown"><a href="/service-area/" aria-haspopup="true">Areas <span class="dd-arrow" aria-hidden="true">&#9662;</span></a><ul class="dropdown">{area_dd}</ul></li>
<li><a href="/blog/">Blog</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li>
<li><a class="nav-cta" href="{TEL}">Call Now</a></li></ul>
<button class="hamburger" id="mob-toggle" aria-expanded="false" aria-controls="mob-drawer" aria-label="Open navigation menu"><span></span><span></span><span></span></button>
</div></nav></header>
<div class="mob-drawer" id="mob-drawer" role="dialog" aria-modal="true" aria-label="Navigation menu" hidden>
<button class="drawer-close" id="drawer-close" aria-label="Close navigation menu">&#10005;</button>
<ul><li><a href="/">Home</a></li>
<li class="drawer-h">Top Services</li>{drawer_svc}<li><a href="/services/">All Services</a></li>
<li class="drawer-h">Areas</li>{drawer_area}<li><a href="/service-area/">All Service Areas</a></li>
<li class="drawer-h">More</li><li><a href="/blog/">Blog</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li>
</ul><p class="drawer-note">Call {PHONE} any hour from the bar at the bottom of the screen.</p></div>
<div class="mob-overlay" id="mob-overlay" aria-hidden="true"></div>
'''

def coverage_map():
    q=quote_plus('Marina del Rey, CA')
    return f'''<section class="map-sec"><div class="container"><h2>Service Area Map: Marina Del Rey and Nearby Towns</h2>
<div class="map-wrap"><iframe src="https://maps.google.com/maps?q={q}&amp;output=embed&amp;z=12" title="Service area map: Marina Del Rey, CA and nearby towns" aria-label="Service area map: Marina Del Rey, CA and nearby towns" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></div></section>
'''

def footer():
    svc=''.join(f'<a href="{url(s)}">{n}</a>' for s,n in SERVICES)+'<a href="/services/">All Services</a>'
    ar=''.join(f'<a href="{url("service-area/"+s)}">{n}</a>' for s,n in AREAS)+'<a href="/service-area/">All Service Areas</a>'
    more=''.join(f'<a href="{url(s)}">{n}</a>' for s,n,g in NEW_SERVICES)
    return f'''<footer class="footer"><div class="container"><div class="footer-grid">
<div><a class="logo" href="/" aria-label="{BRAND} home"><img src="/logo.svg" alt="{BRAND}" width="234" height="56"></a>
<p>24-hour water damage restoration and mold remediation for Marina Del Rey, Venice, Playa Vista, Playa del Rey, Culver City and Santa Monica.</p>
<address>{BRAND}<br>{ADDR_STREET}<br>{ADDR_CITY}, {ADDR_ST} {ADDR_ZIP}</address>
<a class="tel" href="{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div><h2 class="footer-h">Services</h2>{svc}</div>
<div><h2 class="footer-h">More Services</h2>{more}</div>
<div><h2 class="footer-h">Service Areas</h2>{ar}</div>
<div><h2 class="footer-h">Company</h2><a href="/about/">About</a><a href="/contact/">Contact</a><a href="/blog/">Blog</a><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a></div>
</div><div class="footer-bottom">&copy; {YEAR} {BRAND}. All rights reserved. 24/7 emergency dispatch.</div></div></footer>
<div class="sticky-cta"><a href="{TEL}">&#9742; Call {PHONE} &middot; 24/7 Dispatch</a></div>
<a class="float-call" href="{TEL}" aria-label="Call {PHONE}">&#9742;</a>
<script src="/js/main.js" defer></script>
</body></html>'''

def ctaband(h='Water Spreading Right Now?',p='Call the 24/7 line. Describe what you see, and we will explain the next step and how scope and price are set before work starts.'):
    return f'<div class="ctaband"><div class="container"><h2>{esc(h)}</h2><p>{esc(p)}</p>{tel_btn()}</div></div>\n'

# ---------- blocks ----------
def render_blocks(body):
    out=[]; cur=None
    def close():
        nonlocal cur
        if cur is not None: out.append('</section>\n'); cur=None
    for b in body:
        t=b['t']
        if t=='h2':
            close(); out.append(f'<section class="panel-card"><h2>{md(b["text"])}</h2>'); cur='panel'
        elif t=='callout':
            close(); out.append(f'<section class="insight-card"><h2>{md(b["h"])}</h2>'+''.join(f'<p>{md(x)}</p>' for x in b['paras'])+'</section>\n')
        elif t=='localnote':
            close(); out.append(f'<section class="insight-card localnote"><span class="tag">Local note</span><h2>{md(b["h"])}</h2>'+''.join(f'<p>{md(x)}</p>' for x in b['paras'])+'</section>\n')
        elif t=='cta':
            close(); out.append(f'<div class="inline-cta"><p>{md(b["text"])}</p>{tel_btn()}</div>\n')
        else:
            if cur is None: out.append('<section class="panel-card">'); cur='panel'
            if t=='p': out.append(f'<p>{md(b["text"])}</p>')
            elif t=='h3': out.append(f'<h3>{md(b["text"])}</h3>')
            elif t=='ul': out.append('<ul class="icon-list">'+''.join(f'<li><span class="ico" aria-hidden="true">&#10003;</span><span>{md(i)}</span></li>' for i in b['items'])+'</ul>')
            elif t=='table':
                th=''.join(f'<th scope="col">{md(h)}</th>' for h in b['head'])
                tr=''.join('<tr>'+''.join(f'<td>{md(c)}</td>' for c in r)+'</tr>' for r in b['rows'])
                out.append(f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
            elif t=='cards':
                out.append('<div class="cardgrid">'+''.join(f'<div class="minicard"><h3>{md(i["h"])}</h3><p>{md(i["p"])}</p></div>' for i in b['items'])+'</div>')
            elif t=='steps':
                out.append('<ol class="stepslist">'+''.join(f'<li><div><h3>{md(i["h"])}</h3><p>{md(i["p"])}</p></div></li>' for i in b['items'])+'</ol>')
            else: raise ValueError('block '+t)
    close()
    return ''.join(out)

def faq_html(faqs,title='Frequently Asked Questions'):
    if not faqs: return ''
    items=[]
    for q,a in faqs:
        paras=a if isinstance(a,list) else [a]
        items.append(f'<div class="faq-item"><button class="faq-q" type="button" aria-expanded="false">{md(q)}</button><div class="faq-answer"><div class="faq-in">'+''.join(f'<p>{md(p)}</p>' for p in paras)+'</div></div></div>')
    return f'<section class="panel-card faq"><h2>{title}</h2>'+''.join(items)+'</section>\n'

def thumb(b):
    n=blog_img(b['slug'])
    p=ROOT/'images'/f'{n}-thumb.webp' if n else None
    if not p or not p.exists(): return ''
    return f'<a class="thumb" href="{url(b["slug"])}" tabindex="-1" aria-hidden="true"><img src="/images/{n}-thumb.webp" alt="{esc(ALTS.get(n,b["h1"]))}" width="640" height="360" loading="lazy" decoding="async"></a>'

def sidecard(pg):
    sc=pg['sidecard']; l=sc['link']
    return f'''<aside class="sidecard" aria-label="Call us"><div class="side-kick">{'Call to confirm availability' if pg.get('hood') else '24/7 Emergency Line Open'}</div><h2>{md(sc['h3'])}</h2><p>{md(sc['copy'])}</p>{tel_btn()}<ul>{''.join(f"<li>{b}</li>" for b in (APPROVED_HOOD if pg.get('hood') else APPROVED))}</ul><a class="side-link" href="{l[1]}">{esc(l[0])} &rarr;</a></aside>'''

def pagehead(pg,crumbs,extra=''):
    hi=pg.get('_hero')
    cls='pagehead has-hero' if hi else 'pagehead'
    img=''
    if hi:
        alt=ALTS.get(pg.get('photo_name',''),pg['h1'])
        img=f'<img class="hero-bg" src="{hi[0]}" alt="{esc(alt)}" width="{hi[1]}" height="{hi[2]}" fetchpriority="high" decoding="async">'
    cr=' <span>/</span> '.join(f'<a href="{u}">{esc(n)}</a>' if u else esc(n) for n,u in crumbs)
    badge=pg.get('badge') or ('<span class="badge badge-alt">Call to confirm availability</span>' if pg.get('hood') else '<span class="badge badge-alt">24/7 Emergency Line Open</span>')
    zips=''
    if pg['type']=='location':
        zips='<ul class="zips" aria-label="ZIP codes covered"><li class="zips-label">ZIP codes served:</li>'+''.join(f'<li class="zip-chip">{z}</li>' for z in pg['zips'])+'</ul>'
    by=''
    if pg['type']=='blog': by=f'<p class="byline">By the {BRAND} team &middot; Published <time datetime="{pg["date"]}">October 27, 2026</time></p>'
    return f'''<div class="{cls}">{img}<div class="container"><nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>{badge}<h1>{esc(pg['h1'])}</h1><p class="hero-sub">{md(pg['hero_sub'])}</p>{by}{zips}<div class="cta-row">{tel_btn()}<a class="btn btn-ghost" href="/services/">See Our Services</a></div></div></div>
'''

def loc_services(pg):
    chips=''.join(f'<li><a href="{url(sl)}">{esc(n)} in {esc(pg["loc"])}</a></li>' for sl,n,g in NEW_SERVICES)
    return f'<section class="panel-card"><h2>More water damage services in {esc(pg["loc"])}</h2><ul class="svc-chips">{chips}</ul></section>\n'

def loc_facts(pg):
    z=', '.join(pg['zips'])
    return f'''<div class="loc-facts"><div class="loc-fact"><h2>ZIP codes</h2><p>Primary ZIP {pg['primary_zip']}.{(' Also covered: '+', '.join(x for x in pg['zips'] if x!=pg['primary_zip'])+'.') if len(pg['zips'])>1 else ''}{(' '+esc(pg['zip_note'])) if pg.get('zip_note') else ''}</p></div><div class="loc-fact"><h2>Water utility</h2><p>{esc(pg['utility'])}</p></div><div class="loc-fact"><h2>Permits and inspections</h2><p>{esc(pg['permit'])}</p></div><div class="loc-fact"><h2>{'Availability' if pg.get('hood') else 'Dispatch'}</h2><p>{'Call us to confirm availability for your address.' if pg.get('hood') else 'Emergency dispatch available around the clock, every day, from Marina Del Rey.'}</p></div></div>
'''

def loc_map(pg):
    q=quote_plus(pg['map_q'])
    return f'''<section class="panel-card map-small"><h2>Map of {esc(pg['loc'])}, CA</h2><div class="map-wrap"><iframe src="https://maps.google.com/maps?q={q}&amp;output=embed&amp;z={pg['map_z']}" title="Map centered on {esc(pg['loc'])}, CA" aria-label="Map centered on {esc(pg['loc'])}, CA" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></section>
'''

def contact_map():
    q=quote_plus(ADDR_LINE)
    return f'''<section class="panel-card map-small"><h2>Our Marina Del Rey address</h2><div class="map-wrap"><iframe src="https://maps.google.com/maps?q={q}&amp;output=embed&amp;z=15" title="Map of {esc(ADDR_LINE)}" aria-label="Map of {esc(ADDR_LINE)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></section>
'''

# ---------- schema ----------
def business():
    return {"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","@id":DOMAIN+"/#business","name":BRAND,"url":DOMAIN+"/","telephone":PHONE_E164,"email":EMAIL,
     "image":DOMAIN+"/og-image.png","logo":DOMAIN+"/logo.svg","priceRange":"$$",
     "description":"24/7 water damage restoration and mold remediation in Marina Del Rey, CA and nearby Venice, Playa Vista, Playa del Rey, Culver City and Santa Monica.",
     "address":{"@type":"PostalAddress","streetAddress":ADDR_STREET,"addressLocality":ADDR_CITY,"addressRegion":ADDR_ST,"postalCode":ADDR_ZIP,"addressCountry":"US"},
     "areaServed":[{"@type":"Place","name":n} for n in ["Marina del Rey, CA","Venice, Los Angeles, CA","Playa Vista, Los Angeles, CA","Playa del Rey, Los Angeles, CA","Culver City, CA","Santa Monica, CA"]],
     "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}],
     "knowsAbout":KNOWS}
def breadcrumbs(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":DOMAIN+u} for i,(n,u) in enumerate(items)]}
def faq_schema(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":plain(q),"acceptedAnswer":{"@type":"Answer","text":' '.join(plain(x) for x in (a if isinstance(a,list) else [a]))}} for q,a in faqs]}
def schema_for(pg,crumb_items):
    blocks=[business(),{"@context":"https://schema.org","@type":"WebPage","@id":absu(pg['slug']),"url":absu(pg['slug']),"name":pg['title'],"description":pg['meta'],"isPartOf":{"@id":DOMAIN+"/#business"}},breadcrumbs(crumb_items)]
    t=pg['type']
    if t=='service':
        blocks.append({"@context":"https://schema.org","@type":"Service","name":pg['h1'],"serviceType":pg['h1'].replace(' in Marina Del Rey, CA','').replace(' Marina Del Rey, CA',''),"provider":{"@id":DOMAIN+"/#business"},"areaServed":{"@type":"Place","name":"Marina del Rey, CA"},"url":absu(pg['slug'])})
    elif t=='location':
        blocks.append({"@context":"https://schema.org","@type":"Service","name":pg['h1'],"serviceType":"Water damage restoration","provider":{"@id":DOMAIN+"/#business"},"areaServed":{"@type":"Place","name":pg.get('area_name') or f"{pg['loc']}, CA"},"url":absu(pg['slug'])})
    elif t=='blog':
        img=pg.get('_hero'); imgu=DOMAIN+(img[0] if img else '/og-image.png')
        blocks.append({"@context":"https://schema.org","@type":"Article","headline":pg['h1'],"description":pg['meta'],"author":{"@type":"Organization","name":BRAND},"publisher":{"@type":"Organization","name":BRAND,"logo":{"@type":"ImageObject","url":DOMAIN+"/logo.svg"}},"datePublished":pg['date'],"dateModified":TODAY,"image":imgu,"mainEntityOfPage":absu(pg['slug'])})
    if pg.get('faqs'): blocks.append(faq_schema(pg['faqs']))
    return blocks

# ---------- page assembly ----------
def crumbs_for(pg):
    t=pg['type']; s=pg['slug']
    c=[('Home','/')]
    if t=='service': c+= [('Services','/services/'),(pg['h1'].replace(' in Marina Del Rey, CA','').replace(' Marina Del Rey, CA','').replace(' | Water Damage Pros',''),url(s))]
    elif t=='location': c+=[('Service Areas','/service-area/'),(pg['loc'],url(s))]
    elif t=='blog': c+=[('Blog','/blog/'),(pg['h1'][:60],url(s))]
    elif s!='': c+=[(pg.get('crumb') or pg['title'].split('|')[0].strip(),url(s))]
    return c

def render_inner(pg):
    t=pg['type']
    if t in('service','location','blog'):
        pn=pg.get('photo') if t=='service' else (blog_img(pg['slug']) or BLOG_PHOTO.get(pg.get('category')) if t=='blog' else None)
        pg['photo_name']=pn
        pg['_hero']=hero_image(pn) if pn else None
    crumbs=crumbs_for(pg)
    pg['_schema']=schema_for(pg,crumbs)
    parts=[head(pg),header()]
    parts.append('<main id="main-content">\n')
    parts.append(pagehead(pg,crumbs))
    if t in('service','location','blog'):
        art=''
        if t=='location': art+=loc_facts(pg)
        art+=render_blocks(pg['body'])+faq_html(pg.get('faqs'))
        if t=='location': art+=loc_map(pg)+('' if pg.get('hood') else loc_services(pg))
        parts.append(f'<section class="sec sec-soft"><div class="container twocol"><article>{art}</article>{sidecard(pg)}</div></section>\n')
    else:
        art=render_blocks(pg['body'])+faq_html(pg.get('faqs'))
        if pg['slug']=='contact': art=pg.get('_contact_grid','')+art+contact_map()
        parts.append(f'<section class="sec sec-soft"><div class="container prose-max">{art}</div></section>\n')
    parts.append('</main>\n')
    parts.append(ctaband())
    parts.append(coverage_map())
    parts.append(footer())
    return ''.join(parts)

def finder():
    groups={}
    for sl,n,g in NEW_SERVICES: groups.setdefault(g,[]).append((sl,n))
    cols=''.join(f'<div class="find-col"><h3>{esc(g)}</h3><ul>'+''.join(f'<li><a href="{url(sl)}">{esc(n)}</a></li>' for sl,n in items)+'</ul></div>' for g,items in groups.items())
    return f'<section class="sec sec-soft"><div class="container"><div class="kick">Find Your Cause Or Room</div><h2 class="sec-title">Start With What Went Wrong, Or Where</h2><p class="find-intro">Each page below covers one cause, room or material in detail, with the first-hour steps, the drying plan and what shapes the scope. Pick the one that matches what you see, or call and the dispatcher will match it for you.</p><div class="find-grid">{cols}</div></div></section>\n'

def render_home(H):
    pg=dict(H); pg['type']='home'; pg['slug']=''
    hi=hero_image('home'); pg['_hero']=hi
    pg['_schema']=[business(),{"@context":"https://schema.org","@type":"WebSite","@id":DOMAIN+"/#website","url":DOMAIN+"/","name":BRAND,"publisher":{"@id":DOMAIN+"/#business"}},{"@context":"https://schema.org","@type":"WebPage","@id":DOMAIN+"/","url":DOMAIN+"/","name":pg['title'],"description":pg['meta'],"isPartOf":{"@id":DOMAIN+"/#website"}},breadcrumbs([('Home','/')])]
    if H.get('faqs'): pg['_schema'].append(faq_schema(H['faqs']))
    cls='hero has-hero' if hi else 'hero'
    img=f'<img class="hero-bg" src="{hi[0]}" alt="{esc(ALTS.get("home",H["h1"]))}" width="{hi[1]}" height="{hi[2]}" fetchpriority="high" decoding="async">' if hi else ''
    p=[head(pg),header(),'<main id="main-content">\n']
    p.append(f'''<section class="{cls}">{img}<div class="container hero-grid"><div><span class="badge">24/7 Emergency Dispatch</span><h1>Water Damage Restoration <span>in Marina Del Rey, CA</span></h1><p class="hero-sub">{md(H['hero_sub'])}</p><div class="cta-row">{tel_btn()}<a class="btn btn-ghost" href="/services/">See Our Services</a></div><ul class="trustrow"><li>Licensed and insured</li><li>Documentation for your claim</li><li>24/7 dispatch</li></ul></div>
<div class="statpanel"><h2>Dispatch at a glance</h2>{''.join(f'<div class="strow"><span>{a}</span><b>{b}</b></div>' for a,b in H['stats'])}</div></div></section>
<div class="strip"><div class="container strip-inner">{''.join(f'<div class="stripitem"><span class="ic" aria-hidden="true">{i}</span>{esc(t)}</div>' for i,t in [('&#128737;','Licensed and insured'),('&#128203;','Documentation for your claim'),('&#9201;','24/7 emergency dispatch'),('&#128205;','Serving Marina Del Rey and nearby towns')])}</div></div>
<div class="emergency"><div class="container emergency-inner"><div><h2>Active Water, Overflow Or Mold Behind A Wall?</h2><p>The dispatch line is answered 24 hours a day, every day of the year.</p></div>{tel_btn('Call '+PHONE,'btn')}</div></div>
''')
    # services
    cards=''
    icons={'water-damage-repair':'&#128295;','water-mitigation':'&#128167;','water-damage-cleanup':'&#129532;','emergency-water-removal':'&#128680;','flood-damage-restoration':'&#127754;','mold-remediation':'&#129440;'}
    for s,n in SERVICES:
        d=H['service_blurbs'][s]
        cards+=f'<div class="card"><div class="ic" aria-hidden="true">{icons[s]}</div><h3>{n}</h3><p>{md(d)}</p><a class="more" href="{url(s)}">View service &rarr;</a></div>'
    p.append(f'<section class="sec"><div class="container"><div class="kick">Restoration Services</div><h2 class="sec-title">{esc(H["services_h2"])}</h2><div class="cards">{cards}</div></div></section>\n')
    p.append(finder())
    # generic panel sections
    for sec in H['sections']:
        k=sec['kind']
        if k=='panels':
            p.append(f'<section class="sec {sec.get("bg","")}"><div class="container prose-max"><div class="kick">{esc(sec["kick"])}</div>{render_blocks(sec["body"])}</div></section>\n')
        elif k=='why':
            p.append(f'<section class="sec sec-soft"><div class="container"><div class="kick">{esc(sec["kick"])}</div><h2 class="sec-title">{esc(sec["h2"])}</h2><div class="why">'+''.join(f'<div class="whycard"><div class="num">{i+1}</div><h3>{esc(h)}</h3><p>{md(t)}</p></div>' for i,(h,t) in enumerate(sec['items']))+'</div></div></section>\n')
        elif k=='steps':
            p.append(f'<section class="sec"><div class="container"><div class="kick">{esc(sec["kick"])}</div><h2 class="sec-title">{esc(sec["h2"])}</h2><div class="steps">'+''.join(f'<div class="step"><div class="n">{i+1}</div><h3>{esc(h)}</h3><p>{md(t)}</p></div>' for i,(h,t) in enumerate(sec['items']))+'</div></div></section>\n')
        elif k=='hoods':
            p.append(f'<section class="sec"><div class="container"><div class="kick">{esc(sec["kick"])}</div><h2 class="sec-title">{esc(sec["h2"])}</h2>'+render_blocks(sec['body'])+'<div class="areas">'+''.join(f'<a href="{url("service-area/"+s)}">{n}</a>' for s,n in HOODS)+'</div></div></section>\n')
        elif k=='areas':
            p.append(f'<section class="sec sec-soft"><div class="container"><div class="kick">{esc(sec["kick"])}</div><h2 class="sec-title">{esc(sec["h2"])}</h2>'+render_blocks(sec['body'])+'<div class="areas">'+''.join(f'<a href="{url("service-area/"+s)}">{n}</a>' for s,n in AREAS)+'</div></div></section>\n')
    p.append(faq_html_section(H['faqs']))
    p.append('</main>\n'); p.append(ctaband()); p.append(coverage_map()); p.append(footer())
    return ''.join(p)

def faq_html_section(faqs):
    return '<section class="sec"><div class="container prose-max">'+faq_html(faqs)+'</div></section>\n'

JS='''(function(){
function qs(id){return document.getElementById(id);}
var t=qs("mob-toggle"),d=qs("mob-drawer"),o=qs("mob-overlay"),c=qs("drawer-close");
function openMenu(){d.removeAttribute("hidden");o.classList.add("visible");t.setAttribute("aria-expanded","true");t.setAttribute("aria-label","Close navigation menu");document.documentElement.style.overflow="hidden";}
function closeMenu(){d.setAttribute("hidden","");o.classList.remove("visible");t.setAttribute("aria-expanded","false");t.setAttribute("aria-label","Open navigation menu");document.documentElement.style.overflow="";}
if(t&&d&&o){
t.addEventListener("click",function(){if(t.getAttribute("aria-expanded")==="true"){closeMenu();}else{openMenu();}});
if(c){c.addEventListener("click",closeMenu);}
o.addEventListener("click",closeMenu);
var links=d.querySelectorAll("a");for(var i=0;i<links.length;i++){links[i].addEventListener("click",closeMenu);}
document.addEventListener("keydown",function(e){if(e.key==="Escape"){closeMenu();}});
var mq=window.matchMedia("(min-width: 769px)");
var onChange=function(e){if(e.matches){closeMenu();}};
if(mq.addEventListener){mq.addEventListener("change",onChange);}
}
var qb=document.querySelectorAll(".faq-q");
for(var j=0;j<qb.length;j++){qb[j].addEventListener("click",function(){var it=this.parentNode;var open=it.classList.toggle("open");this.setAttribute("aria-expanded",open?"true":"false");});}
})();
'''

def write(path,txt):
    p=SITE/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(txt,encoding='utf-8')

def build():
    if SITE.exists(): shutil.rmtree(SITE)
    SITE.mkdir()
    assets.build(str(SITE))
    write('css/main.css',CSS); write('js/main.js',JS)
    if (ROOT/'images').exists():
        shutil.copytree(ROOT/'images',SITE/'images',ignore=shutil.ignore_patterns('alt.json'))
    pages=[]
    for m in ('service','svc_new_a','svc_new_b','svc_new_c','svc_new_d','location','neighborhood','blog_a','blog_b'): pages+=load(m)
    pages=apply_patches(pages)
    std=None
    std=apply_patches(load('std'))
    from home import HOME
    paths=[]
    write('index.html',render_home(HOME)); paths.append('')
    blogs=[p for p in pages if p['type']=='blog']
    for pg in pages:
        write(url(pg['slug']).strip('/')+'/index.html',render_inner(pg)); paths.append(pg['slug'])
    # standard pages (including hubs). blog index generated
    for pg in std:
        pg=dict(pg); pg['type']='standard'
        if pg['slug']=='blog':
            body=[{'t':'h2','text':'Homeowner guides for Marina Del Rey and nearby towns'},{'t':'p','text':pg['intro']}]
            pg['body']=body
            cards='<div class="bloggrid">'+''.join(f'<div class="blogcard">{thumb(b)}<span class="tagline">{esc(b["category"].title())}</span><h3><a href="{url(b["slug"])}">{esc(b["h1"])}</a></h3><p>{md(b["hero_sub"])}</p><a class="more" href="{url(b["slug"])}">Read the guide &rarr;</a></div>' for b in blogs)+'</div>'
            pg['_blogcards']=cards
        if pg['slug']=='contact':
            pg['_contact_grid']=f'<div class="contact-grid"><div class="loc-fact"><h2>Call 24/7</h2><p><a href="{TEL}">{PHONE}</a></p></div><div class="loc-fact"><h2>Address</h2><p>{ADDR_STREET}<br>{ADDR_CITY}, {ADDR_ST} {ADDR_ZIP}</p></div><div class="loc-fact"><h2>Email</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>'
        html_=render_inner(pg)
        if pg['slug']=='blog': html_=html_.replace('</section>\n</div></section>',f'</section>\n{pg["_blogcards"]}</div></section>',1)
        write(url(pg['slug']).strip('/')+'/index.html',html_); paths.append(pg['slug'])
    # 404
    nf={'title':'Page Not Found | '+BRAND,'meta':'The page you were looking for could not be found. Call the 24/7 line or return to the Marina Del Rey Water Damage Pros home page.','h1':'Page Not Found','hero_sub':'That page is not here. Use the menu, or call the 24/7 line if you have water damage right now.','slug':'404','type':'standard','noindex':True,'body':[{'t':'h2','text':'Where to go next'},{'t':'p','text':'Return to the [home page](/) or browse the [water damage services](/services/) and [service areas](/service-area/) we cover around Marina Del Rey.'}],'_schema':[]}
    h=render_inner(nf); write('404.html',h)
    # sitemap
    urls=''.join(f'<url><loc>{absu(s)}</loc><lastmod>{TODAY}</lastmod></url>' for s in paths)
    write('sitemap.xml',f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write('robots.txt',f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    write('_headers','/*\n  Strict-Transport-Security: max-age=31536000; includeSubDomains\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n')
    write('_redirects','# No redirects needed. Cloudflare Pages serves slug/index.html routes natively.\n')
    print('built',len(paths)+1,'html files')
if __name__=='__main__': build()
