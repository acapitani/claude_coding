// Test del convertitore: casi di cui conosciamo il risultato.
// Uso: node prova-convertitore.mjs percorso/del/convertitore.html
import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import path from "node:path";

const CASI = [
  // [categoria, valore scritto, da, a, risultato atteso]
  ["Lunghezza", "1", "miglia", "chilometri", "1,6093 chilometri"],
  ["Lunghezza", "12", "pollici", "centimetri", "30,48 centimetri"],
  ["Peso", "10", "libbre", "chilogrammi", "4,5359 chilogrammi"],
  ["Temperatura", "-40", "gradi Celsius", "gradi Fahrenheit",
   "-40 gradi Fahrenheit"],
  ["Temperatura", "100", "gradi Celsius", "kelvin", "373,15 kelvin"],
  ["Lunghezza", "1,5", "metri", "centimetri", "150 centimetri"],
  ["Temperatura", "-10", "kelvin", "gradi Celsius",
   "Sotto lo zero assoluto: controlla il valore"],
];

const file = path.resolve(process.argv[2]);
const browser = await chromium.launch();
const pagina = await browser.newPage({ locale: "it-IT" });
await pagina.goto(pathToFileURL(file).href);

let falliti = 0;
for (const [cat, valore, da, a, atteso] of CASI) {
  await pagina.selectOption("#categoria", cat);
  await pagina.selectOption("#da", da);
  await pagina.selectOption("#a", a);
  await pagina.click("#valore");               // scrive come una persona
  await pagina.keyboard.press("Control+A");
  await pagina.keyboard.type(valore);
  const ottenuto = (await pagina.textContent("#risultato")).trim();
  const ok = ottenuto === atteso;
  if (!ok) falliti++;
  console.log(`${ok ? "✔" : "✘"} ${valore} ${da} → ${a}: ${ottenuto}` +
              (ok ? "" : `   (atteso: ${atteso})`));
}
await browser.close();
console.log(falliti ? `\n${falliti} test falliti` : "\nTutti i test superati");
process.exit(falliti ? 1 : 0);
