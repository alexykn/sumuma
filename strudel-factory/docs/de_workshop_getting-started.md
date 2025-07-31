---
source_url: https://strudel.cc/de/workshop/getting-started/
fetched_date: 2025-07-29T17:16:18.679963
title: Intro ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Willkommen

Willkommen zum Strudel Workshop!
Du hast den richtigen Ort gefunden wenn du lernen mÃ¶chtest wie man mit Code Musik macht.

## Was ist Strudel

Mit Strudel kann man dynamische MusikstÃ¼cke in Echtzeit schreiben.
Es ist eine in JavaScript entwickelte Version von [Tidal Cycles](https://tidalcycles.org/) und wurde 2022 von Alex McLean und Felix Roos initiiert.
Tidal Cycles, auch bekannt unter dem Namen Tidal, ist eine Computersprache fÃ¼r algorithmische Muster.
Obwohl sie meistens fÃ¼r die Erzeugung von Musik eingesetzt wird, kann sie fÃ¼r jede Art von TÃ¤tigkeit eingesetzt werden,
in der Muster eine Rolle spielen.

Du brauchst keine Erfahrung in JavaScript oder Tidal Cycles um mit Strudel Musik zu machen.
Dieser interaktive Workshop leitet dich spielerisch durch die Grundlagen von Strudel.
Der beste Ort um mit Strudel Musik zu machen ist das [Strudel REPL](_index.md).

## Was kann man mit Strudel machen?

- Musik Live Coding: In Echtzeit mit Code Musik machen
- Algorithmische Komposition: Schreibe Musik mithilfe Tidals einzigartiger Sprache fÃ¼r Muster
- Lehren: Strudel eignet sich gut fÃ¼r Lehrende, da keine Installation nÃ¶tig ist und die Sprache kein theoretisches Vorwissen erfordert.
- Mit anderen Musik-Anwendungen kombinieren: Per MIDI oder OSC kann Strudel als flexibler Sequencer mit jedem Setup kombiniert werden

## Beispiel

Hier ist ein Beispiel wie Strudel klingen kann:


```

stack(
// drums
s("bd,[~ <sd!3 sd(3,4,2)>],hh*8")
.speed(perlin.range(.8,.9)), // random sample speed variation
// bassline
"<a1 b1*2 a1(3,8) e2>" 
.off(1/8,x=>x.add(12).degradeBy(.5)) // random octave jumps
.add(perlin.range(0,.5)) // random pitch variation
.superimpose(add(.05)) // add second, slightly detuned voice
.note() // wrap in "note"
.decay(.15).sustain(0) // make each note of equal length
.s('sawtooth') // waveform
.gain(.4) // turn down
.cutoff(sine.slow(7).range(300,5000)), // automate cutoff
// chords
"<Am7!3 <Em7 E7b13 Em7 Ebm7b5>>".voicings('lefthand') 
.superimpose(x=>x.add(.04)) // add second, slightly detuned voice
.add(perlin.range(0,.5)) // random pitch variation
.note() // wrap in "note"
.s('sawtooth') // waveform
.gain(.16) // turn down
.cutoff(500) // fixed cutoff
.attack(1) // slowly fade in
)
.slow(3/2)

```


Mehr Beispiele gibt es [hier](examples.md).

Du kannst auch im [Strudel REPL](_index.md) auf `shuffle` klicken um ein zufÃ¤lliges Beispiel zu hÃ¶ren.

## Workshop

Der beste Weg um Strudel zu lernen ist der nun folgende Workshop.
Wenn du bereit bist, lass uns loslegen mit deinen [ersten Sounds](de_workshop_first-sounds.md).

 
