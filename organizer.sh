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

# Rename and move the source file to the archive directory
if [ -f "$SOURCE_FILE" ]; then
    mv "$SOURCE_FILE" "$ARCHIVE_DIR/$NEW_FILE_NAME"
    echo "$(date): Moved '$SOURCE_FILE' to '$ARCHIVE_DIR/$NEW_FILE_NAME'." >> "$LOG_FILE"
else
    echo "$(date): Source file '$SOURCE_FILE' not found." >> "$LOG_FILE"
fi

# Reset the workspace with a new empty grades.csv file
touch "$SOURCE_FILE"
echo "$(date): Created new empty '$SOURCE_FILE'." >> "$LOG_FILE"