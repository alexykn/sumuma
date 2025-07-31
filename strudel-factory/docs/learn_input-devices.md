---
source_url: https://strudel.cc/learn/input-devices/
fetched_date: 2025-07-29T17:16:18.639674
title: Input Devices ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Input Devices

Strudel supports various input devices like Gamepads and MIDI controllers to manipulate patterns in real-time.

# Gamepad

The Gamepad module allows you to integrate gamepad input functionality into your musical patterns. This can be particularly useful for live performances or interactive installations where you want to manipulate sounds using a game controller.

## Getting Started

Initialize a gamepad by calling the gamepad() function with an optional index parameter.


```

// Initialize gamepad (optional index parameter, defaults to 0)
const gp = gamepad(0)
note("c a f e").mask(gp.a)

```


## Available Controls

The gamepad module provides access to buttons and analog sticks as normalized signals (0-1) that can modulate your patterns.

### Buttons

| Type | Controls |
| --- | --- |
| Face Buttons | `a`, `b`, `x`, `y` (or uppercase `A`, `B`, `X`, `Y`) |
| Toggle versions: `tglA`, `tglB`, `tglX`, `tglY` |
| Shoulder Buttons | `lb`, `rb`, `lt`, `rt` (or uppercase `LB`, `RB`, `LT`, `RT`) |
| Toggle versions: `tglLB`, `tglRB`, `tglLT`, `tglRT` |
| D-Pad | `up`, `down`, `left`, `right` (or `u`, `d`, `l`, `r` or uppercase) |
| Toggle versions: `tglUp`, `tglDown`, `tglLeft`, `tglRight` (or `tglU`, `tglD`, `tglL`, `tglR`) |

### Analog Sticks

| Stick | Controls |
| --- | --- |
| Left Stick | `x1`, `y1` (0 to 1 range) |
| `x1_2`, `y1_2` (-1 to 1 range) |
| Right Stick | `x2`, `y2` (0 to 1 range) |
| `x2_2`, `y2_2` (-1 to 1 range) |

### Button Sequence

| Stick | Controls |
| --- | --- |
| Button Sequence | `btnSequence()`, `btnSeq()`, `btnseq()` |

## Using Gamepad Inputs

Once initialized, you can use various gamepad inputs in your patterns. Here are some examples:

### Button Inputs

You can use button inputs to control different aspects of your music, such as gain or triggering events.


```

const gp = gamepad(0)
setcpm(120) 
// Use button values to control amplitude
$: stack(
s("[[hh hh] oh hh oh]/2").mask(gp.tglX).bank("RolandTR909"), // X btn for HH
 s("cr*1").mask(gp.Y).bank("RolandTR909"), // LB btn for CR
s("bd").mask(gp.tglA).bank("RolandTR909"), // A btn for BD
s("[ht - - mt - - lt - ]/2").mask(gp.tglB).bank("RolandTR909"), // B btn for Toms
s("sd*4").mask(gp.RB).bank("RolandTR909"), // RB btn for SD
)


```


### Analog Stick Inputs

Analog sticks can be used for continuous control, such as pitch shifting or panning.


```

const gp = gamepad(0)
setcpm(120)
// Use analog stick for continuous control
$: note("c4 d3 a3 e3").sound("sawtooth") 
.lpf(gp.x1.range(100,4000)) 
.lpq(gp.y1.range(5,30))
.decay(gp.y2.range(0.1,2))
.lpenv(gp.x2.range(-5,5))

```


### Button Sequences

You can define button sequences to trigger specific actions, like playing a sound when a sequence is detected.


```

const gp = gamepad(0)
setcpm(120)
// Define button sequences
const HADOUKEN = [
'd',               // Down
'r',               // Right
'a',               // A
]
const KONAMI = 'uuddlrlrba' //Konami Code ââââââââBA

// Check butto-n sequence (returns 1 while detected, 0 when not within last 1 second)
$: s("free_hadouken -").slow(2)
.mask(gp.btnSequence(HADOUKEN)).room(1)

// hadouken.wav by Syna-Max
//https://freesound.org/people/Syna-Max/sounds/67674/
samples({free_hadouken: 'https://cdn.freesound.org/previews/67/67674_111920-lq.mp3'})


```


## Multiple Gamepads

Strudel supports multiple gamepads. You can specify the gamepad index to connect to different devices.


```

const pad1 = gamepad(0);  // First gamepad
const pad2 = gamepad(1);  // Second gamepad

```

 
