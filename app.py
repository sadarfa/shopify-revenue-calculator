import streamlit as st
import sqlite3

# Database setup
DB_FILE = "database.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_url TEXT,
            estimated_revenue REAL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Page configuration
st.set_page_config(
    page_title="Shopify Revenue & Recovery Calculator",
    page_icon="📈",
    layout="wide"
)

# Navigation setup
st.title("📈 Shopify Revenue & Recovery Calculator")
st.write("Analyze potential revenue recovery and explore expert insights for your Shopify store.")

# Объявление пяти вкладок ДО их использования
nav_tab1, nav_tab2, nav_tab3, nav_tab4, nav_tab5 = st.tabs(["Calculator", "Tool Finder", "SEO Articles", "Admin Leads", "DSGVO & Legal"])

with nav_tab1:
    st.header("Revenue & Recovery Calculator")
    st.write("Estimate how much revenue your Shopify store can recover through automated optimization.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        monthly_visitors = st.number_input("Monthly Visitors", min_value=1000, value=50000, step=5000)
        conversion_rate = st.slider("Current Conversion Rate (%)", min_value=0.5, max_value=5.0, value=1.5, step=0.1)
        avg_order_value = st.number_input("Average Order Value ($)", min_value=10.0, value=75.0, step=5.0)
    
    with col2:
        cart_abandonment_rate = st.slider("Cart Abandonment Rate (%)", min_value=50.0, max_value=90.0, value=70.0, step=1.0)
        store_url = st.text_input("Your Shopify Store URL (optional)", placeholder="my-store.myshopify.com")
        user_email = st.text_input("Your Email (to save your report)", placeholder="name@example.com")

    if st.button("Calculate Recovery Potential", type="primary"):
        monthly_orders = monthly_visitors * (conversion_rate / 100.0)
        current_monthly_revenue = monthly_orders * avg_order_value
        
        abandoned_carts = monthly_visitors * (cart_abandonment_rate / 100.0)
        recoverable_orders = abandoned_carts * 0.15
        potential_monthly_gain = recoverable_orders * avg_order_value
        potential_annual_gain = potential_monthly_gain * 12

        st.divider()
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Current Est. Monthly Revenue", f"${current_monthly_revenue:,.2f}")
        res_col2.metric("Recoverable Monthly Revenue", f"${potential_monthly_gain:,.2f}", delta=f"+{(potential_monthly_gain/max(current_monthly_revenue, 1))*100:.1f}%")
        res_col3.metric("Recoverable Annual Revenue", f"${potential_annual_gain:,.2f}")

        if user_email:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO leads (store_url, estimated_revenue, email) VALUES (?, ?, ?)",
                (store_url, potential_annual_gain, user_email)
            )
            conn.commit()
            conn.close()
            st.success("Your calculation has been saved successfully!")

with nav_tab2:
    st.header("Find Your Revenue Recovery Stack")
    st.write("Answer a few quick questions to find the ideal automation tool tailored to your Shopify store's budget and goals.")

    tf_col1, tf_col2 = st.columns(2)

    with tf_col1:
        budget_choice = st.selectbox(
            "What is your monthly software budget?",
            [
                "Low Budget (Under $50/month)",
                "Growth Stage ($50 - $200/month)",
                "Scale Stage ($200+/month)"
            ],
            key="tf_budget"
        )

    with tf_col2:
        channel_choice = st.selectbox(
            "What recovery channels do you want to prioritize?",
            [
                "Email Only (Simple & Cost-Effective)",
                "Email + SMS (Omnichannel Growth)",
                "Advanced Multi-Channel (Email, SMS, WhatsApp & Automation)"
            ],
            key="tf_channel"
        )

    if st.button("Recommend Best Tool", type="secondary"):
        st.divider()
        st.subheader("Your Recommended Solution:")

        if "Low Budget" in budget_choice:
            st.markdown("### 🥇 **Retainful / Cartly**")
            st.write("""
                * **Why it fits:** Perfect for smaller stores looking for straightforward abandoned cart recovery features without breaking the bank.
                * **Key Highlights:** Easy setup, affordable pricing tiers, essential email reminders, and quick deployment.
            """)
        elif "Growth Stage" in budget_choice or "Scale Stage" in budget_choice:
            if "Email Only" in channel_choice:
                st.markdown("### 🥇 **Klaviyo**")
                st.write("""
                    * **Why it fits:** The gold standard for deep customer data segmentation and advanced email marketing flows.
                    * **Key Highlights:** Powerful data analytics, robust triggers, and granular audience targeting.
                """)
            else:
                st.markdown("### 🥇 **Omnisend** (Top Recommended Partner)")
                st.write("""
                    * **Why it fits:** The ultimate all-in-one marketing automation powerhouse combining high-converting email and SMS workflows designed specifically for Shopify.
                    * **Key Highlights:** Pre-built automation templates, excellent ROI, thousands of 5-star reviews, and seamless multi-channel scaling.
                """)
                st.info("💡 Tip: Omnisend offers deep Shopify integration that bridges the gap between native checkout limits and full revenue recovery.")

