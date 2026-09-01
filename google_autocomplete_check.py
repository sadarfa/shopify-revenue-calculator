"""
Проверка Google Autocomplete подсказок по списку поисковых фраз.
Выводит только те запросы, по которым Google вернул непустой список подсказок.
"""

import requests
import time
import json

# ---------- Настройки ----------

BASE_URL = "http://suggestqueries.google.com/complete/search"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# Список запросов для проверки — можно менять/дополнять
QUERIES = [
    "Shopify revenue recovery",
    "abandoned cart recovery Shopify",
    "Omnisend alternative Shopify",
    "Shopify cart recovery under 50",
    "cheap abandoned cart recovery shopify",
    "free abandoned cart recovery shopify",
    "alternatives to omnisend",
    "omnisend alternatives",
    "shopify cart abandonment app",
    "best cart recovery app shopify",
]

# Задержка между запросами, чтобы не словить блокировку от Google (в секундах)
DELAY_BETWEEN_REQUESTS = 1.0

# Локаль и регион (можно менять под нужный рынок)
PARAMS_BASE = {
    "client": "chrome",   # формат ответа, похожий на JSON
    "hl": "en",           # язык подсказок
    "gl": "us",           # регион
}


def get_autocomplete_suggestions(query: str) -> list:
    """
    Делает запрос к Google Autocomplete и возвращает список подсказок.
    Возвращает пустой список, если подсказок нет или произошла ошибка.
    """
    params = dict(PARAMS_BASE)
    params["q"] = query

    try:
        response = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=10)
        response.raise_for_status()

        # Google возвращает не совсем валидный JSON (иногда с BOM/доп. символами),
        # поэтому аккуратно парсим текст
        data = json.loads(response.text)
        suggestions = data[1] if len(data) > 1 else []
        return suggestions

    except (requests.RequestException, json.JSONDecodeError, IndexError) as e:
        print(f"[Ошибка] Запрос '{query}': {e}")
        return []


def main():
    print("--- Поисковые подсказки Google (Autocomplete) ---\n")

    results = {}

    for query in QUERIES:
        suggestions = get_autocomplete_suggestions(query)
        results[query] = suggestions

        print(f"Базовый запрос: \"{query}\"")
        if suggestions:
            for s in suggestions:
                print(f"  -> {s}")
        else:
            print("  (подсказок нет)")
        print()

        time.sleep(DELAY_BETWEEN_REQUESTS)

    # Итоговая сводка: только запросы с непустыми результатами
    print("\n--- Сводка: запросы с непустыми подсказками ---\n")
    non_empty = {q: s for q, s in results.items() if s}

    if non_empty:
        for query, suggestions in non_empty.items():
            print(f"{query} ({len(suggestions)} подсказок)")
    else:
        print("Ни один запрос не дал подсказок.")

    return results


if __name__ == "__main__":
    main()
