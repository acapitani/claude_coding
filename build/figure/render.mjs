// Renderizza una pagina HTML (o un file SVG) in PNG ad alta risoluzione con Chromium (Playwright),
// oppure in PDF vettoriale se l'uscita finisce in .pdf (copertina di stampa).
// Uso:
//   node build/figure/render.mjs <ingresso.html|.svg> <uscita.png> [--larghezza-cm 13] [--altezza-cm 8] [--dpi 300]
//   node build/figure/render.mjs <ingresso.html> <uscita.pdf> --larghezza-cm 31.32 --altezza-cm 21.6
//        [--query "dorso=11.2&retro=..."]
// Senza --altezza-cm l'altezza è quella del contenuto (solo PNG). La pagina può usare i font installati
// (Cambria, Consolas, DejaVu Sans Mono, Segoe UI Symbol…). --query si aggiunge all'indirizzo della pagina.
import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('uso: node render.mjs <ingresso> <uscita.png|.pdf> [--larghezza-cm N] [--altezza-cm N] [--dpi N] [--query S]');
  process.exit(2);
}
const opz = (nome, def) => { const i = args.indexOf(nome); return i >= 0 ? Number(args[i + 1]) : def; };
const opzS = (nome, def) => { const i = args.indexOf(nome); return i >= 0 ? args[i + 1] : def; };
const [ingresso, uscita] = args;
const larghezzaCm = opz('--larghezza-cm', 13);
const altezzaCm = opz('--altezza-cm', null);
const dpi = opz('--dpi', 300);
const query = opzS('--query', '');
const pdf = uscita.toLowerCase().endsWith('.pdf');
if (pdf && !altezzaCm) {
  console.error('per il PDF serve --altezza-cm');
  process.exit(2);
}
const pxCm = 96 / 2.54;                     // px CSS per centimetro
const width = Math.round(larghezzaCm * pxCm);
const height = altezzaCm ? Math.round(altezzaCm * pxCm) : 800;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: pdf ? 1 : dpi / 96 });
const url = pathToFileURL(resolve(ingresso));
if (query) url.search = query;
await page.goto(url.href);
await page.evaluate(() => document.fonts.ready);
// anche le pagine incluse (iframe) devono aver caricato i font e le immagini
for (const f of page.frames()) await f.evaluate(() => document.fonts.ready).catch(() => {});
await page.waitForLoadState('networkidle');
if (pdf) {
  await page.pdf({
    path: resolve(uscita), width: `${larghezzaCm}cm`, height: `${altezzaCm}cm`,
    printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1',
  });
} else {
  if (!altezzaCm) {
    // altezza del contenuto: si ridimensiona la finestra prima dello scatto
    const h = await page.evaluate(() => Math.ceil(document.documentElement.getBoundingClientRect().height));
    await page.setViewportSize({ width, height: Math.max(h, 1) });
  }
  await page.screenshot({ path: resolve(uscita), omitBackground: false });
}
await browser.close();
console.log(`✔ ${uscita}  (${larghezzaCm} cm × ${altezzaCm ?? 'auto'} cm${pdf ? ', PDF vettoriale' : ` a ${dpi} dpi`})`);
