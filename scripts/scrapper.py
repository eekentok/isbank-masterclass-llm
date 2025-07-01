# scripts/scraper.py

#!/usr/bin/env python3

"""
scraper.py

Amaç:
- Web scraping
- Sayfa başlığı, içerik ve URL'i almak
"""

import pandas as pd

def scrape_page(url):
    """
    TODO:
    - requests ile sayfayı çek
    - BeautifulSoup ile parse et
    - Başlık ve içerik çıkar
    """
    return {"url": url, "title": "Başlık", "content": "İçerik"}  # ÖRNEK

def main():
    urls = [
        "https://tr.wikipedia.org/wiki/Bankacılık",
        "https://tr.wikipedia.org/wiki/Mevduat"
    ]

    results = []
    for url in urls:
        result = scrape_page(url)
        if result:
            results.append(result)

    df = pd.DataFrame(results)
    df.to_csv('../input/scraped_data.csv', index=False)
    print("✅ Scraping tamamlandı.")

if __name__ == "__main__":
    main()
