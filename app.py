import streamlit as st
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ZYRA",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.title("📈 ZYRA")
st.subheader(
    "SME Early Warning & Survival Intelligence Platform"
)

st.info(
    "Transform Business Data into Proactive Risk Signals"
)

# ==========================================
# BUSINESS TYPE
# ==========================================

business_type = st.selectbox(
    "Select Business Type",
    [
        "Retail",
        "Restaurant",
        "Agriculture"
    ]
)

st.markdown("---")

# ==========================================
# INDUSTRY INPUT
# ==========================================

industry_bonus = 0

if business_type == "Restaurant":

    st.subheader("🍽 Restaurant Indicators")

    food_cost = st.slider(
        "Food Cost (%)",
        20,
        80,
        35
    )

elif business_type == "Retail":

    st.subheader("🏪 Retail Indicators")

    inventory_turnover = st.slider(
        "Inventory Turnover",
        1,
        20,
        8
    )

elif business_type == "Agriculture":

    st.subheader("🌾 Agriculture Indicators")

    crop_price_trend = st.slider(
        "Crop Price Trend (%)",
        -30,
        30,
        0
    )

# ==========================================
# BUSINESS DATA
# ==========================================

st.markdown("## Business Information")

revenue = st.number_input(
    "Monthly Revenue (THB)",
    min_value=0,
    value=100000
)

cost = st.number_input(
    "Monthly Cost (THB)",
    min_value=0,
    value=70000
)

cash = st.number_input(
    "Cash Reserve (THB)",
    min_value=0,
    value=50000
)

growth = st.slider(
    "Customer Growth (%)",
    -50,
    50,
    10
)

# ==========================================
# ANALYZE
# ==========================================

if st.button("🚀 Analyze Business"):

    score = 50

    # -------------------------
    # Profitability
    # -------------------------

    profit = revenue - cost

    if revenue > 0:
        profit_margin = profit / revenue
    else:
        profit_margin = 0

    if profit_margin > 0.30:
        score += 20

    elif profit_margin > 0.10:
        score += 10

    else:
        score -= 10

    # -------------------------
    # Cash Flow
    # -------------------------

    if cash > revenue:
        score += 15

    elif cash > revenue * 0.5:
        score += 10

    elif cash < revenue * 0.3:
        score -= 15

    # -------------------------
    # Customer Growth
    # -------------------------

    if growth > 10:
        score += 15

    elif growth > 0:
        score += 10

    else:
        score -= 15

    # -------------------------
    # Industry Logic
    # -------------------------

    if business_type == "Restaurant":

        if food_cost < 35:
            score += 10

        elif food_cost > 55:
            score -= 10

    elif business_type == "Retail":

        if inventory_turnover > 10:
            score += 10

        elif inventory_turnover < 5:
            score -= 10

    elif business_type == "Agriculture":

        if crop_price_trend > 10:
            score += 10

        elif crop_price_trend < -10:
            score -= 10

    score = max(0, min(score, 100))

    # ==========================================
    # KPI SNAPSHOT
    # ==========================================

    st.markdown("---")
    st.subheader("📊 KPI Snapshot")

    k1, k2, k3 = st.columns(3)

    k1.metric(
        "Revenue",
        f"{revenue:,.0f}"
    )

    k2.metric(
        "Profit",
        f"{profit:,.0f}"
    )

    k3.metric(
        "Growth %",
        f"{growth}%"
    )

    # ==========================================
    # RISK DASHBOARD
    # ==========================================

    st.markdown("---")
    st.subheader("🛡 Business Risk Dashboard")

    financial_risk = 100
    marketing_risk = 100
    operational_risk = 100

    if cash < revenue * 0.3:
        financial_risk -= 50

    if growth < 0:
        marketing_risk -= 50

    if revenue < cost:
        operational_risk -= 50

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Financial Risk",
        f"{financial_risk}/100"
    )

    c2.metric(
        "Marketing Risk",
        f"{marketing_risk}/100"
    )

    c3.metric(
        "Operational Risk",
        f"{operational_risk}/100"
    )

    # ==========================================
    # SURVIVAL SCORE
    # ==========================================

    st.markdown("---")
    st.subheader("📈 ZYRA Survival Score")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={
            "text": "Survival Score"
        },
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#198754"},
            "steps": [
                {
                    "range": [0, 40],
                    "color": "#dc3545"
                },
                {
                    "range": [40, 60],
                    "color": "#fd7e14"
                },
                {
                    "range": [60, 80],
                    "color": "#ffc107"
                },
                {
                    "range": [80, 100],
                    "color": "#198754"
                }
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==========================================
    # OVERALL STATUS
    # ==========================================

    st.subheader("🎯 Overall Risk Level")

    if score >= 80:

        st.success(
            "🟢 LOW RISK"
        )

    elif score >= 60:

        st.warning(
            "🟠 MEDIUM RISK"
        )

    else:

        st.error(
            "🔴 HIGH RISK"
        )

    # ==========================================
    # EXECUTIVE SUMMARY
    # ==========================================

    st.markdown("---")
    st.subheader("📋 Executive Summary")

    if score >= 80:

        st.success(
            """
Business performance is healthy.

Current risk level is low and growth potential remains strong.
"""
        )

    elif score >= 60:

        st.warning(
            """
Business performance is stable but requires monitoring.
"""
        )

    else:

        st.error(
            """
Business is exposed to significant risk.

Corrective action is recommended immediately.
"""
        )

    # ==========================================
    # EARLY WARNING
    # ==========================================

    st.markdown("---")
    st.subheader("⚠️ Early Warning")

    risk_found = False

    if growth < 0:

        st.error(
            "Customer growth is declining"
        )

        risk_found = True

    if cash < revenue * 0.3:

        st.error(
            "Cash flow risk detected"
        )

        risk_found = True

    if revenue < cost:

        st.error(
            "Business is operating at a loss"
        )

        risk_found = True

    if not risk_found:

        st.success(
            "No significant risk detected"
        )

    # ==========================================
    # RECOMMENDATION
    # ==========================================

    st.markdown("---")
    st.subheader("💡 ZYRA Recommendations")

    if growth < 0:

        st.write(
            "✅ Improve customer retention programs"
        )

    if cash < revenue * 0.3:

        st.write(
            "✅ Increase cash reserve"
        )

    if revenue < cost:

        st.write(
            "✅ Review pricing strategy and reduce operating costs"
        )

    if not risk_found:

        st.write(
            "✅ Continue current strategy and monitor performance"
        )

    # ==========================================
    # GROWTH OPPORTUNITY
    # ==========================================

    st.markdown("---")
    st.subheader("🚀 Growth Opportunity")

    if business_type == "Restaurant":

        st.info(
            "Opportunity: Increase repeat customers and optimize food cost."
        )

    elif business_type == "Retail":

        st.info(
            "Opportunity: Improve inventory turnover and sales conversion."
        )

    elif business_type == "Agriculture":

        st.info(
            "Opportunity: Monitor crop price trends and diversify sales channels."
        )

    st.markdown("---")

    st.caption(
        "ZYRA Prototype Version 1.0 | SME Early Warning & Survival Intelligence Platform"
    )
