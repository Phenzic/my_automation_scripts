# Web Crawler v1

This script is a single-threaded web crawler that systematically browses web pages with a recursive approach.

## How It Works

Web Crawler v1 is a straightforward crawler that:

1. Starts from specified base URLs and crawls pages up to a specified depth
2. Uses a recursive approach for depth-first crawling
3. Respects crawling etiquette with configurable delays between requests
4. Filters URLs to stay within allowed domains
5. Avoids non-HTML resources (images, PDFs, etc.)
6. Tracks visited URLs to prevent duplicate visits
7. Prints the list of found pages to the console

### Key Components

- **URL Validation**: The `is_valid_url()` function ensures crawling stays within allowed domains and only targets HTML pages
- **Depth Control**: Crawling stops at a configurable maximum depth
- **Session Management**: Uses a single requests session for efficiency
- **Politeness**: Implements delays between requests to avoid overwhelming servers

## How to Run

```bash
python web_crawler_v1.py
```

### Configuration

You can modify these variables at the top of the script:

```python
base_urls = [
    # "https://www.loqate.com/developers/",
    "https://support.loqate.com/"
]
allowed_domains = ['support.loqate.com']
```

And within the `crawl()` function:

```python
crawl(url, max_depth=2, delay=1.0)
```

### Output Format

The script prints the list of crawled URLs to the console:

```
Starting crawl...
Crawling: https://support.loqate.com/
Crawling: https://support.loqate.com/about-us/
...

Documentation pages found:
1. https://support.loqate.com/
2. https://support.loqate.com/about-us/
...

Total documentation pages: 42
```

## Differences from v0

Compared to Web Crawler v0, this version:

- Uses a recursive approach instead of a thread pool
- Is single-threaded (simpler but potentially slower)
- Doesn't save results to a file
- Prints results to the console
- Has a simpler implementation but less control over the crawling process 