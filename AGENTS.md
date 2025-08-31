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
- Compact mix/master "feel" one-liner at the end
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
[Atmospheric descriptors, cultural context, aesthetic vibe]
[Instrumentation and sonic character in descriptive language]
[Arrangement structure and energy progression]
Mix/Master: [1 line feel only — e.g., "analog warmth, punchy, open, loud-but-dynamic"]
```

### Character Optimization Techniques

**Atmospheric Language:**
- Vivid descriptors: "gritty", "crystalline", "saturated", "haunting"
- Cultural references: era-specific gear, studio locations, artist influences
- Sonic textures: "warm analog saturation", "digital crunch", "vintage shimmer"
- Spatial descriptions: "basement rawness", "cathedral reverb", "intimate close-mic"

**Essential Technical Elements:**
- Key gear references: "MPC", "SP-1200", "Juno", "Moog", "Marshall"
- Basic processing: "compression", "saturation", "filtering", "limiting"
- Simple notation: "→" for signal flow

**Descriptive Efficiency:**
- Combine atmosphere with function: "tape-saturated drums", "tube-warmed bass"
- Cultural context shortcuts: "90s boom-bap", "warehouse techno", "bedroom pop lo-fi"
- Mood-driven descriptions over technical specs

### Key/Scale Best Practices

**MANDATORY: Always use `./random_key.py` for key selection** - never manually choose keys.

**3-Attempt Rule:**
- Run `./random_key.py` up to 3 times if first result doesn't fit genre
- Example: Got "C Major" for dark techno? Run 2 more times
- Choose the best fitting scale from your 3 attempts
- This balances randomness with genre appropriateness

**When Script Says "Use note pattern directly"**:
- ✅ "C-Db-E-F-Gb-Ab-Bb" → exotic scale without confusion
- ❌ "Phrygian Dominant" → may trigger ethnic confusion

**When Script Says "Safe to use scale name"**:
- ✅ "F Natural Minor", "G Dorian", "A Harmonic Minor"
- ✅ Standard modal names that Suno recognizes correctly

**Why This System Works**:
- Weighted randomness prevents mainstream predictability
- 3-attempt rule allows genre-appropriate selection
- Exotic scales create emotionally evocative leads
- Dissonance adds tension and interest in electronic music
- Prevents agents from defaulting to boring major keys

### Mix/Master One‑Liner (Minimal)

- Goal: 1 short line at the very end.
- Focus on intent and feel, not chains.
- Examples: "analog warmth, tight low-end, wide but clean," "raw, gritty, club‑ready, controlled peaks."

### Effects and Character Integration

**Integrated Approach (Preferred):**
```
Drums: vintage analog character → punchy compression → room ambience
Bass: warm tube saturation → rhythmic filtering → subtle stereo spread  
Lead: crystalline digital texture → ethereal delay → atmospheric reverb
Master: analog console warmth → transparent limiting
```

**Descriptive Effects Language:**
- Spatial: "room ambience", "hall reverb", "intimate close-mic", "distant echo"
- Temporal: "rhythmic filtering", "pulsing compression", "breathing dynamics"
- Textural: "tape saturation", "digital crunch", "analog warmth", "crystalline shimmer"

### Arrangement Guidance Philosophy

**What Works:**
- Energy progression: "builds from intimate whispers to explosive choruses"
- Atmospheric evolution: "basement-raw intro expanding to cathedral-wide finale" 
- Cultural/temporal context: "classic 90s boom-bap structure", "warehouse techno journey"
- Key sonic moments: "drops into heavy compression", "breaks into filtered breakdown"

**What Confuses Suno:**
- Too many simultaneous instrument specifications
- Overly complex harmonic analysis
- Too many simultaneous technical processing chains
- Detailed orchestration beyond 3-4 main elements

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

Use **square brackets** for all segment markers and production notes.

Important: Do not use parentheses (...) for any instructions; Suno will sing them. Always use square brackets [...] for markers, production notes, samples, SFX, processing, timing, and mix notes.

```
[Intro – Muted Choir Loop + Static Crackle]
[sample: "it's falling apart…"] [whispered, looped softly in background]

[Verse 1 – Broken Flow, Half-whispered]
Your lyrics here
[—vocal processing notes—] [additional production notes]

