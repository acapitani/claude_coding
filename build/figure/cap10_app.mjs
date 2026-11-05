// Prova e fotografa la mini-app del capitolo 10 (esempi/cap10/convertitore.html)
import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import path from "node:path";

const radice = path.resolve(import.meta.dirname, "../..");
const app = pathToFileURL(path.join(radice, "esempi/cap10/convertitore.html")).href;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 420, height: 440 }, deviceScaleFactor: 3 });
await page.goto(app);

// test: alcune conversioni note
const prova = async (cat, v, da, a) => {
  await page.selectOption("#categoria", cat);
  await page.fill("#valore", String(v));
  await page.selectOption("#da", da);
  await page.selectOption("#a", a);
  return page.textContent("#risultato");
};
console.log(await prova("Lunghezza", 1, "miglia", "chilometri"));
console.log(await prova("Peso", 10, "libbre", "chilogrammi"));
console.log(await prova("Temperatura", -40, "gradi Celsius", "gradi Fahrenheit"));
console.log(await prova("Temperatura", 100, "gradi Celsius", "kelvin"));
await page.fill("#valore", "abc").catch(() => {});
console.log(await prova("Lunghezza", 12, "pollici", "centimetri"));
await page.screenshot({ path: path.join(radice, "assets/cap10/IMG-10-02-app.png") });
await browser.close();
