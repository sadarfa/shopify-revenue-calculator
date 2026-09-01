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

# Page configuration (sidebar starts collapsed)
st.set_page_config(
    page_title="Shopify Revenue Recovery Calculator & Tool Finder",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- JAVASCRIPT: AUTO-EXPAND SIDEBAR AFTER 3 SECONDS ---
sidebar_timer_js = """
<script>
setTimeout(function() {
    const doc = window.parent.document;
    const expandButton = doc.querySelector('[data-testid="collapsedControl"]');
    if (expandButton) {
        expandButton.click();
    }
}, 3000);
</script>
"""
components.html(sidebar_timer_js, height=0, width=0)

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

# --- SIDEBAR INPUTS (Store Parameters & Budget) ---
with st.sidebar:
    st.markdown("### ⚙️ Store Parameters")
    monthly_visitors = st.number_input("Monthly Visitors", min_value=1000, value=5000, step=1000, key="b_vis")
    current_monthly_orders = st.number_input("Current Monthly Orders", min_value=10, value=140, step=10, key="b_orders")
    avg_order_value = st.number_input("Average Order Value (AOV, €)", min_value=10.0, value=70.0, step=5.0, key="b_aov")
    
    st.markdown("---")
    st.markdown("### 🎯 Budget & Requirements")
    monthly_budget = st.slider("Monthly Marketing Budget (€)", min_value=0, max_value=500, value=30, step=10, key="b_budget")
    ai_support = st.checkbox("Do you need AI customer support & live chat?", value=False, key="b_ai")

# --- CALCULATIONS ---
conversion_rate = (current_monthly_orders / monthly_visitors) * 100 if monthly_visitors > 0 else 1.5
current_monthly_rev = current_monthly_orders * avg_order_value

estimated_abandoned_carts = monthly_visitors * 0.70
estimated_lost_revenue = estimated_abandoned_carts * avg_order_value * 0.15

# --- MAIN CONTENT TABS ---
main_tab1, main_tab2 = st.tabs(["📊 Revenue Recovery Calculator & Tool Finder", "📝 SEO Article Preview"])

with main_tab1:
    st.markdown("## 🛒 Shopify Revenue Recovery Calculator & Tool Finder")
    st.write("Estimate your store's lost monthly revenue and discover the ideal automation stack in seconds.")
    
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.markdown(f"""
        <div style="font-size: 0.9em; color: gray;">📉 Estimated Lost Revenue / mo</div>
        <div style="font-size: 2.2em; font-weight: bold; color: #222;">€{estimated_lost_revenue:,.2f}</div>
        <span style="background-color: #ffebee; color: #c62828; padding: 2px 6px; border-radius: 4px; font-size: 0.8em;">↑ Growth Potential</span>
        """, unsafe_allow_html=True)
    with metric_col2:
        st.markdown(f"""
        <div style="font-size: 0.9em; color: gray;">📊 Current Conversion Rate</div>
        <div style="font-size: 2.2em; font-weight: bold; color: #222;">{conversion_rate:.2f}%</div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("### 📈 Recovery Scenarios")
    
    scen_tab1, scen_tab2, scen_tab3 = st.tabs(["Conservative (Email)", "Base (Omnichannel)", "Optimistic (AI+SMS)"])
    
    with scen_tab1:
        rev_val = estimated_lost_revenue * 0.25
        orders_val = rev_val / avg_order_value if avg_order_value > 0 else 0
        st.markdown(f"""
        <div style="background-color: #e8f5e9; padding: 15px; border-radius: 5px; border-left: 5px solid #4caf50;">
        <b>Recovered Revenue:</b> €{rev_val:,.2f} / month ({orders_val:.1f} orders)
        </div>
        """, unsafe_allow_html=True)
        st.write("**Strategy:** Basic email automation (e.g., standard Shopify email)")

    with scen_tab2:
        rev_val = estimated_lost_revenue * 0.60
        orders_val = rev_val / avg_order_value if avg_order_value > 0 else 0
        st.markdown(f"""
        <div style="background-color: #e8f5e9; padding: 15px; border-radius: 5px; border-left: 5px solid #4caf50;">
        <b>Recovered Revenue:</b> €{rev_val:,.2f} / month ({orders_val:.1f} orders)
        </div>
        """, unsafe_allow_html=True)
        st.write("**Strategy:** Multi-channel workflows (Email + SMS sequences)")

    with scen_tab3:
        rev_val = estimated_lost_revenue * 0.85
        orders_val = rev_val / avg_order_value if avg_order_value > 0 else 0
        st.markdown(f"""
        <div style="background-color: #e8f5e9; padding: 15px; border-radius: 5px; border-left: 5px solid #4caf50;">
        <b>Recovered Revenue:</b> €{rev_val:,.2f} / month ({orders_val:.1f} orders)
        </div>
        """, unsafe_allow_html=True)
        st.write("**Strategy:** Full AI automation stack with live chat and predictive triggers")

    st.markdown("---")
    st.markdown("### 🛠️ Recommended Tools for Your Store")
    
    st.markdown("#### **Omnisend** — 🏆 *Best Value Choice*")
    st.markdown("**Pricing Tier:** Standard (€16/mo)")
    st.markdown("**Why it fits:** Email + SMS automation with high ROI for small e-commerce stores.")
    st.markdown("""
    <a href="https://www.omnisend.com/" target="_blank">
        <button style="background-color:#ff4b4b; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; font-weight:bold;">
            Launch Recovery with Omnisend 🚀
        </button>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown("#### **Retainful** — 💡 *Budget Alternative*")
    st.markdown("**Pricing Tier:** Free / Starter")
    st.markdown("**Why it fits:** Great dynamic coupons and abandoned cart recovery for early stages.")
    st.markdown("""
    <a href="https://www.retainful.com/" target="_blank">
        <button style="background-color:#f0f2f6; color:#31333F; border:1px solid #d6d6d6; padding:10px 20px; border-radius:5px; cursor:pointer; font-weight:bold;">
            Launch Recovery with Retainful 💡
        </button>
    </a>
    """, unsafe_allow_html=True)

with main_tab2:
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

# --- HIDDEN ADMIN PANEL ---
query_params = st.query_params
if query_params.get("portal") == "secret_admin":
    with st.sidebar:
        st.markdown("---")
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

# --- FOOTER ---
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