# Genera informe-octubre-2026.html (Village Polo Club). Datos: Tiendanube (panel y CSV de ventas de octubre) y Meta Ads (CSV oct).
import os
OUT=os.path.join(os.path.dirname(__file__),'..','informe-octubre-2026.html')
def m(v): return '$'+f'{v:,.0f}'.replace(',','.')
daily=[2,4,0,2,4,3,1,1,2,1,2,2,4,0,0,1,2,0,0,0,0,1,2,0,1,2,4,1,3,0,1]
assert sum(daily)==46

def daily_svg():
    W,H,pl,pr,pt,pb=760,250,34,10,26,34
    cw=(W-pl-pr)/31; bw=cw-4; mx=4
    y=lambda v: pt+(H-pt-pb)*(1-v/mx)
    g=[]
    for t in range(0,5):
        g.append(f'<line x1="{pl}" x2="{W-pr}" y1="{y(t):.1f}" y2="{y(t):.1f}" class="grid"/><text x="{pl-8}" y="{y(t)+4:.1f}" class="ax" text-anchor="end">{t}</text>')
    # zona del checkout 18-21
    x0=pl+17*cw; g.append(f'<rect x="{x0:.1f}" y="{pt-14}" width="{4*cw:.1f}" height="{H-pb-pt+14}" class="gap"/><text x="{x0+2*cw:.1f}" y="{pt-3}" text-anchor="middle" class="gaplbl">Checkout caído</text>')
    for i,v in enumerate(daily):
        x=pl+i*cw+2; d=i+1
        if v>0:
            yy=y(v); h=H-pb-yy; r=min(4,h/2)
            g.append(f'<path class="bar" d="M{x:.1f},{H-pb} V{yy+r:.1f} Q{x:.1f},{yy:.1f} {x+r:.1f},{yy:.1f} H{x+bw-r:.1f} Q{x+bw:.1f},{yy:.1f} {x+bw:.1f},{yy+r:.1f} V{H-pb} Z"><title>{d} de octubre: {v} {"venta" if v==1 else "ventas"}</title></path>')
        else:
            g.append(f'<rect x="{x:.1f}" y="{pt}" width="{bw:.1f}" height="{H-pb-pt}" fill="transparent"><title>{d} de octubre: sin ventas</title></rect>')
        if d in (1,5,10,15,20,25,31): g.append(f'<text x="{x+bw/2:.1f}" y="{H-pb+18}" text-anchor="middle" class="ax">{d}</text>')
    g.append(f'<line x1="{pl}" x2="{W-pr}" y1="{H-pb}" y2="{H-pb}" class="base"/>')
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Ventas por día en octubre: entre 0 y 4 por día, sin ventas del 18 al 21">{"".join(g)}</svg>'

cats=[("Buzos, sweaters y darlon",1422600),("Buzo corderoy",898200),("Chombas tejidas y de manga larga",579400),("Hechter (chaleco y campera)",389800),("Jeans",349500),("Chombas piqué",299400),("Pantalones",179800),("Camperas",149700),("Chombas jersey",119600),("Otros",63700)]
tot=sum(v for _,v in cats); assert tot==4451700
def cat_rows():
    mx=cats[0][1]; out=[]
    for n,v in cats:
        out.append(f'<div class="hb"><span class="hb-l">{n}</span><span class="hb-t"><span class="hb-b" style="width:{v/mx*100:.1f}%" title="{n}: {m(v)}"></span></span><span class="hb-v num">{v/tot*100:.0f}%</span></div>')
    return ''.join(out)

def split(a,b,la,lb,title):
    t=a+b
    return f'''<div class="split" role="img" aria-label="{title}: {la} {a}, {lb} {b}"><div class="seg s1" style="flex:{a}" title="{la}: {a} de {t}"></div><div class="seg s2" style="flex:{b}" title="{lb}: {b} de {t}"></div></div>
<div class="legend"><span><i class="k1"></i>{la} <b class="num">{a}</b> <span class="muted">({a/t*100:.0f}%)</span></span><span><i class="k2"></i>{lb} <b class="num">{b}</b> <span class="muted">({b/t*100:.0f}%)</span></span></div>'''

