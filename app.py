import streamlit as st
import sqlite3
import os

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

nav_tab1, nav_tab2, nav_tab3 = st.tabs(["Calculator", "SEO Articles", "Admin Leads"])

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
        # Calculations
        monthly_orders = monthly_visitors * (conversion_rate / 100.0)
        current_monthly_revenue = monthly_orders * avg_order_value
        
        abandoned_carts = monthly_visitors * (cart_abandonment_rate / 100.0)
        recoverable_orders = abandoned_carts * 0.15  # Assuming 15% recovery rate via automation
        potential_monthly_gain = recoverable_orders * avg_order_value
        potential_annual_gain = potential_monthly_gain * 12

        st.divider()
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Current Est. Monthly Revenue", f"${current_monthly_revenue:,.2f}")
        res_col2.metric("Recoverable Monthly Revenue", f"${potential_monthly_gain:,.2f}", delta=f"+{(potential_monthly_gain/max(current_monthly_revenue, 1))*100:.1f}%")
        res_col3.metric("Recoverable Annual Revenue", f"${potential_annual_gain:,.2f}")

        # Save lead if email is provided
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
    st.header("Expert SEO & Growth Articles")
    st.write("Learn how to scale your e-commerce business with proven optimization strategies.")

    article_choice = st.selectbox(
        "Select an article to read:",
        [
            "How to Reduce Shopify Cart Abandonment in 2026",
            "Maximizing Customer Lifetime Value (LTV) on Shopify",
            "Top SEO Strategies for E-commerce Stores"
        ]
    )

    if article_choice == "How to Reduce Shopify Cart Abandonment in 2026":
        st.subheader("How to Reduce Shopify Cart Abandonment in 2026")
        st.write("""
            Cart abandonment remains one of the biggest leaks in e-commerce revenue. 
            On average, nearly 70% of shoppers leave items in their cart without completing the purchase.
            
            ### Key Strategies:
            1. **Multi-channel Retargeting:** Combine automated email sequences with SMS reminders within the first hour of abandonment.
            2. **Frictionless Checkout:** Enable one-click payment methods like Shop Pay, Apple Pay, and Google Pay.
            3. **Transparent Pricing:** Display shipping costs and taxes early in the customer journey to prevent checkout sticker shock.
        """)
    elif article_choice == "Maximizing Customer Lifetime Value (LTV) on Shopify":
        st.subheader("Maximizing Customer Lifetime Value (LTV) on Shopify")
        st.write("""
            Acquiring a new customer is significantly more expensive than retaining an existing one. 
            Focusing on LTV ensures long-term profitability and sustainable growth for your Shopify storefront.
            
            ### Core Tactics:
            - Implement post-purchase upsells and cross-sells.
            - Build a tiered loyalty and rewards program.
            - Send personalized email recommendations based on previous purchase history.
        """)
    else:
        st.subheader("Top SEO Strategies for E-commerce Stores")
        st.write("""
            Organic search traffic provides high-intent visitors without ongoing ad spend. 
            Optimizing your store structure is vital for sustained online visibility.
            
            ### Checklist:
            - Optimize category and product page meta titles and descriptions.
            - Improve site loading speed by compressing images and auditing heavy apps.
            - Publish helpful buyer guides and informational blog posts targeting long-tail keywords.
        """)

with nav_tab3:
    st.header("Admin Leads Overview")
    st.write("Review collected lead details and estimated recovery values from the calculator.")
    
    if st.checkbox("Show Lead Database"):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, store_url, estimated_revenue, email, created_at FROM leads")
        rows = cursor.fetchall()
        conn.close()
        
        if rows:
            st.table(rows)
        else:
            st.info("No leads recorded in the database yet.")