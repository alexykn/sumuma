---
source_url: https://strudel.cc/learn/accumulation/
fetched_date: 2025-07-29T17:16:17.337049
title: Accumulation Modifiers ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Accumulation Modifiers

## superimpose

Superimposes the result of the given function(s) on top of the original pattern:


```

"<0 2 4 6 ~ 4 ~ 2 0!3 ~!5>*8"
  .superimpose(x=>x.add(2))
  .scale('C minor').note()

```


## layer

Synonyms: `apply`Layers the result of the given function(s). Like `superimpose`, but without the original pattern:


```

"<0 2 4 6 ~ 4 ~ 2 0!3 ~!5>*8"
  .layer(x=>x.add("0,2"))
  .scale('C minor').note()

```


## off

Superimposes the function result on top of the original pattern, delayed by the given time.

- time (Pattern|number): offset time
- func (function): function to apply


```

"c3 eb3 g3".off(1/8, x=>x.add(7)).note()

```


## echo

Superimpose and offset multiple times, gradually decreasing the velocity

- times (number): how many times to repeat
- time (number): cycle offset between iterations
- feedback (number): velocity multiplicator for each iteration


```

s("bd sd").echo(3, 1/6, .8)

```


## echoWith

Synonyms: `echowith, stutWith, stutwith`Superimpose and offset multiple times, applying the given function each time.

- times (number): how many times to repeat
- time (number): cycle offset between iterations
- func (function): function to apply, given the pattern and the iteration index


```

"<0 [2 4]>"
.echoWith(4, 1/8, (p,n) => p.add(n*2))
.scale("C:minor").note()

```


## stut

Deprecated. Like echo, but the last 2 parameters are flipped.

- times (number): how many times to repeat
- feedback (number): velocity multiplicator for each iteration
- time (number): cycle offset between iterations


```

s("bd sd").stut(3, .8, 1/6)

```


There are also [Tonal Functions](learn_tonal.md).

 
