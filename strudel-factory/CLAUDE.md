# CLAUDE.md

Advanced Guide for Strudel Pattern Factory

1. Project Overview
The repository is a Strudel Pattern Factory—a workspace for crafting complete electronic music pieces in the browser using Strudel. It is organised into:

strudel-factory/
├── tracks/          # Finished full-length track patterns (.js)
├── docs/              # Bundled Strudel documentation
├── validate_pattern.sh# Syntax validator for patterns
└── CLAUDE.md  # This guide

Mandatory Workflow Summary

Write and layer patterns in JavaScript using Strudel syntax. Start with a tempo (use setcpm(bpm/4)), then program drums, basslines, harmonic content and effects. Use advanced Strudel features (synths, wavetables, FM, random/conditional modifiers, accumulation, tonal functions, stepwise patterning) described below.

Apply professional audio production techniques: frequency separation, gain staging, stereo imaging, dynamic movement, and proper arrangement (intro, builds, drop, breakdown, outro). Detailed guidelines are provided in Section 7.

Validate your pattern with ./validate_pattern.sh to catch syntax errors. Strudel patterns can be long; there is no length limit.

Name and save the pattern in tracks/ using descriptive names: [BPM]-[GENRE]-[SCALE]-[MOOD].js (e.g., 128-dark-techno-f-phrygian.js). For reusable sequences, use [FUNCTION]-[STYLE].js.

2. Essentials of Strudel
2.1 Pattern Assignment and Mini‑notation
In Strudel, patterns are assigned implicitly. Each statement produces sound or values. Use $: to run multiple patterns concurrently. Use mini‑notation to specify rhythmic structures succinctly. Examples:

javascript
Copy
Edit
// Basic drum pattern
s("bd hh sd hh")

// Multiple layers
$: s("bd*4")                    // Kick
$: note("c e g").s("sawtooth")   // Bass
$: n("0 2 4 6").scale("f:phrygian").s("triangle") // Lead

// Mini‑notation operators
sound("bd*4")         // multiply/repeat
sound("bd/2")         // divide/slow down
sound("bd ~ sd ~")     // rest (~)
sound("[bd sd] hh")   // sub‑sequence
sound("bd,hh*8")      // parallel patterns
sound("<bd sd cp>")    // alternation
sound("bd(3,8)")      // Euclidean rhythms (3 hits in 8 steps)
2.2 Time and Tempo
Use setcpm(tempo/4) to set the tempo in beats per minute (BPM). For example, setcpm(128/4) sets the track to 128 BPM. Changing tempo mid‑song is possible but rarely desirable for electronic music.

2.3 Samples and Sample Maps
Strudel ships with a comprehensive set of drum machines and instrument samples from the tidal-drum-machines and VCSL libraries. The s() or sound() function triggers samples. Use bank() to select a drum machine and n() or the colon syntax to pick individual hits:

javascript
Copy
Edit
// Kick, snare, and hi‑hat using Roland TR‑808 samples
s("bd sd,hh*16").bank("RolandTR808")

// Sequence through different hi‑hat samples
s("hh*8").bank("RolandTR909").n("0 1 2 3")

// Colon notation inside mini‑notation
s("bd*4, hh:0 hh:1 hh:2 hh:3 hh:4 hh:5 hh:6 hh:7").bank("RolandTR909")
Loading Custom Samples
Use the samples() function to map custom names to sample files. This supports single files, arrays of files, GitHub repositories (via samples('github:user/repo')), and local folders (via the REPL’s import sounds dialog or the @strudel/sampler package). Use samples() early in your script so your new sample names are available later.

javascript
Copy
Edit
// Map custom names to sample files from a GitHub repository
samples({
  bassdrum: 'bd/BT0AADA.wav',
  hihat: 'hh27/000_hh27closedhh.wav',
  snaredrum: ['sd/rytm-01-classic.wav','sd/rytm-00-hard.wav']
}, 'https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/');

s("bassdrum snaredrum:0 bassdrum snaredrum:1, hihat*16")
Strudel also supports pitched samples and wavetables by declaring key‑ranges or prefixing sample names with wt_. See Section 3 for synthesiser details.

