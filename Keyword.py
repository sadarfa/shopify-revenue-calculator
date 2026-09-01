import pandas as pd
from pytrends.request import TrendReq

# Инициализация клиента PyTrends (язык английский, таймзона UTC)
pytrends = TrendReq(hl='en-US', tz=360)

# Наш стартовый список ключевых гипотез для проверки
keywords = [
    "Shopify revenue recovery calculator",
    "Best abandoned cart recovery for Shopify under $50",
    "Omnisend vs Klaviyo for Shopify",
    "Best automated recovery tool for small Shopify store",
]

# 1. Сбор данных интереса во времени (Interest Over Time)
pytrends.build_payload(
    kw_list=keywords[:4], timeframe='today 12-m', geo='US'  # Берем топ-4 для теста
)
df_interest = pytrends.interest_over_time()

if not df_interest.empty:
  df_interest = df_interest.drop(columns=['isPartial'])
  print('--- Динамика интереса (средний уровень за год) ---')
  print(df_interest.mean().sort_values(ascending=False))
  print('\n')

# 2. Сбор связанных запросов и подсказок (Related Queries)
print('--- Поиск связанных поисковых фраз (Related Queries) ---')
related_queries = pytrends.related_queries()

for kw in keywords[:2]:
  print(f'\nКлюч: {kw}')
  try:
    top_df = related_queries[kw]['top']
    if top_df is not None:
      print(top_df.head(5))
  except Exception as e:
    print('Данные ограничены или заблокированы Google (Rate Limit):', e)