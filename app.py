import streamlit as st

st.set_page_config(
    page_title="ZYRA",
    page_icon="📈",
    layout="wide"
)

st.title("📈 ZYRA")
st.subheader("SME Early Warning & Survival Intelligence Platform")

business_type = st.selectbox(
    "Business Type",
    ["Retail", "Restaurant", "Agriculture"]
)

revenue = st.number_input(
    "Monthly Revenue (THB)",
    value=100000
)

cost = st.number_input(
    "Monthly Cost (THB)",
    value=70000
)

cash = st.number_input(
    "Cash Reserve (THB)",
    value=50000
)

growth = st.slider(
    "Customer Growth (%)",
    -50,
    50,
    10
)

if st.button("Analyze"):

    score = 50

    if revenue > cost:
        score += 20

    if cash > revenue * 0.3:
        score += 15

    if growth > 0:
        score += 15

    score = min(score, 100)

    st.metric(
        "ZYRA Survival Score",
        f"{score}/100"
    )

    if score >= 80:
        st.success("Healthy Business")
    elif score >= 60:
        st.warning("Moderate Risk")
    else:
        st.error("High Risk")
st.markdown("---")

st.subheader("⚠️ Early Warning")

risk_found = False

if growth < 0:
    st.error("Customer growth is declining")
    risk_found = True

if cash < revenue * 0.3:
    st.error("Cash flow risk detected")
    risk_found = True

if revenue < cost:
    st.error("Business is operating at a loss")
    risk_found = True

if not risk_found:
    st.success("No significant risk detected")


st.markdown("---")

st.subheader("💡 ZYRA Recommendations")

if growth < 0:
    st.write("✅ Improve customer retention programs")

if cash < revenue * 0.3:
    st.write("✅ Increase cash reserve")

if revenue < cost:
    st.write("✅ Review pricing strategy and reduce operating costs")

if not risk_found:
    st.write("✅ Continue current strategy and monitor performance")
    
