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

# Set default calculated state so results are visible instantly as an example
if "b_calc_done" not in st.session_state:
    st.session_state["b_calc_done"] = True
    st.session_state["b_annual"] = 94500.00
    st.session_state["b_curr_rev"] = 112500.00
    st.session_state["b_pot_mon"] = 7875.00

st.title("📈 Shopify Revenue & Recovery Calculator")
st.write("Professional multi-tool suite for e-commerce growth and tool selection.")

# Navigation Tabs (removed Legal & Privacy tab)
nav_tab1, nav_tab2, nav_tab3 = st.tabs(["Calculator", "Tool Finder", "Guides & Articles"])

with nav_tab1:
    st.header("Revenue & Recovery Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        monthly_visitors = st.number_input("Monthly Visitors", min_value=1000, value=50000, step=5000, key="b_vis")
        conversion_rate = st.slider("Current Conversion Rate (%)", min_value=0.5, max_value=5.0, value=1.5, step=0.1, key="b_cr")
    with col2:
        avg_order_value = st.number_input("Average Order Value ($)", min_value=10.0, value=75.0, step=5.0, key="b_aov")
        cart_abandonment_rate = st.slider("Cart Abandonment Rate (%)", min_value=50.0, max_value=90.0, value=70.0, step=1.0, key="b_car")

    store_url = st.text_input("Shopify Store URL (optional)", placeholder="my-store.myshopify.com", key="b_url")

    if st.button("Calculate Recovery Potential", type="primary", use_container_width=True, key="b_btn"):
        monthly_orders = monthly_visitors * (conversion_rate / 100.0)
        current_monthly_revenue = monthly_orders * avg_order_value
        abandoned_carts = monthly_visitors * (cart_abandonment_rate / 100.0)
        recoverable_orders = abandoned_carts * 0.15
        potential_monthly_gain = recoverable_orders * avg_order_value
        potential_annual_gain = potential_monthly_gain * 12
        
        st.session_state["b_annual"] = potential_annual_gain
        st.session_state["b_curr_rev"] = current_monthly_revenue
        st.session_state["b_pot_mon"] = potential_monthly_gain
        st.session_state["b_calc_done"] = True

    if st.session_state.get("b_calc_done", False):
        st.divider()
        st.markdown("### 📊 Your Revenue Recovery Results")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Current Monthly Rev", f"${st.session_state['b_curr_rev']:,.2f}")
        res_col2.metric("Monthly Recoverable", f"${st.session_state['b_pot_mon']:,.2f}", delta=f"+{(st.session_state['b_pot_mon']/max(st.session_state['b_curr_rev'], 1))*100:.1f}%")
        res_col3.metric("Annual Recoverable", f"${st.session_state['b_annual']:,.2f}")

        st.divider()
        st.subheader("🛠️ Find Your Recovery Tool Stack")
        st.write("Find your ideal software stack based on your store profile.")
        
        budget_choice = st.selectbox("Monthly software budget?", ["Low Budget (<$50)", "Growth ($50-$200)", "Scale ($200+)"], key="b_bud_main")
        if "Low Budget" in budget_choice:
            st.info("🥇 Recommendation: **Retainful / Cartly** — Budget-friendly recovery apps.")
        else:
            st.info("🥇 Recommendation: **Omnisend** (Top Partner Pick) — Ultimate email & SMS automation powerhouse.")

    st.divider()
    st.info("💡 **Want to save this report and unlock personalized software recommendations?**")
    saved_email_b = st.text_input("Enter your email to save report", placeholder="your-email@store.com", key="b_email")
    if st.button("Save & Unlock Report", key="b_save_btn"):
        if saved_email_b:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO leads (store_url, estimated_revenue, email, variant) VALUES (?, ?, ?, ?)",
                (store_url, st.session_state.get('b_annual', 94500.00), saved_email_b, "B")
            )
            conn.commit()
            conn.close()
            st.success("Report saved successfully! Check your inbox soon.")
        else:
            st.warning("Please enter a valid email address.")

with nav_tab2:
    st.header("Tool Finder")
    st.write("Find your ideal software stack based on your store profile.")
    
    budget_choice_tab = st.selectbox("Monthly software budget?", ["Low Budget (<$50)", "Growth ($50-$200)", "Scale ($200+)"], key="b_bud_tab")
    if "Low Budget" in budget_choice_tab:
        st.info("🥇 Recommendation: **Retainful / Cartly** — Budget-friendly recovery apps.")
    else:
        st.info("🥇 Recommendation: **Omnisend** (Top Partner Pick) — Ultimate email & SMS automation powerhouse.")

with nav_tab3:
    st.header("E-Commerce Growth & Recovery Guides")
    st.write("Explore our expert articles designed to help Shopify merchants maximize revenue and optimize customer lifecycle value.")
    
    st.markdown("---")
    st.subheader("1. Abandoned Cart Recovery Strategies for Shopify")
    st.write("Learn how to turn lost checkouts into completed orders using multi-channel automated workflows (Email & SMS).")
    
    st.markdown("---")
    st.subheader("2. Shopify Native Features vs. Third-Party Recovery Apps")
    st.write("A deep dive into why built-in platform features often fall short and when it's time to upgrade to advanced tools.")
    
    st.markdown("---")
    st.subheader("3. Maximizing Customer Lifetime Value (LTV)")
    st.write("Tactics on retention, post-purchase segmentation, and email marketing to increase repeat purchases.")

st.divider()

# --- PROTECTED ADMIN PANEL IN SIDEBAR ---
with st.sidebar:
    st.subheader("Admin Portal")
    admin_password = st.text_input("Admin Password", type="password")
    
    if admin_password == "admin123":
        st.success("Access Granted")
        show_admin = True
    else:
        show_admin = False

if show_admin:
    st.markdown("---")
    st.subheader("🔐 Admin Analytics Dashboard")
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*), SUM(estimated_revenue) FROM leads")
    total_leads, total_rev = cursor.fetchone()
    total_rev_display = total_rev if total_rev else 0.0
    st.write(f"- **Total Leads:** {total_leads} | Total Est. Potential: ${total_rev_display:,.2f}")
    
    cursor.execute("SELECT id, store_url, estimated_revenue, email, created_at FROM leads")
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        st.table(rows)
    else:
        st.info("No leads recorded in the database yet.")

# --- IMPRESSUM (FOOTER) ---
st.markdown("---")
st.markdown("### **Impressum**")
st.markdown("""
**Angaben gemäß § 5 TMG:**  
Igor Widiker  
Erkrath, Germany  
**E-Mail:** business.iwi@gmail.com  
""")