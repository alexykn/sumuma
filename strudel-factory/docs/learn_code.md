---
source_url: https://strudel.cc/learn/code/
fetched_date: 2025-07-29T17:16:17.542730
title: Coding syntax ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Coding Syntax

Letâs take a step back and understand how the syntax in Strudel works.

Take a look at this simple example:


```

note("c a f e").s("piano")

```


- We have a word `note` which is followed by some brackets `()` with some words/letters/numbers inside, surrounded by quotes `"c a f e"`
- Then we have a dot `.` followed by another similar piece of code `s("piano")`.
- We can also see these texts are *highlighted* using colours: word `note` is purple, the brackets `()` are grey, and the content inside the `""` are green. (The colors could be different if youâve changed the default theme)

What happens if we try to âbreakâ this pattern in different ways?


```

note(c a f e).s(piano)

```



```

note("c a f e")s("piano")

```



```

note["c a f e"].s{"piano"}

```


Ok, none of these seem to workâ¦


```

s("piano").note("c a f e")

```


This one does work, but now we only hear the first noteâ¦

So what is going on here?

# Functions, arguments and chaining

So far, weâve seen the following syntax:


```

xxx("foo").yyy("bar")

```


Generally, `xxx` and `yyy` are called [*functions*](https://en.wikipedia.org/wiki/Function_(computer_programming)), while `foo` and `bar` are called function [*arguments* or *parameters*](https://en.wikipedia.org/wiki/Parameter_(computer_programming)).
So far, weâve used the functions to declare which aspect of the sound we want to control, and their arguments for the actual data.
The `yyy` function is called a [*chained* function](https://en.wikipedia.org/wiki/Method_chaining), because it is appended with a dot (`.`).

Generally, the idea with chaining is that code such as `a("this").b("that").c("other")` allows `a`, `b` and `c` functions to happen in a specified order, without needing to write them as three separate lines of code.
You can think of this as being similar to chaining audio effects together using guitar pedals or digital audio effects.

Strudel makes heavy use of chained functions. Here is a more sophisticated example:


```

note("a3 c#4 e4 a4")
.s("sawtooth")
.cutoff(500)
//.delay(0.5)
.room(0.5)

```


# Comments

The `//` in the example above is a line comment, resulting in the `delay` function being ignored.
It is a handy way to quickly turn code on and off.
Try uncommenting this line by deleting `//` and refreshing the pattern.
You can also use the keyboard shortcut `cmd-/` to toggle comments on and off.

You might noticed that some comments in the REPL samples include some words starting with a â@â, like `@by` or `@license`.
Those are just a convention to define some information about the music. We will talk about it in the [Music metadata](learn_metadata.md) section.

# Strings

Ok, so what about the content inside the quotes (e.g. `"c a f e"`)?
In JavaScript, as in most programming languages, this content is referred to as being a [*string*](https://en.wikipedia.org/wiki/String_(computer_science)).
A string is simply a sequence of individual characters.
In TidalCycles, double quoted strings are used to write *patterns* using the mini-notation, and you may hear the phrase *pattern string* from time to time.
If you want to create a regular string and not a pattern, you can use single quotes, e.g. `'C minor'` will not be parsed as Mini Notation.

The good news is, that this covers most of the JavaScript syntax needed for Strudel!

