# import scrapy 
# from scrapy.crawler import CrawlerProcess 

# class DocSpider(scrapy.Spider):
#     name = "doc_spider"
#     start_urls = ["https://www.loqate.com/developers"]
#     custom_settings = {"DEPTH_LIMIT": 10}  # Prevent infinite crawling

#     def parse(self, response):
#         yield {"url": response.url}
#         for link in response.css('a::attr(href)').getall():
#             if link.startswith("/docs"):
#                 yield response.follow(link, self.parse)

# process = CrawlerProcess(settings={"FEEDS": {"urls.json": {"format": "json"}}})
# process.crawl(DocSpider)
# process.start()

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import re

visited = set()
base_urls = [
    # "https://www.loqate.com/developers/",
    "https://support.loqate.com/"
]
allowed_domains = ['support.loqate.com']

# Configure requests session
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})

def is_valid_url(url):
    """Check if URL should be crawled"""
    parsed = urlparse(url)
    
    # Check domain
    if not any(parsed.netloc.endswith(domain) for domain in allowed_domains):
        return False
    
    # Exclude non-HTML resources
    if any(ext in parsed.path.lower() for ext in ['.pdf', '.jpg', '.png', '.zip', '.exe', '.css', '.js']):
        return False
    
    # Accept all paths on allowed domains
    return True

def crawl(url, max_depth=2, delay=1.0):
    """Crawl with depth control and politeness delay"""
    if url in visited or not is_valid_url(url):
        return
    
    try:
        print(f"Crawling: {url}")  # Debug output
        time.sleep(delay)
        response = session.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"Skipping {url} - Status code: {response.status_code}")
            return
            
        content_type = response.headers.get('content-type', '')
        if 'text/html' not in content_type:
            print(f"Skipping {url} - Non-HTML content: {content_type}")
            return
            
        visited.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links but skip navigation menus if possible
        links = soup.find_all('a', href=True)
        
        for link in links:
            href = link['href']
            absolute_url = urljoin(url, href)
            absolute_url = absolute_url.split('#')[0].split('?')[0]  # Clean URL
            
            if (is_valid_url(absolute_url) and 
                absolute_url not in visited and 
                max_depth > 0):
                crawl(absolute_url, max_depth-1, delay)
                
    except Exception as e:
        print(f"Error crawling {url}: {e}")

print("Starting crawl...")
for url in base_urls:
    crawl(url, max_depth=2)

# Filter and sort results
doc_pages = sorted(visited)

print("\nDocumentation pages found:")
for i, page in enumerate(doc_pages, 1):
    print(f"{i}. {page}")

print(f"\nTotal documentation pages: {len(doc_pages)}")