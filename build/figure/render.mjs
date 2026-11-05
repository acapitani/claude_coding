// Renderizza una pagina HTML (o un file SVG) in PNG ad alta risoluzione con Chromium (Playwright).
// Uso:
//   node build/figure/render.mjs <ingresso.html|.svg> <uscita.png> [--larghezza-cm 13] [--altezza-cm 8] [--dpi 300]
// Senza --altezza-cm l'altezza è quella del contenuto. La pagina può usare i font installati
// (Cambria, Consolas, DejaVu Sans Mono, Segoe UI Symbol…).
import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('uso: node render.mjs <ingresso> <uscita.png> [--larghezza-cm N] [--altezza-cm N] [--dpi N]');
  process.exit(2);
}
const opz = (nome, def) => { const i = args.indexOf(nome); return i >= 0 ? Number(args[i + 1]) : def; };
const [ingresso, uscita] = args;
const larghezzaCm = opz('--larghezza-cm', 13);
const altezzaCm = opz('--altezza-cm', null);
const dpi = opz('--dpi', 300);
const pxCm = 96 / 2.54;                     // px CSS per centimetro
const width = Math.round(larghezzaCm * pxCm);
const height = altezzaCm ? Math.round(altezzaCm * pxCm) : 800;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: dpi / 96 });
await page.goto(pathToFileURL(resolve(ingresso)).href);
await page.evaluate(() => document.fonts.ready);
if (!altezzaCm) {
  // altezza del contenuto: si ridimensiona la finestra prima dello scatto
  const h = await page.evaluate(() => Math.ceil(document.documentElement.getBoundingClientRect().height));
  await page.setViewportSize({ width, height: Math.max(h, 1) });
}
await page.screenshot({ path: resolve(uscita), omitBackground: false });
await browser.close();
console.log(`✔ ${uscita}  (${larghezzaCm} cm × ${altezzaCm ?? 'auto'} cm a ${dpi} dpi)`);
