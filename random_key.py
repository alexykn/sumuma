#!/usr/bin/env python3
"""
Suno Key Generator - Weighted random key/scale selection
Favors dissonant, exotic, and emotionally evocative keys for electronic music
"""

import random
import sys

# Musical keys/scales with weights (higher = more likely)
# Weight philosophy:
# 10 = Dark minor modes (perfect for electronic underground)
# 8  = Interesting minor variations (creative but accessible)
# 6  = Exotic/dissonant scales (occasional spice)
# 4  = Standard minor keys
# 2  = Major modes (occasional use)
# 1  = Mainstream major (rare)

KEYS_AND_SCALES = {
    # EXOTIC & DISSONANT SCALES (Weight: 6)
    "C-C#-E-F-G-Ab-B": 6,  # Hungarian Major
    "C-Db-E-F-G-Ab-B": 6,  # Double Harmonic Major
    "C-Db-Eb-F#-G-Ab-B": 6,  # Byzantine
    "C-Db-E-F-G-Ab-Bb": 6,  # Arabic/Hijaz
    "C-D-Eb-F#-G-Ab-Bb": 6,  # Hungarian Minor
    "C-Db-Eb-F#-G-A-Bb": 6,  # Persian
    "C-D-Eb-F#-G-A-B": 6,   # Harmonic Minor
    "C-Db-Eb-F-Gb-Ab-A": 6, # Neapolitan Minor
    "C-D-E-F#-G#-A-B": 6,   # Harmonic Major
    "C-Db-E-F-Gb-Ab-Bb": 6, # Phrygian Dominant
    
    # DARK MINOR MODES (Weight: 10)
    "C Natural Minor": 10,     # C-D-Eb-F-G-Ab-Bb
    "C Phrygian": 10,          # C-Db-Eb-F-G-Ab-Bb  
    "C Locrian": 10,           # C-Db-Eb-F-Gb-Ab-Bb
    "C Aeolian": 10,           # Same as natural minor
    "D Natural Minor": 10,
    "D Phrygian": 10,
    "E Natural Minor": 10,
    "E Phrygian": 10,
    "F Natural Minor": 10,
    "F# Natural Minor": 10,
    "G Natural Minor": 10,
    "G# Natural Minor": 10,
    "A Natural Minor": 10,
    "B Natural Minor": 10,
    
    # INTERESTING MINOR VARIATIONS (Weight: 8)
    "C Dorian": 8,            # C-D-Eb-F-G-A-Bb
    "D Dorian": 8,
    "E Dorian": 8,
    "F Dorian": 8,
    "G Dorian": 8,
    "A Dorian": 8,
    "B Dorian": 8,
    "C Melodic Minor": 8,     # C-D-Eb-F-G-A-B (ascending)
    "D Melodic Minor": 8,
    "E Melodic Minor": 8,
    "F Melodic Minor": 8,
    "G Melodic Minor": 8,
    "A Melodic Minor": 8,
    "B Melodic Minor": 8,
    
    # PENTATONIC & BLUES (Weight: 8)
    "C Minor Pentatonic": 8,  # C-Eb-F-G-Bb
    "D Minor Pentatonic": 8,
    "E Minor Pentatonic": 8,
    "F Minor Pentatonic": 8,
    "G Minor Pentatonic": 8,
    "A Minor Pentatonic": 8,
    "B Minor Pentatonic": 8,
    "C Blues Scale": 8,       # C-Eb-F-F#-G-Bb
    "D Blues Scale": 8,
    "E Blues Scale": 8,
    "F Blues Scale": 8,
    "G Blues Scale": 8,
    "A Blues Scale": 8,
    
    # DIMINISHED & WHOLE TONE (Weight: 10)
    "C Diminished": 10,        # C-D-Eb-F-Gb-Ab-A-B
    "C# Diminished": 10,
    "D Diminished": 10,
    "C Whole Tone": 10,        # C-D-E-F#-G#-A#
    "Db Whole Tone": 10,
    
    # MAJOR MODES (Weight: 2-4)
    "C Lydian": 4,            # C-D-E-F#-G-A-B (raised 4th)
    "D Lydian": 4,
    "E Lydian": 4,
    "F Lydian": 4,
    "G Lydian": 4,
    "A Lydian": 4,
    "B Lydian": 4,
    "C Mixolydian": 4,        # C-D-E-F-G-A-Bb (flat 7th)
    "D Mixolydian": 4,
    "E Mixolydian": 4,
    "F Mixolydian": 4,
    "G Mixolydian": 4,
    "A Mixolydian": 4,
    
    # MAJOR KEYS (Weight: 2, occasional use)
    "C Major": 2,
    "D Major": 2,
    "E Major": 2,
    "F Major": 2,
    "G Major": 2,
    "A Major": 2,
    "B Major": 2,
    
    # MAINSTREAM HAPPY KEYS (Weight: 1, rare)
    "C Major Pentatonic": 1,  # C-D-E-G-A
    "G Major Pentatonic": 1,  # G-A-B-D-E
    "D Major Pentatonic": 1,  # D-E-F#-A-B
}

def get_random_key():
    """Return a weighted random key/scale selection"""
    keys = list(KEYS_AND_SCALES.keys())
    weights = list(KEYS_AND_SCALES.values())
    
    selected = random.choices(keys, weights=weights, k=1)[0]
    return selected

def get_scale_notes(key_name):
    """Convert common scale names to note patterns for exotic scales"""
    # For exotic scales that should use note patterns instead of names
    exotic_patterns = {
        "C-C#-E-F-G-Ab-B": "Hungarian Major in C",
        "C-Db-E-F-G-Ab-B": "Double Harmonic Major in C", 
        "C-Db-Eb-F#-G-Ab-B": "Byzantine in C",
        "C-Db-E-F-G-Ab-Bb": "Arabic/Hijaz in C",
        "C-D-Eb-F#-G-Ab-Bb": "Hungarian Minor in C",
        "C-Db-Eb-F#-G-A-Bb": "Persian in C",
        "C-D-Eb-F#-G-A-B": "Harmonic Minor in C",
        "C-Db-Eb-F-Gb-Ab-A": "Neapolitan Minor in C",
        "C-D-E-F#-G#-A-B": "Harmonic Major in C",
        "C-Db-E-F-Gb-Ab-Bb": "Phrygian Dominant in C",
    }
    
    return exotic_patterns.get(key_name, key_name)

def main():
    selected_key = get_random_key()
    
    # Check if it's an exotic scale that should use note pattern
    if selected_key.count('-') >= 4:  # Has note pattern
        print(f"Key/Scale: {selected_key}")
        print(f"Usage: Use note pattern directly (avoids confusion)")
    else:
        print(f"Key/Scale: {selected_key}")
        print(f"Usage: Safe to use scale name")
    
    # Show weight info
    weight = KEYS_AND_SCALES[selected_key]
    if weight >= 10:
        print(f"Vibe: Dark/Underground (perfect for electronic)")
    elif weight >= 8:
        print(f"Vibe: Interesting/Creative")  
    elif weight >= 6:
        print(f"Vibe: Exotic/Dissonant (occasional spice)")
    elif weight >= 4:
        print(f"Vibe: Balanced/Modal")
    elif weight >= 2:
        print(f"Vibe: Mainstream Major")
    else:
        print(f"Vibe: Very Mainstream (use sparingly)")

if __name__ == "__main__":
    main()