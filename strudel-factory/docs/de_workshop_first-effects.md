---
source_url: https://strudel.cc/de/workshop/first-effects/
fetched_date: 2025-07-29T17:16:18.960903
title: Erste Effekte ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Erste Effekte

## Ein paar grundlegende Effekte

**low-pass filter**


```

note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("sawtooth").lpf(800)

```


 lpf = **l**ow **p**ass **f**ilter

- Ãndere `lpf` in 200. HÃ¶rst du, wie der Bass dumpfer klingt? Es klingt so, als wÃ¼rde die Musik hinter einer geschlossenen TÃ¼r spielen ðª
- Lass uns nun die TÃ¼r Ã¶ffnen: Ãndere `lpf` in 5000. Der Klang wird dadurch viel heller und schÃ¤rfer â¨ðª©
  
**filter automatisieren**


```

note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("sawtooth").lpf("200 1000")

```


 - FÃ¼g noch mehr `lpf` Werte hinzu
- Das Pattern in `lpf` Ã¤ndert nicht den Rhythmus der Basslinie

SpÃ¤ter sehen wir, wie man mit Wellenformen Dinge automatisieren kann.

  
**vowel = Vokal**


```

note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>/2")
.sound("sawtooth").vowel("<a e i o>/2")

```


**gain = VerstÃ¤rkung**


```

stack(
sound("hh*8").gain("[.25 1]*2"),
sound("bd*2,~ sd:1")
) 

```


 Bei Rhythmen ist die Dynamik (= VerÃ¤nderungen der LautstÃ¤rke) sehr wichtig.

- Entferne `.gain(...)` und achte darauf, wie es viel flacher klingt.
- Mach es rÃ¼ckgÃ¤ngig (strg+z dann strg+enter)
  
**stacks in stacks**

Lass uns die obigen Beispiele kombinieren:


```

stack(
stack(
  sound("hh*8").gain("[.25 1]*2"),
  sound("bd*2,~ sd:1")
),
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("sawtooth").lpf("200 1000"),
note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>/2")
.sound("sawtooth").vowel("<a e i o>/2")
) 

```


 Versuche die einzelnen Teile innerhalb von `stack` zu erkennen. Schau dir an wie die Kommas gesetzt sind.

Die 3 Teile (Drums, Bass, Akkorde) sind genau wie vorher, nur in einem `stack`, getrennt durch Kommas.

  
**Den Sound formen mit ADSR-HÃ¼llkurve**


```

note("<c3 bb2 f3 eb3>")
.sound("sawtooth").lpf(600)
.attack(.1)
.decay(.1)
.sustain(.25)
.release(.2)

```


 Versuche herauszufinden, was die Zahlen machen. Probier folgendes:

- attack: `.5` vs `0`
- decay: `.5` vs `0`
- sustain: `1` vs `.25` vs `0`
- release: `0` vs `.5` vs `1`

Kannst du erraten, was die einzelnen Werte machen?

  
LÃ¶sung anzeigen
**adsr-Kurznotation**


```

note("<c3 bb2 f3 eb3>")
.sound("sawtooth").lpf(600)
.adsr(".1:.1:.5:.2")


```


**delay = VerzÃ¶gerung**


```

stack(
note("~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]")
.sound("gm_electric_guitar_muted"),
sound("<bd rim>").bank("RolandTR707")
).delay(".5")

```


 Probier verschiedene `delay` Werte zwischen 0 und 1. Ãbrigens: `.5` ist kurz fÃ¼r `0.5`.

Was passiert, wenn du `.delay(".8:.125")` schreibst? Kannst du erraten, was die zweite Zahl macht?

Was passiert, wenn du `.delay(".8:.06:.8")` schreibst? Kannst du erraten, was die dritte Zahl macht?

  
LÃ¶sung anzeigen
**room aka reverb = Hall**


```

n("<4 [3@3 4] [<2 0> ~@16] ~>/2")
.scale("D4:minor").sound("gm_accordion:2")
.room(2)

```


 Spiel mit verschiedenen Werten.

FÃ¼g auch ein Delay hinzu!

  
**kleiner Dub-Tune**


