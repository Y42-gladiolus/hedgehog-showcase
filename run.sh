#!/bin/bash
# Hedgehog Showcase — Quick Start

echo "🦔 Hedgehog Core — Verification Demo"
echo "===================================="
echo

# Check if binaries exist
if [ ! -d "bin" ]; then
    echo "❌ Error: bin/ directory not found"
    exit 1
fi

echo "Available implementations:"
ls -1 bin/hedgehog-* | xargs -n1 basename
echo

# Run all implementations
echo "Running all implementations..."
echo

for binary in bin/hedgehog-*; do
    echo "[$(basename $binary)]"
    $binary 2>&1 | head -3
    echo
done

echo "✅ All implementations completed"
echo
echo "To configure: edit rules.json"
echo "To view dashboard: open index.html in browser"
