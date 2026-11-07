import glob,re,json,itertools,os
from lxml import html
site='site'
pages={}
for f in sorted(glob.glob(site+'/**/index.html',recursive=True)):
    slug=f[len(site)+1:-len('index.html')].strip('/')
    pages[slug]=(f,html.fromstring(open(f).read()))
def kind(s):
    if s=='' : return 'home'
    if s.startswith('blog/'): return 'blog'
    if s.startswith('service-area/') and s!='service-area': return 'loc'
    if s in('about','contact','privacy','terms','blog','services','service-area'): return 'std'
    return 'svc'
rows=[]
for s,(f,d) in pages.items():
    t=d.xpath('//title')[0].text; h1=d.xpath('//h1')[0].text_content().strip()
    h2=[x.text_content().strip() for x in d.xpath('//main//h2')]
    rows.append((s,kind(s),t,h1,h2))
print('TITLE MATRIX (service pages)')
for s,k,t,h1,h2 in rows:
    if k=='svc': print(f'{len(t):2d} {s:34s} {t}  || H1 ok={h1 in t}')
# near-duplicate titles
def toks(t): return set(re.findall(r'[a-z0-9/]+',t.lower().split('|')[0]))-{'in','marina','del','rey','ca','emergency'}
print('\nPAIRS with title token overlap >=0.8 or one-word difference:')
bad=0
for a,b in itertools.combinations(rows,2):
    ta,tb=toks(a[2]),toks(b[2])
    j=len(ta&tb)/max(1,len(ta|tb))
    if (a[1] in('svc','home') and b[1] in('svc','home')) and (j>=0.8 or len(ta^tb)<=1): print(' ',a[0],'|',b[0],round(j,2)); bad+=1
print('flagged',bad)
# duplicate H1 / title
from collections import Counter
for nm,idx in(('title',2),('h1',3)):
    c=Counter(r[idx] for r in rows); print('dup',nm,[k for k,v in c.items() if v>1])
# H2 duplicates among money pages
c=Counter(h.lower() for r in rows if r[1] in('svc','home') for h in r[4]); print('H2 shared by >1 money page:',[(k,v) for k,v in c.items() if v>1 and k not in('frequently asked questions',)])
# links
allslugs=set(pages)|{''}
inbound=Counter(); probs=[]
for s,(f,d) in pages.items():
    k=kind(s)
    for a in d.xpath('//main//a/@href'):
        if a.startswith('tel:') or a.startswith('mailto:'): continue
        if a.startswith('http') or not a.startswith('/') or not a.endswith('/'): probs.append(('ABS/REL',s,a)); continue
        t=a.strip('/')
        if t not in allslugs: probs.append(('BROKEN',s,a))
        else: inbound[t]+=1
        if k=='svc' and t.startswith('blog'): probs.append(('SILO money->blog',s,a))
        if k=='loc' and t.startswith('blog/'): probs.append(('SILO loc->blog',s,a))
        if k=='blog' and t.startswith('blog/') : probs.append(('SILO blog->blog',s,a))
    for im in d.xpath('//img/@src'):
        if not os.path.exists(site+im): probs.append(('IMG missing',s,im))
print('\nlink problems:',probs)
print('orphans (no inbound from main):',[s for s in allslugs if s and not inbound[s]])
print('inbound counts new pages:',{s:inbound[s] for s in pages if kind(s)=='svc'})
