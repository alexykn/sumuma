setcpm(110/4);

// Drums
$: stack(
  s("bd*4").gain(0.9),
  s("hh*8").degradeBy(0.1).gain(0.6).pan(perlin.range(0.3, 0.7)),
  s("~ sd").gain(0.8)
).lpf(3000);

// Bassline
$: note("f#1*8").scale("f#:lydian").s("sawtooth")
  .lpf(sine.slow(8).range(400, 1200))
  .resonance(0.1)
  .gain(0.8)
  .sometimes(x => x.transpose(12));

// Pad
$: note("f#3 a#3 c#4").s("sawtooth").slow(2)
  .lpf(sine.slow(16).range(800, 2000))
  .gain(0.5)
  .room(0.3);

// Melody
$: note("f#5 c#5 a#4 g#4").s("triangle").slow(4)
  .delay(0.5)
  .delayfeedback(0.5)
  .gain(0.4)
  .pan(sine.slow(4).range(0.2, 0.8));
