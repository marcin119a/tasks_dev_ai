import requests
from bs4 import BeautifulSoup
import json
import csv
import time

BASE_LIST_URL = "https://adresowo.pl/mieszkania/warszawa/_l{}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Step 1: Gather offer URLs
offer_urls = []
for page in range(1, 12):  # You can increase this range if needed
    url = BASE_LIST_URL.format(page)
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    items = soup.select('section.search-results__item')
    for item in items:
        data_url = item.get('data-url')
        if data_url:
            offer_urls.append(f'https://adresowo.pl{data_url}')
    # time.sleep(1)  # Optional: Be nice to the server

# Remove duplicates
offer_urls = list(dict.fromkeys(offer_urls))
print(f"🔍 Found {len(offer_urls)} unique offer URLs")

# Step 2: Scrape offer details
results = []
for url in offer_urls:
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    price = currency = url_offer = address = description = None
    num_images = None

    # JSON-LD data
    for script in soup.select('script[type="application/ld+json"]'):
        try:
            data = json.loads(script.string)
        except Exception:
            continue
        if isinstance(data, dict) and data.get('@type') == 'Offer':
            price = data.get('price')
            currency = data.get('priceCurrency')
            url_offer = data.get('url', url)

        graph = data.get('@graph') if isinstance(data, dict) else None
        if graph:
            for node in graph:
                if node.get('@type') == 'Place':
                    address = node.get('address', {}).get('streetAddress')
                    description = node.get('description')
                    break

    # Image count from inline JS
    js_text = soup.find(string=lambda t: t and 're.numberOfImages' in t)
    if js_text:
        try:
            num_images = int(js_text.split('=')[1].split(';')[0].strip())
        except Exception:
            num_images = None

    results.append({
        'offer_url': url_offer or url,
        'price': price,
        'currency': currency,
        'num_images': num_images,
        'street_address': address,
        'description': description
    })
    print(f"Scraped {url}")
    # time.sleep(1)  # Optional delay

# Step 3: Save to CSV
output_file = "adresowo_offers_detail.csv"
if results:
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"Data saved to {output_file}")
else:
    print("No results to save.")