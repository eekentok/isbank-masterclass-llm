# scripts/clean.py

#!/usr/bin/env python3

"""
clean.py

Amaç:
- HTML ve gereksiz karakterleri temizle
- Lower-case
"""

import pandas as pd

def clean_text(text):
    """
    TODO:
    - lower-case yap
    - Gereksiz boşlukları sil
    - Noktalama kaldır (isteğe bağlı)
    """
    return text  # Şu anda değiştirmiyor

def main():
    df = pd.read_csv('../input/scraped_data.csv')
    df['cleaned_content'] = df['content'].apply(clean_text)
    df.to_csv('../output/cleaned_data.csv', index=False)
    print("✅ Temizleme tamamlandı.")

if __name__ == "__main__":
    main()