2.4 Synthesiser Engine
In addition to samples, Strudel includes a built‑in synthesiser. The default waveform is triangle. Use sound() or s() to select waveforms like sine, triangle, sawtooth, square, and noise sources (white, pink, brown). You can add noise to any oscillator via the noise() control. The n parameter sets the number of partials (harmonics) for a waveform, enabling additive synthesis. For example:

javascript
Copy
Edit
note("c e g b").sound("sawtooth").n("<32 16 8 4>")   // Limit harmonics
sound("white").decay(.1).sustain(0)                   // Noise for hi‑hats
FM Synthesis
Frequency‑modulation (FM) allows complex timbres. Use .fm() to set the modulation index, .fmh() for harmonicity ratio, and .fmattack(), .fmdecay(), .fmsustain(), .fmenv() for envelope control.

Wavetable Synthesis
Prefix a sample name with wt_ to load it as a single‑cycle waveform. Strudel includes the Adventure Kid Waveforms (AKWF) by default. Use loopBegin and loopEnd to scan through the wavetable.

ZZFX
Strudel integrates Frank Force’s ZZFX synth engine. Use s("{z_sawtooth z_tan z_noise z_sine z_square}") to pick ZZFX waveforms. Numerous parameters control distortion, pitch slides, bit‑crush, delays, LFOs and more (e.g., .curve(), .slide(), .deltaSlide(), .noise(), .zmod(), .zcrush(), .zdelay(), .pitchJump(), .lfo(), .tremolo()). These can be combined with Strudel’s own effects.

3. Audio Effects
Strudel offers a rich suite of effects. All parameters can be patterned. Combine them to create evolving timbres.

3.1 Filters
lpf(f) / cutoff(f): Low‑pass filter. Use .lpq(q) / .resonance(q) for resonance.

hpf(f): High‑pass filter. Use .hpq(q) for resonance.

bpf(f): Band‑pass filter. Use .bpq(q) for resonance.

ftype(type): Filter type (0 = 12 dB, 1 = ladder, 2 = 24 dB).

Filter envelopes: .lpattack(t), .lpdecay(t), .lpsustain(lvl), .lprelease(t), .lpenv(shape) for low‑pass; analogous methods exist for pitch (pattack, pdecay, penv) and other parameters.

3.2 Amplitude & Dynamics
Gain: .gain(v) or .velocity(v) set amplitude. Keep levels below 1 to avoid clipping.

Compressor: .compressor(settings) applies dynamic range compression. Use .postgain() to compensate gain reduction.

Envelope: .attack(), .decay(), .sustain(), .release(), or .adsr("a:d:s:r") shape amplitude.

Amplitude Modulation: .am(depth) modulates amplitude; .tremolosync(), .tremolodepth(), .tremoloskew(), .tremolophase(), .tremoloshape() create rhythmic tremolos.

3.3 Time‑Based Effects
Delay: .delay(level) sets delay mix; .delaytime(time) sets delay length; .delayfeedback(feedback) controls feedback (0–1). Avoid values ≥ 1.

Reverb: .room(level) sets reverb mix; .roomsize(size), .roomfade(), .roomlp(), .roomdim(), .iresponse() fine‑tune the reverb. Adjust these sparingly.

Phaser: .phaser(speed) for modulation speed; .phaserdepth(), .phasercenter(freq), .phasersweep(range) for shaping.

3.4 Panning & Stereo
.pan(position): Pan within stereo field (0 = left, 1 = right). Accepts patterns to move sounds over time.

jux(fn): Splits the pattern into left and right; applies fn to the right channel.

juxBy(pat, fn): Switches between the original and processed pattern based on pat.

Keep low‑frequency elements (kick, sub‑bass) centred; pan percussive and harmonic elements to create width.

3.5 Waveshaping & Distortion
.coarse(bits): Reduce bit depth.

.crush(amount): Bit‑crush effect.

.distort(amount): Soft‑clip distortion.

3.6 Global vs Local Effects
Use .orbit(n) to route patterns to different effect buses. Effects are processed per bus; use this to manage global vs local reverbs or delays. For example, send multiple hi‑hat patterns to the same delay by setting .orbit(1) on each.

4. Pattern Modifiers
4.1 Random Modifiers
Randomness adds variation and life to patterns. Key functions include:

.choose(x1, x2, ...): Randomly picks one value per event.

