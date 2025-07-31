setcpm(124/4);

// --- DYNAMIC HOUSE GROOVE ---

// Four-on-the-floor kick drum
$: s("bd*4").gain(1.0);

// Clap on the 2 and 4
$: s("~ cp ~ cp").gain(0.8);

// Groovy hi-hats with swing and open hats
$: stack(
  s("hh*8").qs(0.1).gain(0.7), // 8th note hats with swing
  s("~ oh").gain(0.6) // Open hat on the off-beats
);

// --- MELODIC & HARMONIC CORE ---

// Melodic walking bassline
$: note("a2 g2 c3 f2").scale("a:minor").s("fmsquare")
  .lpf(600)
  .gain(0.9)
  .release(0.1);

// Expanded classic house chord progression (Am7 - Gmaj7 - Cmaj7 - Fmaj7)
$: note("a3:min7 g3:maj7 c4:maj7 f3:maj7").s("square").n(3)
  .slow(1)
  .gain(0.6)
  .release(0.4)
  .room(0.2);

// Atmospheric pad
$: note("a2 g2 c3 f2").s("sawtooth").slow(4)
  .lpf(1000)
  .gain(0.4)
  .room(0.3);

// --- LEAD MELODY ---

// Simple, memorable synth lead
$: note("c5 e5 g5 a5").scale("a:minor").s("triangle")
  .slow(2)
  .delay(0.25)
  .delayfeedback(0.4)
  .gain(0.5);