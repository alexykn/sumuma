---
source_url: https://strudel.cc/de/workshop/first-sounds/
fetched_date: 2025-07-29T17:16:19.044305
title: Erste Sounds ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Erste Sounds

Dies ist das erste Kapitel im Strudel Workshop, schÃ¶n dich an Bord zu haben!

## Textfelder

Der Workshop ist voller interaktiver Textfelder. Lass uns lernen wie sie funktionieren. Hier ist eins:


```

sound("casio")

```


 1. â¬ï¸ Klicke in das obige Textfeld â¬ï¸
2. DrÃ¼cke `Strg`+`Enter` zum Abspielen
3. Ãndere `casio` in `metal`
4. DrÃ¼cke `Strg`+`Enter` zum Aktualisieren
5. DrÃ¼cke `Strg`+`Punkt` zum Stoppen

Mac: `Strg` = `control` oder auch `option`

  
GlÃ¼ckwunsch, du kannst jetzt live coden!

## Sounds

Gerade haben wir schon den ersten sound mit `sound` abgespielt:


```

sound("casio")

```


 `casio` ist einer von vielen Standard Sounds.

Probier ein paar andere Sounds aus:


```

insect wind jazz metal east crow casio space numbers

```

Es kann sein, dass du kurz nichts hÃ¶rst wÃ¤hrend ein neuer Sound lÃ¤dt.

  
**Sample Nummer Ã¤ndern mit :**

Ein Sound kann mehrere Samples (Audio Dateien) enthalten.

Du kannst ein anderes Sample wÃ¤hlen, indem du `:` und eine Zahl an den Sound-Namen anhÃ¤ngst:


```

sound("casio:1")

```


 Probiere verschiedene Sound / Zahlen Kombinationen.

Ohne Zahl ist gleichbedeutend mit `:0`

  
Jetzt weiÃt du wie man Sounds abspielt und ihre Sample Nummer einstellt.
Vorerst bleiben wir bei den voreingestellten Sounds, spÃ¤ter erfahren wir noch wie man eigene benutzt.

## Drum Sounds

Strudel kommt von Haus aus mit einer breiten Auswahl an Drum Sounds:


```

sound("bd hh sd oh")

```


 Diese Kombinationen von Buchstaben stehen fÃ¼r verschiedene Teile eines Schlagzeugs:

