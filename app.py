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
