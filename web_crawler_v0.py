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
import concurrent.futures
import json

# Configuration
base_url = "https://support.loqate.com/"
max_depth = 3  # Limit crawl depth
delay = 0.5  # Delay between requests (seconds)
max_workers = 5  # Number of parallel workers
output_file = "crawled_pages.json"

# Track visited URLs and results
visited = set()
results = []

def is_valid_url(url):
    """Check if URL should be crawled"""
    parsed = urlparse(url)
    
    # Stay within the base domain
    if not parsed.netloc.endswith(urlparse(base_url).netloc):
        return False
    
    # Exclude non-HTML resources
    if any(ext in parsed.path.lower() for ext in ['.pdf', '.jpg', '.png', '.zip', '.exe', '.css', '.js']):
        return False
    
    return True

def crawl(url, depth=0):
    """Crawl with depth control and politeness delay"""
    if url in visited or not is_valid_url(url) or depth > max_depth:
        return []
    
    # Add to visited before making request to prevent concurrent duplicates
    visited.add(url)
    found_urls = []
    
    try:
        print(f"Crawling: {url} (depth: {depth})")
        time.sleep(delay)
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"Skipping {url} - Status code: {response.status_code}")
            return []
        
        # Log the crawled page
        page_info = {"url": url, "depth": depth, "status": response.status_code}
        results.append(page_info)
        
        # Parse HTML and extract links
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        
        for link in links:
            href = link['href']
            absolute_url = urljoin(url, href)
            # Clean URL fragments and query parameters
            absolute_url = absolute_url.split('#')[0].split('?')[0]
            
            if absolute_url not in visited and is_valid_url(absolute_url):
                found_urls.append((absolute_url, depth + 1))
                
    except Exception as e:
        print(f"Error crawling {url}: {e}")
    
    return found_urls

def main():
    start_time = time.time()
    to_crawl = [(base_url, 0)]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        while to_crawl:
            # Take a batch of URLs to process
            batch = to_crawl[:max_workers]
            to_crawl = to_crawl[max_workers:]
            
            # Submit crawl jobs
            future_to_url = {executor.submit(crawl, url, depth): (url, depth) for url, depth in batch}
            
            # Process results and add new URLs to crawl
            for future in concurrent.futures.as_completed(future_to_url):
                new_urls = future.result()
                # Add new URLs that aren't already visited
                to_crawl.extend([(url, depth) for url, depth in new_urls if url not in visited])
    
    # Save results to file
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nCrawling completed in {time.time() - start_time:.2f} seconds")
    print(f"Total documentation pages: {len(results)}")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()