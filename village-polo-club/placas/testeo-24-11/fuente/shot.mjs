import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [,,file,w,h,out]=process.argv;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:+h}});
await p.goto('file://'+process.cwd()+'/'+file);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:out,fullPage:true});await b.close();
