from gen import page, BEN, NAVY, GOLD
RED='#9e2b25'
STAR='<svg width="26" height="26" viewBox="0 0 24 24" style="vertical-align:-4px"><path d="M12 2l2.6 6.6L21 9.3l-5 4.4 1.6 6.8L12 16.9 6.4 20.5 8 13.7 3 9.3l6.4-.7z" fill="#b08a55"/></svg>'
def head(top): return f'<div style="position:absolute;top:{top}px;left:0;right:0" class="brand">VILLAGE POLO CLUB</div>'
def foot(b): return f'<div style="position:absolute;bottom:{b}px;left:0;right:0" class="ben">{BEN}</div>'
BASE=f""".ey3{{font-size:26px;letter-spacing:.24em;font-weight:700;color:{GOLD};text-transform:uppercase;text-align:center}}
.box{{border-radius:18px;overflow:hidden;position:relative}}"""
def f8(fmt):
    W,H=(1080,1350) if fmt=='feed' else (1080,1920); st=fmt!='feed'; top=250 if st else 70
    items=[('Hasta $35.000','Remera escote en V','$29.900','remera-manga-corta-escote-en-v-azul-1.webp','inset(20% 4% 0 4%)'),
           ('Hasta $50.000','Chomba piqué','$49.900','chomba-pique-azul-marino-2.webp','inset(27% 4% 0 4%)'),
           ('Hasta $80.000','Camisa de lino manga corta','$69.900','camisa-manga-corta-lino-algodon-celeste-cloque-1.webp','inset(20% 4% 0 4%)')]
    ph=520 if not st else 760
    cards=''.join(f'<div class="card"><div class="tier">{t}</div><div class="box" style="height:{ph}px"><img class="ph" src="{i}" style="object-view-box:{c}"></div><div class="nm">{n}</div><div class="pr">{p}</div></div>' for t,n,p,i,c in items)
    body=f"""{head(top)}<div style="position:absolute;top:{top+56}px;left:50px;right:50px;text-align:center">
<div class="ey3">{STAR} Guía de regalos {STAR}</div><h1 style="font-size:{92 if not st else 100}px;margin:10px 0 34px">Regalos que sí va a usar</h1>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px">{cards}</div></div>{foot(top)}"""
    extra=BASE+f""".tier{{background:{RED};color:#fff;font-weight:700;font-size:26px;padding:10px 0;border-radius:40px;margin-bottom:14px}}
.nm{{font-size:28px;font-weight:700;color:{NAVY};margin-top:16px;line-height:1.15}}.pr{{font-family:'PF';font-weight:600;font-size:44px;color:{NAVY}}}"""
    return page(W,H,body,extra)
def f9(fmt):
    W,H=(1080,1350) if fmt=='feed' else (1080,1920); st=fmt!='feed'; top=250 if st else 70
    gh=560 if not st else 640
    body=f"""{head(top)}<div style="position:absolute;top:{top+56}px;left:60px;right:60px;text-align:center">
<div class="ey3">{STAR} Aguinaldo {STAR}</div><h1 style="font-size:{96 if not st else 92}px;margin:10px 0 30px">Este año, el aguinaldo es para vos.</h1>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:{gh}px">
<div class="box"><img class="ph" src="camisa-lino-algodon-blanco-1.webp" style="object-view-box:inset(22% 6% 0 6%)"><span class="tag">Camisa de lino $79.900</span></div>
<div class="box"><img class="ph" src="pantalon-chino-lino-camel-claro-1.webp"><span class="tag">Chino de lino $79.900</span></div></div>
<div class="tot" style="font-family:'PF';font-weight:600;font-size:56px">Armá tu look completo</div><div class="cuo">CON ENVÍO GRATIS</div><div class="cu2">y en 3 cuotas sin interés</div></div>"""
    extra=BASE+f""".tag{{position:absolute;left:16px;bottom:16px;background:{NAVY};color:#fff;font-weight:700;font-size:26px;padding:10px 20px;border-radius:40px}}
.tot{{font-size:40px;font-weight:700;color:{NAVY};margin-top:30px}}.tot b{{font-family:'PF';font-size:60px;color:{RED}}}
.cu2{{font-size:30px;font-weight:700;color:{NAVY};margin-top:14px;opacity:.8}}
.cuo{{display:inline-block;margin-top:14px;background:{RED};color:#fff;font-size:44px;letter-spacing:.04em;font-weight:700;padding:14px 32px;border-radius:60px}}"""
    return page(W,H,body,extra)
BOT='<svg width="200" height="240" viewBox="0 0 40 64"><path d="M16 2h8v14c0 3 6 6 6 14v30a2 2 0 0 1-2 2H12a2 2 0 0 1-2-2V30c0-8 6-11 6-14z" fill="none" stroke="#f0d3a5" stroke-width="2"/><rect x="12" y="34" width="16" height="14" fill="none" stroke="#f0d3a5" stroke-width="1.5"/></svg>'
def f11(fmt):
    W,H=(1080,1350) if fmt=='feed' else (1080,1920); st=fmt!='feed'; top=250 if st else 70
    ch=680 if not st else 860
    body=f"""{head(top)}<div style="position:absolute;top:{top+56}px;left:60px;right:60px;text-align:center">
<div class="ey3">{STAR} Fiestas {STAR}</div><h1 style="font-size:{92 if not st else 104}px;margin:10px 0 30px">Si vas a regalar, que dure.</h1>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;height:{ch}px">
<div class="box" style="background:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px">{BOT}<div style="font-family:'PF';font-weight:600;font-size:52px;color:#fff">Una botella</div></div>
<div class="box"><img class="ph" src="camisa-manga-corta-lino-algodon-celeste-cloque-1.webp" style="object-view-box:inset(20% 5% 0 5%)"></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:22px">
<div class="d">Dura una noche</div><div class="d" style="color:{RED}">Una camisa de lino<br>dura años</div></div></div>{foot(top)}"""
    extra=BASE+""".d{font-family:'PF';font-weight:600;font-size:46px;line-height:1.15;color:#1c2840}"""
    return page(W,H,body,extra)
for f in ('feed','story'):
    for n,fn in (('F8-guia-regalos',f8),('F9-aguinaldo',f9),('F11-regalar-que-dure',f11)):
        open(f'{n}-{f}.html','w').write(fn(f))
