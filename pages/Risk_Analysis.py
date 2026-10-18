import streamlit as st

from utils.scoring import calculate_score
from utils.recommendation import get_recommendations
from utils.history import save_analysis

st.title("⚠️ การวิเคราะห์ความเสี่ยงธุรกิจ")

st.markdown("""
กรอกข้อมูลเพื่อประเมินสุขภาพธุรกิจ
และรับสัญญาณเตือนความเสี่ยงเบื้องต้น
""")

# ---------------------------------
# Business Type
# ---------------------------------

business_type = st.selectbox(
    "ประเภทธุรกิจ",
    [
        "Retail",
        "Restaurant",
        "Agriculture"
    ]
)

# ---------------------------------
# Industry Factor
# ---------------------------------

industry_value = 0

if business_type == "Restaurant":

    food_cost = st.slider(
        "ต้นทุนวัตถุดิบ (%)",
        20,
        80,
        35
    )

    if food_cost < 35:
        industry_value = 10
    elif food_cost > 55:
        industry_value = -10

elif business_type == "Retail":

    inventory_turnover = st.slider(
        "อัตราหมุนเวียนสินค้า",
        1,
        20,
        8
    )

    if inventory_turnover > 10:
        industry_value = 10

    elif inventory_turnover < 5:
        industry_value = -10

elif business_type == "Agriculture":

    crop_price_trend = st.slider(
        "แนวโน้มราคาพืชผล (%)",
        -30,
        30,
        0
    )

    if crop_price_trend > 10:
        industry_value = 10

    elif crop_price_trend < -10:
        industry_value = -10

# ---------------------------------
# Input
# ---------------------------------

revenue = st.number_input(
    "รายได้เฉลี่ยต่อเดือน (บาท)",
    value=100000
)

cost = st.number_input(
    "ต้นทุนเฉลี่ยต่อเดือน (บาท)",
    value=70000
)

cash = st.number_input(
    "เงินสดสำรอง (บาท)",
    value=50000
)

growth = st.slider(
    "อัตราการเติบโตของลูกค้า (%)",
    -50,
    50,
    10
)

# ---------------------------------
# Analyze
# ---------------------------------

if st.button("วิเคราะห์ธุรกิจ"):

    score = calculate_score(
        revenue,
        cost,
        cash,
        growth,
        business_type,
        industry_value
    )

    save_analysis(
        business_type,
        score
    )

    st.metric(
        "Business Health Index",
        f"{score}/100"
    )

    if score >= 80:

        st.success(
            "ธุรกิจอยู่ในเกณฑ์แข็งแรง"
        )

    elif score >= 60:

        st.warning(
            "ธุรกิจอยู่ในกลุ่มเฝ้าระวัง"
        )

    else:

        st.error(
            "ธุรกิจอยู่ในกลุ่มความเสี่ยงสูง"
        )

    # -----------------------------
    # Recommendation
    # -----------------------------

    st.markdown("---")
    st.subheader("แนวทางที่แนะนำ")

    rec = get_recommendations(
        revenue,
        cost,
        cash,
        growth
    )

    for r in rec:

        st.write(
            "✅",
            r
        )
