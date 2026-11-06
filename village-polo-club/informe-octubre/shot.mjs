import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const html=fs.readFileSync('/home/user/Claude-carpeta-/village-polo-club/informe-octubre-2026.html','utf8');
const doc=`<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>${html}</body></html>`;
const b=await chromium.launch();
for (const [w,n,s] of [[1100,'desk','light'],[400,'phone','dark']]){const p=await b.newPage({viewport:{width:w,height:900},colorScheme:s});await p.setContent(doc,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:`/tmp/claude-0/-home-user-Claude-carpeta-/fb0368fc-256e-50a1-a1a0-31633a781b5f/scratchpad/inf-${n}.png`,fullPage:true});
 const ov=await p.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);console.log(n,'overflow',ov);}
const p=await b.newPage({colorScheme:'light'});await p.setContent(doc,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:'/home/user/Claude-carpeta-/village-polo-club/Village-informe-octubre-2026.pdf',format:'A4',printBackground:true,margin:{top:'14mm',bottom:'14mm',left:'12mm',right:'12mm'}});
await b.close();