[original von Pbroks13](https://de.wikipedia.org/wiki/Schlagzeug#/media/Datei:Drum_set.svg)- `bd` = **b**ass **d**rum - Basstrommel
- `sd` = **s**nare **d**rum - Schnarrtrommel
- `rim` = **rim**shot - Rahmenschlag
- `hh` = **h**i**h**at - Hallo Hut
- `oh` = **o**pen **h**ihat - Offener Hallo Hut
- `lt` = **l**ow tom
- `mt` = **m**iddle tom
- `ht` = **h**igh tom
- `rd` = **r**i**d**e cymbal
- `cr` = **cr**ash cymbal

Probier verschiedene Sounds aus!

  
Wir kÃ¶nnen den Charakter des Drum Sounds verÃ¤ndern, indem wir mit `bank` die Drum Machine auswÃ¤hlen:


```

sound("bd hh sd oh").bank("RolandTR909")

```


In diesem Beispiel ist `RolandTR909` der Name der Drum Machine, die eine prÃ¤gende Rolle fÃ¼r House und Techno Musik spielte.

 Ãndere `RolandTR909` in

- `AkaiLinn`
- `RhythmAce`
- `RolandTR808`
- `RolandTR707`
- `ViscoSpaceDrum`

Es gibt noch viel mehr, aber das sollte fÃ¼rs Erste reichen..

ð¦¥ Tipp fÃ¼r faule: Mach Doppel-Klick auf einen Namen um ihn zu markieren.
Dann kannst du ihn mit `Strg`+`C` kopieren und mit `Strg`+`V` einfÃ¼gen.

  
## Sequenzen / Sequences

Im letzten Beispiel haben wir schon gesehen dass man mehrere Sounds hintereinander abspielen kann wenn man sie durch Leerzeichen trennt:


```

sound("bd hh sd hh")

```


Beachte wie der aktuell gespielte Sound im Code markiert und auch darunter visualisiert wird.

 Versuch noch mehr Sounds hinzuzfÃ¼gen!

  
**Je lÃ¤nger die Sequence, desto schneller**


```

sound("bd bd hh bd rim bd hh bd")

```


Der Inhalt einer Sequence wird in einen sogenannten Cycle (=Zyklus) zusammengequetscht. Ein Cycle ist standardmÃ¤Ãig 2 Sekunden lang.

**Eins pro Cycle mit `< .. >`**

Hier ist die gleiche Sequence, aber dieses mal umgeben von `< .. >` (angle brackets):


```

sound("<bd bd hh bd rim bd hh bd>")

```


Jetzt spielt nur ein Sound pro Cycle. Mit diesen Klammern bleibt das Tempo immer gleich, ganz egal wieviele Elemente enhalten sind!

Das ist jetzt aber etwas langsam, machen wir es schneller mit `*`:


```

sound("<bd bd hh bd rim bd hh bd>*8")

```


Die `*8` macht die ganze Sequenz 8 mal so schnell.

 Warte mal, ist das jetzt nicht das gleiche Ergebnis wie ohne `< ... >*8`? WofÃ¼r ist das dann gut?

Korrekt, der echte Vorteil dieser Schreibweise zeigt sich wenn du Elemente entfernst oder hinzufÃ¼gst. Versuch es mal!

Ãndere auch mal die Zahl am Ende um das Tempo zu verÃ¤ndern.

  
**Tempo Ã¤ndern mit `setcpm`**


```

setcpm(90/4)
sound("<bd hh rim hh>*8")

```


 cpm = **c**ycles per **m**inute = Cycles pro Minute

Das Tempo is standardmÃ¤Ãig is 30 Cycles pro Minute = 120/4 = 1 Cycle alle 2 Sekunden

In taditioneller Musik-Terminologie kÃ¶nnte man sagen, das Pattern oben besteht aus 8tel Noten auf 90bpm im 4/4 Takt.

Kein Sorge wenn dir diese Begriffe nichts sagen, das ist nicht notwendig um mit Strudel Musik zu machen.

  
Wir werden spÃ¤ter noch mehr MÃ¶glichkeiten kennen lernen das Tempo zu verÃ¤ndern.

**Pausen mit â-â oder â~â**


```

sound("bd hh - rim")

```


 Du siehst wahrscheinlich auch Patterns von anderen Leuten mit â~â als Pausensymbol.
Besonders fÃ¼r deutsche Tastaturen ist `-` eine Alternative zum schwer tippbaren `~`.

  
**Unter-Sequenzen mit [Klammern]**


```

sound("bd [hh hh] rim [hh hh]")

```


 Der Inhalt der Klammer wird ebenfalls zusammengequetscht!

FÃ¼ge noch mehr Sounds in die Klammern ein!

  
Genau wie bei der ganzen Sequence wird eine Unter-Sequence schneller je mehr drin ist.

**Multiplikation: Dinge schneller machen**


```

sound("bd hh*2 sd hh*3")

```


**Multiplikation: Vieeeeeeel schneller**


```

sound("bd hh*16 sd hh*8")

```


 TonhÃ¶he = sehr schneller Rhythmus

  
**Multiplikation: Ganze Unter-Sequences schneller machen**


```

sound("bd [sd hh]*2")

```


Bolero:


```


setcpm(10)
sound("sd sd*3 sd sd*3 sd sd sd sd*3 sd sd*3 sd*3 sd*3")

```


**Unter-Unter-Sequenzen mit [[Klammern]]**


```

sound("bd [[rim rim] hh]")

```


 Du kannst so tief verschachteln wie du willst!

  
**Parallele Sequenzen mit Komma**


```

sound("hh hh hh, bd casio")

```


Du kannst so viele Kommas benutzen wie du mÃ¶chtest:


```

sound("hh hh hh, bd bd, - casio")

```


Kommas kÃ¶nnen auch in Unter-Sequenzen verwendet werden:


```

sound("hh hh hh, bd [bd,casio]")

```


 Ist dir aufgefallen dass sich die letzten beiden Beispiele gleich anhÃ¶ren?

Es kommt Ã¶fter vor, dass man die gleiche Idee auf verschiedene Arten ausdrÃ¼cken kann.

  
**Mehrere Zeilen schreiben mit ` (backtick)**


```

sound(`bd*2, - cp, 
- - - oh, hh*4,
[- casio]*2`)

```


 Ob man â oder ` benutzt ist nur eine Frage der Ãbersichtlichkeit.

  
**Sample Nummer separat auswÃ¤hlen**

Benutzt man nur einen Sound mit unterschiedlichen Sample Nummer sieht das so aus:


```

sound("jazz:0 jazz:1 [jazz:4 jazz:2] jazz:3*2")

```


Das gleiche kann man auch so schreiben:


```

n("0 1 [4 2] 3*2").sound("jazz")

```


## RÃ¼ckblick

Wir haben jetzt die Grundlagen der sogenannten Mini-Notation gelernt, der Rhythmus-Sprache von Tidal.

Das haben wir bisher gelernt:

| Concept | Syntax | Example |
| --- | --- | --- |
| Sequenz | Leerzeichen | ``` sound("bd bd sd hh") ``` |
| Sound Nummer | :x | ``` sound("hh:0 hh:1 hh:2 hh:3") ``` |
| Pausen | - | ``` sound("metal - jazz jazz:1") ``` |
| Unter-Sequenzen | [] | ``` sound("bd wind [metal jazz] hh") ``` |
| Unter-Unter-Sequenzen | [[]] | ``` sound("bd [metal [jazz sd]]") ``` |
| Schneller | \* | ``` sound("bd sd*2 cp*3") ``` |
| Parallel | , | ``` sound("bd*2, hh*2 [hh oh]") ``` |

Die mit Apostrophen umgebene Mini-Notation benutzt man normalerweise in einer sogenannten Funktion.
Die folgenden Funktionen haben wir bereits gesehen:

| Name | Description | Example |
| --- | --- | --- |
| sound | Spielt den Sound mit dem Namen | ``` sound("bd sd") ``` |
| bank | WÃ¤hlt die Soundbank / Drum Machine | ``` sound("bd sd").bank("RolandTR909") ``` |
| setcpm | Tempo in **C**ycles **p**ro **M**inute | ``` setcpm(90); sound("bd sd") ``` |
| n | Sample Nummer | ``` n("0 1 4 2").sound("jazz") ``` |

## Beispiele

**Einfacher Rock Beat**


```

setcpm(100/2)
sound("bd sd, hh*4").bank("RolandTR505")

```


**Klassischer House**


```

sound("bd*2, - cp, [- hh]*2").bank("RolandTR909")

```


 Ist die aufgefallen dass die letzten 2 Patterns extrem Ã¤hnlich sind?
Bestimmte Drum Patterns werden oft genreÃ¼bergreifend wiederverwendet.

  
We Will Rock you


```

setcpm(81/2)
sound("bd*2 cp").bank("RolandTR707")

```


**Yellow Magic Orchestra - Firecracker**


```

sound("bd sd, - - - hh - hh - -, - perc - perc:1*2")
.bank("RolandCompurhythm1000")

```


**Nachahmung eines 16 step sequencers**


```

setcpm(90/4)
sound(`
[-  -  oh - ] [-  -  -  - ] [-  -  -  - ] [-  -  -  - ],
[hh hh -  - ] [hh -  hh - ] [hh -  hh - ] [hh -  hh - ],
[-  -  -  - ] [cp -  -  - ] [-  -  -  - ] [cp -  -  - ],
[bd -  -  - ] [-  -  -  bd] [-  -  bd - ] [-  -  -  bd]
`)

```


**Noch eins**


```

setcpm(88/4)
sound(`
[-  -  -  - ] [-  -  -  - ] [-  -  -  - ] [-  -  oh:1 - ],
[hh hh hh hh] [hh hh hh hh] [hh hh hh hh] [hh hh -  - ],
[-  -  -  - ] [cp -  -  - ] [-  -  -  - ] [-  cp -  - ],
[bd bd -  - ] [-  -  bd - ] [bd bd - bd ] [-  -  -  - ]
`).bank("RolandTR808")

```


**Nicht so typische Drums**


```

setcpm(100/2)
s(`jazz*2, 
insect [crow metal] - -, 
- space:4 - space:1,
- wind`)

```


Jetzt haben wir eine grundlegende Ahnung davon wie man mit Strudel Beats baut!
Im nÃ¤chsten Kapitel werden wir ein paar [TÃ¶ne spielen](de_workshop_first-notes.md).

 