[Hook – Female Vocal, Echoed + Flattened]
Chorus lyrics
[—sound effect—] [timing and mix notes]
```

### Professional Lyrics Writing Techniques

**CRITICAL: Avoid Cliché and Generic Content**
- Never use overused rap phrases or predictable rhymes
- Write from authentic perspective, not generic "flexing"
- Avoid forced rhymes that don't serve the meaning
- Study successful artists' techniques, don't copy their content

**Advanced Rhyme Schemes (Essential for Hip-Hop)**
- **Internal rhymes**: Place rhymes within lines, not just at ends
- **Irregular patterns**: Use AABX schemes (X = non-rhyming line for natural flow)
- **Break established patterns**: Disrupt expected rhythms for impact
- **Multisyllabic rhymes**: Match multiple syllables, not just end sounds
- **Avoid same vowel sounds**: Don't rhyme "-ee" sounds throughout entire section

**Flow and Rhythm Mastery**
- **16-bar verse structure**: Standard hip-hop format with precise beat alignment
- **Syllable counting**: Match syllable density to beat patterns
- **Diphthongs**: Use vowel combinations for smoother fast delivery
- **Natural speech patterns**: Write conversational, not forced poetic

**Wordplay and Literary Devices**
- **Double entendres**: Words with multiple meanings in context
- **Metaphors/similes**: Fresh comparisons, avoid overused ones
- **Synecdoche**: Part represents whole (e.g., "wheels" for car)
- **Alliteration**: Strategic, not excessive
- **Avoid nursery rhyme patterns**: Don't sound childish

**Storytelling Structure**
- **Narrative progression**: Each verse advances the story
- **Character development**: Show growth or change
- **Concrete imagery**: Specific details over vague concepts
- **Emotional arc**: Build tension and resolution
- **Conversational authenticity**: "Tell your truth"

**Hip-Hop Specific Techniques**
- **Punchlines**: Sharp, clever conclusions to verses
- **Cultural references**: Current, relevant, not dated
- **Delivery markers**: Write for rhythm and emphasis
- **Battle rap elements**: Clever wordplay and wit
- **Beat integration**: Write to complement, not fight the track

**Production Integration:**
- Samples and sound effects in square brackets (never parentheses)
- Mix notes in square brackets  
- Rhythmic integration with backing track
- Vocal processing guidance in section headers

**Common Clichés to AVOID:**
- Generic "money, cars, chains" flexing without substance
- Overused rhymes: "game/fame", "street/beat", "real/feel"  
- Predictable punchlines everyone has heard
- Dated slang or references
- Forced rhymes that sacrifice meaning
- Basic ABAB rhyme schemes throughout
- "Yo, yo, yo" or similar filler words
- Generic party/club descriptions
- Obvious internal rhymes (lazy/crazy, money/honey)

**Quality Control Checklist:**
- [ ] No cliché phrases or overused rhymes
- [ ] Complex rhyme schemes with internal rhymes
- [ ] Natural flow that matches beat rhythm
- [ ] Authentic voice and perspective
- [ ] Progressive narrative or thematic development
- [ ] Fresh metaphors and wordplay
- [ ] Proper song structure with clear sections

**Example: Avoiding Cliché**

❌ **Cliché/Cringe Version:**
```
I'm on the block making money every day
Got my chain and my car, that's the only way
Haters gonna hate but I don't really care
I'm living my life, money everywhere
```

✅ **Professional Version:**
```
Corner store fluorescents flicker on my grind [internal: flicker/grind]
Twenty-hour shifts got me losing track of time [AABX pattern]
Pockets light but vision heavy, dreams on layaway
While my neighbors count their blessings, I count days
```

**Why It Works:**
- Specific imagery ("fluorescent flicker") over generic ("on the block")
- Internal rhymes without forcing
- AABX rhyme scheme creates natural flow
- Authentic struggle narrative vs. empty flexing
- Fresh metaphors ("dreams on layaway")

**No Character Limit** - Suno handles long lyrics well, use full creative expression while maintaining quality.

## Genre-Specific Lyric Writing Techniques

### General Songwriting Principles (All Genres)

**Universal Best Practices:**
- **Simplicity and repetition**: What gets repeated gets remembered
- **Emotional authenticity**: Write from genuine experience, not manufactured personas
- **Clear central message**: One coherent theme throughout the song
- **Memorability over complexity**: Could a child sing this back?
- **Consistent practice**: Write regularly to develop your unique voice
- **Study successful tracks**: Learn from songs in your target genre

**Structural Fundamentals:**
- **Strong hook/chorus**: The most memorable and singable section
- **Verse storytelling**: Advance narrative or develop theme
- **Bridge contrast**: Different perspective or musical departure
- **Cohesive flow**: Lyrics should fit rhythm and melody naturally

### Punk Rock

**Core Philosophy:**
- **Raw authenticity over polish**: Emotion and passion over technical perfection
- **Direct, simple language**: Short, punchy phrases that cut through noise
- **Social commentary**: Address injustice, rebellion, personal struggles
- **DIY ethos**: Break rules, do things your own way

**Technical Approach:**
- **Straightforward structures**: Verse-chorus-verse-chorus-bridge-chorus
- **Aggressive vocal delivery**: Shouting, snarling, passionate expression
- **Repetitive choruses**: Easy to sing along, memorable slogans
- **Fast, driving rhythms**: Match intensity with tempo
- **Authenticity over rhyme perfection**: Message clarity prioritized

**Avoid:** Overly complex poetry, perfect pitch requirements, lengthy elaborate verses

### Rock Music

**Thematic Focus:**
- **Classic rock**: Nostalgia, rebellion, freedom, human experience
- **Grunge**: Alienation, authenticity, raw emotion
- **Alternative**: Individual expression, non-conformity

**Songwriting Techniques:**
- **Guitar-driven composition**: Write with/around main riffs and chord progressions
- **Anthemic choruses**: Big, singable, emotionally resonant
- **Narrative verses**: Tell stories, paint vivid scenes
- **Dynamic range**: Quiet verses building to explosive choruses
- **Collaborative writing**: Work with band members, especially guitarists

**Structural Elements:**
- **Strong instrumental hooks**: Memorable riffs that define the song
- **Key and tempo matching**: Musical elements support lyrical emotion
- **Build and release**: Create tension and resolution patterns

### Pop Music

**Commercial Songwriting:**
- **Audience-focused**: Write with listeners and radio play in mind
- **Maximum catchiness**: Every element designed for memorability
- **Simple, accessible melodies**: Easy to sing and remember
- **Broad appeal**: Themes that resonate with wide audiences
- **Strategic repetition**: Hooks repeated for maximum impact

**Professional Standards:**
- **Clear, coherent lyrics**: One message throughout the song
- **Emotional connection**: Authentic feelings that resonate deeply
- **Standard song structures**: Familiar patterns audiences expect
- **Radio-friendly length**: Typically 3-4 minutes
- **Strong first impression**: Hook listeners immediately

**Lyrical Approach:**
- **Universal themes**: Love, relationships, personal growth, dreams
- **Relatable scenarios**: Situations most people have experienced
- **Conversational tone**: Natural, not overly poetic
- **Positive or empowering**: Often uplifting or aspirational

### Electronic/EDM

**Unique Considerations:**
- **Instrumental focus**: Music is primary, vocals are complementary
- **Rhythm and timbre priority**: Less emphasis on traditional melody/harmony
- **Loop-based structure**: Vocals must work with repetitive elements
- **Genre-specific timing**: Build-ups, drops, breakdowns at expected moments

**Vocal Integration:**
- **Strategic placement**: Vocals highlight key moments (drops, builds)
- **Vocal chops and samples**: Fragmented vocals as rhythmic elements
- **Atmospheric vocals**: Ethereal, processed, ambient textures
- **Call-and-response**: Vocals that interact with instrumental elements

**EDM-Specific Structures:**
- **Intro-breakdown-buildup-drop**: Standard EDM progression
- **Verse storytelling**: Set up the emotional journey to the drop
- **Euphoric choruses**: Big, immersive, festival-ready moments
- **Minimal lyrics**: Let the music carry the emotional weight
- **Vocal effects**: Heavy processing, pitch shifting, filtering

**Genre Variations:**
- **House/Techno**: Repetitive, hypnotic, minimal vocals
- **Dubstep/Trap**: Aggressive, rhythmic, vocal chops
- **Future Bass**: Pop-influenced, melodic, catchy vocals
- **Progressive**: Evolving, cinematic, emotional journey

### Common Clichés to Avoid (All Genres)

**Overused Themes:**
- Generic party/club descriptions
- Shallow materialism without substance  
- Predictable love song tropes
- Tired rebellion clichés
- Obvious rhyming patterns

**Technical Pitfalls:**
- Forcing rhymes that sacrifice meaning
- Using filler words to complete lines
- Overly complex vocabulary that sounds unnatural
- Repetitive rhyme schemes throughout entire song
- Dated slang or references

**Quality Control for All Genres:**
- [ ] Authentic voice and perspective
- [ ] Genre-appropriate themes and language
- [ ] Natural flow that matches musical rhythm
- [ ] Fresh metaphors and imagery
- [ ] Clear emotional arc or narrative progression
- [ ] Memorable, singable elements
- [ ] Proper song structure for target genre
- [ ] **MANDATORY: File saved to lyrics/ directory with descriptive name**

**No Character Limit** - Suno handles long lyrics well, use full creative expression while maintaining quality and genre authenticity.

## Workflow

### Style Prompt Creation Process

1. **MANDATORY: Generate key with `./random_key.py`** - never choose manually
   - If scale doesn't fit genre, run up to 3 times total
   - Choose the best fitting scale from your attempts
2. **Start with template structure** (tempo, genre, selected key)
3. **Add technical specifications** (instruments, processing)  
4. Add optional 1‑line Mix/Master feel at the very end
5. **MANDATORY: Validate character count with `./validate_style.sh`**
6. **Optimize if needed** - use abbreviations, compact notation
7. **MANDATORY: Re-validate with `./validate_style.sh` until "okay ✓"**
8. **MANDATORY: Save to styles/ directory as .md file** with descriptive filename

**CRITICAL FILE SAVING REQUIREMENTS:**
- **ALWAYS save style prompts** to `styles/[BPM]-[GENRE]-[KEY]-[MOOD].md`
- **ALWAYS save lyrics** to `lyrics/[THEME]-[GENRE]-[MOOD].md`
- **Never just output to console** - user needs files for Suno usage
- **Use descriptive filenames** that identify genre, mood, tempo, key
- **No markdown formatting inside files** - pure text only to save characters

### Character Optimization Loop (MANDATORY)

```bash
# MANDATORY: Validate your draft prompt
./validate_style.sh "your draft prompt"

