#!/bin/bash

# Define the base directory where the mint.json file is located
base_dir="."

# Function to extract paths from mint.json
extract_paths() {
    # Use jq to extract all notable paths
    jq -r '.. | .pages? // empty | .[] | select(type == "string")' "$base_dir/mint.json"
}

# Create directories and files
extract_paths | while read -r path; do
    # Create the directory structure if it doesn't exist
    dir=$(dirname "$path")
    mkdir -p "$dir"

    # Create an empty .mdx file only if it does not exist
    mdx_file="$path.mdx"
    if [ ! -f "$mdx_file" ]; then
        touch "$mdx_file"
        echo "Created: $mdx_file"
    else
        echo "File already exists: $mdx_file"
    fi
done