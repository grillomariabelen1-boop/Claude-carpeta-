CSS=open('base.css').read()
NAVY='#1c2840';CREAM='#f4f0e8';GOLD='#b08a55';INK='#1c2840'
BEN='3 cuotas sin interés · Envío gratis desde $100.000'
def page(W,H,body,extra=''):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
.c{{width:{W}px;height:{H}px;background:{CREAM};color:{INK}}}
.brand{{font-size:22px;letter-spacing:.32em;font-weight:700;color:{NAVY};text-align:center}}
.ben{{font-size:26px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;text-align:center;color:{NAVY}}}
h1{{font-family:'PF';font-weight:600;line-height:1.02;letter-spacing:-.01em;text-align:center;color:{NAVY}}}
.ph{{width:100%;height:100%;object-fit:cover}}
{extra}</style></head><body><div class="c">{body}</div></body></html>'''
X='<svg width="40" height="40" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#c9553f"/><path d="M8 8l8 8M16 8l-8 8" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/></svg>'
V='<svg width="40" height="40" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#3f8a5a"/><path d="M7 12.5l3.2 3.2L17 9" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def r1(fmt):
    W,H=(1080,1350) if fmt=='feed' else (1080,1920)
    probs=['No sé qué talle soy','Me da miedo comprar online','La ropa se me deforma','El envío me sale caro']
    sols=['Te asesoramos con el talle','Llega en 2 a 4 días hábiles','Calidad que dura','Envío gratis desde $100.000']
    top=70 if fmt=='feed' else 250
    L=''.join(f'<li>{X}<span>{p}</span></li>' for p in probs)
    R=''.join(f'<li>{V}<span>{s}</span></li>' for s in sols)
    story=fmt!='feed'
    cols='1fr' if story else '1fr 1fr'
    pad='56px 60px' if story else '60px 36px'
    body=f"""<div style="position:absolute;top:{top}px;left:0;right:0" class="brand">VILLAGE POLO CLUB</div>
<div style="position:absolute;top:{top+50}px;bottom:{top+50}px;left:60px;right:60px;display:flex;flex-direction:column;justify-content:center">
<div style="display:grid;grid-template-columns:{cols};gap:24px">
 <div style="background:#fff;border-radius:22px;padding:{pad}">
  <div class="t">Tus problemas</div><ul>{L}</ul></div>
 <div style="border-radius:22px;overflow:hidden;position:relative;background:{NAVY};padding:{pad}">
  <img class="ph" src="chomba-jersey-azul-1.webp" style="position:absolute;inset:0;object-view-box:inset(22% 8% 0 8%)">
  <div style="position:absolute;inset:0;background:rgba(28,40,64,.74)"></div>
  <div style="position:relative;color:#fff"><div class="t" style="color:#f0d3a5">Nuestra solución</div><ul class="w">{R}</ul></div>
 </div></div></div>
<div style="position:absolute;bottom:{top}px;left:0;right:0" class="ben">{BEN}</div>"""
    fs=46 if story else 38
    extra=f""".t{{font-family:'PF';font-weight:600;font-size:{74 if story else 62}px;line-height:1.05;margin-bottom:40px}}
ul{{list-style:none;display:flex;flex-direction:column;gap:{34 if story else 40}px}}li{{display:flex;gap:18px;align-items:flex-start;font-size:{fs}px;font-weight:700;line-height:1.2}}li svg{{flex:none;margin-top:4px;width:{fs}px;height:{fs}px}}
ul.w li{{color:#fff}}"""
    return page(W,H,body,extra)
def r2(fmt,q='qué ponerme para un casamiento de día',a='camisa-lino-algodon-blanco-2.webp',ta='Camisa de lino',ca='inset(20% 6% 0 6%)',b='pantalon-chino-lino-azul-2.webp',tb='Chino de lino',cb='inset(0 0 0 0)'):
    W,H=(1080,1350) if fmt=='feed' else (1080,1920)
    top=70 if fmt=='feed' else 250
    ph=620 if fmt=='feed' else 900
    body=f'''<div style="position:absolute;top:{top}px;left:0;right:0" class="brand">VILLAGE POLO CLUB</div>
<div style="position:absolute;top:{top+70}px;left:60px;right:60px">
 <div class="lab">La búsqueda</div>
 <div class="bar"><svg width="40" height="40" viewBox="0 0 24 24"><circle cx="10" cy="10" r="6.5" stroke="#5f6368" stroke-width="2.2" fill="none"/><path d="M15 15l5 5" stroke="#5f6368" stroke-width="2.4" stroke-linecap="round"/></svg><span>{q}</span><span class="cur"></span></div>
 <div class="lab" style="margin-top:46px">La solución</div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;height:{ph}px">
  <div class="box"><img class="ph" src="{a}" style="object-view-box:{ca}"><span class="tag">{ta}</span></div>
  <div class="box"><img class="ph" src="{b}" style="object-view-box:{cb}"><span class="tag">{tb}</span></div>
 </div>
