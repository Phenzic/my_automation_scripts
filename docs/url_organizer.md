# URL Organizer

This script organizes URLs from a JSON input file into a hierarchical directory structure.

## How It Works

The URL Organizer script works by:

1. Reading a JSON file containing URLs and associated metadata
2. Parsing each URL to extract the path components
3. Building a tree structure where each path component becomes a directory
4. Converting the tree structure back to JSON format with URLs organized by directory
5. Saving the organized structure to an output JSON file

### Key Functions

- `organize_urls_by_directory(input_file, output_file)`: Main function that processes the input file and generates the organized output
- `convert_tree_to_json(tree)`: Helper function that converts the internal tree structure to a clean JSON format

## How to Run

```bash
python url_organizer.py
```

### Input Format

The script expects a JSON file with an array of objects, where each object contains at least a "url" field:

```json
[
  {
    "url": "https://example.com/path/to/page",
    "title": "Example Page",
    ...
  },
  ...
]
```

### Output Format

The script produces a JSON file with URLs organized hierarchically by directory:

```json
[
  {
    "directory": "path",
    "urls": [],
    "subdirectories": [
      {
        "directory": "to",
        "urls": [],
        "subdirectories": [
          {
            "directory": "page",
            "urls": [
              {
                "url": "https://example.com/path/to/page",
                "title": "Example Page",
                ...
              }
            ],
            "subdirectories": []
          }
        ]
      }
    ]
  }
]
```

## Configuration

By default, the script uses:
- Input file: `/support.loqate.com.json`
- Output file: `organized_urls.json`

You can modify these paths directly in the script to process different files. 