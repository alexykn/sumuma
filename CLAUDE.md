# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Suno Prompt Factory** - a collection and workspace for creating effective Suno AI music generation prompts. The repository contains battle-tested style prompts and lyrics that produce high-quality musical results.

## Directory Structure

```
suno/
├── styles/          # Style prompts (.md files, 800-975 chars)
├── lyrics/          # Lyrics prompts (.md files, no limit)
├── validate_style.sh # Character validation script
├── random_key.py    # Weighted random key/scale generator
├── generate_style   # Style prompt generator wrapper
├── generate_lyrics  # Lyrics generator wrapper
└── CLAUDE.md        # This guide
```

## Essential Commands

### Style Prompt Validation

```bash
# ALWAYS validate before saving style prompts
./validate_style.sh "your style prompt here"
cat styles/some_prompt.md | ./validate_style.sh

# Script output:
# Character count: 342
# too short ⚠ (if <800 chars)
# okay ✓  (if 800-975 chars)
# no no ✗ (if >975 chars)
```

**CRITICAL RULE**: Every style prompt MUST pass validation. Target 800-975 characters for optimal information density.

### Random Key Selection

```bash
# Generate emotion-evoking key for electronic music
./random_key.py

# Example output:
# Key/Scale: C-Db-E-F-Gb-Ab-Bb
# Usage: Use note pattern directly (avoids confusion)  
# Vibe: Dissonant/Exotic (perfect for electronic)
```

**Key Selection Philosophy**: Prioritize dark, underground modes for electronic music authenticity. The generator weights:
- **Weight 10**: Dark minor modes (Phrygian, Locrian, Natural Minor, Diminished)
- **Weight 8**: Interesting variations (Dorian, Melodic Minor, Pentatonic, Blues)
- **Weight 6**: Exotic scales (Hungarian, Byzantine, Arabic - occasional spice)
- **Weight 2**: Major modes (occasional use)
- **Weight 1**: Mainstream major (rare, for contrast)

## Style Prompt Architecture

### Quality Hierarchy (Analysis of 15 Successful Prompts)

**Tier 1 (Exceptional)**: Prompts 1-8
- Highly technical specifications
- Dedicated MIX + MASTER sections
- Specific instrument models & settings
- Dense with musical abbreviations

**Tier 2 (Good)**: Prompts 9-13  
- Technical but less mixing detail
- Clear arrangement structure
- Specific scales and instruments

**Tier 3 (Basic)**: Prompts 14-15
- Generic descriptions
- Limited technical detail
- Minimal mixing guidance

### Optimal Structure Template

```
[TEMPO] BPM [GENRE] — [KEY/SCALE]
[Key notes if exotic scale] — [mood/feel descriptor]
[Instrumentation sources/style]; [vocal notes]

MIX + MASTER
[Instrument]: [source] → [processing chain] → [EQ/comp settings]
[Next instrument]: [same pattern]
Master: [overall processing] → [limiter settings]
```

### Character Optimization Techniques

**Use Music Abbreviations:**
- BPM, Hz, dB, ms, LPF, HPF, EQ, Comp
- "909 BD", "808 sub", "TB-303", "Juno-106"
- "GR" (gain reduction), "LS" (low shelf), "HC" (high cut)

**Compact Notation:**
- "→" instead of "routed to" or "sent to"
- "1-♭2-6-♭7" for interval patterns
- "4:1, 2 dB GR" for compression settings
- "+2 dB @ 30 Hz" for EQ moves

**Efficient Punctuation:**
- Use bullet points for sections
- Semicolons to separate related ideas
- Parentheses for brief technical notes

### Key/Scale Best Practices

**ALWAYS use `./random_key.py` for key selection** - avoid manually choosing mainstream keys.

**When Script Says "Use note pattern directly"**:
- ✅ "C-Db-E-F-Gb-Ab-Bb" → exotic scale without confusion
- ❌ "Phrygian Dominant" → may trigger ethnic confusion

