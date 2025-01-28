#!/bin/bash

# Define the base directory where the documentation is located
base_dir="."

# Find and process all .mdx files in the directory
find "$base_dir" -type f -name "*.mdx" | while read -r file; do
    echo "Processing: $file"
    
    # Use sed to find and replace links in the specified format
    sed -i -E 's|/community/doc/([^/]+)/[^/]+|./\1|g' "$file"

    echo "Updated links in: $file"
done

echo "Link update process completed!" 