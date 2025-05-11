import os
import re

from pathlib import Path

def clean_markdown(content: str) -> str:
    # Remove curly braces and their contents
    content = re.sub(r'\{[^}]*\}', '', content)

    # Remove all lines with only colons (e.g., "::::", ":::", etc.)
    content = re.sub(r'^\s*:+\s*$', '', content, flags=re.MULTILINE)

    # Remove '[Back to top](#)' and other links with just `#`
    content = re.sub(r'\[.*?\]\(#\)', '', content)

    # Remove trailing double newlines caused by removals
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


def process_directory(input_dir: str, output_dir: str):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for file in input_path.rglob('*'):
        if file.is_file() and file.suffix in ['.md', '.mdx']:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

            cleaned = clean_markdown(content)

            # Determine new file path
            relative_path = file.relative_to(input_path)
            new_file_path = output_path / relative_path
            new_file_path = new_file_path.with_suffix('.mdx')

            # Ensure parent directory exists
            new_file_path.parent.mkdir(parents=True, exist_ok=True)

            # Write cleaned content
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned)

            print(f'✅ Processed: {relative_path} -> {new_file_path.relative_to(output_path)}')


# Example usage
input_directory = 'path/to/your/input/markdowns'
output_directory = 'path/to/cleaned/output'

process_directory(input_directory, output_directory)