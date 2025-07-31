---
source_url: https://strudel.cc/learn/hydra/
fetched_date: 2025-07-29T17:16:17.557121
title: Hydra ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Using Hydra inside Strudel

You can write [hydra](https://hydra.ojack.xyz/) code in strudel! All you have to do is to call `await initHydra()` at the top:

## H patterns

There is a special function `H` that allows you to use a pattern as an input to hydra:

## detectAudio

To use hydra audio capture, call `initHydra` with `{detectAudio:true}` configuration param:

You might now be able to see this properly here: [open in REPL](_index_1.md#YXdhaXQgaW5pdEh5ZHJhKCkKbGV0IHBhdHRlcm4gPSAiMyA0IDUgWzYgN10qMiIKc2hhcGUoSChwYXR0ZXJuKSkub3V0KG8wKQpuKHBhdHRlcm4pLnNjYWxlKCJBOm1pbm9yIikucGlhbm8oKS5yb29tKDEpIA%3D%3D)

Similar to `detectAudio`, all the [available hydra options](https://github.com/hydra-synth/hydra-synth#api) can be passed to `initHydra`.

## feedStrudel

Using the `feedStrudel` option, you can transform strudel visualizations with hydra:

