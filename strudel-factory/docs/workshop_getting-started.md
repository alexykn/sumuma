---
source_url: https://strudel.cc/workshop/getting-started/
fetched_date: 2025-07-29T17:16:17.259643
title: Getting Started ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Welcome

Welcome to the Strudel documentation pages!
Youâve come to the right place if you want to learn how to make music with code.

## What is Strudel?

With Strudel, you can expressively write dynamic music pieces.
It is an official port of the [Tidal Cycles](https://tidalcycles.org/) pattern language to JavaScript.
You donât need to know JavaScript or Tidal Cycles to make music with Strudel.
This interactive tutorial will guide you through the basics of Strudel.
The best place to actually make music with Strudel is the [Strudel REPL](_index.md)

## What can you do with Strudel?

- live code music: make music with code in real time
- algorithmic composition: compose music using tidalâs unique approach to pattern manipulation
- teaching: focussing on a low barrier of entry, Strudel is a good fit for teaching music and code at the same time.
- integrate into your existing music setup: either via MIDI or OSC, you can use Strudel as a really flexible sequencer

## Examples

Here are some examples of how strudel can sound:


```

// "coastline" @by eddyflux
// @version 1.0
samples('github:eddyflux/crate')
setcps(.75)
let chords = chord("<Bbm9 Fm9>/4").dict('ireal')
stack(
  stack( // DRUMS
    s("bd").struct("<[x*<1 2> [~@3 x]] x>"),
    s("~ [rim, sd:<2 3>]").room("<0 .2>"),
    n("[0 <1 3>]*<2!3 4>").s("hh"),
    s("rd:<1!3 2>*2").mask("<0 0 1 1>/16").gain(.5)
  ).bank('crate')
  .mask("<[0 1] 1 1 1>/16".early(.5))
  , // CHORDS
  chords.offset(-1).voicing().s("gm_epiano1:1")
  .phaser(4).room(.5)
  , // MELODY
  n("<0!3 1*2>").set(chords).mode("root:g2")
  .voicing().s("gm_acoustic_bass"),
  chords.n("[0 <4 3 <2 5>>*2](<3 5>,8)")
  .anchor("D5").voicing()
  .segment(4).clip(rand.range(.4,.8))
  .room(.75).shape(.3).delay(.25)
  .fm(sine.range(3,8).slow(8))
  .lpf(sine.range(500,1000).slow(8)).lpq(5)
  .rarely(ply("2")).chunk(4, fast(2))
  .gain(perlin.range(.6, .9))
  .mask("<0 1 1 0>/16")
)
.late("[0 .01]*4").late("[0 .01]*2").size(4)

```


These examples cannot fully encompass the variety of things you can do, so [check out the showcase](intro_showcase.md) for some videos of how people use Strudel.

## Getting Started

The best way to start learning Strudel is the workshop.
If youâre ready to dive in, letâs start with your [first sounds](workshop_first-sounds.md)

 
