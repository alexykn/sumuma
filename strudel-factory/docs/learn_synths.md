---
source_url: https://strudel.cc/learn/synths/
fetched_date: 2025-07-29T17:16:18.169320
title: Synths ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Synths

In addition to the sampling engine, strudel comes with a synthesizer to create sounds on the fly.

## Basic Waveforms

The basic waveforms are `sine`, `sawtooth`, `square` and `triangle`, which can be selected via `sound` (or `s`):


```

note("c2 <eb2 <g2 g1>>".fast(2))
.sound("<sawtooth square triangle sine>")
._scope()

```


If you donât set a `sound` but a `note` the default value for `sound` is `triangle`!

## Noise

You can also use noise as a source by setting the waveform to: `white`,Â `pink` or `brown`. These are different
flavours of noise, here written from hard to soft.


```

sound("<white pink brown>")._scope()

```


Hereâs a more musical example of how to use noise for hihats:


```

sound("bd*2,<white pink brown>*8")
.decay(.04).sustain(0)._scope()

```


Some amount of pink noise can also be added to any oscillator by using the `noise` paremeter:


```

note("c3").noise("<0.1 0.25 0.5>")._scope()

```


You can also use the `crackle` type to play some subtle noise crackles. You can control noise amount by using the `density` parameter:


```

s("crackle*4").density("<0.01 0.04 0.2 0.5>".slow(2))._scope()

```


### Additive Synthesis

To tame the harsh sound of the basic waveforms, we can set the `n` control to limit the overtones of the waveform:


```

note("c2 <eb2 <g2 g1>>".fast(2))
.sound("sawtooth")
.n("<32 16 8 4>")
._scope()

```


When the `n` control is used on a basic waveform, it defines the number of harmonic partials the sound is getting.
You can also set `n` directly in mini notation with `sound`:


```

note("c2 <eb2 <g2 g1>>".fast(2))
.sound("sawtooth:<32 16 8 4>")
._scope()

```


Note for tidal users: `n` in tidal is synonymous to `note` for synths only.
In strudel, this is not the case, where `n` will always change timbre, be it though different samples or different waveforms.

## Vibrato

### vib

Synonyms: `vibrato, v`Applies a vibrato to the frequency of the oscillator.

- frequency (number|Pattern): of the vibrato in hertz


```

note("a e")
.vib("<.5 1 2 4 8 16>")
._scope()

```



```

// change the modulation depth with ":"
note("a e")
.vib("<.5 1 2 4 8 16>:12")
._scope()

```


### vibmod

Synonyms: `vmod`Sets the vibrato depth in semitones. Only has an effect if `vibrato` | `vib` | `v` is is also set

- depth (number|Pattern): of vibrato (in semitones)


```

note("a e").vib(4)
.vibmod("<.25 .5 1 2 12>")
._scope()

```



```

// change the vibrato frequency with ":"
note("a e")
.vibmod("<.25 .5 1 2 12>:8")
._scope()

```


## FM Synthesis

FM Synthesis is a technique that changes the frequency of a basic waveform rapidly to alter the timbre.

You can use fm with any of the above waveforms, although the below examples all use the default triangle wave.

### fm

Synonyms: `fmi`Sets the Frequency Modulation of the synth.
Controls the modulation index, which defines the brightness of the sound.

- brightness (number|Pattern): modulation index


```

note("c e g b g e")
.fm("<0 1 2 8 32>")
._scope()

```


### fmh

Sets the Frequency Modulation Harmonicity Ratio.
Controls the timbre of the sound.
Whole numbers and simple ratios sound more natural,
while decimal numbers and complex ratios sound metallic.

- harmonicity (number|Pattern):


```

note("c e g b g e")
.fm(4)
.fmh("<1 2 1.5 1.61>")
._scope()

```


### fmattack

Attack time for the FM envelope: time it takes to reach maximum modulation

- time (number|Pattern): attack time


```

note("c e g b g e")
.fm(4)
.fmattack("<0 .05 .1 .2>")
._scope()

```


### fmdecay

Decay time for the FM envelope: seconds until the sustain level is reached after the attack phase.

- time (number|Pattern): decay time


```

note("c e g b g e")
.fm(4)
.fmdecay("<.01 .05 .1 .2>")
.fmsustain(.4)
._scope()

```


### fmsustain

Sustain level for the FM envelope: how much modulation is applied after the decay phase

- level (number|Pattern): sustain level


```

note("c e g b g e")
.fm(4)
.fmdecay(.1)
.fmsustain("<1 .75 .5 0>")
._scope()

```


### fmenv

Ramp type of fm envelope. Exp might be a bit broken..

- type (number|Pattern): lin | exp


```

note("c e g b g e")
.fm(4)
.fmdecay(.2)
.fmsustain(0)
.fmenv("<exp lin>")
._scope()

```


## Wavetable Synthesis

Strudel can also use the sampler to load custom waveforms as a replacement of the default waveforms used by WebAudio for the base synth. A default set of more than 1000 wavetables is accessible by default (coming from the [AKWF](https://www.adventurekid.se/akrt/waveforms/adventure-kid-waveforms/) set). You can also import/use your own. A wavetable is a one-cycle waveform, which is then repeated to create a sound at the desired frequency. It is a classic but very effective synthesis technique.

Any sample preceded by the `wt_` prefix will be loaded as a wavetable. This means that the `loop` argument will be set to `1` by default. You can scan over the wavetable by using `loopBegin` and `loopEnd` as well.


```

samples('bubo:waveforms');
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>")
.n("<1 2 3 4 5 6 7 8 9 10>/2").room(0.5).size(0.9)
.s('wt_flute').velocity(0.25).often(n => n.ply(2))
.release(0.125).decay("<0.1 0.25 0.3 0.4>").sustain(0)
.cutoff(2000).cutoff("<1000 2000 4000>").fast(4)
._scope()


```


## ZZFX

The âZuper Zmall Zound Zynthâ [ZZFX](https://github.com/KilledByAPixel/ZzFX) is also integrated in strudel.
Developed by [Frank Force](https://frankforce.com/), it is a synth and FX engine originally intended to be used for size coding games.

It has 20 parameters in total, here is a snippet that uses all:


```

note("c2 eb2 f2 g2") // also supports freq
.s("{z_sawtooth z_tan z_noise z_sine z_square}%4")
.zrand(0) // randomization
// zzfx envelope
.attack(0.001)
.decay(0.1)
.sustain(.8)
.release(.1)
// special zzfx params
.curve(1) // waveshape 1-3
.slide(0) // +/- pitch slide
.deltaSlide(0) // +/- pitch slide (?)
.noise(0) // make it dirty
.zmod(0) // fm speed
.zcrush(0) // bit crush 0 - 1
.zdelay(0) // simple delay
.pitchJump(0) // +/- pitch change after pitchJumpTime
.pitchJumpTime(0) // >0 time after pitchJump is applied
.lfo(0) // >0 resets slide + pitchJump + sets tremolo speed
.tremolo(0) // 0-1 lfo volume modulation amount
//.duration(.2) // overwrite strudel event duration
//.gain(1) // change volume
._scope() // vizualise waveform (not zzfx related)


```


Note that you can also combine zzfx with all the other audio fx (next chapter).

Next up: [Audio Effects](learn_effects.md)â¦

 
