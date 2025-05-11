import os
import re
import requests
import subprocess
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# /developers/api/capture/interactive/geolocation/1/
# ---------- CONFIG ----------
base_url = 'https://www.loqate.com'
start_path = 'https://www.loqate.com/developers/api/capture'
# start_path = '/developers/getting-started/'
output_root = 'loqate_api_docs'  # folder to save markdown files
visited = set()
# ----------------------------

def slugify(text):
    return re.sub(r'[^a-zA-Z0-9_-]', '-', text.strip().lower())

def get_links(soup, base):
    links = set()
    for a in soup.find_all('a', href=True):
        href = a['href']
        full_url = urljoin(base, href)
        if full_url.startswith(base_url) and '/developers/api/capture/' in full_url:
            links.add(full_url.split('#')[0])  
    return links

def save_page_as_markdown(url):
    print(f"📄 Scraping: {url}")
    try:
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')
        main_content = soup.find('main') or soup.body
        if not main_content:
            print(f"⚠️ No main content found on: {url}")
            return

        # Build output path from URL
        parsed = urlparse(url)
        parts = [slugify(part) for part in parsed.path.strip('/').split('/')]
        if not parts:
            parts = ['index']
        filename = parts[-1] + '.md'
        dir_path = os.path.join(output_root, *parts[:-1])
        os.makedirs(dir_path, exist_ok=True)

        temp_path = os.path.join(dir_path, 'temp.html')
        output_path = os.path.join(dir_path, filename)

        # Save HTML to temp file
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(str(main_content))

        # Convert to markdown
        subprocess.run(['pandoc', temp_path, '-f', 'html', '-t', 'markdown', '-o', output_path])

        # Remove temp file
        os.remove(temp_path)

        print(f"✅ Saved: {output_path}")

    except Exception as e:
        print(f"❌ Failed to process {url}: {e}")

def crawl(url):
    if url in visited:
        return
    visited.add(url)

    print(f"🔗 Crawling: {url}")
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        save_page_as_markdown(url)

        for link in get_links(soup, url):
            crawl(link)

    except Exception as e:
        print(f"❌ Error crawling {url}: {e}")

if __name__ == '__main__':
    start_url = urljoin(base_url, start_path)
    crawl(start_url)
    print("🎉 Done scraping the docs.")