#!/bin/bash
# organizer.sh - A simple script to organize files in a directory based on their extensions.

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
SOURCE_FILE="grades.csv"

# Archive directory check and creation
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "$(date): Created archive directory '$ARCHIVE_DIR'." >> "$LOG_FILE"
fi

# Timestamp generation
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
NEW_FILE_NAME="grades_$TIMESTAMP.csv"