.wchoose([value, weight], ...): Weighted random selection.

.chooseCycles(...)/.wchooseCycles(...): Chooses a value each cycle.

.degradeBy(amount): Randomly removes events with probability amount (0 = never, 1 = always). .degrade() is degradeBy(0.5). Use .undegradeBy() or .undegrade() to invert.

.sometimesBy(probability, fn): Applies fn with the given probability. Shorthands: .sometimes(fn) (50%), .often(fn) (75%), .rarely(fn) (25%), .almostNever(fn), .almostAlways(fn), .never(fn), .always(fn).

.someCyclesBy(prob, fn): Applies fn randomly per cycle.

4.2 Conditional Modifiers
These apply transformations based on pattern conditions:

.firstOf(n, fn): Apply fn on the first cycle of every group of n cycles.

.lastOf(n, fn): Apply fn on the last cycle of every n cycles.

.when(binaryPattern, fn): Apply fn when binaryPattern is 1.

.chunk(n, fn): Divide the pattern into n parts and apply fn to each successive part per cycle; .chunkBack iterates backwards.

.struct(mask): Gate events using a binary mask ('1' triggers; '0' mutes). .mask(mask) is shorthand.

.reset(pat) / .restart(pat): Reset or restart patterns based on pat.

.invert(): Swap 1s and 0s in a binary pattern.

.pick(list) / .pickmod(): Index into lists or objects; wraps indices when out of range.

4.3 Accumulation & Layering
.superimpose(fn): Layer the result of fn on top of the original pattern.

.layer(fn): Apply fn and discard the original.

.off(time, fn): Superimpose a function with a time offset (delay) for echoes or call‑and‑response.

.echo(times, time, feedback): Create multiple repeats decreasing in volume.

.echoWith(times, time, fn): Repeat a pattern applying fn each time (e.g., transposing each echo up a step).

4.4 Tonal Functions
Use helpers from tonal.js:

.scale(name): Convert numbers into notes within the given scale and set the scale for transpositions. Format: root:mode (e.g., "c4:minor", "f#:phrygian dominant").

.voicing(options): Turn chord symbols into specific voicings; options include dict, anchor, mode, offset, and n (play voicing as scale degrees).

.transpose(semitones): Shift notes by semitones.

.scaleTranspose(steps): Shift notes by scale steps.

.rootNotes(octave): Extract root notes from chord symbols.

4.5 Stepwise Patterning (Experimental)
Stepwise functions operate on step counts rather than cycles. Use them to create polyrhythms and complex sequences:

.pace(n): Rescale a pattern to play n steps per cycle.

.stepcat(p1, p2, ...): Concatenate patterns proportionally to their step counts (like fastcat but step‑aware).

.expand(n): Increase the number of steps in a pattern by factor n (or pattern of factors); use .pace to set speed.

5. Continuous Signals and Control Sources
Signals are patterns with continuous values used to modulate parameters. They range from 0–1 or –1–1. Use .range(min, max) to map to any interval and .slow(factor) or .fast(factor) to stretch/compress them in time. Important signals:

sine, cosine, saw, tri, square: periodic LFOs between 0 and 1.

sine2, cosine2, saw2, tri2, square2: periodic LFOs between –1 and 1.

rand: random values (0–1); perlin: smooth random noise; irand(n): random integers (0–n–1); brand: random 0 or 1; brandBy(p): binary random with probability p of being 1.

mousex, mousey: current mouse position (0–1) in the REPL; use for live control.

Example: automate filter cutoff with a sine LFO and random gain modulation:

javascript
Copy
Edit
s("bd*4, hh*8").cutoff(sine.range(200, 2000).slow(8))
  .gain(perlin.range(0.7, 1.0))
6. External Integration: MIDI & OSC
Strudel can control external hardware and software instruments via WebMIDI, OSC, and MQTT. Use these methods to send notes, control changes, or timing messages. For example:

javascript
Copy
Edit
// Send chords to an external synth on MIDI channel 3
$: chord("<C^7 A7b13 Dm7 G7>").voicing().midi('IAC Driver', { midichannel: 3 })

// Map MIDI CC values to control filter cutoff and resonance
let cc = await midiin('IAC Driver');
note("c a f e").lpf(cc(0).range(200, 2000)).lpq(cc(1).range(0, 10)).sound("sawtooth")

