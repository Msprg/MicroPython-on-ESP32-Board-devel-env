# Keď už MicroPython, tak poriadne!

Myslím si, že väčšina IDE prostredí ako Thony a uPyCraft je viac vtipom než serióznym nástrojom na vývoj vstavaného software. Keď som ich skúšal bolo tam viac bugov než vo Windows - a to je už čo povedať. Taktiež som nebol jediný ktorý sa pri používaní (alebo skôr trpení) týchto IDE potýkal s nezmyselnými problémami!

Preto vám chcem navrhnúť oveľa robustnejšie riešenie.

# Odporúčané vývojové prostredie

Poznámka: Najnovší VScode má nejaké zmeny ktoré spôsobili nekompatibilitu s PyMakr. Musíte si nainštalovať len o pár mesiacov staršiu verziu 1.65.2 . Po inštalácii nezabudnite vypnúť automatické aktualizácie inak sa vám VScode jedného dňa sktualizuje, a prestane to fungovať. Viac info tu: https://github.com/pycom/pymakr-vsc/issues/144#issuecomment-1084408002

VScode s nainštalovaným extension PyMakr **a Node.js !** Sú k dispozícií 2 verzie: staršia a novšia(preview).

Zdá sa, že novšia zatiaľ takmer vôbec nefeunguje, takže medzitým je najlepšie používať tú staršiu.

Po jej nainštalovaní vo VScode, stlačte **`CTRL+K`**, (pustite ctrl aj k), a stlačte **`F`**. Tým sa zavrú otvorené prostredia a projekty.

Potom si ľubovoľným spôsobom dajte vo VScode otvoriť zložku s projektom (alebo na začiatku nejakú prázdnu). Je dôležité otvoriť zložku až úplne keď budete v adresári so súbormi (main.py, boot.py, etc.).

Po tom, čo otvoríte zložku, a VScode sa reloadne, by sa malo samo spustiť rozšírenie PyMakr a pripojiť sa ku ESP32 (s predpokladom že ju máte pripojenú).

## Základné ovládanie

Po úspešnom pripojení ku ESP32 budete dole v termináli vidieť `>>>`.

Súbory s kódom sa ukladajú na ESP32 dosku, takže ak ich odtiaľ chcete vytiahnuť, dole na stavovej lište (modrom riadku) stlačte **Download**. Toto vytiahne súbory z dosky a dá vám ich do otvorenej zložky na počítači.

Po zmenení kódu, napríklad v súbore `main.py`, ***si súbor najprv nezabudnite uložiť,*** a potom môžete stlačiť **Upload**. Po úspešnom uploade by sa malo ESP32 soft reštarovať, a mal by sa sputiť váš skript.

Za zmienku ešte stojí, že napriek prítomnosti tlačítka **Run**, podľa mojich skúseností funguje nespoľahlivo. Oveľa istejšia metóda je jednoducho používať **Upload**.

Na to ako funguje zvyšok už určite prídete sami~!