</div>
<div style="position:absolute;bottom:{70 if fmt=='feed' else 250}px;left:0;right:0" class="ben">{BEN}</div>'''
    extra='''.lab{font-family:'PF';font-weight:600;font-size:56px;margin-bottom:22px;color:#1c2840}
.bar{background:#fff;border-radius:60px;box-shadow:0 6px 24px rgba(0,0,0,.12);padding:28px 36px;display:flex;gap:20px;align-items:center;font-size:36px;color:#202124}
.cur{width:3px;height:40px;background:#202124;margin-left:-14px}
.box{border-radius:22px;overflow:hidden;position:relative}
.tag{position:absolute;left:18px;bottom:18px;background:#1c2840;color:#fff;font-weight:700;font-size:28px;padding:12px 22px;border-radius:40px}'''
    return page(W,H,body,extra)
def r3(fmt):
    W,H=(1080,1350) if fmt=='feed' else (1080,1920)
    top=70 if fmt=='feed' else 250
    ch=700 if fmt=='feed' else 820
    plate='<svg width="230" height="230" viewBox="0 0 64 64"><circle cx="32" cy="34" r="20" fill="none" stroke="#f0d3a5" stroke-width="2.4"/><circle cx="32" cy="34" r="13" fill="none" stroke="#f0d3a5" stroke-width="1.6"/><path d="M6 14v14M3 14v8c0 3 6 3 6 0v-8M6 28v24" stroke="#f0d3a5" stroke-width="2.2" stroke-linecap="round" fill="none"/><path d="M58 14c-4 2-5 8-5 14h5v24" stroke="#f0d3a5" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>'
    body=f'''<div style="position:absolute;top:{top}px;left:0;right:0" class="brand">VILLAGE POLO CLUB</div>
<h1 style="position:absolute;top:{top+70}px;left:60px;right:60px;font-size:{86 if fmt=='feed' else 96}px">Si vas a darte un gusto, pensalo bien</h1>
<div style="position:absolute;left:60px;right:60px;top:{top+70+(200 if fmt=='feed' else 230)}px;height:{ch}px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
 <div class="box" style="background:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:30px">{plate}<div class="k" style="color:#fff">Una cena</div></div>
 <div class="box"><img class="ph" src="chomba-tejida-hilo-algodon-vison-1.webp" style="object-view-box:inset(24% 4% 0 4%)"></div>
</div>
<div style="position:absolute;left:60px;right:60px;top:{top+70+(200 if fmt=='feed' else 230)+ch+26}px;display:grid;grid-template-columns:1fr 1fr;gap:24px;text-align:center">
 <div class="d">Te dura 2 horas<br><span class="cal">y suma ~1.200 calorías</span></div><div class="d" style="color:{GOLD}">Te dura años<br><span class="cal">y 0 calorías</span></div></div>
<div style="position:absolute;bottom:{70 if fmt=='feed' else 250}px;left:0;right:0" class="ben">{BEN}</div>'''
    extra='''.box{border-radius:22px;overflow:hidden;position:relative}.k{font-family:'PF';font-weight:600;font-size:54px}.d{font-family:'PF';font-weight:600;font-size:48px;line-height:1.15}.cal{font-family:'DM';font-size:30px;font-weight:700;color:#1c2840;opacity:.75}'''
    return page(W,H,body,extra)
def grid(fmt,imgs,eyebrow,h,sub,crops):
    W,H=(1080,1350) if fmt=='feed' else (1080,1920)
    top=70 if fmt=='feed' else 250
    gh=680 if fmt=='feed' else 840
    n=len(imgs);cols=2 if n in (2,4) else 3
    cells=''.join(f'<div class="box"><img class="ph" src="{i}" style="object-view-box:{c}"></div>' for i,c in zip(imgs,crops))
    body=f'''<div style="position:absolute;top:{top}px;left:0;right:0" class="brand">VILLAGE POLO CLUB</div>
<div style="position:absolute;top:{top+60}px;left:60px;right:60px;display:grid;grid-template-columns:repeat({cols},1fr);gap:14px;height:{gh}px">{cells}</div>
<div style="position:absolute;top:{top+60+gh+40}px;left:60px;right:60px;text-align:center">
 <div class="ey">{eyebrow}</div><h1 style="font-size:{100 if fmt=='feed' else 116}px">{h}</h1><div class="sub">{sub}</div></div>
<div style="position:absolute;bottom:{70 if fmt=='feed' else 250}px;left:0;right:0" class="ben">{BEN}</div>'''
    extra=f'''.box{{border-radius:18px;overflow:hidden}}.ey{{font-size:30px;letter-spacing:.14em;background:#1c2840;color:#fff;display:inline-block;padding:10px 22px;border-radius:40px;font-weight:700;color:{GOLD};text-transform:uppercase;margin-bottom:14px}}
.sub{{font-size:34px;font-weight:700;margin-top:18px;color:{NAVY}}}'''
    return page(W,H,body,extra)

def p1(fmt):
    W,H=(1080,1350) if fmt=='feed' else (1080,1920)
    story=fmt!='feed'
    top=70 if not story else 250
    gh=600 if not story else 780
    crop='inset(27% 5% 0 5%)'
    body=f"""<div style="position:absolute;top:{top}px;left:0;right:0" class="brand">VILLAGE POLO CLUB</div>
<div style="position:absolute;top:{top+56}px;left:60px;right:60px;height:{gh}px;display:grid;grid-template-columns:1fr 1fr;gap:14px">
 <div class="box"><img class="ph" src="chomba-jersey-azul-1.webp" style="object-view-box:{crop}"></div>
 <div class="box"><img class="ph" src="chomba-jersey-beige-1.webp" style="object-view-box:{crop}"></div>
 <div class="badge"><span class="b1">PROMO</span><span class="b2">2x</span><span class="b3">$49.900</span></div>
</div>
<div style="position:absolute;top:{top+56+gh+34}px;left:60px;right:60px;text-align:center">
 <div class="ey2">Pack de 2 chombas</div>
 <h1 style="font-size:150px;color:#b0392b;white-space:nowrap">2 x $49.900</h1>
 <div class="sub2">Antes <s>$69.800</s> · Ahorrás $19.900</div>
 <div class="price">Combiná colores y talles</div>
</div>
<div style="position:absolute;bottom:{top}px;left:0;right:0" class="ben">{BEN}</div>"""
    extra=""".box{border-radius:18px;overflow:hidden}
.badge{position:absolute;right:-18px;top:-22px;width:210px;height:210px;border-radius:50%;background:#b0392b;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);box-shadow:0 10px 30px rgba(0,0,0,.25)}
.b1{font-size:26px;font-weight:700;letter-spacing:.16em}.b2{font-family:'PF';font-weight:600;font-size:84px;line-height:.95}.b3{font-size:34px;font-weight:700;letter-spacing:.02em}
.ey2{font-family:'PF';font-weight:600;font-size:52px;color:#1c2840;margin-bottom:6px}
.sub2{font-size:38px;font-weight:700;color:#1c2840;margin-top:6px}.sub2 s{opacity:.6}
.price{display:inline-block;margin-top:26px;background:#1c2840;color:#fff;font-size:40px;font-weight:700;padding:16px 34px;border-radius:60px}.price b{color:#f0d3a5;font-size:48px}"""
    return page(W,H,body,extra)

C1='inset(22% 6% 0 6%)'
P=[]
for f in ('feed','story'):
    P+= [(f'R1-problemas-solucion-{f}',r1(f)),(f'R2-busqueda-solucion-{f}',r2(f)),(f'R3-comparacion-{f}',r3(f)),
    (f'P1-packs-chombas-{f}',grid(f,['chomba-jersey-azul-1.webp','chomba-jersey-beige-1.webp'],'Hasta 30% OFF comprando en cantidad','Packs de chombas','Chomba jersey $34.900 · Combiná colores y talles.',['inset(27% 5% 0 5%)']*2)),
    (f'P2-pack-x3-remeras-{f}',grid(f,['pack-x3-remeras-omz80-2.webp','pack-x3-remeras-omz80-4.webp','pack-x3-remeras-omz80-3.webp'],'Pack x3','Pack x3 remeras','El básico que más usás, de a tres.',['inset(9% 0 0 0)']*3))]
for f in ('feed','story'):
    P+=[(f'R2b-asado-{f}',r2(f,'qué ponerme para un asado con amigos','chomba-jersey-azul-1.webp','Chomba jersey','inset(22% 6% 0 6%)','bermuda-gabardina-cintura-elastica-camel-1.webp','Bermuda de gabardina','inset(0 0 0 0)')),
        (f'R2d-regalo-viejo-{f}',r2(f,'regalo para mi viejo que realmente use','camisa-manga-corta-lino-algodon-celeste-cloque-1.webp','Camisa de lino manga corta','inset(20% 6% 0 6%)','chomba-pique-azul-marino-2.webp','Chomba piqué','inset(27% 6% 0 6%)')),
        (f'R2f-fin-de-ano-{f}',r2(f,'qué ponerme para la cena de fin de año','camisa-lino-algodon-blanco-1.webp','Camisa de lino','inset(22% 6% 0 6%)','pantalon-chino-lino-camel-claro-1.webp','Chino de lino','inset(0 0 0 0)'))]
P=[x for x in P if not x[0].startswith('P1-')]+[(f'P1-packs-chombas-{f}',p1(f)) for f in ('feed','story')]
for n,h in P: open(n+'.html','w').write(h)
print(len(P))
