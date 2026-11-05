// Fotografa «Spese di casa» in funzione (server avviato a parte su localhost:8000)
import { chromium } from "playwright";
import path from "node:path";
const radice = path.resolve(import.meta.dirname, "../..");
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 840, height: 900 }, deviceScaleFactor: 2.5, locale: "it-IT" });
await p.goto("http://localhost:8000/?mese=2026-10");
await p.locator("main").screenshot({ path: path.join(radice, "assets/cap13/IMG-13-02-app.png") });
// (il grafico è già nella pagina: nessuna figura a parte)
await b.close();
console.log("ok");