// Send transport messages to hardware via midicmd
$: midicmd("clock*48,<start stop>/2").midi('IAC Driver')
7. Professional Electronic Music Production
Strudel gives you powerful tools, but professional results demand careful sound design, arrangement and mixing. The following principles are distilled from professional producers and mixing engineers
audioservices.studio
berktmusic.medium.com
:

7.1 Sound Selection and Arrangement
Choose high‑quality sounds that fit the genre and mood. Good samples and synth presets reduce the need for heavy processing
berktmusic.medium.com
.

Limit the number of layers. Aim for 4–5 major elements (kick, bass, drums/percussion, lead, pad)
audioservices.studio
. Overcrowding makes mixing harder.

Arrange with intention. Give each element its own space in the timeline and avoid having multiple elements compete in the same frequency band
berktmusic.medium.com
audioservices.studio
. Use Strudel’s pattern functions (struct, mask, reset, off, etc.) to sequence parts and create space.

7.2 Gain Staging and Amplitude Hierarchy
Normalise your source samples and synths to near 0 dB before adjusting levels
audioservices.studio
. Use Strudel’s .gain() or .velocity() to set the target amplitude.

Decide which element is the leader (usually the kick in electronic music) and make it the loudest
audioservices.studio
. Other elements should sit below it.

Maintain headroom. When exporting or mixing in Strudel, aim for peaks around –6 dBFS on the master bus
berktmusic.medium.com
.

7.3 Frequency Spectrum Management
Divide the spectrum: sub (20–80 Hz), mid‑bass (80–400 Hz), midrange (400–2000 Hz), presence (2–5 kHz), air (5–20 kHz)
audioservices.studio
.

Use filters (lpf, hpf, bpf) to carve out space. For instance, low‑pass synth pads to avoid clashing with vocals or hi‑hats; high‑pass pads so they don’t muddy the bass.

Use dynamic filter automation (e.g., .cutoff(sine.range(200,2000).slow(8))) to keep elements evolving and avoid static timbres.

7.4 Compression and Dynamics
Apply gentle compression to control peaks and add sustain
berktmusic.medium.com
. Avoid over‑compressing—maintain dynamic range to keep the track lively
audioservices.studio
.

Use sidechain compression to create space for the kick or other lead elements
berktmusic.medium.com
. In Strudel, mimic sidechain by automating .gain() or using .am() modulated by the kick’s envelope.

Introduce intentional silence or negative space. Rests and short decays improve punch and clarity
audioservices.studio
.

7.5 Spatial Processing and Stereo Field
Centre your kick and sub‑bass (.pan(0.5))
audioservices.studio
.

Pan hats, claps, percussion, synth lines, and effects to create width. Use patterns to move them over time (.pan(sine.range(0.2,0.8).slow(4))).

Use reverb and delay sparingly to add depth; too much smears transients and reduces dynamic range
audioservices.studio
berktmusic.medium.com
.

Use jux or juxBy to create call‑and‑response effects across the stereo field.

7.6 Reference Tracks and Monitoring
Regularly compare your work to professional tracks in the same genre to calibrate levels, spectrum balance and dynamics
berktmusic.medium.com
.

Use quality monitors or headphones and treat your room acoustically; accurate listening is essential for clean mixes
berktmusic.medium.com
.

Mix in stages: set levels, sculpt with EQ, apply dynamics, then add effects
berktmusic.medium.com
.

8. Advanced Production Techniques in Strudel
8.1 Dynamic Movement
Static parameters sound amateur. Use continuous signals and random modifiers to animate filters, amplitude, resonance, and panning. For example:

javascript
Copy
Edit
note("c2").s("sawtooth")
  .lpf(perlin.slow(8).range(400, 1200))    // moving cutoff
  .gain(sine.slow(4).range(0.6, 0.8))       // breathing amplitude
  .pan(sine.slow(8).range(0.3, 0.7))        // stereo movement
  .attack(rand.range(0.01, 0.05))           // varied attack
8.2 Multi‑layer Bass Design
Professional tracks often layer bass into sub, mid, and high components to achieve depth and clarity. Use stack() to layer synthesised and sampled elements:

