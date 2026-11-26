import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# Словарь для перевода рейтинга в число
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

all_books = []

print("Начинаю сбор данных с books.toscrape.com...\n")

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    print(f"Страница {page}/50...")
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Больше страниц нет.")
        break
    
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.find("h3").find("a")["title"]
        
        price_text = book.find("p", class_="price_color").text.strip()
        price = float(price_text.replace("£", "").replace("Â", ""))
        
        rating_word = book.find("p", class_="star-rating")["class"][1]
        rating = RATING_MAP.get(rating_word, 0)
        
        availability = book.find("p", class_="instock availability").text.strip()
        
        all_books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })
    
    time.sleep(0.3)

# Создаём DataFrame
df = pd.DataFrame(all_books)

print(f"\nСобрано книг: {len(df)}")
print("\nПример данных:")
print(df.head())

# Сохраняем в Excel
df.to_excel("books.xlsx", index=False)
print("\nФайл books.xlsx сохранён успешно!")