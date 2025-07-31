---
source_url: https://strudel.cc/de/workshop/first-notes/
fetched_date: 2025-07-29T17:16:18.871422
title: Erste TÃ¶ne ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Erste TÃ¶ne

Jetzt schauen wir uns an wie man mit TÃ¶nen mit der `note` Funktion spielt.

## Zahlen und Noten

**TÃ¶ne mit Zahlen**


```

note("48 52 55 59").sound("piano")

```


 Probiere verschiedene Zahlen aus!

Versuch auch mal Kommazahlen, z.B. 55.5 (beachte die englische Schreibweise von Kommazahlen mit â.â anstatt â,â)

  
**TÃ¶ne mit Buchstaben**


```

note("c e g b").sound("piano")

```


 Versuch verschiedene Buchstaben aus (a - g).

Findest du Melodien die auch gleichzeitig ein Wort sind? Tipp: â ð ð§

  
**Vorzeichen**


```

note("db eb gb ab bb").sound("piano")

```



```

note("c# d# f# g# a#").sound("piano")

```


**Andere Oktaven**


```

note("c2 e3 g4 b5").sound("piano")

```


 Probiere verschiedene Oktaven aus (1-8)

  
Normalerweise kommen Leute die keine Noten besser mit Zahlen anstatt mit Buchstaben zurecht.
Daher benutzen die folgenden Beispiele meistens Zahlen.
SpÃ¤ter sehen wir auch noch ein paar Tricks die es uns erleichtern TÃ¶ne zu spielen die zueinander passen.

## Den Sound verÃ¤ndern

Genau wie bei gerÃ¤uschhaften Sounds kÃ¶nnen wir den Klang unserer TÃ¶ne mit `sound` verÃ¤ndern:


```

note("36 43, 52 59 62 64").sound("piano")

```


 Probier ein paar sounds aus:

- gm\_electric\_guitar\_muted - E-Gitarre
- gm\_acoustic\_bass - Kontrabass
- gm\_voice\_oohs - Chords
- gm\_blown\_bottle - Flasche
- sawtooth - SÃ¤gezahn-Welle
- square - Rechteck-Welle
- triangle - Dreieck-Welle
- Was ist mit bd, sd oder hh?
- Entferne `.sound('...')` komplett
  
**Zwischen Sounds hin und her wechseln**


```

note("48 67 63 [62, 58]")
.sound("piano gm_electric_guitar_muted")

```


**Gleichzeitige Sounds**


```

note("48 67 63 [62, 58]")
.sound("piano, gm_electric_guitar_muted")

```


 Die patterns in `note` und `sound` werden kombiniert!

Wir schauen uns spÃ¤ter noch mehr MÃ¶glichkeiten an wie man patterns kombiniert.

  
## LÃ¤ngere Sequenzen

**Sequenzen verlangsamen mit `/`**


```

note("[36 34 41 39]/4").sound("gm_acoustic_bass")

```


 Das `/4` spielt die Sequenz 4 mal so langsam, also insgesamt 4 cycles = 8s.

Jede Note ist nun also 2s lang.

Schreib noch mehr TÃ¶ne in die Klammern und achte darauf dass es schneller wird.

  
Wenn eine Sequenz unabhÃ¤ngig von ihrem Inhalt immer gleich schnell bleiben soll, gibt es noch eine andere Art Klammern:

**Eins pro Cycle per < >**

Im letzten Kapitel haben wir schon gelernt dass `< ... >` (angle brackets) nur ein Element pro Cycle spielt.
Das ist fÃ¼r Melodien auch sehr nÃ¼tzlich:


```

note("<36 34 41 39>").sound("gm_acoustic_bass")

```


 FÃ¼g noch mehr TÃ¶ne hinzu und achte darauf wie das Tempo gleich bleibt!

TatsÃ¤chlich sind diese Klammern nur eine AbkÃ¼rzung:

`<a b c>` = `[a b c]/3`

`<a b c d>` = `[a b c d]/4`

usw..

  
**Eine Sequenz pro Cycle**


```

note("<[36 48] [34 46] [41 53] [39 51]>")
.sound("gm_acoustic_bass")

```


oder auchâ¦


```

note("<[36 48]*4 [34 46]*4 [41 53]*4 [39 51]*4>/2")
.sound("gm_acoustic_bass")

```


**Alternativen**

Ãhnlich wie Unter-Sequenzen, kann auch `<...>` innerhalb einer Sequenz verwendet werden:


```

note("60 <63 62 65 63>")
.sound("gm_xylophone")

```


Das ist auch praktisch fÃ¼r atonale Sounds:


