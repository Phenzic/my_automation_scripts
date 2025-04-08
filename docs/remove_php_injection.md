# Remove PHP Injection

This script cleans up HTML content within SQL files by converting HTML to Markdown format.

## How It Works

The Remove PHP Injection script:

1. Reads an SQL file that contains HTML content (often found in database dumps)
2. Identifies HTML content within the SQL file using regular expressions
3. Converts the HTML to cleaner Markdown format
4. Replaces the original HTML with the converted Markdown
5. Saves the cleaned SQL content to a new file

### Key Functions

- `html_to_markdown(html_content)`: Converts HTML to Markdown using regex replacements
- `process_sql_file(input_file, output_file)`: Processes an SQL file and saves the cleaned version

## How to Run

```bash
python remove_php_injection.py
```

### Configuration

You need to specify the input and output file paths in the script:

```python
# Specify the input and output file paths
input_file = '/path/to/your/input.sql'  # Replace with your input SQL file path
output_file = './output_cleaned.sql'  # Replace with your desired output SQL file path
```

## HTML to Markdown Conversions

The script performs the following conversions:

| HTML | Markdown |
|------|----------|
| `<strong>text</strong>` or `<b>text</b>` | `**text**` |
| `<em>text</em>` or `<i>text</i>` | `*text*` |
| `<br/>` or `<br>` | Newline |
| `<p>text</p>` | `text` followed by two newlines |
| Other HTML tags | Removed |

## Use Cases

- Cleaning up database dumps before importing into a new system
- Migrating content from HTML to Markdown format
- Removing potentially harmful PHP code injections from SQL files 