```

stack(
note("~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]")
.sound("gm_electric_guitar_muted").delay(.5),
sound("<bd rim>").bank("RolandTR707").delay(.5),
n("<4 [3@3 4] [<2 0> ~@16] ~>/2")
.scale("D4:minor").sound("gm_accordion:2")
.room(2).gain(.5)
)

```


FÃ¼r echten Dub fehlt noch der Bass:


```

stack(
note("~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]")
.sound("gm_electric_guitar_muted").delay(.5),
sound("<bd rim>").bank("RolandTR707").delay(.5),
n("<4 [3@3 4] [<2 0> ~@16] ~>/2")
.scale("D4:minor").sound("gm_accordion:2")
.room(2).gain(.4),
n("<0 [~ 0] 4 [3 2] [0 ~] [0 ~] <0 2> ~>*2")
.scale("D2:minor")
.sound("sawtooth,triangle").lpf(800)
)

```


 FÃ¼g `.hush()` ans Ende eines Patterns im stackâ¦

  
**pan = Panorama**


```

sound("numbers:1 numbers:2 numbers:3 numbers:4")
.pan("0 0.3 .6 1")
.slow(2)

```


**speed = Geschwindigkeit**


```

sound("bd rim").speed("<1 2 -1 -2>").room(.2)

```


**fast and slow = schnell und langsam**

Mit `fast` und `slow` kann man das Tempo eines Patterns auÃerhalb der Mini-Notation Ã¤ndern:


```

sound("bd*2,~ rim").slow(2)

```


 Ãndere den `slow`-Wert. Ersetze `slow` durch `fast`.

Was passiert, wenn du den Wert automatisierst? z.b. `.fast("<1 [2 4]>")` ?

  
Ãbrigens, innerhalb der Mini-Notation: `fast` ist `*` und `slow` ist `/`.


```

sound("[bd*2,~ rim]*<1 [2 4]>")

```


## Automation mit Signalen

Anstatt Werte schrittweise zu automatisieren, kÃ¶nnen wir auch sogenannte Signale benutzen:


```

sound("hh*16").gain(sine)

```


 Die grundlegenden Wellenformen sind `sine`, `saw`, `square`, `tri` ð

Probiere auch die zufÃ¤lligen Signale `rand` und `perlin`!

Der `gain`-Wert (VerstÃ¤rkung) wird in der Visualisierung als Transparenz dargestellt.

  
**Bereich Ã¤ndern mit `range`**

Signale bewegen sich standardmÃ¤Ãig zwischen 0 und 1. Wir kÃ¶nnen das mit `range` Ã¤ndern:


```

sound("hh*8").lpf(saw.range(500, 2000))

```


`range` ist nÃ¼tzlich wenn wir Funktionen mit einem anderen Wertebereich als 0 und 1 automatisieren wollen (z.b. `lpf`)

 Was passiert wenn du die beiden Werte vertauschst?

  
Wir kÃ¶nnen die Geschwindigkeit der Automation mit slow / fast Ã¤ndern:


```

note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("sawtooth")
.lpf(sine.range(100, 2000).slow(8))

```


 Die ganze Automation braucht nun 8 cycle bis sie sich wiederholt.

  
## RÃ¼ckblick

| Name | Beispiel |
| --- | --- |
| lpf | ``` note("c2 c3").s("sawtooth").lpf("<400 2000>") ``` |
| vowel | ``` note("c3 eb3 g3").s("sawtooth").vowel("<a e i o>") ``` |
| gain | ``` s("hh*8").gain("[.25 1]*2") ``` |
| delay | ``` s("bd rim").delay(.5) ``` |
| room | ``` s("bd rim").room(.5) ``` |
| pan | ``` s("bd rim").pan("0 1") ``` |
| speed | ``` s("bd rim").speed("<1 2 -1 -2>") ``` |
| range | ``` s("hh*16").lpf(saw.range(200,4000)) ``` |

Lass uns nun die fÃ¼r Tidal typischen [Pattern-Effekte anschauen](de_workshop_pattern-effects.md).

 
