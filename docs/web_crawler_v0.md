# Web Crawler v0

This script is a multi-threaded web crawler that systematically browses web pages and collects information about them.

## How It Works

Web Crawler v0 is a robust crawler that:

1. Starts from a base URL and crawls pages up to a specified depth
2. Uses multiple worker threads to crawl pages concurrently
3. Respects crawling etiquette with configurable delays between requests
4. Filters URLs to stay within specified domains
5. Avoids non-HTML resources (images, PDFs, etc.)
6. Tracks visited URLs to prevent duplicate visits
7. Saves crawl results to a JSON file

### Key Components

- **URL Validation**: The `is_valid_url()` function ensures crawling stays within specified domains and only targets HTML pages
- **Depth Control**: Crawling stops at a configurable maximum depth
- **Concurrency**: Uses ThreadPoolExecutor for parallel processing
- **Politeness**: Implements delays between requests to avoid overwhelming servers

## How to Run

```bash
python web_crawler_v0.py
```

### Configuration

You can modify these variables at the top of the script:

```python
# Configuration
base_url = "https://support.loqate.com/"
max_depth = 3  # Limit crawl depth
delay = 0.5  # Delay between requests (seconds)
max_workers = 5  # Number of parallel workers
output_file = "crawled_pages.json"
```

### Output Format

The script produces a JSON file with information about each crawled page:

```json
[
  {
    "url": "https://support.loqate.com/",
    "depth": 0,
    "status": 200
  },
  {
    "url": "https://support.loqate.com/about-us/",
    "depth": 1,
    "status": 200
  },
  ...
]
```

## Performance Considerations

- The script's performance depends on the number of workers (`max_workers`)
- Increasing workers improves throughput but may increase server load
- The `delay` parameter helps prevent overwhelming target servers 