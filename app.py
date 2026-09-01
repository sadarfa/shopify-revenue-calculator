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
        ### Why Enterprise Tools Aren't Always the Answer
        Most e-commerce guides recommend heavy tools costing $150–$300+ per month. If your Shopify store is generating €5k–€10k monthly, spending a huge chunk of your margin on software is a direct path to the red. You need lean, predictable automation that pays for itself with just two or three recovered checkouts.
        
        ### Top Budget-Friendly Recovery Solutions (<$50/mo)
        
        #### 1. Omnisend (Standard Plan — Starting at $16/mo)
        * **Why it fits:** It's our top recommendation for growing stores. You get automated multi-channel workflows (Email + SMS), pre-built abandoned cart & checkout sequences, and a generous free tier up to 250 contacts.
        * **Verdict:** Unbeatable feature-to-price ratio if you want room to scale without switching platforms later.
        
        #### 2. Retainful (Starting at $9/mo)
        * **Why it fits:** Perfect if you want pure email-based recovery without paying for advanced enterprise features you won't use. 
        * **Verdict:** Lightweight, straightforward setup directly inside Shopify.
        
        #### 3. Shopify Native Abandoned Checkout (Free)
        * **Why it fits:** Shopify includes a basic automated email reminder out of the box.
        * **Verdict:** Good for day one, but lacks advanced segmentation, multi-channel SMS triggers, and custom exit-intent popups needed long-term.
        
        ---
        ### 💡 Ready to find your exact fit?
        Don't guess your numbers. Use our **[Revenue & Recovery Calculator](#)** (Tab 1) to see how much uncaptured revenue you're leaving on the table right now, or check out our automated **Tool Finder** (Tab 2).
        """)

  elif "Omnisend vs Klaviyo" in article_choice:
    st.markdown(
        "## Omnisend vs Klaviyo: Which Is Better for Small Shopify Stores in"
        " 2026?"
    )
    st.markdown("*Published by Growth & Recovery Lab | Reading time: 6 mins*")

    st.markdown("""
        ### Executive Summary
        Both **Klaviyo** and **Omnisend** are top-tier marketing automation platforms built specifically for Shopify. However, they serve very different business scales:
        * **Klaviyo** is an enterprise data engine designed for stores with dedicated marketing teams and larger budgets.
        * **Omnisend** is a streamlined, highly profitable growth stack built for solo founders, small teams, and stores under $100k/mo.

        ---

        ### 1. Pricing Structure & Hidden Costs
        
        | Feature / Plan | **Omnisend** | **Klaviyo** |
        | :--- | :--- | :--- |
        | **Starting Price** | **$16 / month** | **$20 / month** |
        | **Pricing Metric** | Total emails sent per tier | Total active contacts stored |
        | **SMS Integration** | Free SMS credits included in Pro plan | Paid separately via extra credit packs |
        | **Support** | 24/7 Live Chat (all plans, including Free) | Email-only on lower tiers / slower responses |

        **The Verdict on Pricing:** Klaviyo’s pricing scales aggressively based on total profile storage, regardless of how often you email them. Omnisend provides a far smoother pricing curve, making it significantly cheaper as your email list expands.

        ---

        ### 2. Abandoned Cart & Recovery Workflows
        * **Omnisend:** Features pre-built, one-click automation templates for *Browse Abandonment*, *Cart Abandonment*, and *Checkout Abandonment*. You can combine Email + SMS + Push Notifications inside a single visual flowchart in under 15 minutes.
        * **Klaviyo:** Offers deep custom event triggers and advanced conditional branching. While powerful, setting up full multi-channel workflows often requires technical configuration and ongoing testing.

        ---

        ### 3. Final Recommendation: Which Should You Choose?

        * **Choose Klaviyo if:** You manage an established brand ($100k+/month), have a dedicated data analyst or email marketer, and need granular predictive analytics.
        * **Choose Omnisend if:** You are a solo merchant or small team running a Shopify store under $50k/month, and you want high-converting abandoned cart recovery with minimal setup overhead and predictable costs.

        ---
        ### 🎯 Calculate Your Exact ROI
        Unsure how much revenue an automated workflow would actually recover for your store? 
        Head back to **Tab 1 (Calculator)** to run your numbers through our сustom scenarios!
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