**When Script Says "Safe to use scale name"**:
- ✅ "F Natural Minor", "G Dorian", "A Harmonic Minor"
- ✅ Standard modal names that Suno recognizes correctly

**Why This Matters**:
- Exotic scales create emotionally evocative leads
- Dissonance adds tension and interest in electronic music
- Mainstream major keys are overused and predictable
- The generator ensures variety while avoiding confusion

### MIX + MASTER Section (Quality Multiplier)

**Why It Works:**
- Suno understands detailed audio processing
- Prevents generic production choices
- Creates professional, intentional sound design

**Essential Elements:**
```
Kick: [drum machine] → [saturation/comp] → [EQ curve]
Bass: [synth type] → [filter] → [compression] → [stereo processing]
[Other instruments]: [similar technical chains]
Master: [metering target] → [limiter type and settings]
```

**Common Processing Chains:**
- "909 BD → Saturator 40% → Comp 4:1, 2 dB GR"
- "Juno-106 saw → LPF → side-chain → EQ mid cut 250 Hz"
- "SPAN target –6 dBFS → Pro-L2 Modern, 1.5 dB GR"

### Filtering & Effects Integration

**Approach 1: Separate Sections**
```
MIX + MASTER
[standard processing chains]

FILTERING
Bass: 18dB LPF opens 64 bars, resonance 30%
Lead: HPF 80Hz → band-pass sweep 200Hz-2kHz

EFFECTS  
Delay: 1/8 dotted ping-pong, 18% wet, HC 6kHz
Reverb: cathedral 3.2s, 45ms pre-delay on pads
```

**Approach 2: Integrated (Preferred for Density)**
```
Bass: Juno-106 saw → 18dB LPF opens 64 bars, 30% res → side-chain comp → ping-pong delay 1/8 dotted 18% wet
```

**Approach 3: Direct Application**
```
Acid: TB-303 saw+pulse → bitcrush → delay 1/16, 20% wet, HC 6kHz → filter sweep automation
```

### Arrangement Guidance Philosophy

**What Works:**
- Rough structural timing ("0:08 kick → 0:24 sub + snare")
- Key instrument roles and patterns
- 1-2 melodic instruments with note patterns
- General energy arc description

**What Confuses Suno:**
- Too many simultaneous instrument specifications
- Overly complex harmonic analysis
- Detailed orchestration for 8+ instruments

### File Naming Convention

Style prompt files should follow this pattern:
`[BPM]-[GENRE]-[KEY]-[MOOD].md`

Examples:
- `128-dark-industrial-techno-f-minor.md`
- `124-progressive-house-g-sharp-minor.md` 
- `94-tech-house-g-phrygian-dominant.md`

**No markdown formatting inside files** - pure text only to save characters.

## Lyrics Guide

### Suno Lyrics Formatting

Use **square brackets** for all segment markers and production notes:

```
[Intro – Muted Choir Loop + Static Crackle]
(sample: "it's falling apart…") [whispered, looped softly in background]

[Verse 1 – Broken Flow, Half-whispered]
Your lyrics here
(Vocal processing notes) [additional production notes]

[Hook – Female Vocal, Echoed + Flattened]
Chorus lyrics
(—sound effect—) [timing and mix notes]
```

### Effective Lyrics Principles

**Structure:**
- Clear song sections with descriptive production notes
- Vocal style guidance in section headers
- Sound effects and samples integrated rhythmically

**Vocal Direction:**
- Specify vocal character: "whispered", "aggressive", "breathy"
- Processing notes: "echoed", "flattened", "pitch-shifted"
- Multiple voices: indicate layers and harmonies

**Production Integration:**
- Samples and sound effects in parentheses
- Mix notes in square brackets
- Rhythmic integration with backing track

**No Character Limit** - Suno handles long lyrics well, use full creative expression.

## Workflow

### Style Prompt Creation Process

1. **Generate key with `./random_key.py`** - never choose manually
2. **Start with template structure** (tempo, genre, generated key)
3. **Add technical specifications** (instruments, processing)  
4. **Include MIX + MASTER section** for quality boost
5. **Validate character count**: `./validate_style.sh`
6. **Optimize if needed** - use abbreviations, compact notation
7. **Re-validate until "okay ✓"**
8. **Save as descriptive .md filename**

