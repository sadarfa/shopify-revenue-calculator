with nav_tab3:
  st.header("E-Commerce Growth & Recovery Guides")
  st.write(
      "Explore our expert articles designed to help Shopify merchants"
      " maximize revenue and optimize customer lifecycle value."
  )

  st.markdown("---")

  # Выбор статьи для чтения
  article_choice = st.selectbox(
      "Select a Guide to Read:",
      [
          (
              "1. Best Abandoned Cart Recovery for Shopify Under $50/Month"
              " (Recommended)"
          ),
          (
              "2. Omnisend vs Klaviyo: Which Is Better for Small Shopify Stores"
              " in 2026?"
          ),
          "3. Shopify Native Features vs. Third-Party Recovery Apps",
          "4. Maximizing Customer Lifetime Value (LTV)",
      ],
      key="guide_select",
  )

  if "Under $50" in article_choice:
    st.markdown(
        "## Best Abandoned Cart Recovery for Shopify Under $50/Month (2026"
        " Guide)"
    )
    st.markdown("*Published by Growth & Recovery Lab | Reading time: 4 mins*")

    st.markdown("""
        ### Введение
        Большинство SEO-гайдов советуют инструменты за $150–$300 в месяц. Если небольшой Shopify-магазин делает €5k–€10k оборота, отдавать такие деньги за автоматизацию корзин — прямой путь в минус. Разбираем платформы, которые реально укладываются в бюджет до $50/мес и окупаются с первых же двух-трех возвращенных заказов.

        ### Ловушка Enterprise-платформ для малого бизнеса
        Коротко объясняем, почему раскрученные экосистемы навязывают скрытые переплаты за профили и тяжелую аналитику, которая нужна только брендам с оборотом от €100k. Задаем критерии отбора: предсказуемая фиксированная цена, готовые шаблоны под Shopify и быстрый старт без разработчиков.  

        ### Топ доступных решений до $50/месяц  
        
        #### 1. Omnisend (Standard Plan) — старт от $16/мес
        * **Почему подходит:** Идеальный баланс: полноценные автоматические цепочки брошенных корзин (Abandoned Cart & Checkout), встроенный мультиканальный функционал (Email + SMS) и щедрый бесплатный тариф на старте. *(Здесь вшита наша партнёрская ссылка с 20% рекуррентной комиссией).*
        
        #### 2. Альтернативы с фиксированной ценой (например, нишевые плагины уровня Retainful)
        * **Почему подходит:** Для тех, кому нужен только базовый email-возврат без лишних переплат.
        
        #### 3. Встроенный функционал Shopify
        * **Почему подходит:** Честный разбор плюсов и минусов штатных напоминаний движка (почему их не хватает для долгосрочного роста из-за отсутствия гибкой сегментации).

        ---
        ### Сравнительная таблица
        | Инструмент | Цена за старт | Брошенная корзина / Чекаут | Наличие бесплатного плана |
        | :--- | :--- | :--- | :--- |
        | **Omnisend** | $16 / мес | Полная автоматизация | Да (до 250 контактов) |
        | **Retainful / Аналоги** | $9–$19 / мес | Базовая | Ограниченно |
        | **Shopify Built-in** | Бесплатно | Только базовый Email | Встроено в движок |

        ---
        ### Призыв к действию (CTA)
        «Не уверен, какой инструмент выгоднее именно под твой текущий трафик? Посчитай точный объём упущенной выручки в нашем **[Shopify Revenue Recovery Calculator](#)** (Tab 1), чтобы подобрать стек под свой бюджет».
        """)

  elif "Omnisend vs Klaviyo" in article_choice:
    st.markdown(
        "## Omnisend vs Klaviyo: Which Is Better for Small Shopify Stores in"
        " 2026?"
    )
    st.markdown("*Published by Growth & Recovery Lab | Reading time: 6 mins*")

    st.markdown("""
        ### Введение
        Klaviyo — признанный тяжеловес e-commerce, а Omnisend — главный выбор для быстрого запуска с фокусом на омниканальность. Но кто из них объективно выгоднее для небольшого интернет-магазина, где каждая сотня евро на счету? Разбираем без маркетинговой шелухи.

        ### Ценообразование и пороги: где скрыт подвох
        * **Klaviyo:** тарификация идет по активным профилям (общей базе подписчиков). По мере роста базы ценник резко скачивается ступеньками ($20 за 500 контактов превращаются в тяжелые чеки на больших объемах), а SMS оплачивается отдельно через кредитные пакеты.  
        * **Omnisend:** более мягкая шкала масштабирования. План Standard начинается с $16/мес, а тариф Pro ($59/мес) сразу объединяет безлимитный email и встроенный пакет SMS-кредитов. Для небольшого бренда это прогнозируемая экономия бюджета.  

        ### Функционал автоматизации брошенных корзин
        Сравнение готовых workflow (Abandoned Cart, Browse Abandonment, Checkout Recovery). У обоих отличная глубокая интеграция с Shopify, но у Omnisend готовые сценарии собираются за 15 минут «из коробки», тогда как под Klaviyo часто приходится настраивать кастомные события и копаться в глубокой аналитике, избыточной для небольшого оборота.  

        ### Итоговый вердикт: Кого выбрать?
        * **Выбирай Klaviyo, если:** у тебя крупный магазин, штат маркетологов и критически важен продвинутый predictive AI-анализ поведения покупателей enterprise-уровня.  
        * **Выбирай Omnisend (наша рекомендация для старта):** если ты управляешь магазином в одиночку или небольшой командой, ценишь простоту и хочешь получить омниканальный возврат выручки без переплаты за сложные инструменты. *(Аккуратная партнёрская ссылка с предложением протестировать бесплатный тариф).*

        ---
        ### 🎯 Calculate Your Exact ROI
        Head back to **Tab 1 (Calculator)** to run your numbers through our custom scenarios!
        """)

  elif "Native Features" in article_choice:
    st.markdown("## Shopify Native Features vs. Third-Party Recovery Apps")
    st.write(
        "A deep dive into why built-in platform features often fall short and"
        " when it's time to upgrade to advanced tools."
    )
    st.markdown(
        "*(Full article text loading... Focus on calculator metrics to"
        " evaluate your current setup).*"
    )

  else:
    st.markdown("## Maximizing Customer Lifetime Value (LTV)")
    st.write(
        "Tactics on retention, post-purchase segmentation, and email marketing"
        " to increase repeat purchases."
    )
    st.markdown(
        "*(Full article text loading... Use the Tool Finder to match your store"
        " with top retention apps).*"
    )