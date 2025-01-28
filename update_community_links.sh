#!/bin/bash

# Define the base directory
base_dir="."

# Find all .mdx files and process them
find "$base_dir" -type f -name "*.mdx" | while read -r file; do
    echo "Processing: $file"
    
    # Replace absolute paths with relative ones (adding ./ if missing)
    sed -i.bak -E '
        # First replace community doc links
        s|/community/doc/([^/]+)/doc[A-Za-z0-9]+|./\1|g
        # Then ensure all internal links start with ./
        s|"(/[^"]*)"|\"\./\1\"|g
        s|"\.//"|\"\./|g
        # Clean up any double slashes that might have been created
        s|\.//|\./|g
    ' "$file"
    
    # Remove the backup files created by sed
    rm "${file}.bak"
    
    echo "Completed processing: $file"
done

echo "All files have been processed!"