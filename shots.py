import sys
from playwright.sync_api import sync_playwright
pages=sys.argv[1:] or ['/']
with sync_playwright() as p:
    b=p.chromium.launch()
    for vw,name in ((1280,'d'),(390,'m')):
        pg=b.new_page(viewport={'width':vw,'height':900})
        for u in pages:
            pg.goto('http://localhost:8765'+u,wait_until='load'); pg.wait_for_timeout(400)
            slug=u.strip('/').replace('/','_') or 'home'
            pg.screenshot(path=f'/tmp/shot_{slug}_{name}.png',full_page=True)
            ov=pg.evaluate('document.documentElement.scrollWidth - window.innerWidth')
            print(u,vw,'overflow',ov)
    b.close()
