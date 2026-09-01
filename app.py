import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Shopify Recovery & ROI Calculator 2026",
    page_icon="📊",
    layout="wide"
)

# Создание вкладок
main_tab1, main_tab2 = st.tabs([
    "📊 Revenue Calculator & Tool Finder", 
    "📝 SEO Article & Guide"
])

# ================= TAB 1: КАЛЬКУЛЯТОР =================
with main_tab1:
    st.title("📊 Shopify Abandoned Cart Recovery & ROI Calculator")
    st.write("Calculate how much revenue you are losing to abandoned carts and find the ideal app stack for your budget.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Store Metrics")
        monthly_visitors = st.number_input("Monthly Store Visitors", min_value=100, max_value=1000000, value=10000, step=500)
        conversion_rate = st.slider("Average Conversion Rate (%)", min_value=0.5, max_value=10.0, value=2.0, step=0.1)
        aov = st.number_input("Average Order Value ($ AOV)", min_value=10, max_value=1000, value=75, step=5)
        abandonment_rate = st.slider("Cart Abandonment Rate (%)", min_value=50.0, max_value=90.0, value=70.0, step=1.0)

    # Расчеты
    total_orders = monthly_visitors * (conversion_rate / 100.0)
    monthly_revenue = total_orders * aov
    
    # Считаем брошенные корзины (покупатели, которые дошли до чекаута, но ушли)
    # Формула: если conversion_rate = 2%, то это завершенные заказы. Брошенные корзины составляют abandonment_rate от всех начатых чекаутов.
    initiated_checkouts = total_orders / (1 - (abandonment_rate / 100.0))
    lost_orders = initiated_checkouts * (abandonment_rate / 100.0)
    lost_revenue = lost_orders * aov

    # Потенциальное восстановление (обычно возвращают 5-15% брошенных корзин)
    recovered_orders = lost_orders * 0.10
    recovered_revenue = recovered_orders * aov

    with col2:
        st.subheader("Financial Impact")
        st.metric(label="Estimated Monthly Revenue", value=f"${monthly_revenue:,.2f}")
        st.metric(label="Estimated Lost Monthly Revenue", value=f"${lost_revenue:,.2f}", delta_color="inverse")
        st.metric(label="Potential Recovered Revenue (10% recovery)", value=f"${recovered_revenue:,.2f}", delta="Profit boost")

    st.markdown("---")
    st.subheader("Recommended Tool Stack for Your Size")
    
    if monthly_visitors < 5000:
        st.info("💡 **Recommendation:** Since you are starting out lean, use **Shopify Email** (for zero fixed cost) or **Retainful** (for dynamic coupons under $20/mo).")
    elif monthly_visitors < 25000:
        st.success("🔥 **Recommendation:** Your store is growing fast. **Omnisend Standard** ($16/mo) gives you the best multi-channel ROI (Email + SMS) without overpaying.")
    else:
        st.warning("⚡ **Recommendation:** High traffic volume detected. Consider advanced automated workflows with Omnisend Pro or Klaviyo to capture maximum high-value carts.")


# ================= TAB 2: ПОЛНАЯ СТАТЬЯ =================
with main_tab2:
    st.markdown("## Best Abandoned Cart Recovery Apps for Shopify Under $50/Month (2026 Guide)")
    st.caption("Published by Shopify Growth Lab | 7 min read")
    
    st.write(
        "Over 70% of e-commerce shoppers abandon their carts before completing checkout. "
        "For small-to-medium Shopify stores doing under 500–1,000 orders a month, losing this revenue hurts—but "
        "paying $150+ per month for enterprise-level tools like Klaviyo doesn't make financial sense."
    )
    st.write(
        "If you're running a lean operation and want maximum ROI without bleeding cash on software subscriptions, "
        "you need a lean, high-performing recovery stack. Here are the best abandoned cart recovery apps for Shopify under $50/month."
    )
    
    st.markdown("### Quick Comparison Table")
    
    st.markdown("""
| App Name | Starting Price | Key Channels | Best For |
| :--- | :--- | :--- | :--- |
| **Omnisend** | Free / $16/mo | Email + SMS | Best overall ROI & automation |
| **Retainful** | Free / ~$19/mo | Email + Dynamic Coupons | Micro-stores & timer popups |
| **Shopify Email** | Free ($1/1000 emails) | Email only | Absolute beginners on zero budget |
    """)
    
    st.markdown("---")
    st.markdown("### 1. Omnisend (Standard Plan — From $16/mo)")
    st.write(
        "Omnisend remains the gold standard for growing Shopify stores. While their free tier covers basic email blasts, "
        "the Standard plan unlocks pre-built automation workflows for abandoned carts, browse abandonment, and SMS reminders."
    )
    st.markdown("**Why it wins under $50:** You get multi-channel capabilities (Email + SMS) under the $20 mark, whereas competitors often gate SMS behind much higher pricing tiers.")
    st.link_button("Try Omnisend Free / Upgrade", "https://www.omnisend.com/")
    
    st.markdown("---")
    st.markdown("### 2. Retainful (Growth Tier — From $19/mo)")
    st.write(
        "Retainful focuses heavily on driving urgency. It features easy-to-use countdown timers inside recovery emails "
        "and unique, dynamic coupon codes that generate automatically for each dropped cart."
    )
    st.markdown("**Why it wins under $50:** Exceptional value for stores that want to boost conversion rates using psychological triggers without complex setups.")
    st.link_button("Try Retainful Free", "https://www.retainful.com/")
    
    st.markdown("---")
    st.markdown("### The Verdict: Which one should you pick?")
    st.write(
        "If you want a proven multi-channel workflow that scales smoothly as your store grows, go with **Omnisend**. "
        "If you are starting out lean and want razor-sharp focus on email discount hooks, try **Retainful**."
    )
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background-color: #f1f3f5; padding: 20px; border-radius: 8px; text-align: center; margin-top: 20px;">
        <h4 style="margin-bottom: 8px; color: #333;">Not sure which tool fits your metrics?</h4>
        <p style="color: #666; margin-bottom: 0;">Use our interactive calculator to find your exact lost revenue and ideal tool stack.</p>
    </div>
    """, unsafe_allow_html=True)