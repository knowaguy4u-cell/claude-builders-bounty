#!/bin/bash

# Create a CHANGELOG.md file if it doesn't exist
mkdir -p changelog && touch changelog/CHANGELOG.md

# Initialize the CHANGELOG.md file with a header
cat << 'EOF' > changelog/CHANGELOG.md
# CHANGELOG.md

## Changes

