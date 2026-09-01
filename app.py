import streamlit as st
import sqlite3
import streamlit.components.v1 as components

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

# --- GOOGLE ANALYTICS (GA4) INTEGRATION ---
GA_ID = "G-XXXXXXXXXX"

ga_code = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{GA_ID}');
</script>
"""
components.html(ga_code, height=0, width=0)

# Set default calculated state so results are visible instantly as an example
if "b_calc_done" not in st.session_state:
    st.session_state["b_calc_done"] = True
    st.session_state["b_annual"] = 94500.00
    st.session_state["b_curr_rev"] = 112500.00
    st.session_state["b_pot_mon"] = 7875.00

st.title("📈 Shopify Revenue & Recovery Calculator")
st.write("Professional multi-tool suite for e-commerce growth and tool selection.")

# Navigation Tabs
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
            st.markdown("""
            * **🥇 1st Place:** **Omnisend (Standard)** — Starts at $16/mo; excellent multi-channel automation and 20% recurring affiliate setup.
            * **🥈 2nd Place:** **Retainful** — Great budget-friendly recovery emails & live triggers.
            * **🥉 3rd Place:** **Shopify Email (Native)** — Cost-effective starter option.
            """)
        else:
            st.markdown("""
            * **🥇 1st Place:** **Omnisend** (Top Partner Pick) — Ultimate email & SMS automation powerhouse.
            * **🥈 2nd Place:** **Klaviyo** — Advanced data segmentation and flows.
            * **🥉 3rd Place:** **Recart** — High-converting SMS-first recovery platform.
            """)

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
        st.markdown("""
        * **🥇 1st Place:** **Omnisend (Standard)** — Starts at $16/mo; ideal budget automation choice.
        * **🥈 2nd Place:** **Retainful** — Great budget-friendly recovery emails & live triggers.
        * **🥉 3rd Place:** **Shopify Email (Native)** — Cost-effective starter option.
        """)
    else:
        st.markdown("""
        * **🥇 1st Place:** **Omnisend** (Top Partner Pick) — Ultimate email & SMS automation powerhouse.
        * **🥈 2nd Place:** **Klaviyo** — Advanced data segmentation and flows.
        * **🥉 3rd Place:** **Recart** — High-converting SMS-first recovery platform.
        """)

with nav_tab3:
    st.header("E-Commerce Growth & Recovery Guides")
    st.write("Explore our expert articles designed to help Shopify merchants maximize revenue and optimize customer lifecycle value.")
    
    st.markdown("---")
    
    article_choice = st.selectbox("Select a Guide to Read:", [
        "1. Best Abandoned Cart Recovery for Shopify Under $50/Month (Recommended)",
        "2. Shopify Native Features vs. Third-Party Recovery Apps",
        "3. Maximizing Customer Lifetime Value (LTV)"
    ])
    
    if "Under $50" in article_choice:
        st.markdown("## Best Abandoned Cart Recovery for Shopify Under $50/Month (2026 Guide)")
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
        Don't guess your numbers. Use our **Revenue & Recovery Calculator** (Tab 1) to see how much uncaptured revenue you're leaving on the table right now, or check out our automated **Tool Finder** (Tab 2).
        """)
        
    elif "Native Features" in article_choice:
        st.markdown("## Shopify Native Features vs. Third-Party Recovery Apps")
        st.write("A deep dive into why built-in platform features often fall short and when it's time to upgrade to advanced tools.")
        st.markdown("*(Full article text loading... Focus on calculator metrics to evaluate your current setup).*")
        
    else:
        st.markdown("## Maximizing Customer Lifetime Value (LTV)")
        st.write("Tactics on retention, post-purchase segmentation, and email marketing to increase repeat purchases.")
        st.markdown("*(Full article text loading... Use the Tool Finder to match your store with top retention apps).*")

st.divider()

# --- HIDDEN ADMIN PANEL (Accessible only via secret URL parameter ?portal=secret_admin) ---
query_params = st.query_params
if query_params.get("portal") == "secret_admin":
    with st.sidebar:
        st.subheader("🔐 Admin Analytics Dashboard")
        admin_password = st.text_input("Admin Password", type="password")
        
        if admin_password == "admin123":
            st.success("Access Granted")
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*), SUM(estimated_revenue) FROM leads")
            total_leads, total_rev = cursor.fetchone()
            total_rev_display = total_rev if total_rev else 0.0
            st.write(f"- **Total Leads:** {total_leads}")
            st.write(f"- **Est. Potential:** ${total_rev_display:,.2f}")
            
            cursor.execute("SELECT id, store_url, estimated_revenue, email, created_at FROM leads")
            rows = cursor.fetchall()
            conn.close()
            
            if rows:
                st.table(rows)
            else:
                st.info("No leads recorded yet.")
        else:
            st.warning("Enter admin password.")

# --- FOOTER (IMPRESSUM & DSGV / PRIVACY POLICY ACCORDIONS) ---
st.markdown("---")

col_imp, col_dsg = st.columns(2)

with col_imp:
    with st.expander("Impressum"):
        st.markdown("""
        <div style="font-size: 0.85em; color: #555;">
        Information according to § 5 TMG:<br>
        Igor Widiker<br>
        Erkrath, Germany<br>
        <b>E-Mail:</b> business.iwi@gmail.com
        </div>
        """, unsafe_allow_html=True)

with col_dsg:
    with st.expander("Data Protection (DSGVO)"):
        st.markdown("""
        <div style="font-size: 0.85em; color: #555;">
        <b>Data Privacy Policy:</b><br>
        We process user data strictly in accordance with the GDPR (DSGVO). Collected lead information is used solely for reporting and communication purposes. No third-party sharing without consent.
        </div>
        """, unsafe_allow_html=True)