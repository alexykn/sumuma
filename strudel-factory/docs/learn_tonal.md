---
source_url: https://strudel.cc/learn/tonal/
fetched_date: 2025-07-29T17:16:17.802244
title: Tonal Functions ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Tonal Functions

These functions use [tonaljs](https://github.com/tonaljs/tonal) to provide helpers for musical operations.

### voicing()

Turns chord symbols into voicings. You can use the following control params:

- `chord`: Note, followed by chord symbol, e.g. C Am G7 Bb^7
- `dict`: voicing dictionary to use, falls back to default dictionary
- `anchor`: the note that is used to align the chord
- `mode`: how the voicing is aligned to the anchor
	- `below`: top note <= anchor
	- `duck`: top note <= anchor, anchor excluded
	- `above`: bottom note >= anchor
- `offset`: whole number that shifts the voicing up or down to the next voicing
- `n`: if set, the voicing is played like a scale. Overshooting numbers will be octaved

All of the above controls are optional, except `chord`.
If you pass a pattern of strings to voicing, they will be interpreted as chords.


```

n("0 1 2 3").chord("<C Am F G>").voicing()

```


Hereâs an example of how you can play chords and a bassline:


```

chord("<C^7 A7b13 Dm7 G7>*2")
.dict('ireal').layer(
x=>x.struct("[~ x]*2").voicing()
,
x=>n("0*4").set(x).mode("root:g2").voicing()
.s('sawtooth').cutoff("800:4:2")
)

```


### scale(name)

Turns numbers into notes in the scale (zero indexed). Also sets scale for other scale operations, like [Pattern#scaleTranspose](#pattern-scaleTranspose).

A scale consists of a root note (e.g. `c4`, `c`, `f#`, `bb4`) followed by semicolon (':') and then a [scale type](https://github.com/tonaljs/tonal/blob/main/packages/scale-type/data.ts).

The root note defaults to octave 3, if no octave number is given.

- scale (string): Name of scale


```

n("0 2 4 6 4 2").scale("C:major")

```



```

n("[0,7] 4 [2,7] 4")
.scale("C:<major minor>/2")
.s("piano")

```



```

n(rand.range(0,12).segment(8))
.scale("C:ritusen")
.s("piano")

```


### transpose(semitones)

Transposes all notes to the given number of semitones:

This method gets really exciting when we use it with a pattern as above.

Instead of numbers, scientific interval notation can be used as well:

### scaleTranspose(steps)

Transposes notes inside the scale by the number of steps:


```

"[-8 [2,4,6]]*2"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>*2")
.note()

```


### rootNotes(octave = 2)

Turns chord symbols into root notes of chords in given octave.

Together with layer, struct and voicings, this can be used to create a basic backing track:


```

"<C^7 A7b13 Dm7 G7>*2".layer(
x => x.voicings('lefthand').struct("[~ x]*2").note(),
x => x.rootNotes(2).note().s('sawtooth').cutoff(800)
)

```

 
