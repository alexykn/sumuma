---
source_url: https://strudel.cc/workshop/first-effects/
fetched_date: 2025-07-29T17:16:17.657372
title: First Effects ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # First Effects

We have sounds, we have notes, now letâs look at effects!

## Some basic effects

**low-pass filter**


```

note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf(800)

```


 lpf = **l**ow **p**ass **f**ilter

- Change lpf to 200. Notice how it gets muffled. Think of it as standing in front of the club with the door closed ðª.
- Now letâs open the doorâ¦ change it to 5000. Notice how it gets brighter â¨ðª©
  
**pattern the filter**


```

note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf("200 1000 200 1000")

```


 - Try adding more values
- Notice how the pattern in lpf does not change the overall rhythm

We will learn how to automate with waves laterâ¦

  
**vowel**


```

note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>")
.sound("sawtooth").vowel("<a e i o>")

```


**gain**


```

$: sound("hh*16").gain("[.25 1]*4")

$: sound("bd*4,[~ sd:1]*2")

```


 Rhythm is all about dynamics!

- Remove `.gain(...)` and notice how flat it sounds.
- Bring it back by undoing (ctrl+z)
  
Letâs combine all of the above into a little tune:


```

$: sound("hh*8").gain("[.25 1]*4")

$: sound("bd*4,[~ sd:1]*2")

$: note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf("200 1000 200 1000")

$: note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>")
.sound("sawtooth").vowel("<a e i o>")

```


**shape the sound with an adsr envelope**


```

note("c3 bb2 f3 eb3")
.sound("sawtooth").lpf(600)
.attack(.1)
.decay(.1)
.sustain(.25)
.release(.2)

```


 Try to find out what the numbers do.. Compare the following

- attack: `.5` vs `0`
- decay: `.5` vs `0`
- sustain: `1` vs `.25` vs `0`
- release: `0` vs `.5` vs `1`

Can you guess what they do?

  
Click to see solution
**adsr short notation**


```

note("c3 bb2 f3 eb3")
.sound("sawtooth").lpf(600)
.adsr(".1:.1:.5:.2")


```


**delay**


```

$: note("[~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]]*2")
.sound("gm_electric_guitar_muted").delay(.5)

$: sound("bd rim").bank("RolandTR707").delay(".5")

```


 Try some `delay` values between 0 and 1. Btw, `.5` is short for `0.5`

What happens if you use `.delay(".8:.125")` ? Can you guess what the second number does?

What happens if you use `.delay(".8:.06:.8")` ? Can you guess what the third number does?

  
Click to see solution
**room aka reverb**


```

n("<4 [3@3 4] [<2 0> ~@16] ~>")
.scale("D4:minor").sound("gm_accordion:2")
.room(2)

```


 Try different values!

Add a delay too!

  
**little dub tune**


```

$: note("[~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]]*2")
.sound("gm_electric_guitar_muted").delay(.5)

$: sound("bd rim").bank("RolandTR707").delay(.5)

$: n("<4 [3@3 4] [<2 0> ~@16] ~>")
.scale("D4:minor").sound("gm_accordion:2")
.room(2).gain(.5)

```


Letâs add a bass to make this complete:


```

$: note("[~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]]*2")
.sound("gm_electric_guitar_muted").delay(.5)

$: sound("bd rim").bank("RolandTR707").delay(.5)

$: n("<4 [3@3 4] [<2 0> ~@16] ~>")
.scale("D4:minor").sound("gm_accordion:2")
.room(2).gain(.4)

$: n("[0 [~ 0] 4 [3 2] [0 ~] [0 ~] <0 2> ~]/2")
.scale("D2:minor")
.sound("sawtooth,triangle").lpf(800)

```


 Try adding `.hush()` at the end of one of the patterns in the stackâ¦

  
**pan**


```

sound("numbers:1 numbers:2 numbers:3 numbers:4")
.pan("0 0.3 .6 1")

```


**speed**


```

sound("bd rim [~ bd] rim").speed("<1 2 -1 -2>").room(.2)

```


**fast and slow**

We can use `fast` and `slow` to change the tempo of a pattern outside of Mini-Notation:


```

sound("bd*4,~ rim ~ cp").slow(2)

```


 Change the `slow` value. Try replacing it with `fast`.

What happens if you use a pattern like `.fast("<1 [2 4]>")`?

  
By the way, inside Mini-Notation, `fast` is `*` and `slow` is `/`.


```

sound("[bd*4,~ rim ~ cp]*<1 [2 4]>")

```


## modulation with signals

Instead of changing values stepwise, we can also control them with signals:


```

sound("hh*16").gain(sine)

```


 The basic waveforms for signals are `sine`, `saw`, `square`, `tri` ð

Try also random signals `rand` and `perlin`!

The gain is visualized as transparency in the pianoroll.

  
**setting a range**

By default, waves oscillate between 0 to 1. We can change that with `range`:


```

sound("hh*16").lpf(saw.range(500, 2000))

```


 What happens if you flip the range values?

  
We can change the modulation speed with slow / fast:


```

note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth")
.lpf(sine.range(100, 2000).slow(4))

```


 The whole modulation will now take 8 cycles to repeat.

  
## Recap

| name | example |
| --- | --- |
| lpf | ``` note("c2 c3 c2 c3").s("sawtooth").lpf("<400 2000>") ``` |
| vowel | ``` note("c3 eb3 g3").s("sawtooth").vowel("<a e i o>") ``` |
| gain | ``` s("hh*16").gain("[.25 1]*2") ``` |
| delay | ``` s("bd rim bd cp").delay(.5) ``` |
| room | ``` s("bd rim bd cp").room(.5) ``` |
| pan | ``` s("bd rim bd cp").pan("0 1") ``` |
| speed | ``` s("bd rim bd cp").speed("<1 2 -1 -2>") ``` |
| signals | `sine`, `saw`, `square`, `tri`, `rand`, `perlin` ``` s("hh*16").gain  (saw) ``` |
| range | ``` s("hh*16").lpf(saw.range(200,4000)) ``` |

Let us now take a look at some of Tidalâs typical [pattern effects](workshop_pattern-effects.md).

 
