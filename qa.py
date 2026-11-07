import re, json, sys, itertools, glob
from pathlib import Path
from lxml import html as LH
site=Path('/home/claude/mdr/site'); DOM='marinadelreywaterdamagepros.com'
BANNED=["free estimate","free inspection","guaranteed arrival","near me","insurance approved","direct billing","aggregaterating","\"review\"","howto","whatsapp","delve into","peace of mind","rest assured","seamless","cutting-edge","state-of-the-art","a wide range of","when it comes to","look no further","top-notch","game-changer","nestled","boasts","we pride ourselves","in today's fast-paced"]
rows=[]; fails=0
tels=set(); shingles={}
def words(t): return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’%$.-]*",t))
pages=sorted(site.rglob('*.html'))
for f in pages:
    rel=str(f.relative_to(site)); raw=f.read_text('utf-8'); doc=LH.fromstring(raw)
    main=doc.xpath('//main')
    mt=' '.join(main[0].itertext()) if main else ''
    prob=[]
    title=doc.xpath('//title/text()')[0]; meta=(doc.xpath('//meta[@name="description"]/@content') or [''])[0]
    if rel!='404.html':
        if not 140<=len(meta)<=160: prob.append(f'meta{len(meta)}')
        if len(title)>66: prob.append(f'title{len(title)}')
    if len(doc.xpath('//h1'))!=1: prob.append('h1count')
    if len(doc.xpath('//main'))!=1: prob.append('maincount')
    for t in re.findall(r'href="tel:([^"]+)"',raw): tels.add(t)
    tc=len(re.findall(r'href="tel:',raw))
    if re.search(r'<form|<input|<textarea|<select',raw): prob.append('FORM')
    if re.search(r'[—–]|&mdash;|&ndash;',raw): prob.append('DASH')
    # prose semicolons
    prose=re.sub(r'\s+',' ',mt)
    if ';' in prose: prob.append(f'semi{prose.count(";")}')
    low=raw.lower()
    for b in BANNED:
        if b in low: prob.append('BANNED:'+b)
    for p in doc.xpath('//main//p'):
        t=' '.join(p.itertext()).strip()
        if words(t)>80: prob.append('LONGP'+str(words(t)))
    long=[]
    for e in doc.xpath('//main//p|//main//li|//main//td'):
        t=' '.join(e.itertext())
        for s in re.split(r'(?<=[.!?])\s+',t):
            if words(s)>45: long.append(words(s))
    if long: prob.append(f'LONGSENT{long}')
    # abs links
    for a in doc.xpath('//a/@href'):
        if a.startswith('https://'+DOM) or a.startswith('http://'+DOM): prob.append('ABSLINK')
    # silo
    typ='home' if rel=='index.html' else ('blog' if rel.startswith('blog/') and rel!='blog/index.html' else 'other')
    if typ!='blog':
        for a in doc.xpath('//main//article//a/@href|//main//div[@class="container prose-max"]//a/@href'):
            if a.startswith('/blog/') and rel!='blog/index.html': prob.append('MONEY->BLOG '+a)
    if typ=='blog':
        for a in doc.xpath('//main//article//a/@href'):
            if a.startswith('/blog/'): prob.append('BLOG->BLOG '+a)
    # faq equality
    gq=[]; ga=[]
    for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>',raw,re.S):
        j=json.loads(s)
        for n in j.get('@graph',[j]):
            if n.get('@type')=='FAQPage': gq=[q['name'] for q in n['mainEntity']]; ga=[q['acceptedAnswer']['text'] for q in n['mainEntity']]
    dq=[' '.join(b.itertext()).strip() for b in doc.xpath('//button[@class="faq-q"]')]
    if gq!=dq: prob.append(f'FAQMISMATCH {len(gq)} vs {len(dq)}')
    else:
        da=[re.sub(r'\s+',' ',' '.join(' '.join(p.itertext()) for p in a.xpath('.//p'))) for a in doc.xpath('//div[@class="faq-in"]')]
        if [re.sub(r'\s+',' ',x).strip() for x in ga]!=[x.strip() for x in da] and gq:
            bad=sum(1 for x,y in zip([re.sub(r'\s+',' ',x).strip() for x in ga],[x.strip() for x in da]) if x!=y)
            if bad: prob.append(f'FAQTEXT{bad}')
    sc=len(doc.xpath('//aside[@class="sidecard"]'))
    if typ=='blog' or rel.split('/')[0] in ('water-mitigation','water-damage-cleanup','water-damage-repair','flood-damage-restoration','emergency-water-removal','mold-remediation') or (rel.startswith('service-area/') and rel!='service-area/index.html'):
        if sc!=1: prob.append(f'SIDECARD{sc}')
        NEUTRAL=rel.split('/')[-2] in ('venice-canals-ca','marina-peninsula-ca','oxford-triangle-ca')  # neighborhood pages use 2 neutral bullets by design
        if len(doc.xpath('//aside[@class="sidecard"]//li'))!=(2 if NEUTRAL else 4): prob.append('SIDEBULLETS')
    if tc<6 or tc>10: prob.append(f'TEL{tc}')
    if 'has-hero' in raw and 'class="hero-bg"' not in raw: prob.append('HEROMISSING')
    if 'style="' in raw: prob.append('INLINESTYLE')
    wc=words(mt)
    sh=set(prose[i:i+40] for i in range(0,max(len(prose)-40,0),8)); shingles[rel]=(sh,len(sh))
    rows.append((rel,wc,tc,len(title),len(meta),prob))
    fails+=bool(prob)
for r in rows: print(f'{r[0]:75s} w={r[1]:5d} tel={r[2]} t={r[3]} m={r[4]} {r[5] if r[5] else "ok"}')
print('unique tel hrefs:',tels)
# shingle dup
worst=[]
for a,b in itertools.combinations(shingles,2):
    A,na=shingles[a]; B,nb=shingles[b]
    if not A or not B: continue
    inter=len(A&B)/min(na,nb)
    if inter>0.08: worst.append((round(inter,3),a,b))
print('page pairs sharing >8% 40-char shingles (sampled every 8 chars):',sorted(worst,reverse=True)[:12])
print('pages with problems:',fails)
