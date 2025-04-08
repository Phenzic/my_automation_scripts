# Update MDX Files

This script adds frontmatter to all `.mdx` files in a directory tree, automatically generating a title from the filename.

## How It Works

The Update MDX Files script:

1. Finds all `.mdx` files in the current directory and its subdirectories using the `find` command
2. For each file, extracts the filename without the extension
3. Formats the filename into a title by replacing hyphens with spaces and capitalizing first letters of words
4. Adds frontmatter to the beginning of each file with the formatted title
5. Preserves existing content after the frontmatter

### Key Components

- **File Finding**: Uses the `find` command to locate all `.mdx` files recursively
- **Title Formatting**: Uses `sed` and `awk` to format filenames into proper titles
- **Content Preservation**: Checks for existing frontmatter to avoid duplication

## How to Run

```bash
# Make the script executable
chmod +x update_mdx_files.sh

# Run the script
./update_mdx_files.sh
```

### Configuration

By default, the script searches for `.mdx` files in the current directory (`.`). You can modify the `base_dir` variable to point to a different directory:

```bash
# Define the base directory where the .mdx files are located
base_dir="./your/custom/path"
```

### Generated Frontmatter

The script adds the following frontmatter to each file:

```yaml
---
title: 'Formatted Title'
description: ''
---

```

## Examples

| Filename | Generated Title |
|----------|----------------|
| hello-world.mdx | Hello World |
| api-reference.mdx | Api Reference |
| getting-started.mdx | Getting Started |

## Use Cases

- Preparing MDX files for Mintlify documentation
- Automating frontmatter generation
- Ensuring consistency across documentation files 