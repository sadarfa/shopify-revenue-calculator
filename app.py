with nav_tab2:
  st.subheader("📚 Content & SEO Guides")
  article_choice = st.selectbox(
      "Select an article to read:",
      [
          (
              "Best Abandoned Cart Recovery Apps for Shopify Under"
              " $50/Month (2026 Guide)"
          ),
          "Omnisend vs Klaviyo for Small Shopify Stores: Cost Breakdown",
      ],
  )

  if "Under $50" in article_choice:
    components.html(get_article_html(), height=1100, scrolling=True)
  else:
    components.html(get_second_article_html(), height=1100, scrolling=True)