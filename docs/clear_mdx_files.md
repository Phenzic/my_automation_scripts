# Clear MDX Files

This script clears the content of all `.mdx` files in a directory tree.

## How It Works

The Clear MDX Files script:

1. Finds all `.mdx` files in the current directory and its subdirectories using the `find` command
2. For each found file, it clears/empties the content of the file
3. It preserves the files themselves, just removes their content

### Key Components

- **File Finding**: Uses the `find` command to locate all `.mdx` files recursively
- **Content Clearing**: Uses the bash redirection operator `>` to clear each file's content

## How to Run

```bash
# Make the script executable
chmod +x clear_mdx_files.sh

# Run the script
./clear_mdx_files.sh
```

### Configuration

By default, the script searches for `.mdx` files in the current directory (`.`). You can modify the `base_dir` variable to point to a different directory:

```bash
# Define the base directory where the .mdx files are located
base_dir="./your/custom/path"
```

## Use Cases

- Preparing for a fresh content import
- Cleaning up test content
- Resetting a documentation site structure while preserving file layout

## Warning

This script permanently deletes the content of all `.mdx` files it finds. Make sure you have backups of any important content before running it. 