# If "too short ⚠": Expand high‑value details (priority order):
#   1. Arrangement and energy markers (builds, breaks, drops)
#   2. Instrument specifics + performance nuance (articulation, register)
#   3. Effects and filtering on key parts (LPF/HPF, delay, verb, modulation)
#   4. Optional: add a single Mix/Master feel line at the end

# If "no no ✗": Optimize with abbreviations
# - Replace words with abbreviations  
# - Use compact notation (→, ♭, #)
# - Combine similar descriptors
# - Remove redundant words

# MANDATORY: Repeat validation until "okay ✓"
./validate_style.sh "optimized prompt"
```

### Quality Checklist

**Essential Elements:**
- [ ] **MANDATORY: Random key generated with `./random_key.py` (up to 3 attempts)**
- [ ] BPM and genre specified
- [ ] Key/scale information (notes for exotic scales)
- [ ] Atmospheric and cultural descriptors
- [ ] Sonic character descriptions using vivid language
- [ ] Optional 1‑line Mix/Master feel at end
- [ ] Energy progression and arrangement flow
- [ ] **MANDATORY: Character count 800-975 validated with `./validate_style.sh`**
- [ ] **MANDATORY: File saved to styles/ directory with descriptive name**

**Optimization Check:**
- [ ] Rich atmospheric language and cultural references
- [ ] Descriptive sonic textures and spatial character
- [ ] Essential gear and processing (not over-technical)
- [ ] Clear energy and structural guidance
- [ ] Vivid, evocative descriptions that paint sonic pictures
- [ ] **MANDATORY: Final validation passed with "okay ✓"**

### Expanding "Too Short" Prompts

**Priority 1: Atmospheric Descriptors**
Add vivid cultural and sonic atmosphere:
- Era-specific aesthetic: "90s basement rawness", "2000s digital crunch"
- Spatial character: "warehouse reverb", "bedroom intimacy", "cathedral expansiveness"
- Textural descriptions: "analog tape warmth", "digital crystalline clarity"
- Cultural references: artist influences, studio locations, scene contexts

**Priority 2: Effects/Texture Specifics**
Essential, compact notes that color the sound (not chains):
- Filtering and movement (LPF/HPF, rhythmic gating, side‑chain)
- Space and texture (room/hall, slap delay, tape grit)
- Optional: 1‑line Mix/Master feel at the very end if needed

**Priority 3: Energy and Structure**
- Dynamic progression: builds, drops, breakdowns
- Arrangement flow: intro character → verse energy → chorus explosion
- Sonic evolution throughout the track

**What NOT to Add:**
- Excessive technical specifications
- Multiple detailed processing chains  
- Redundant atmospheric words
- Complex harmonic analysis

## Advanced Techniques

### Instrument Character Patterns

**Drums:**
- Source character: "punchy 909 analog warmth", "crispy 808 digital snap"
- Processing vibe: "vintage compression punch", "tape saturation grit"

**Bass:**
- Sonic identity: "warm Moog analog thickness", "crystalline Juno shimmer"  
- Key treatment: "rhythmic filtering pulse", "tube saturation warmth"

**Leads/Pads:**
- Textural description: "wide analog supersaw", "intimate digital pluck"
- Atmospheric processing: "ethereal delay wash", "vintage reverb space"

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

Use this factory to create prompts that consistently produce professional-quality Suno generations. Dense, well-aimed content, a compact Mix/Master feel line, and exotic key selection are your secret weapons for superior results.