javascript
Copy
Edit
stack(
  // Sub layer: pure sine, centred
  note("c1").s("sine").lpf(80).gain(0.8).pan(0.5),
  // Mid layer: moving sawtooth, band‑limited
  note("c2").s("sawtooth").lpf(sine.slow(4).range(150, 400)).hpf(60).gain(0.6),
  // High layer: square wave with stereo movement
  note("c3").s("square").lpf(800).hpf(200)
    .pan(sine.slow(2).range(0.3, 0.7)).gain(0.4)
)
8.3 Filter Automation and Modulation
Use filter envelopes and continuous signals to create movement. Example: evolving acid bassline:

javascript
Copy
Edit
note("[c2*2 ~ eb2]*2").s("sawtooth")
  .lpf(sine.slow(8).range(300, 1200))   // sweeping filter
  .resonance(perlin.slow(3).range(0.3, 0.9)) // moving resonance
  .sometimes(x => x.transpose(12))      // occasional octave jumps
8.4 Probabilistic Variations
Introduce randomness to avoid repetition. For instance, degrade hats randomly and occasionally speed them up:

javascript
Copy
Edit
s("hh*8").rarely(x => x.speed(2)).degradeBy(0.2).pan(perlin.range(0.2, 0.8))
8.5 Arrangement and Structure
Use arrange() to structure multi‑section pieces with intros, builds, drops and breakdowns. Example of an 8‑bar build:

javascript
Copy
Edit
arrange(
  [4, s("bd*4").gain("0.9 0.85 0.88 0.82")],
  [2, note("c2").s("sawtooth").mask("0 1").lpf(sine.slow(16).range(200, 800)).gain(0.7)],
  [8, stack(
    s("bd*4, hh*8").gain(perlin.range(0.8, 1.0)),
    note("c4 g4").s("triangle").mask("0 0 0 1").gain(saw.slow(16).range(0, 0.6)).room(saw.slow(16).range(0.2, 0.8)).attack(3).release(4)
  )]
).slow(8)
8.6 Professional Builds and Drops
To create tension before a drop, layer noise sweeps, snare rolls, and filter sweeps. Example:

javascript
Copy
Edit
stack(
  // Rising noise sweep
  s("noise").lpf(sine.slow(2).range(100, 10000)).gain(sine.slow(2).range(0, 0.8)).hpf(sine.slow(2).range(80, 1000)),
  // Accelerating snare roll
  s("sd*16").speed(sine.slow(4).range(0.8, 1.5)).gain(sine.slow(2).range(0.4, 0.9)),
  // Filter sweep on bass
  note("c2").s("sawtooth").lpf(sine.slow(1).range(60, 4000)).gain(0.8)
)
9. Quality Checklist
Before finalising any track:

Scale: Generated with random_scale.py and used via .scale().

Tempo: Set with setcpm().

Rhythmic foundation: Kick, snare, hats or percussion are present and professionally balanced.

Bass design: Multi‑layered and frequency‑separated.

Melodic/harmonic elements: Use scales, voicings, chord progressions, and dynamic modulation.

Effects and modulation: Filters, envelopes, delay, reverb, distortion used tastefully and modulated over time.

Arrangement: Clear song structure (intro, build, drop, breakdown, outro). Use arrange() or manual structuring.

Professional mixing: Frequency separation, gain staging, dynamic range, stereo placement, and sparing use of reverb/delay

Randomness and variation: Patterns evolve over time; parameters are not static.

Validation: Pattern passes validate_pattern.sh with no errors.

Naming: File saved in tracks/ with descriptive name.

10. Troubleshooting
No sound: Ensure the browser has audio permissions and samples are loaded. If using custom samples, check URLs or local paths.

Syntax errors: The Strudel validator checks for pattern assignments, functions, and structural correctness. Pay attention to commas, brackets and quotes.

Method names: Strudel uses .room() instead of .reverb(), .delayfeedback() instead of .feedback(), .resonance() instead of .lpq(), and .degrade() takes no parameters.

Performance issues: Reduce the number of simultaneous patterns or complexity; use .hush() to stop all patterns.

Mix sounds muddy: Carve out frequency space with filters, adjust gain and panning, simplify arrangement, and shorten release times.

Remember: Aim for full length tracks in professional quality!
