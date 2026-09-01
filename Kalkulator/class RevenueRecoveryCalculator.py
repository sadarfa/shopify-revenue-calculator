class ToolFinderEngine:
  """Подбирает оптимальный SaaS-инструмент для восстановления выручки

  на основе бюджета, объема заказов и потребностей магазина.
  """

  def recommend_stack(
      self,
      monthly_budget_eur: float,
      monthly_orders: int,
      needs_ai_chat: bool = False,
  ):
    recommendations = []

    if needs_ai_chat:
      recommendations.append({
          "tool": "Tidio",
          "tier": "Starter / Growth",
          "fit": "Высокое соответствие",
          "reason": (
              "Сочетает AI-поддержку клиентов, живой чат и автоматизацию брошенных"
              " корзин."
          ),
          "affiliate_link": (
              "https://www.tidio.com/?aff_id=our_tracker"  # Заглушка для реферальной ссылки
          ),
      })

    if monthly_budget_eur < 40 and monthly_orders < 500:
      recommendations.append({
          "tool": "Omnisend",
          "tier": "Standard (€16/мес)",
          "fit": "Лучшая цена/качество",
          "reason": (
              "Email + SMS автоматизация с высокой окупаемостью для небольших"
              " магазинов (до 500 заказов)."
          ),
          "affiliate_link": "https://www.omnisend.com/?aff_id=our_tracker",
      })
      recommendations.append({
          "tool": "Retainful",
          "tier": "Free / Starter",
          "fit": "Бюджетная альтернатива",
          "reason": (
              "Отличные динамические купоны и возврат корзин для микро-магазинов"
              " на старте."
          ),
          "affiliate_link": "https://www.retainful.com/?aff_id=our_tracker",
      })
    else:
      recommendations.append({
          "tool": "Klaviyo",
          "tier": "Growth Tier",
          "fit": "Масштаб Enterprise",
          "reason": (
              "Продвинутая сегментация и предиктивная аналитика для больших"
              " объемов."
          ),
          "affiliate_link": "https://www.klaviyo.com/?aff_id=our_tracker",
      })
      recommendations.append({
          "tool": "Omnisend",
          "tier": "Pro Tier",
          "fit": "Альтернативный выбор",
          "reason": (
              "Мощный мультиканальный функционал без сложного обучения и высоких"
              " тарифов Klaviyo."
          ),
          "affiliate_link": "https://www.omnisend.com/?aff_id=our_tracker",
      })

    return recommendations


# Тест подбора для магазина с бюджетом €30 и 140 заказами
finder = ToolFinderEngine()
stack = finder.recommend_stack(monthly_budget_eur=30, monthly_orders=140)

for rec in stack:
  print(
      f"[{rec['fit']}] {rec['tool']} ({rec['tier']}) -> Причина:"
      f" {rec['reason']} | Ссылка: {rec['affiliate_link']}"
  )