# scripts/rag.py

#!/usr/bin/env python3

"""
rag.py

Amaç:
- Prompt oluştur
- Groq ChatCompletion ile yanıt üret
"""

from groq import Groq

GROQ_API_KEY = "YOUR_API_KEY_HERE"
client = Groq(api_key=GROQ_API_KEY)

def generate_answer(context, question):
    """
    TODO:
    - ChatCompletion çağrısı yap
    - prompt tasarla
    """
    return "YANIT (örnek)"

def main():
    question = "Vadeli mevduat nedir?"
    context = "En yakın chunk buraya gelecek."

    answer = generate_answer(context, question)
    print("\nYanıt:")
    print(answer)

if __name__ == "__main__":
    main()