```

sound("bd*2, ~ <sd cp>, [~ hh]*2")
.bank("RolandTR909")

```


## Skalen

Es kann mÃ¼hsam sein die richtigen Noten zu finden wenn man alle zur VerfÃ¼gung hat.
Mit Skalen ist das einfacher:


```

n("0 2 4 <[6,8] [7,9]>")
.scale("C:minor").sound("piano")

```


 Probier verschiedene Zahlen aus. Jede klingt gut!

Probier verschiedene Skalen:

- C:major
- A2:minor
- D:dorian
- G:mixolydian
- A2:minor:pentatonic
- F:major:pentatonic
  
**Automatisierte Skalen**

Wie alle Funktionen kÃ¶nnen auch Skalen mit einem Pattern automatisiert werden:


```

n("<0 -3>, 2 4 <[6,8] [7,9]>")
.scale("<C:major D:mixolydian>/4")
.sound("piano")

```


 Wenn du keine Ahnung hast was die Skalen bedeuten, keine Sorge.
Es sind einfach nur Namen fÃ¼r verschiedene Gruppen von TÃ¶nen die gut zusammenpassen.

Nimm dir Zeit um herauszufinden welche Skalen du magst.

  
## Wiederholen und VerlÃ¤ngern

**VerlÃ¤ngern mit @**


```

note("c@3 eb").sound("gm_acoustic_bass")

```


 Ein Element ohne `@` ist gleichbedeutend mit `@1`. Im Beispiel ist `c` drei Einheiten lang, `eb` nur eine.

Spiel mit der LÃ¤nge!

  
**Unter-Sequenzen verlÃ¤ngern**


```

n("<[4@2 4] [5@2 5] [6@2 6] [5@2 5]>*2")
.scale("<C2:mixolydian F2:mixolydian>/4")
.sound("gm_acoustic_bass")

```


 Dieser Groove wird auch `shuffle` genannt.
Jeder Schlag enthÃ¤lt 2 TÃ¶ne, wobei der erste doppelt so lang wie der zweite ist.
Das nennt man auch manchmal `triolen swing`. Es ist ein typischer Rhythmus im Blues und Jazz.

  
**Wiederholen**


```

note("c!2 [eb,<g a bb a>]").sound("piano")

```


 Wechsel zwischen `!`, `*` und `@` hin und her.

Was ist der Unterschied?

  
## RÃ¼ckblick

Das haben wir in diesem Kapitel gelernt:

| Concept | Syntax | Example |
| --- | --- | --- |
| Verlangsamen | / | ``` note("[c a f e]/2") ``` |
| Alternativen | <> | ``` note("c <e g>") ``` |
| VerlÃ¤ngern | @ | ``` note("c@3 e") ``` |
| Wiederholen | ! | ``` note("c!3 e") ``` |

Neue Funktionen:

| Name | Description | Example |
| --- | --- | --- |
| note | TonhÃ¶he als Buchstabe oder Zahl | ``` note("b g e c").sound("piano") ``` |
| scale | Interpretiert `n` als Skalenstufe | ``` n("6 4 2 0").scale("C:minor").sound("piano") ``` |
| stack | Spiele mehrere Patterns parallel (s.u.) | ``` stack(s("bd sd"),note("c eb g")) ``` |

## Beispiele

**Bassline**


```

note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("gm_synth_bass_1")
.lpf(800) // <-- we'll learn about this soon

```


**Melodie**


```

n(`<
[~ 0] 2 [0 2] [~ 2]
[~ 0] 1 [0 1] [~ 1]
[~ 0] 3 [0 3] [~ 3]
[~ 0] 2 [0 2] [~ 2]
>*2`).scale("C4:minor")
.sound("gm_synth_strings_1")

```


**Drums**


```

sound("bd*2, ~ <sd cp>, [~ hh]*2")
.bank("RolandTR909")

```


**Wenn es doch nur einen Weg gÃ¤be das alles gleichzeitig zu spielenâ¦**

 Das geht mit `stack` ð

  


```

stack(
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("gm_synth_bass_1").lpf(800),
n(`<
[~ 0] 2 [0 2] [~ 2]
[~ 0] 1 [0 1] [~ 1]
[~ 0] 3 [0 3] [~ 3]
[~ 0] 2 [0 2] [~ 2]
>*2`).scale("C4:minor")
.sound("gm_synth_strings_1"),
sound("bd*2, ~ <sd cp>, [~ hh]*2")
.bank("RolandTR909")
)

```


Das hÃ¶rt sich doch langsam nach echter Musik an!
Wir haben Sounds, wir haben TÃ¶ne.. noch ein Puzzleteil fehlt: [Effekte](de_workshop_first-effects.md)

 
