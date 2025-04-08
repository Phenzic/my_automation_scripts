#!/usr/bin/env python3
import json
import os
from urllib.parse import urlparse

def organize_urls_by_directory(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Initialize a tree structure to organize URLs
    url_tree = {}
    
    # Process each URL entry
    for entry in data:
        url = entry["url"]
        # Parse the URL to get the path
        parsed_url = urlparse(url)
        path = parsed_url.path.strip('/')
        
        if not path:  # Root URL
            continue
        
        # Split the path into components
        path_components = path.split('/')
        
        # Navigate/build the tree
        current_level = url_tree
        for component in path_components:
            if component not in current_level:
                current_level[component] = {"_urls": [], "_children": {}}
            
            # Store the full entry at the appropriate level
            if path_components[-1] == component:  # If this is the final component
                current_level[component]["_urls"].append(entry)
            
            # Move deeper into the tree
            current_level = current_level[component]["_children"]
    
    # Convert the tree to a JSON structure for output
    organized_data = convert_tree_to_json(url_tree)
    
    # Write the organized data to the output file
    with open(output_file, 'w') as f:
        json.dump(organized_data, f, indent=2)
    
    print(f"Organized URLs saved to {output_file}")

def convert_tree_to_json(tree):
    """Convert the internal tree structure to a clean JSON format"""
    result = []
    
    # Process each directory in the current level
    for directory, content in tree.items():
        dir_entry = {
            "directory": directory,
            "urls": content["_urls"],
            "subdirectories": convert_tree_to_json(content["_children"])
        }
        result.append(dir_entry)
    
    # Sort directories alphabetically
    result.sort(key=lambda x: x["directory"])
    
    return result

if __name__ == "__main__":
    input_file = "/support.loqate.com.json"
    output_file = "organized_urls.json"
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
    else:
        organize_urls_by_directory(input_file, output_file) 