import json
import requests


def get_google_suggest(query):
  url = f'https://suggestqueries.google.com/complete/search?client=firefox&q={query}'
  try:
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      return data[1]  # Список подсказок
  except Exception as e:
    print(f'Ошибка запроса для {query}: {e}')
  return []


seed_keywords = [
    'Shopify revenue recovery',
    'abandoned cart recovery Shopify',
    'Omnisend alternative Shopify',
    'Shopify cart recovery under 50',
]

print('--- Поисковые подсказки Google (Autocomplete) ---')
for seed in seed_keywords:
  suggestions = get_google_suggest(seed)
  print(f'\nБазовый запрос: "{seed}"')
  for item in suggestions:
    print(f'  -> {item}')