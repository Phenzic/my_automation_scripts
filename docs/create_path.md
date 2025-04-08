# Create Path

This script automates the creation of directory structures and empty `.mdx` files based on paths defined in a `mint.json` file.

## How It Works

The Create Path script:

1. Extracts page paths from a `mint.json` configuration file using `jq`
2. For each path found, creates the required directory structure
3. Creates empty `.mdx` files at each path location if they don't already exist
4. Logs the created files to the console

### Key Components

- **Path Extraction**: Uses `jq` to parse the JSON and extract page paths
- **Directory Creation**: Creates necessary nested directories with `mkdir -p`
- **File Creation**: Creates empty files only if they don't already exist, preserving existing content

## How to Run

```bash
# Make the script executable
chmod +x create_path.sh

# Run the script
./create_path.sh
```

### Requirements

- `jq`: JSON processor (must be installed on the system)
- A valid `mint.json` file in the target directory

### Configuration

By default, the script looks for a `mint.json` file in the current directory (`.`). You can modify the `base_dir` variable to point to a different directory:

```bash
# Define the base directory where the mint.json file is located
base_dir="./your/custom/path"
```

## Use Cases

- Setting up a new Mintlify documentation structure
- Creating placeholder files based on a documentation plan
- Ensuring all pages defined in the navigation structure exist as actual files

### Expected mint.json Structure

The script expects `mint.json` to have a structure like:

```json
{
  "pages": [
    "page1",
    "section/page2",
    "section/subsection/page3"
  ],
  "navigation": [
    {
      "group": "Group Name",
      "pages": [
        "another-page",
        "yet-another-page"
      ]
    }
  ]
}
```

This would create:
- page1.mdx
- section/page2.mdx
- section/subsection/page3.mdx
- another-page.mdx
- yet-another-page.mdx 