### Character Optimization Loop

```bash
# Draft your prompt
./validate_style.sh "your draft prompt"
# If "too short ⚠": Expand technical details (priority order):
#   1. MIX + MASTER processing chains
#   2. Filtering specifications (LPF, HPF, band-pass)
#   3. Effects processing (delay, reverb, modulation)
# If "no no ✗": Optimize with abbreviations
# - Replace words with abbreviations  
# - Use compact notation (→, ♭, #)
# - Combine similar descriptors
# - Remove redundant words
# Repeat until "okay ✓"
```

### Quality Checklist

**Essential Elements:**
- [ ] BPM and genre specified
- [ ] Key/scale information (notes for exotic scales)
- [ ] Specific instrument models (909, 808, Juno, Moog, etc.)
- [ ] MIX + MASTER section with technical details
- [ ] Character count 800-975 (validated with script)
- [ ] Descriptive filename saved in styles/

**Optimization Check:**
- [ ] Maximum use of music abbreviations
- [ ] Compact notation throughout  
- [ ] No redundant descriptions
- [ ] Technical density maximized
- [ ] Clear arrangement guidance without overwhelming detail

### Expanding "Too Short" Prompts

**Priority 1: MIX + MASTER Details**
Add specific processing chains for each instrument:
- Compression ratios, attack/release times
- EQ moves with frequencies and dB amounts  
- Saturation/distortion percentages
- Master limiter settings and headroom targets

**Priority 2: Filtering Specifications**
- Filter types: "18dB LPF", "12dB HPF", "band-pass 200Hz-2kHz"
- Automation: "opens 64 bars", "sweep automation", "resonance 30%"
- Envelope settings: "60ms attack, 400ms release"

**Priority 3: Effects Processing**  
- Delay: timing, wet/dry, high-cut frequencies
- Reverb: type, decay time, pre-delay amounts
- Modulation: LFO rates, depth percentages
- Stereo effects: Haas delays, ping-pong timing

**What NOT to Add:**
- More instruments (confuses arrangement)
- Generic genre descriptors  
- Redundant mood words
- Complex harmonic theory

## Advanced Techniques

### Instrument Specification Patterns

**Drums:**
- "909 BD" (bass drum), "808 sub", "909 CH/OH" (closed/open hat)
- Always specify processing: "→ Comp 4:1 → EQ shelf +2 dB"

**Bass:**
- Synthesizer model + waveform: "Juno-106 saw+sub", "Moog square"
- Side-chain and filtering: "side-chained → LPF 18dB"

**Leads/Pads:**
- Layer description: "wide supersaw", "detuned saw-pluck"
- Effects chain: "ping-pong delay → Haas spread"

### Scale Emotional Mapping (Generated by `./random_key.py`)

**Dark/Underground** (Weight 10): Phrygian, Locrian, Natural Minor, Diminished, Whole Tone
- Creates brooding, underground atmosphere
- Perfect for techno, industrial, and dark electronic genres
- Most authentic for electronic music scenes

**Interesting/Creative** (Weight 8): Dorian, Melodic Minor, Minor Pentatonic, Blues
- Balanced darkness with musical accessibility
- Good for progressive and melodic electronic styles
- Creative without being too exotic

**Exotic/Dissonant** (Weight 6): Hungarian, Byzantine, Arabic, Persian
- Occasional spice for unique character
- Always use note patterns to avoid ethnic confusion
- Use sparingly for special impact

**Balanced/Modal** (Weight 2-4): Lydian, Mixolydian, Major modes
- Occasional use for contrast and dynamics
- Sparingly used to avoid mainstream predictability

**NEVER manually choose mainstream major keys** - let the weighted generator ensure proper variety and emotional depth.

Use this factory to create prompts that consistently produce professional-quality Suno generations. The technical density, MIX + MASTER sections, and exotic key selection are your secret weapons for superior results.