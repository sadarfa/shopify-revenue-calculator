import streamlit as st
import sqlite3

# --- STARLETTE / FASTAPI HOOK FÜR STATISCHE VERIFIZIERUNG ---
try:
    from streamlit.runtime.scriptrunner import get_script_run_ctx
    ctx = get_script_run_ctx()
    if ctx and hasattr(ctx, "session_id"):
        import streamlit.runtime.runtime as runtime
        session = runtime.get_instance()._session_mgr.get_session(ctx.session_id)
        if session and hasattr(session, "app"):
            app = session.app
            @app.get("/impact-verification.txt")
            async def impact_verify():
                from starlette.responses import PlainTextResponse
                return PlainTextResponse("Impact-Site-Verification: b7541e6d-2c99-4189-bec6-fb8049fd966d")
except Exception:
    pass

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
    page_title="Shopify Revenue Recovery Calculator & Tool Finder",
    page_icon="📈",
    layout="wide"
)

# --- SIDEBAR INPUTS (Store Parameters & Budget) ---
with st.sidebar:
    st.markdown("### ⚙️ Your Shopify Store")
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

# --- MAIN CONTENT TABS (WICHTIG: Hier werden main_tab1 und main_tab2 definiert) ---
main_tab1, main_tab2 = st.tabs(["📊 Revenue Recovery Calculator & Tool Finder", "📝 SEO Article & Guide"])

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
    st.link_button("Launch Recovery with Omnisend", "https://www.omnisend.com/")

    st.markdown("---")
    
    st.markdown("#### **Retainful** — 💡 *Budget Alternative*")
    st.markdown("**Pricing Tier:** Free / Starter")
    st.markdown("**Why it fits:** Great dynamic coupons and abandoned cart recovery for early stages.")
    st.link_button("Launch Recovery with Retainful", "https://www.retainful.com/")

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

st.divider()

# --- FOOTER ---
col_imp, col_dsg = st.columns(2)

with col_imp:
    with st.expander("Impressum"):
        st.markdown("""
        <div style="font-size: 0.85em; color: #555;">
        Information according to § 5 TMG:<br>
        Igor Widiker<br>
        Erkrath, Germany<br>
        <b>E-Mail:</b> business.iwi@gmail.com<br><br>
        © 2026 IgorWidiker.com - All Rights Reserved by IgorWidiker
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

st.markdown("Impact-Site-Verification: b7541e6d-2c99-4189-bec6-fb8049fd966d")