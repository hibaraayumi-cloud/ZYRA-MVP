import streamlit as st
import plotly.graph_objects as go

from utils.scoring import calculate_score
from utils.recommendation import get_recommendations
from utils.history import save_analysis

st.set_page_config(
    page_title="Risk Analysis",
    page_icon="⚠️",
    layout="wide"
)

# =====================================
# HEADER
# =====================================

st.title("⚠️ การวิเคราะห์ความเสี่ยงทางธุรกิจ")

st.markdown("""
ประเมินสุขภาพธุรกิจ ความเสี่ยง และโอกาสในการเติบโต
จากข้อมูลทางการเงิน การตลาด และปัจจัยเฉพาะอุตสาหกรรม
""")

# =====================================
# BUSINESS TYPE
# =====================================

business_type = st.selectbox(
    "ประเภทธุรกิจ",
    [
        "Retail",
        "Restaurant",
        "Agriculture"
    ]
)

st.markdown("---")

# =====================================
# INDUSTRY INPUTS
# =====================================

industry_value = 0

if business_type == "Restaurant":

    st.subheader("🍽 ตัวชี้วัดธุรกิจร้านอาหาร")

    food_cost = st.slider(
        "ต้นทุนวัตถุดิบ (%)",
        20,
        80,
        35
    )

    if food_cost < 35:
        industry_value += 10

    elif food_cost > 55:
        industry_value -= 10

elif business_type == "Retail":

    st.subheader("🏪 ตัวชี้วัดธุรกิจค้าปลีก")

    inventory_turnover = st.slider(
        "อัตราการหมุนเวียนสินค้า",
        1,
        20,
        8
    )

    if inventory_turnover > 10:
        industry_value += 10

    elif inventory_turnover < 5:
        industry_value -= 10

elif business_type == "Agriculture":

    st.subheader("🌾 ตัวชี้วัดธุรกิจเกษตรกรรม")

    crop_price_trend = st.slider(
        "แนวโน้มราคาพืชผล (%)",
        -30,
        30,
        0
    )

    if crop_price_trend > 10:
        industry_value += 10

    elif crop_price_trend < -10:
        industry_value -= 10

# =====================================
# BUSINESS INFORMATION
# =====================================

st.markdown("## ข้อมูลทางธุรกิจ")

revenue = st.number_input(
    "รายได้เฉลี่ยต่อเดือน (บาท)",
    min_value=0,
    value=100000
)

cost = st.number_input(
    "ต้นทุนเฉลี่ยต่อเดือน (บาท)",
    min_value=0,
    value=70000
)

cash = st.number_input(
    "เงินสดสำรอง (บาท)",
    min_value=0,
    value=50000
)

growth = st.slider(
    "อัตราการเติบโตของลูกค้า (%)",
    -50,
    50,
    10
)

# =====================================
# FORMULA EXPLANATION
# =====================================

with st.expander("ℹ วิธีการประเมินคะแนน"):

    st.markdown("""
### องค์ประกอบของคะแนนสุขภาพธุรกิจ

- ความสามารถในการทำกำไร
- สภาพคล่องทางการเงิน
- การเติบโตของลูกค้า
- ปัจจัยเฉพาะอุตสาหกรรม

คะแนนยิ่งสูง ยิ่งสะท้อนถึงความแข็งแรงของธุรกิจ
""")

# =====================================
# ANALYZE
# =====================================

if st.button("🚀 วิเคราะห์ธุรกิจ"):

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
        revenue,
        cost,
        cash,
        growth,
        score
    )

    profit = revenue - cost

    # =====================================
    # KPI SNAPSHOT
    # =====================================

    st.markdown("---")

    st.subheader("📊 ตัวชี้วัดสำคัญ")

    k1, k2, k3 = st.columns(3)

    k1.metric(
        "รายได้",
        f"{revenue:,.0f} บาท"
    )

    k2.metric(
        "กำไร",
        f"{profit:,.0f} บาท"
    )

    k3.metric(
        "การเติบโต",
        f"{growth}%"
    )

    # =====================================
    # HEALTH INDEX
    # =====================================

    st.markdown("---")

    st.subheader("📈 ดัชนีสุขภาพธุรกิจ")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={
            "text":"Business Health Index"
        },
        gauge={
            "axis": {"range":[0,100]},
            "bar": {"color":"#0B8457"},
            "steps":[
                {"range":[0,40],"color":"#dc3545"},
                {"range":[40,60],"color":"#fd7e14"},
                {"range":[60,80],"color":"#ffc107"},
                {"range":[80,100],"color":"#198754"}
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # RISK LEVEL
    # =====================================

    st.subheader("🎯 ระดับความเสี่ยงโดยรวม")

    if score >= 80:

        st.success(
            "🟢 ระดับความเสี่ยงต่ำ"
        )

        level = "LOW"

    elif score >= 60:

        st.warning(
            "🟠 ระดับความเสี่ยงปานกลาง"
        )

        level = "MEDIUM"

    else:

        st.error(
            "🔴 ระดับความเสี่ยงสูง"
        )

        level = "HIGH"

    # =====================================
    # ROOT CAUSE
    # =====================================

    st.markdown("---")

    st.subheader("🔍 ปัจจัยที่ต้องติดตาม")

    issue_found = False

    if cash < revenue * 0.3:

        st.warning(
            "เงินสดสำรองต่ำกว่าระดับที่แนะนำ"
        )

        issue_found = True

    if revenue < cost:

        st.warning(
            "ต้นทุนสูงกว่ารายได้"
        )

        issue_found = True

    if growth < 0:

        st.warning(
            "ลูกค้ามีแนวโน้มลดลง"
        )

        issue_found = True

    if not issue_found:

        st.success(
            "ยังไม่พบปัจจัยเสี่ยงที่สำคัญ"
        )

    # =====================================
    # RECOMMENDATION
    # =====================================

    st.markdown("---")

    st.subheader("💡 แนวทางที่แนะนำ")

    recommendations = get_recommendations(
        revenue,
        cost,
        cash,
        growth
    )

    for rec in recommendations:

        st.write(
            "✅",
            rec
        )

    # =====================================
    # EXECUTIVE SUMMARY
    # =====================================

    st.markdown("---")

    st.subheader("📋 สรุปสถานะธุรกิจ")

    if level == "LOW":

        st.success("""
ธุรกิจมีผลการดำเนินงานอยู่ในระดับดี

มีสภาพคล่องทางการเงินที่เหมาะสม
และสามารถเติบโตต่อได้ภายใต้การติดตามผลอย่างต่อเนื่อง
""")

    elif level == "MEDIUM":

        st.warning("""
ธุรกิจยังสามารถดำเนินงานได้ตามปกติ

แต่ควรเฝ้าระวังและจัดการความเสี่ยงบางประการ
เพื่อป้องกันผลกระทบในระยะยาว
""")

    else:

        st.error("""
ธุรกิจมีความเสี่ยงในระดับสูง

ควรปรับปรุงด้านการเงิน การตลาด
หรือการดำเนินงานโดยเร็ว
""")

    # =====================================
    # SAVE CONFIRMATION
    # =====================================

    st.markdown("---")

    st.success(
        "✅ บันทึกผลการวิเคราะห์ลงระบบเรียบร้อยแล้ว"
    )
