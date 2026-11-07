import re, glob, json
from pathlib import Path
from playwright.sync_api import sync_playwright
site=Path('site'); urls=[]
for f in sorted(site.rglob('index.html')):
    r='/'+str(f.parent.relative_to(site)).replace('\\','/')+'/'; urls.append('/' if r=='/./' else r)
urls.append('/404.html')
res={'overflow':[],'local404':[],'broken_img':[],'jserr':[]}
with sync_playwright() as p:
    b=p.chromium.launch()
    for vw in (320,390,768,1280):
        pg=b.new_page(viewport={'width':vw,'height':900})
        errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.on('response',lambda r:(res['local404'].append((r.url,r.status)) if r.url.startswith('http://localhost') and r.status>=400 else None))
        for u in urls:
            pg.goto('http://localhost:8765'+u,wait_until='load')
            ov=pg.evaluate('document.documentElement.scrollWidth-window.innerWidth')
            if ov>0: res['overflow'].append((vw,u,ov))
            bi=pg.evaluate('[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src)')
            if bi: res['broken_img'].append((vw,u,bi))
        res['jserr']+=errs
        pg.close()
    # nav one-line at 1280 and 1920
    for vw in (1280,1920):
        pg=b.new_page(viewport={'width':vw,'height':900}); pg.goto('http://localhost:8765/')
        h=pg.evaluate('document.querySelector(".nav-inner").getBoundingClientRect().height')
        print('nav height at',vw,h)
    # mobile menu at 360
    pg=b.new_page(viewport={'width':360,'height':800}); pg.goto('http://localhost:8765/')
    pg.click('#mob-toggle'); pg.wait_for_timeout(400)
    print('drawer open visible:',pg.evaluate('getComputedStyle(document.getElementById("mob-drawer")).visibility'),pg.evaluate('document.getElementById("mob-toggle").getAttribute("aria-expanded")'))
    pg.click('#drawer-close'); pg.wait_for_timeout(400)
    print('drawer closed aria:',pg.evaluate('document.getElementById("mob-toggle").getAttribute("aria-expanded")'), 'overflow reset:',repr(pg.evaluate('document.documentElement.style.overflow')))
    # sticky sidecard after 1400px
    pg=b.new_page(viewport={'width':1280,'height':900}); pg.goto('http://localhost:8765/mold-remediation/')
    pg.evaluate('window.scrollTo(0,1400)'); pg.wait_for_timeout(300)
    print('sidecard top after 1400px scroll:',pg.evaluate('document.querySelector(".sidecard").getBoundingClientRect().top'))
    # faq toggle
    pg.evaluate('document.querySelector(".faq-q").click()')
    print('faq open class:',pg.evaluate('document.querySelector(".faq-item").classList.contains("open")'))
    b.close()
print(json.dumps({k:v[:10] for k,v in res.items()},indent=1)); print({k:len(v) for k,v in res.items()})