html=f'''<title>Village · Octubre 2026</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap">
<style>
/* Layout: informe para leer de corrido, una columna de lectura con datos en tablas y gráficos simples. Colores de marca: azul marino, crema y dorado. */
:root{{
  --bg:#f4f1ec; --paper:#fffdf9; --ink:#1b2a3a; --muted:#5f6670; --line:#e1d9cd;
  --accent:#8a6533; --accent-soft:#f2e8d8; --s1:#3a6ea5; --s2:#b07a2a; --gap:#f6e3df; --gapink:#a03a2c;
  --ok:#2f6b47; --ok-soft:#e3efe6; --warn:#94650f; --warn-soft:#f6ecd6;
  --f-display:"Libre Baskerville",Georgia,"Times New Roman",serif;
  --f-body:"DM Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{
  --bg:#11171e; --paper:#18202a; --ink:#ede6db; --muted:#9ea7b1; --line:#2c3743;
  --accent:#d2a86c; --accent-soft:#2c2418; --s1:#5a8fd0; --s2:#b8852f; --gap:#35201c; --gapink:#ec8f80;
  --ok:#7cc79a; --ok-soft:#1c2d23; --warn:#e3b45d; --warn-soft:#2f2614; color-scheme:dark}}}}
:root[data-theme="dark"]{{
  --bg:#11171e; --paper:#18202a; --ink:#ede6db; --muted:#9ea7b1; --line:#2c3743;
  --accent:#d2a86c; --accent-soft:#2c2418; --s1:#5a8fd0; --s2:#b8852f; --gap:#35201c; --gapink:#ec8f80;
  --ok:#7cc79a; --ok-soft:#1c2d23; --warn:#e3b45d; --warn-soft:#2f2614; color-scheme:dark}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:16px;line-height:1.6}}
.page{{max-width:820px;margin:0 auto;padding-block:40px 70px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:44px}}
h1,h2,h3{{font-family:var(--f-display);font-weight:400;text-wrap:balance;margin:0;line-height:1.2}}
h1{{font-size:clamp(2rem,6vw,3rem)}} h2{{font-size:1.6rem}} h3{{font-size:1.15rem}}
p{{margin:0;max-width:68ch}} .muted{{color:var(--muted)}} .num{{font-variant-numeric:tabular-nums}}
section{{display:flex;flex-direction:column;gap:16px}}
.eyebrow{{font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--accent)}}
.lead{{font-size:1.12rem}}
.tiles{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}}
@media (max-width:640px){{.tiles{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.tile{{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px;display:grid;gap:2px;min-width:0}}
.tile b{{font-family:var(--f-display);font-size:1.6rem;font-weight:400}}
.tile small{{font-size:.8rem;color:var(--muted)}}
.up{{color:var(--ok);font-weight:700}} .down{{color:var(--warn);font-weight:700}}
.card{{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:18px;display:flex;flex-direction:column;gap:12px;min-width:0}}
.tbl{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:.95rem}}
th{{text-align:left;font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:700;padding:8px;border-bottom:1px solid var(--line)}}
td{{padding:10px 8px;border-bottom:1px solid var(--line)}} td.r,th.r{{text-align:right}}
svg{{width:100%;height:auto;display:block;max-width:100%}}
svg .grid{{stroke:var(--line);stroke-width:1}} svg .base{{stroke:var(--muted);stroke-width:1}}
svg .ax{{fill:var(--muted);font-size:11px;font-family:var(--f-body)}}
svg .bar{{fill:var(--s1)}} svg .bar:hover{{opacity:.8}}
svg .gap{{fill:var(--gap)}} svg .gaplbl{{fill:var(--gapink);font-size:11px;font-weight:700;font-family:var(--f-body)}}
.hb{{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,2fr) 44px;gap:10px;align-items:center;font-size:.92rem}}
.hb-t{{height:14px;background:transparent}} .hb-b{{display:block;height:14px;background:var(--s1);border-radius:0 4px 4px 0}}
.hb-v{{text-align:right;font-weight:700}}
.hbs{{display:grid;gap:8px}}
.split{{display:flex;gap:2px;height:22px}} .seg{{border-radius:4px}} .s1{{background:var(--s1)}} .s2{{background:var(--s2)}}
.legend{{display:flex;flex-wrap:wrap;gap:6px 20px;font-size:.92rem}} .legend i{{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:baseline}}
.k1{{background:var(--s1)}} .k2{{background:var(--s2)}}
.facts{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}}
@media (max-width:640px){{.facts{{grid-template-columns:1fr}}}}
.fact{{border-left:2px solid var(--accent);padding:2px 0 2px 12px;min-width:0}} .fact b{{display:block;font-size:1.25rem;font-family:var(--f-display);font-weight:400}}
.callout{{background:var(--accent-soft);border-radius:10px;padding:14px 16px}}
.note{{font-size:.85rem;color:var(--muted)}}
ol.next,ul.list{{margin:0;padding-left:22px;display:grid;gap:10px;max-width:70ch}}
.decide{{display:grid;gap:10px}} .decide div{{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:12px 14px}}
.phases{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}} @media (max-width:640px){{.phases{{grid-template-columns:1fr}}}}
.phase{{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px;display:grid;gap:4px}} .phase b{{font-family:var(--f-display);font-size:1.4rem;font-weight:400}}
footer{{border-top:1px solid var(--line);padding-top:16px;font-size:.82rem;color:var(--muted);display:grid;gap:6px}}
@media print{{body{{background:#fff}} .page{{padding-block:10px}} section,.card{{break-inside:avoid}}}}
</style>

<div class="page">
<header style="display:flex;flex-direction:column;gap:14px">
  <div class="eyebrow">Village Polo Club · Informe de octubre 2026</div>
  <h1>Octubre: 46 ventas, 28% más que septiembre</h1>
  <p class="lead muted">Vendimos más, con el mismo costo por venta. El ticket bajó porque se vendió mucho de la Winter Sale a $49.900, y perdimos 4 días de ventas por una falla del checkout que ya está resuelta.</p>
  <div class="tiles">
    <div class="tile"><small>Ventas</small><b class="num">46</b><small><span class="up">+28%</span> vs. septiembre</small></div>
    <div class="tile"><small>Facturación</small><b class="num">$4,7 M</b><small><span class="up">+5%</span> · {m(4705026)}</small></div>
    <div class="tile"><small>Ticket promedio</small><b class="num">{m(102283)}</b><small><span class="down">−18%</span> vs. septiembre</small></div>
    <div class="tile"><small>ROAS real</small><b class="num">3,18</b><small>Facturación ÷ gasto en Meta</small></div>
  </div>
</header>

<section>
  <h2>De dónde vinieron las ventas</h2>
  <p>Meta se adjudica 33 compras, pero en Tiendanube entraron 46. Las otras 13 llegaron por Instagram sin pauta, búsquedas, mails o gente que entró directo a la web. Por eso medimos siempre contra las ventas reales de Tiendanube y no contra el panel de Meta.</p>
  <div class="card">
    <h3>Ventas según Meta y ventas reales</h3>
    {split(33,13,"Registradas por Meta","Otras vías (orgánico, mails, directo)","Ventas de octubre por origen")}
  </div>
  <div class="card">
    <h3>Dónde viven los que compran</h3>
    {split(18,28,"CABA y Gran Buenos Aires","Interior del país","Ventas de octubre por zona")}
    <p class="note">Interior: provincia de Buenos Aires 15 (Bahía Blanca, Mar del Plata, Junín, Bolívar y otras), Mendoza 3, Santa Fe 3, Córdoba 3, San Juan, Tucumán, La Pampa y Tierra del Fuego 1 cada una.</p>
  </div>
  <div class="facts">
    <div class="fact"><b class="num">80%</b>compró desde el celular (37 de 46)</div>
    <div class="fact"><b class="num">1 de cada 3</b>pagó en 3 cuotas sin interés</div>
    <div class="fact"><b class="num">33 de 46</b>recibieron el pedido en su casa; 8 en un punto de retiro y 5 en el local</div>
  </div>
  <p class="muted">También hubo compras para regalo: pedidos con nota de "presentado para regalo" o "cartita de Feliz Cumpleaños". Es una señal para Navidad.</p>
</section>

<section>
  <h2>Septiembre contra octubre</h2>
  <div class="card tbl">
    <table>
      <thead><tr><th></th><th class="r">Septiembre</th><th class="r">Octubre</th><th class="r">Cambio</th></tr></thead>
      <tbody>
        <tr><td>Ventas</td><td class="r num">36</td><td class="r num">46</td><td class="r num up">+28%</td></tr>
        <tr><td>Facturación</td><td class="r num">{m(4499222)}</td><td class="r num">{m(4705026)}</td><td class="r num up">+5%</td></tr>
        <tr><td>Ticket promedio</td><td class="r num">{m(124978)}</td><td class="r num">{m(102283)}</td><td class="r num down">−18%</td></tr>
        <tr><td>Gasto en Meta</td><td class="r num">{m(1167903)}</td><td class="r num">{m(1478957)}</td><td class="r num">+27%</td></tr>
        <tr><td>Costo por venta</td><td class="r num">{m(32442)}</td><td class="r num">{m(32151)}</td><td class="r num">Igual</td></tr>
        <tr><td>ROAS real</td><td class="r num">3,85</td><td class="r num">3,18</td><td class="r num down">−17%</td></tr>
        <tr><td>Visitas a la web</td><td class="r num">~20.000</td><td class="r num">26.685</td><td class="r num up">+33%</td></tr>
      </tbody>
    </table>
    <p class="note">Septiembre tuvo 4 días sin pauta por falta de presupuesto. Las visitas de septiembre son estimadas a partir de su conversión de 0,18%.</p>
  </div>
  <p><b>Qué significa:</b> cada venta nos costó lo mismo que en septiembre, unos $32.000, y conseguimos 10 ventas más. El ROAS bajó porque el ticket bajó: se vendieron muchas prendas de $49.900 de la Winter Sale y ningún ambo. Para crecer no alcanza con más ventas: hay que volver a subir el ticket.</p>
</section>

<section>
  <h2>Ventas día por día</h2>
  <div class="card">
    {daily_svg()}
    <p class="note">Del 18 al 21 de octubre no entró ninguna venta: falló el checkout. Con las ventas que veníamos teniendo, estimamos que se perdieron unas 6.</p>
  </div>
</section>

<section>
  <h2>En qué se invirtió y qué funcionó</h2>
  <h3>El video del local que vende</h3>
  <p>El anuncio que más vendió fue un video con tomas del local y una voz en off que cuenta la promoción: 17 compras según Meta, con un ROAS de 3,5. Aunque el video hablaba de los ambos, en octubre no se vendió ningún ambo: la gente compró buzos, corderoy y chombas. Lo que funciona es <b>el formato</b>, no el producto que muestra. Es el formato que vamos a repetir con la colección nueva.</p>
  <h3>Lo que se vendió: el invierno</h3>
  <div class="card"><div class="hbs">{cat_rows()}</div><p class="note">Porcentaje de lo facturado en productos ({m(tot)}).</p></div>
  <p>Más de la mitad de lo facturado fueron buzos y corderoy de la Winter Sale. La colección de verano todavía vende poco: 4 chombas jersey, 6 chombas piqué y 2 chinos. Cuando se termine el stock de invierno, el anuncio ganador se queda sin qué vender, y por eso noviembre se enfoca en llevar ese formato a verano.</p>
  <h3>Lo que no funcionó</h3>
  <ul class="list">
    <li><b>Las visitas baratas.</b> Una parte de la pauta se usó para traer visitas y seguidores. Trajo miles de visitas y solo 2 ventas. Sirve para llegar a los 10.000 seguidores, y después se apaga.</li>
    <li><b>Los creativos nuevos no llegaron a probarse.</b> Compartían presupuesto con el anuncio ganador y Meta les dio muy poca plata. En noviembre tienen presupuesto propio.</li>
  </ul>
</section>

<section>
  <h2>La tienda</h2>
  <h3>El checkout, resuelto</h3>
  <p>Del 18 al 21 de octubre no se podía terminar la compra. Las ventas volvieron el 22 y en noviembre verificamos el checkout completo, de punta a punta, incluidos los cupones.</p>
  <h3>Mucha gente llega al carrito y no compra</h3>
  <p>En octubre se agregaron productos al carrito 523 veces y se concretaron 46 ventas. Como el pago funciona, lo que frena es otra cosa: <b>la duda con el talle</b>, <b>el costo del envío</b> y la desconfianza de comprar a distancia. En septiembre vimos que 4 de cada 10 compras se abandonaban en el paso donde aparece el envío.</p>
  <div class="callout">Es donde más plata se puede recuperar sin gastar más en pauta. Las tablas de talles, el envío gratis más accesible y los videos que muestran cómo calza cada prenda apuntan acá.</div>
</section>

<section>
  <h2>Lo que sigue en noviembre</h2>
  <ol class="next">
    <li><b>Creativos que venden emoción.</b> Contar cómo se siente uno con la ropa puesta (seguro, bien vestido, a la altura) y dejar la promo para el cierre. Más videos tipo "POV", que se comparten mucho.</li>
    <li><b>Creadores de contenido reales.</b> Videos con Raúl, que mide 2 metros, y con un creador de contextura grande: muestran que la ropa le queda bien a cualquier cuerpo y responden la duda del talle.</li>
    <li><b>El formato ganador, con verano.</b> Los videos del local con voz en off, ahora con chombas, lino, bermudas y packs.</li>
    <li><b>Fiestas y aguinaldo.</b> Regalos que se usan, el look para las fiestas y "date un gusto con el aguinaldo", con fecha límite para que llegue antes del 24.</li>
    <li><b>Una cuenta más simple.</b> Menos campañas, el presupuesto concentrado en vender y una campaña para quienes ya visitaron la web.</li>
  </ol>
  <h3>El camino a $20 millones por mes</h3>
  <p>La facturación sale de tres números: <b>visitas × conversión × ticket</b>. Para llegar a $20 millones hay que mover los tres a la vez: unas 160 ventas por mes, con un ticket de $125.000. Si solo se aumenta la pauta, el costo por venta sube y deja de convenir.</p>
  <div class="phases">
    <div class="phase"><small class="muted">Noviembre</small><b class="num">$7–8 M</b><span class="note">Conversión, ticket y creativos nuevos</span></div>
    <div class="phase"><small class="muted">Diciembre</small><b class="num">$12–15 M</b><span class="note">Navidad, el pico del año para regalos</span></div>
    <div class="phase"><small class="muted">Enero y febrero</small><b class="num">$15–20 M</b><span class="note">Escalar la pauta con lo que ya funciona</span></div>
  </div>
  <p class="note">Con un margen supuesto del 45% (a confirmar), el negocio no pierde plata mientras el ROAS real esté por encima de 2,22 o cada venta cueste menos de unos $46.000. Octubre cerró en 3,18 y $32.000: hay margen para crecer.</p>
  <h3>Lo que necesitamos que decidan</h3>
  <div class="decide">
    <div><b>El margen real.</b> Con ese número sabemos hasta cuánto se puede invertir por venta y cuánto escalar la pauta.</div>
    <div><b>Envío gratis desde $120.000.</b> Hoy es desde $150.000 y la mayoría de las compras no llega. Bajarlo empuja a sumar una prenda más y recupera carritos.</div>
    <div><b>Stock y producción para crecer.</b> Si vendemos el triple, ¿hay talles y mercadería? Lo propio se puede fabricar; Hechter depende de la reposición.</div>
    <div><b>Aumento de la pauta por etapas.</b> Subir de a poco, cada semana, mientras cada venta siga costando unos $30.000.</div>
  </div>
</section>

<footer>
  <span><b>Fuentes:</b> Tiendanube (panel de estadísticas y exportación de las 46 ventas de octubre), Meta Ads (informes de campañas, conjuntos y anuncios del 1 al 31 de octubre de 2026), informe de septiembre.</span>
  <span><b>Estimaciones:</b> visitas de septiembre, ventas perdidas por el checkout y margen del 45%. Las compras "según Meta" son las que Meta se atribuye con su configuración de atribución.</span>
</footer>
</div>
'''
open(OUT,'w').write(html); print('ok',OUT)