with nav_tab3:
    st.header("Expert SEO & Growth Articles")
    st.write("Learn how to scale your e-commerce business with proven abandoned cart optimization strategies.")

    article_choice = st.selectbox(
        "Select an article to read:",
        [
            "Does Shopify Have Native Abandoned Cart Recovery?",
            "Best Shopify Abandoned Cart Apps in 2026",
            "How to Recover Abandoned Carts Without Heavy Discounts",
            "Email vs. Multi-Channel Reminders for Checkout Recovery"
        ],
        key="seo_article"
    )

    if article_choice == "Does Shopify Have Native Abandoned Cart Recovery?":
        st.subheader("Does Shopify Have Native Abandoned Cart Recovery?")
        st.write("""
            Yes, Shopify includes basic built-in checkout recovery features, but they come with notable limitations depending on your pricing plan.
            
            ### What Native Shopify Offers:
            - Automatic emails sent to customers who abandon their checkout *after* entering their email address.
            - Basic email templates that can be customized with your store branding.
            
            ### Where It Falls Short:
            1. **The Gap:** It only triggers at the checkout stage, completely ignoring **browse abandonment** and early cart additions.
            2. **Limited Customization & Timing:** You cannot easily split-test sequences, set multi-step conditional workflows, or integrate SMS and WhatsApp channels natively without third-party apps.
            
            *Solution:* Most growing stores quickly transition to specialized automated recovery tools to capture the missing revenue streams.
        """)
    elif article_choice == "Best Shopify Abandoned Cart Apps in 2026":
        st.subheader("Best Shopify Abandoned Cart Apps in 2026")
        st.write("""
            Choosing the right app depends on your store's volume, budget, and required automation depth. 
            
            ### Top Contenders on the Market:
            - **Omnisend:** A robust, all-in-one marketing automation platform powerhouse combining email, SMS, and deep Shopify workflow integrations with thousands of 5-star reviews.
            - **Klaviyo:** The enterprise-grade choice for advanced data segmentation, though it can carry a steeper learning curve and higher scaling costs.
            - **Retainful / Cartly:** Excellent lightweight alternatives for smaller stores looking for straightforward recovery features under a tighter budget.
            
            Use our **Revenue Recovery Calculator** in the first tab to estimate how much recovered income can easily offset these software costs.
        """)
    elif article_choice == "How to Recover Abandoned Carts Without Heavy Discounts":
        st.subheader("How to Recover Abandoned Carts Without Heavy Discounts")
        st.write("""
            Relying solely on discount codes to win back shoppers erodes your profit margins and conditions customers to wait for sales.
            
            ### Better Recovery Tactics:
            1. **Friction Reduction:** Address sudden shipping costs or unexpected taxes transparently earlier in the funnel.
            2. **Social Proof & Urgency:** Include product reviews, ratings, and limited-stock reminders inside your recovery emails.
            3. **Customer Support Availability:** Add live chat or quick-answer prompts right at the checkout stage to resolve last-minute hesitations instantly.
        """)
    else:
        st.subheader("Email vs. Multi-Channel Reminders for Checkout Recovery")
        st.write("""
            Relying exclusively on email is no longer enough as inbox competition grows fiercer.
            
            ### Channel Comparison:
            - **Email:** High ROI, great for detailed product recommendations, storytelling, and rich media.
            - **SMS / WhatsApp:** Exceptional open rates within the first 15 minutes of abandonment, ideal for time-sensitive cart reminders or flash incentives.
            
            Combining email with a gentle SMS reminder typically yields the highest overall recovery conversion rate for mid-sized Shopify stores.
        """)

with nav_tab4:
    st.header("Admin Leads Overview")
    st.write("Review collected lead details and estimated recovery values from the calculator.")
    
    if st.checkbox("Show Lead Database", key="admin_checkbox"):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, store_url, estimated_revenue, email, created_at FROM leads")
        rows = cursor.fetchall()
        conn.close()
        
        if rows:
            st.table(rows)
        else:
            st.info("No leads recorded in the database yet.")

with nav_tab5:
    st.header("Datenschutzerklärung & Impressum (DSGVO)")
    st.write("""
    ### 1. Datenschutz auf einen Blick
    **Allgemeine Hinweise**  
    Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können.

    ### 2. Datenerfassung auf dieser Website
    **Wer ist verantwortlich für die Datenerfassung auf dieser Website?**  
    Die Datenverarbeitung auf dieser Website erfolgt durch den Website-Betreiber (Kontakt siehe Impressum unten).

    **Wie erfassen wir Ihre Daten?**  
    Ihre Daten werden zum einen dadurch erhoben, dass Sie uns diese mitteilen (z. B. durch Eingabe Ihrer E-Mail-Adresse und Ihrer Shop-URL im Berechnungsformular).

    **Wofür nutzen wir Ihre Daten?**  
    Ein Teil der Daten wird erhoben, um eine fehlerfreie Bereitstellung der Website zu gewährleisten. Andere Daten (Ihre E-Mail-Adresse und Shop-Daten) werden ausschließlich zur Speicherung Ihres Berichts und zur Bereitstellung relevanter Software-Empfehlungen genutzt.

    ### 3. Ihre Rechte
    Sie haben jederzeit das Recht, unentgeltlich Auskunft über Herkunft, Empfänger und Zweck Ihrer gespeicherten personenbezogenen Daten zu erhalten. Sie haben außerdem ein Recht, die Berichtigung oder Löschung dieser Daten zu verlangen.

    ---

    ### Impressum
    **Angaben gemäß § 5 TMG / Angaben nach DSGVO:**  
    Igor Widiker  
    Erkrath, Deutschland  
    E-Mail: (Wird für den Support über die App bereitgestellt)
    """)