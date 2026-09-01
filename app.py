import streamlit as st
import sqlite3
import random

# Database setup with A/B variant tracking
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
            variant TEXT,
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
    layout="centered"
)

# A/B Test Session Assignment (hidden from user)
if "ab_variant" not in st.session_state:
    st.session_state["ab_variant"] = random.choice(["A", "B"])

current_variant = st.session_state["ab_variant"]

# --- VARIANT A: Single-page high-converting landing ---
if current_variant == "A":
    st.title("📈 Shopify Revenue & Recovery Calculator")
    st.write("Calculate your store's hidden losses and see how much revenue you can recover instantly.")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        monthly_visitors = st.number_input("Monthly Visitors", min_value=1000, value=50000, step=5000, key="a_vis")
        conversion_rate = st.slider("Current Conversion Rate (%)", min_value=0.5, max_value=5.0, value=1.5, step=0.1, key="a_cr")
        avg_order_value = st.number_input("Average Order Value ($)", min_value=10.0, value=75.0, step=5.0, key="a_aov")

    with col2:
        cart_abandonment_rate = st.slider("Cart Abandonment Rate (%)", min_value=50.0, max_value=90.0, value=70.0, step=1.0, key="a_car")
        store_url = st.text_input("Shopify Store URL", placeholder="my-store.myshopify.com", key="a_url")
        user_email = st.text_input("Your Email (to unlock report)", placeholder="business.iwi@gmail.com", key="a_email")

    st.markdown("")
    if st.button("Calculate Recovery Potential", type="primary", use_container_width=True, key="a_btn"):
        monthly_orders = monthly_visitors * (conversion_rate / 100.0)
        current_monthly_revenue = monthly_orders * avg_order_value
        
        abandoned_carts = monthly_visitors * (cart_abandonment_rate / 100.0)
        recoverable_orders = abandoned_carts * 0.15
        potential_monthly_gain = recoverable_orders * avg_order_value
        potential_annual_gain = potential_monthly_gain * 12

        st.divider()
        st.markdown("### 📊 Your Revenue Recovery Results")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Current Monthly Rev", f"${current_monthly_revenue:,.2f}")
        res_col2.metric("Monthly Recoverable", f"${potential_monthly_gain:,.2f}", delta=f"+{(potential_monthly_gain/max(current_monthly_revenue, 1))*100:.1f}%")
        res_col3.metric("Annual Recoverable", f"${potential_annual_gain:,.2f}")

        if user_email:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO leads (store_url, estimated_revenue, email, variant) VALUES (?, ?, ?, ?)",
                (store_url, potential_annual_gain, user_email, current_variant)
            )
            conn.commit()
            conn.close()
            st.success("Your report has been saved successfully!")

    st.divider()
    st.subheader("🛠️ Find Your Recovery Tool Stack")
    budget_choice = st.selectbox("Monthly software budget?", ["Low Budget (<$50)", "Growth ($50-$200)", "Scale ($200+)"], key="a_bud")
    if "Low Budget" in budget_choice:
        st.info("🥇 Recommendation: **Retainful / Cartly** — Budget-friendly recovery apps.")
    else:
        st.info("🥇 Recommendation: **Omnisend** (Top Partner Pick) — Ultimate email & SMS automation powerhouse.")

# --- VARIANT B: Multi-tab structured interface ---
else:
    st.title("📈 Shopify Revenue & Recovery Calculator")
    st.write("Professional multi-tool suite for e-commerce growth and tool selection.")

    nav_tab1, nav_tab2, nav_tab3 = st.tabs(["Calculator", "Tool Finder", "Legal & Privacy"])

    with nav_tab1:
        st.header("Revenue & Recovery Calculator")
        col1, col2 = st.columns(2)
        with col1:
            monthly_visitors = st.number_input("Monthly Visitors", min_value=1000, value=50000, step=5000, key="b_vis")
            conversion_rate = st.slider("Current Conversion Rate (%)", min_value=0.5, max_value=5.0, value=1.5, step=0.1, key="b_cr")
            avg_order_value = st.number_input("Average Order Value ($)", min_value=10.0, value=75.0, step=5.0, key="b_aov")
        with col2:
            cart_abandonment_rate = st.slider("Cart Abandonment Rate (%)", min_value=50.0, max_value=90.0, value=70.0, step=1.0, key="b_car")
            store_url = st.text_input("Shopify Store URL", placeholder="my-store.myshopify.com", key="b_url")
            user_email = st.text_input("Your Email", placeholder="business.iwi@gmail.com", key="b_email")

        if st.button("Calculate Revenue", type="primary", key="b_btn"):
            monthly_orders = monthly_visitors * (conversion_rate / 100.0)
            current_monthly_revenue = monthly_orders * avg_order_value
            abandoned_carts = monthly_visitors * (cart_abandonment_rate / 100.0)
            potential_annual_gain = abandoned_carts * 0.15 * avg_order_value * 12
            
            st.metric("Annual Recoverable Revenue", f"${potential_annual_gain:,.2f}")
            if user_email:
                conn = sqlite3.connect(DB_FILE)
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO leads (store_url, estimated_revenue, email, variant) VALUES (?, ?, ?, ?)",
                    (store_url, potential_annual_gain, user_email, current_variant)
                )
                conn.commit()
                conn.close()
                st.success("Saved successfully!")

    with nav_tab2:
        st.header("Tool Finder")
        st.write("Find your ideal software stack based on your store profile.")
        st.info("🥇 Top Recommendation: **Omnisend** for multi-channel Shopify recovery.")

    with nav_tab3:
        st.header("Privacy Policy & Legal Notice")
        st.write("""
        **Legal Notice (Impressum):**  
        Igor Widiker | Erkrath, Germany | E-Mail: business.iwi@gmail.com  
        Data processing complies with GDPR (DSGVO).
        """)

st.divider()

# --- ADMIN ANALYTICS PANEL ---
with st.expander("🔐 Admin & A/B Test Analytics Dashboard"):
    st.write("Review collected leads and performance breakdown by experiment variant.")
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Summary stats per variant
    cursor.execute("SELECT variant, COUNT(*), SUM(estimated_revenue) FROM leads GROUP BY variant")
    stats = cursor.fetchall()
    
    if stats:
        st.markdown("### Variant Performance Summary")
        for row in stats:
            variant_name, lead_count, total_rev = row
            rev_display = total_rev if total_rev else 0.0
            st.write(f"- **Variant {variant_name}:** {lead_count} leads | Total Est. Potential: ${rev_display:,.2f}")
    
    st.markdown("### Raw Leads Database")
    cursor.execute("SELECT id, store_url, estimated_revenue, email, variant, created_at FROM leads")
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        st.table(rows)
    else:
        st.info("No leads recorded in the database yet.")

st.caption("Legal Notice: Igor Widiker | Erkrath, Germany | business.iwi@gmail.com")