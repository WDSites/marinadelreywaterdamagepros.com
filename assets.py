import os, math, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image, ImageDraw, ImageFont

ROSE='#7A1F35'; ROSE_D='#5C1627'; GOLD='#C9962C'; INK='#241A1C'
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
SANS='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

def text_path(fontfile, text, size, x, y, spacing=0.0):
    f=TTFont(fontfile); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
    s=size/upm; cx=x; d=[]
    for ch in text:
        g=cmap.get(ord(ch))
        if g is None: continue
        pen=SVGPathPen(gs)
        tp=TransformPen(pen,(s,0,0,-s,cx,y))
        gs[g].draw(tp)
        d.append(pen.getCommands())
        cx+=gs[g].width*s+spacing
    return ' '.join(d), cx

def icon_svg(bg=True, fg='#fff', accent=GOLD, fill=ROSE):
    # 56x56 mark: rounded square, roof chevron, water drop
    parts=[]
    if bg: parts.append(f'<rect width="56" height="56" rx="12" fill="{fill}"/>')
    parts.append(f'<path d="M9 28 L28 11 L47 28" fill="none" stroke="{fg}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    parts.append(f'<path d="M28 24 C28 24 20 33 20 38.5 A8 8 0 0 0 36 38.5 C36 33 28 24 28 24 Z" fill="{accent}"/>')
    return ''.join(parts)

def logo(light=False):
    ink='#FFFFFF' if light else INK
    sub='#F0D9DD' if light else ROSE
    fill='#FFFFFF' if light else ROSE
    fg=ROSE if light else '#FFFFFF'
    d1,w1=text_path(SERIF,'Marina Del Rey',19,66,25)
    d2,w2=text_path(SANS,'WATER DAMAGE PROS',10.5,66,43,spacing=1.6)
    W=int(max(w1,w2))+4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 56" width="{W}" height="56" role="img" aria-label="Marina Del Rey Water Damage Pros">'
            f'<title>Marina Del Rey Water Damage Pros</title>'
            f'<g>{icon_svg(True,fg,GOLD,fill)}</g>'
            f'<path d="{d1}" fill="{ink}"/><path d="{d2}" fill="{sub}"/></svg>'), W

def lum(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def contrast(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb); return (hi+0.05)/(lo+0.05)

def draw_icon_png(size):
    S=size*4
    im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,S-1,S-1],radius=int(S*12/56),fill=ROSE)
    k=S/56
    pts=[(9*k,28*k),(28*k,11*k),(47*k,28*k)]
    d.line(pts,fill='#FFFFFF',width=int(5*k),joint='curve')
    for p in (pts[0],pts[2],pts[1]):
        r=2.5*k; d.ellipse([p[0]-r,p[1]-r,p[0]+r,p[1]+r],fill='#FFFFFF')
    # drop: triangle top + circle
    cx,cy,r=28*k,38.5*k,8*k
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GOLD)
    d.polygon([(28*k,24*k),(cx-r*0.93,cy-r*0.37),(cx+r*0.93,cy-r*0.37)],fill=GOLD)
    return im.resize((size,size),Image.LANCZOS)

def build(site):
    os.makedirs(site,exist_ok=True)
    svg,W=logo(False); open(f'{site}/logo.svg','w').write(svg)
    svgl,_=logo(True); open(f'{site}/logo-light.svg','w').write(svgl)
    open(f'{site}/favicon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 56 56" width="56" height="56">{icon_svg(True)}</svg>')
    i512=draw_icon_png(512); i512.save(f'{site}/icon-512.png')
    draw_icon_png(192).save(f'{site}/icon-192.png')
    # apple touch: opaque bg, no rounding
    a=Image.new('RGB',(180,180),ROSE); ic=draw_icon_png(180); a.paste(ic,(0,0),ic); 
    a=Image.new('RGB',(180,180),ROSE); inner=draw_icon_png(140); a.paste(inner,(20,20),inner); a.save(f'{site}/apple-touch-icon.png')
    ims=[draw_icon_png(s) for s in (48,32,16)]
    ims[0].save(f'{site}/favicon.ico',format='ICO',sizes=[(16,16),(32,32),(48,48)],append_images=ims[1:])
    json.dump({"name":"Marina Del Rey Water Damage Pros","short_name":"MDR Water Pros","start_url":"/","display":"browser","background_color":"#ffffff","theme_color":ROSE_D,"icons":[{"src":"/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/icon-512.png","sizes":"512x512","type":"image/png"}]},open(f'{site}/site.webmanifest','w'),indent=1)
    # OG image
    im=Image.new('RGB',(1200,630),ROSE_D); px=im.load()
    for y in range(630):
        for x in range(0,1200):
            t=(x/1200*0.6+y/630*0.4); r=int(0x5C+(0x7A-0x5C)*t); g=int(0x16+(0x1F-0x16)*t); b=int(0x27+(0x35-0x27)*t); px[x,y]=(r,g,b)
    d=ImageDraw.Draw(im)
    ic=draw_icon_png(150).convert('RGBA'); bg=Image.new('RGBA',(150,150),(255,255,255,0)); im.paste(ic,(80,90),ic)
    ft=ImageFont.truetype(SERIF,76); fs=ImageFont.truetype(SANS,34); fb=ImageFont.truetype(SANS,30)
    d.text((80,270),'Marina Del Rey',font=ft,fill='#FFFFFF')
    d.text((84,372),'WATER DAMAGE PROS',font=fs,fill=GOLD)
    d.rectangle([84,440,260,444],fill=GOLD)
    d.text((84,466),'Water Damage Restoration  |  Marina Del Rey, CA',font=fb,fill='#F0D9DD')
    d.text((84,516),'24/7 Emergency Line  |  (424) 550-5662',font=fb,fill='#FFFFFF')
    im.save(f'{site}/og-image.png',optimize=True)
    print('logo width',W)
    print('contrast ink on white header/footer:',round(contrast(INK,'#FFFFFF'),2),' rose sub-line on white:',round(contrast(ROSE,'#FFFFFF'),2))
    print('light logo white on rose-d (topbar/cta band):',round(contrast('#FFFFFF',ROSE_D),2),' sub-line on rose-d:',round(contrast('#F0D9DD',ROSE_D),2))
if __name__=='__main__':
    import sys; build(sys.argv[1])
