#!/bin/bash

# Set the path to the directory containing the images
dir_path="/path/to/folder"

# Iterate over each file in the directory
for file in "$dir_path"/*; do
    # Check if the file is a regular file (not a directory or symlink)
    if [ -f "$file" ]; then
        # Call the python script with the file path as an argument
        python append-clip-interrogation.py --path "$file"
    fi
done
