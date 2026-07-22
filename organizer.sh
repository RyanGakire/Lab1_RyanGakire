#!/bin/bash
# organizer.sh - A simple script to organize files in a directory based on their extensions.

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
SOURCE_FILE="grades.csv"

# 1. Ensure the archive directory exists
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "$(date): Created archive directory '$ARCHIVE_DIR'." >> "$LOG_FILE"
fi