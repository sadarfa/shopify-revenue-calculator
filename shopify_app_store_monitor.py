"""
Мониторинг конкурентов в нише "Abandoned Cart Recovery" через Shopify App Store.

Собирает по списку app-хендлов (slug из URL приложения):
- название
- рейтинг
- количество отзывов
- стартовую цену (если удаётся распарсить)

Использование:
    python3 shopify_app_store_monitor.py

Требования:
    pip install requests beautifulsoup4 --break-system-packages
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# Список приложений для отслеживания — slug берётся из URL вида
# https://apps.shopify.com/<slug>
APP_SLUGS = [
    "klaviyo-email-marketing",
    "omnisend-email-marketing-sms",
    "shopify-email",
    "recart",
    "retainful",
    "cartly-abandoned-cart-recovery",  # slug может отличаться — проверьте реальный URL
]

DELAY_BETWEEN_REQUESTS = 2.0
OUTPUT_CSV = "shopify_competitors.csv"


def fetch_app_data(slug: str) -> dict:
    """
    Загружает страницу приложения и извлекает название, рейтинг, число отзывов и цену.
    Возвращает словарь с данными (поля могут быть None, если не удалось распарсить).
    """
    url = f"https://apps.shopify.com/{slug}"
    result = {
        "slug": slug,
        "url": url,
        "name": None,
        "rating": None,
        "reviews_count": None,
        "starting_price": None,
        "error": None,
    }

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except requests.RequestException as e:
        result["error"] = str(e)
        return result

    soup = BeautifulSoup(resp.text, "html.parser")

    # Название приложения
    title_tag = soup.find("h1")
    if title_tag:
        result["name"] = title_tag.get_text(strip=True)

    # Рейтинг и количество отзывов часто лежат в тексте вида "4.7 (300 reviews)"
    # Ищем по регулярке во всём тексте страницы, т.к. вёрстка App Store может меняться
    page_text = soup.get_text(" ", strip=True)

    rating_match = re.search(r"(\d\.\d)\s*(?:out of 5|★|stars)?\s*\(?([\d,]+)\s*review", page_text, re.IGNORECASE)
    if rating_match:
        result["rating"] = rating_match.group(1)
        result["reviews_count"] = rating_match.group(2).replace(",", "")

    # Цена — ищем первое упоминание "$X/month" или "Free"
    price_match = re.search(r"(Free plan|Free to install|\$\d+(?:\.\d{2})?\s*/?\s*month)", page_text, re.IGNORECASE)
    if price_match:
        result["starting_price"] = price_match.group(1)

    return result


def main():
    print("--- Мониторинг конкурентов Shopify App Store ---\n")

    all_results = []

    for slug in APP_SLUGS:
        print(f"Загружаю: {slug} ...")
        data = fetch_app_data(slug)
        all_results.append(data)

        if data["error"]:
            print(f"  Ошибка: {data['error']}")
        else:
            print(f"  Название: {data['name']}")
            print(f"  Рейтинг: {data['rating']} | Отзывов: {data['reviews_count']}")
            print(f"  Цена от: {data['starting_price']}")
        print()

        time.sleep(DELAY_BETWEEN_REQUESTS)

    # Сохраняем в CSV для дальнейшего анализа в Excel/Sheets
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["slug", "url", "name", "rating", "reviews_count", "starting_price", "error"])
        writer.writeheader()
        writer.writerows(all_results)

    print(f"Готово. Результаты сохранены в {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
