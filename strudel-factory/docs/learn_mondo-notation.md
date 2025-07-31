---
source_url: https://strudel.cc/learn/mondo-notation/
fetched_date: 2025-07-29T17:16:17.463498
title: Mondo Notation ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Mondo Notation

âMondo Notationâ is a new kind of notation that is similar to [Mini Notation](learn_mini-notation.md), but with enough abilities to make it work as a standalone pattern language.
Hereâs an example:


```

$ note (c2 # euclid <3 6 3> <8 16>) # *2 
# s "sine" # add (note [0 <12 24>]*2)
# dec(sine # range .2 2) 
# room .5
# lpf (sine/3 # range 120 400)
# lpenv (rand # range .5 4)
# lpq (perlin # range 5 12 # * 2)
# dist 1 # fm 4 # fmh 5.01 # fmdecay <.1 .2>
# postgain .6 # delay .1 # clip 5

$ s [bd bd bd bd] # bank tr909 # clip .5

# ply <1 [1 [2 4]]>

$ s oh*4 # press # bank tr909 # speed.8

# dec (<.02 .05>*2 # add (saw/8 # range 0 1))


```


## Mondo in the REPL

For now, you can only use mondo in the repl like this:


```

mondo`s hh*8`

```


The rest of this site will only use the mondo notation itself.
In the future, the REPL might get a way to use mondo notation directly.

## Calling Functions

Compared to Mini Notation, the most notable feature of Mondo Notation is the ability to call functions using round brackets:


```

(s hh*8)

```


The first element inside the brackets is the function name. In JS, this would look like:


```

s("hh*8")

```


The outermost parens are not needed, so we can drop them:


```

s hh*8

```


## Mini Notation Features

Besides function calling with round parens, Mondo Notation has a lot in common with Mini Notation:

### Brackets

- `[]` for 1-cycle sequences
- `<>` for multi-cycle sequences
- `{}` for stepped sequences (more on that later)

### Infix Operators

- \* => [fast](learn_time-modifiers_1.md#fast)
- / => [slow](learn_time-modifiers_2.md#slow)
- ! => [extend](learn_stepwise.md#extend)
- @ => [expand](learn_stepwise_1.md#expand)
- % => [pace](learn_stepwise_2.md#pace)
- ? => [degradeBy](learn_random-modifiers_1.md#degradeby) (currently requires right operand)
- : => tail (creates a list)
- .. => range (between numbers)
- , => [stack](learn_factories_1.md#stack)
- | => [chooseIn](learn_random-modifiers_2.md#choose)

### Example


```

note <
[e5 [b4 c5] d5 [c5 b4]]
[a4 [a4 c5] e5 [d5 c5]]
[b4 [~ c5] d5 e5]
[c5 a4 a4 ~]
[[~ d5] [~ f5] a5 [g5 f5]]
[e5 [~ c5] e5 [d5 c5]]
[b4 [b4 c5] d5 e5]
[c5 a4 a4 ~]
>

```


## Chaining Functions

Similar to how â.â works in javascript (JS), we can chain functions calls with the â#â operator:


```

n <0 2 4 [3 1] -1>*4 
# scale C4:minor 
# jux rev 
# dec .2
# delay .5

```


Hereâs the same written in JS:


```

n("<0 2 4 [3 1] -1>*4")
.scale("C4:minor")
.jux(rev)
.dec(.2)
.delay(.5)

```


### Chaining Functions Locally

A function can be applied to a single element by wrapping it in round parens:


```

s [bd hh bd (cp # delay .6)] # bank tr909

```


in this case, `delay .6` will only be applied to `cp`. compare this with the JS version:


```

s(seq("bd", "hh", "bd", "cp".delay(.6))).bank('tr909')

```


here we can see how much we can save when thereâs no boundary between mini notation and function calls!

### Chaining Infix Operators

Infix operators exist as regular functions, so they can be chained as well:


```

s [bd hh] # bank tr909 # *2

```


In this case, the \*2 will be applied to the whole pattern.

### Lambda Functions

Some functions in strudel expect a function as input, for example:


```

n("0 .. 7").scale("C:minor").sometimes(x=>x.dec(.1))

```


in mondo, the `x=>x.` can be shortened to:


```

n 0..7 # scale C:minor # sometimes (# dec .1)

```


chaining works as expected:


```

n 0..7 # scale C:minor # sometimes (# dec .1 # jux rev)

```


## Strings

You can use âdouble quotesâ and âsingle quotesâ to get a string:


```

n 0..7 # scale 'C minor'

```


## Multiple Patterns

The `$` sign can be used to separate multiple patterns:


```

$ s [bd rim [~ bd] rim] # bank tr707
$ chord <Dm9!3 Db7> # voicing
# struct[x ~ ~ x ~ x ~ ~] # delay .5

```


The `$` sign is an alias for `,` so it will create a stack behind the scenes.

## variables

using the `def` keyword, you can define variables:


```


$ def melody [0 1 2 3]
$ n melody # scale C:minor


```

 
