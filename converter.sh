#!/bin/bash

INPUT_FILE="report.pdf"
OUTPUT_FILE="data.txt"

if [ ! -f "$INPUT_FILE" ]; then
    echo "❌ Error: $INPUT_FILE not found."
    exit 1
fi

pdftotext "$INPUT_FILE" "$OUTPUT_FILE"

echo "✅ Converted $INPUT_FILE to $OUTPUT_FILE"

