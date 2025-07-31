---
source_url: https://strudel.cc/learn/factories/
fetched_date: 2025-07-29T17:16:17.408147
title: Creating Patterns ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Creating Patterns

The following functions will return a pattern.
These are the equivalents used by the Mini Notation:

| function | mini |
| --- | --- |
| `cat(x, y)` | `"<x y>"` |
| `seq(x, y)` | `"x y"` |
| `stack(x, y)` | `"x,y"` |
| `stepcat([3,x],[2,y])` | `"x@3 y@2"` |
| `polymeter([a, b, c], [x, y])` | `"{a b c, x y}"` |
| `polymeterSteps(2, x, y, z)` | `"{x y z}%2"` |
| `silence` | `"~"` |

## cat

Synonyms: `slowcat`The given items are con**cat**enated, where each one takes one cycle.

- items (any): The items to concatenate


```

cat("e5", "b4", ["d5", "c5"]).note()
// "<e5 b4 [d5 c5]>".note()

```



```

// As a chained function:
s("hh*4").cat(
   note("c4(5,8)")
)

```


## seq

Synonyms: `sequence, fastcat`Like **cat**, but the items are crammed into one cycle.


```

seq("e5", "b4", ["d5", "c5"]).note()
// "e5 b4 [d5 c5]".note()

```



```

// As a chained function:
s("hh*4").seq(
  note("c4(5,8)")
)

```


## stack

Synonyms: `polyrhythm, pr`The given items are played at the same time at the same length.


```

stack("g3", "b3", ["e4", "d4"]).note()
// "g3,b3,[e4,d4]".note()

```



```

// As a chained function:
s("hh*4").stack(
  note("c4(5,8)")
)

```


## stepcat

Synonyms: `timeCat, timecat`'Concatenates' patterns like `fastcat`, but proportional to a number of steps per cycle.
The steps can either be inferred from the pattern, or provided as a [length, pattern] pair.
Has the alias `timecat`.


```

stepcat([3,"e3"],[1, "g3"]).note()
// the same as "e3@3 g3".note()

```



```

stepcat("bd sd cp","hh hh").sound()
// the same as "bd sd cp hh hh".sound()

```


## arrange

Allows to arrange multiple patterns together over multiple cycles.
Takes a variable number of arrays with two elements specifying the number of cycles and the pattern to use.


```

arrange(
  [4, "<c a f e>(3,8)"],
  [2, "<g a>(5,8)"]
).note()

```


## polymeter

Synonyms: `pm`*Experimental*

Aligns the steps of the patterns, creating polymeters. The patterns are repeated until they all fit the cycle. For example, in the below the first pattern is repeated twice, and the second is repeated three times, to fit the lowest common multiple of six steps.


```

// The same as note("{c eb g, c2 g2}%6")
polymeter("c eb g", "c2 g2").note()

```


## polymeterSteps

## silence

Does absolutely nothing..


```

silence // "~"

```


## run

A discrete pattern of numbers from 0 to n-1


```

n(run(4)).scale("C4:pentatonic")
// n("0 1 2 3").scale("C4:pentatonic")

```


## binary

Creates a pattern from a binary number.

- n (number): input number to convert to binary


```

"hh".s().struct(binary(5))
// "hh".s().struct("1 0 1")

```


## binaryN

Creates a pattern from a binary number, padded to n bits long.

- n (number): input number to convert to binary
- nBits (number): pattern length, defaults to 16


```

"hh".s().struct(binaryN(55532, 16))
// "hh".s().struct("1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 0")

```


After Pattern Constructors, letâs see what [Time Modifiers](learn_time-modifiers.md) are available.

 
