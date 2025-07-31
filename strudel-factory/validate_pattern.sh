#!/bin/bash

# Strudel Pattern Validator
# Basic syntax and structure validation for Strudel patterns

if [ $# -eq 0 ]; then
    # Read from stdin if no arguments
    text=$(cat)
else
    # Use first argument as text
    text="$1"
fi

# Count lines (excluding empty lines)
line_count=$(echo "$text" | grep -c '^[[:space:]]*[^[:space:]]')

echo "Line count: $line_count"
echo "Basic validation: checking for common Strudel syntax..."

# Check for basic Strudel syntax elements
has_pattern_assignment=$(echo "$text" | grep -c '\$:')
has_sound_or_note=$(echo "$text" | grep -c '\(sound\|note\|s(\)')
has_setcpm=$(echo "$text" | grep -c 'setcpm')

if [ $has_pattern_assignment -gt 0 ] && [ $has_sound_or_note -gt 0 ]; then
    echo "Structure: ✓ (has pattern assignments and sound/note functions)"
    echo "Ready for Strudel REPL ✓"
    exit 0
elif [ $has_sound_or_note -gt 0 ]; then
    echo "Structure: ✓ (has sound/note functions)"
    echo "Tip: Use \$: for multiple simultaneous patterns"
    echo "Ready for Strudel REPL ✓"
    exit 0
else
    echo "Warning: No clear Strudel pattern functions found"
    echo "Make sure to use sound(), note(), or s() functions"
    exit 1
fi