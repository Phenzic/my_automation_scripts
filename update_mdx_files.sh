#!/bin/bash

# Define the base directory where the .mdx files are located
base_dir="."

# Function to format the title
format_title() {
    echo "$1" | sed 's/-/ /g' | awk '{ for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2); }1'
}

# Find all .mdx files and update their content
find "$base_dir" -type f -name "*.mdx" | while read -r file; do
    # Extract the filename without the extension
    filename=$(basename "$file" .mdx)
    
    # Format the title
    formatted_title=$(format_title "$filename")

    # Create the new content
    new_content="---
title: '$formatted_title'
description: ''
---

"

    # Check if the file already has the prepend content
    if ! grep -qF "$new_content" "$file"; then
        # If the file is not empty, prepend the new content
        if [ -s "$file" ]; then
            echo -e "$new_content$(cat "$file")" > "$file"
        else
            # If the file is empty, just write the new content
            echo -e "$new_content" > "$file"
        fi
    fi
done