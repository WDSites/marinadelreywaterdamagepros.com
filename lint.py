import sys, re, importlib.util, json
BANNED = ["delve into","navigate the complexities","in today's fast-paced","it's important to note","it's worth noting","tapestry","robust","comprehensive","seamless","cutting-edge","state-of-the-art","meticulous","underscore","leverage","elevate your","transform your","unlock your","at the forefront","whether you're","look no further","rest assured","we pride ourselves","peace of mind","top-notch","nestled","boasts","game-changer","a wide range of","when it comes to","free estimate","free inspection","guaranteed arrival","near me","insurance approved","direct billing","warranty"]
LINK = re.compile(r'\[([^\]]+)\]\((/[^)]*)\)')
def strings(p):
    out=[]
    for b in p.get('body',[]):
        t=b['t']
        if t in('h2','h3','p','cta'): out.append(b['text'])
        elif t=='ul': out+=b['items']
        elif t=='table': out+=b['head']+[c for r in b['rows'] for c in r]
        elif t in('cards','steps'): out+=[x['h'] for x in b['items']]+[x['p'] for x in b['items']]
        elif t in('callout','localnote'): out+=[b['h']]+b['paras']
    for q,a in p.get('faqs',[]):
        out.append(q); out+= a if isinstance(a,list) else [a]
    return out
def paras(p):
    out=[]
    for b in p.get('body',[]):
        if b['t']=='p': out.append(b['text'])
        if b['t'] in('callout','localnote'): out+=b['paras']
    for q,a in p.get('faqs',[]):
        out+= a if isinstance(a,list) else [a]
    return out
def words(s): return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’%$.-]*", LINK.sub(r'\1',s)))
def main(path, valid_slugs=None):
    spec=importlib.util.spec_from_file_location('m',path); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    ok=True
    for p in m.PAGES:
        ss=strings(p); allt=' '.join(ss+[p['title'],p['meta'],p['h1'],p['hero_sub']])
        wc=sum(words(s) for s in ss)
        floor={'service':800,'location':800,'blog':1100,'standard':0}[p.get('type','standard')]
        probs=[]
        if wc<floor: probs.append(f'WORDS {wc}<{floor}')
        if re.search(r'[—–]|---',allt) or ';' in allt: probs.append('DASH/SEMI')
        if not(140<=len(p['meta'])<=160): probs.append(f"META {len(p['meta'])}")
        tl=len(p['title']); 
        if tl>65 or (p.get('type')!='blog' and tl>62): probs.append(f'TITLE {tl}')
        low=allt.lower()
        for b in BANNED:
            if b in low: probs.append('BANNED:'+b)
        for s in paras(p):
            if words(s)>80: probs.append('LONGP '+str(words(s)))
        links=[l[1] for s in ss for l in LINK.findall(s)]
        if valid_slugs:
            for l in links:
                if l not in valid_slugs: probs.append('BADLINK '+l)
        if p.get('type')=='blog' and not any(b['t']=='localnote' for b in p['body']): probs.append('NO LOCALNOTE')
        if p.get('type')=='blog' and len(links)<4: probs.append(f'LINKS {len(links)}<4')
        if p.get('type','standard') not in ('blog',) and len(links)<3 and p.get('slug')!='privacy': probs.append(f'LINKS {len(links)}<3')
        print(f"{p['slug']:60s} words={wc:5d} title={tl} meta={len(p['meta'])} links={len(links)} {'OK' if not probs else probs}")
        ok&=not probs
    return ok
if __name__=='__main__':
    VALID={'/burst-pipe-water-damage/','/roof-leak-water-damage/','/water-heater-leak-cleanup/','/appliance-leak-water-damage/','/ac-leak-water-damage/','/slab-leak-water-damage/','/crawl-space-water-damage/','/sewage-backup-cleanup/','/structural-drying/','/commercial-water-damage/','/storm-water-damage/','/kitchen-water-damage/','/carpet-water-damage/','/drywall-water-damage-repair/','/','/water-mitigation/','/water-damage-cleanup/','/water-damage-repair/','/flood-damage-restoration/','/emergency-water-removal/','/mold-remediation/','/services/','/service-area/','/service-area/venice-ca/','/service-area/playa-vista-ca/','/service-area/playa-del-rey-ca/','/service-area/culver-city-ca/','/service-area/santa-monica-ca/','/service-area/venice-canals-ca/','/service-area/marina-peninsula-ca/','/service-area/oxford-triangle-ca/','/about/','/contact/','/blog/','/privacy/','/terms/'}
    sys.exit(0 if main(sys.argv[1],VALID) else 1)
