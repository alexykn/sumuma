setcpm(122/4);

// --- RHYTHMIC FOUNDATION ---
// Solid kick drum foundation
$: s("bd*4").gain(0.95);

// Complex, evolving hi-hats and percussion
$: stack(
  s("hh*16").degradeBy(0.1).gain(perlin.range(0.5, 0.7)).pan(0.3),
  s("oh").gain(0.6).pan(0.7),
  s("cp(3,8)").gain(0.8).pan(0.6),
  s("~ sn(5,8)").gain(0.9)
).lpf(6000);

// --- HARMONIC BEDS ---
// Chord progression in D Phrygian Dominant with a slow filter sweep
$: note("d3:min7 f#3:dim g3:maj bb3:maj7")
  .s("sawtooth").slow(4)
  .lpf(sine.slow(16).range(800, 2500))
  .resonance(0.2)
  .gain(0.5)
  .room(0.4);

// --- PUSH AND PULL INTERPLAY ---
// Rhythmic bassline that follows the chords and interacts with the kick
$: note("d1 f#1 g1 bb1").scale("d:phrygian dominant").s("square")
  .mask("<t f t f*2 t f*3>")
  .lpf(400)
  .gain(0.8)
  .pan(0.5);

// Call and response synth melody
$: note("d5 bb4 g4 f#4").scale("d:phrygian dominant")
  .s("triangle")
  .slow(2)
  .gain(0.6)
  .off(0.25, x => x.s("sawtooth").gain(0.4).lpf(1000).delay(0.25))
  .jux(x => x.pan(sine.slow(4).range(0.2, 0.4)))
  .pan(sine.slow(4).range(0.6, 0.8));
