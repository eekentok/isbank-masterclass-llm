# scripts/chunk.py

#!/usr/bin/env python3

"""
chunk.py

Amaç:
- Uzun metinleri belirli büyüklükte parçalara bölmek
"""

import pandas as pd

def chunk_text(text, size=100):
    """
    TODO:
    - text.split() ile kelimelere ayır
    - belirli büyüklükte parçala
    """
    return [text]  # Şu an parçalamıyor

def main():
    df = pd.read_csv('../output/cleaned_data.csv')
    records = []

    for idx, row in df.iterrows():
        chunks = chunk_text(row['cleaned_content'])
        for chunk in chunks:
            records.append({
                'url': row['url'],
                'title': row['title'],
                'chunk': chunk
            })

    out_df = pd.DataFrame(records)
    out_df.to_csv('../output/chunked_data.csv', index=False)
    print("✅ Chunk işlemi tamamlandı.")

if __name__ == "__main__":
    main()
