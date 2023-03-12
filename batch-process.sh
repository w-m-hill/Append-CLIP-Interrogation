#!/bin/bash

# Accept an argument for the path to the directory containing the images
dir_path=$1

# Iterate over each file in the directory
for file in "$dir_path"/*; do
    # Check if the file is a regular file (not a directory or symlink)
    if [ -f "$file" ]; then
        # Check if the file is an image with a .png, .jpg, or .jpeg extension
        if [[ "$file" == *.png ]] || [[ "$file" == *.jpg ]] || [[ "$file" == *.jpeg ]]; then
            # Call the python script with the file path as an argument
            python append-clip-interrogation.py --path "$file"
        fi
    fi
done
