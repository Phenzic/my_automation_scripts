#!/bin/bash

# Define the base directory where the .mdx files are located
base_dir="."

# Find all .mdx files and clear their content
find "$base_dir" -type f -name "*.mdx" | while read -r file; do
    # Clear the content of the file
    > "$file"
done 
