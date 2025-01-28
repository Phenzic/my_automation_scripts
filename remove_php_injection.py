import re

def html_to_markdown(html_content):
    # Replace <strong> and <b> tags with Markdown bold
    html_content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', html_content)
    html_content = re.sub(r'<b>(.*?)</b>', r'**\1**', html_content)

    # Replace <em> and <i> tags with Markdown italic
    html_content = re.sub(r'<em>(.*?)</em>', r'*\1*', html_content)
    html_content = re.sub(r'<i>(.*?)</i>', r'*\1*', html_content)

    # Replace <br/> and <br> tags with Markdown newline
    html_content = re.sub(r'<br\s*/?>', '\n', html_content)

    # Replace <p> tags with Markdown newline
    html_content = re.sub(r'<p>(.*?)</p>', r'\1\n\n', html_content)

    # Remove all other HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Remove extra newlines and spaces
    html_content = re.sub(r'\n\s*\n', '\n\n', html_content).strip()

    return html_content

def process_sql_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        sql_content = file.read()

    # Find all content within the HTML tags in the SQL file
    html_matches = re.findall(r"'(<.*?>.*?)'", sql_content, re.DOTALL)

    for html_content in html_matches:
        # Convert HTML to Markdown
        markdown_content = html_to_markdown(html_content)
        # Replace the original HTML content with the cleaned Markdown content
        sql_content = sql_content.replace(f"'{html_content}'", f"'{markdown_content}'")

    # Write the cleaned SQL content to a new file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(sql_content)

# Specify the input and output file paths
input_file = '/Users/home/Downloads/Doujins_DB/ljb_posts_20250126.sql'  # Replace with your input SQL file path
output_file = './ljb_posts_20250126_cleaned.sql'  # Replace with your desired output SQL file path

# Process the SQL file
process_sql_file(input_file, output_file)

print(f"Processed SQL file saved to {output_file}")