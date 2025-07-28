#!/bin/bash

# Suno Style Prompt Validator
# Checks if style prompt is within 975 character limit

if [ $# -eq 0 ]; then
    # Read from stdin if no arguments
    text=$(cat)
else
    # Use first argument as text
    text="$1"
fi

# Count characters (including spaces)
char_count=${#text}

echo "Character count: $char_count"

if [ $char_count -ge 800 ] && [ $char_count -le 975 ]; then
    echo "okay ✓"
    exit 0
elif [ $char_count -lt 800 ]; then
    echo "too short ⚠"
    exit 1
else
    echo "no no ✗"
    exit 1
fi