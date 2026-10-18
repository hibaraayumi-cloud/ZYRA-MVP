import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="ZYRA Risk Analysis",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ การวิเคราะห์ความเสี่ยงทางธุรกิจ")

st.markdown("""
ประเมินสุขภาพธุรกิจ ความเสี่ยง และโอกาสในการเติบโต
โดยอาศัยข้อมูลทางการเงิน การตลาด และปัจจัยเฉพาะอุตสาหกรรม
""")

# ==========================================
# BUSINESS TYPE
# ==========================================

business_type = st.selectbox(
    "ประเภทธุรกิจ",
    [
        "ค้าปลีก (Retail)",
        "ร้านอาหาร (Restaurant)",
        "เกษตรกรรม (Agriculture)"
    ]
)

st.markdown("---")

# ==========================================
# INDUSTRY INPUT
# ==========================================

industry_score = 0

if "Restaurant" in business_type:

    st.subheader("🍽 ข้อมูลเฉพาะธุรกิจร้านอาหาร")

    food_cost = st.slider(
        "ต้นทุนวัตถุดิบ (%)",
        20,
        80,
        35
    )

    if food_cost < 35:
        industry_score += 10

    elif food_cost > 55:
        industry_score -= 10

elif "Retail" in business_type:

    st.subheader("🏪 ข้อมูลเฉพาะธุรกิจค้าปลีก")

    inventory_turnover = st.slider(
        "อัตราหมุนเวียนสินค้า",
        1,
        20,
        8
    )

    if inventory_turnover > 10:
        industry_score += 10

    elif inventory_turnover < 5:
        industry_score -= 10

elif "Agriculture" in business_type:

    st.subheader("🌾 ข้อมูลเฉพาะธุรกิจเกษตร")

    crop_price_trend = st.slider(
        "แนวโน้มราคาพืชผล (%)",
        -30,
        30,
        0
    )

    if crop_price_trend > 10:
        industry_score += 10

    elif crop_price_trend < -10:
        industry_score -= 10

# ==========================================
# BUSINESS INPUT
# ==========================================

st.markdown("## ข้อมูลพื้นฐานทางธุรกิจ")

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

# ==========================================
# FORMULA
# ==========================================

with st.expander("ℹ วิธีการประเมินคะแนน"):

    st.markdown("""
คะแนนสุขภาพธุรกิจคำนวณจาก

- ความสามารถในการทำกำไร (40%)
- สภาพคล่องทางการเงิน (30%)
- การเติบโตของลูกค้า (20%)
- ปัจจัยเฉพาะอุตสาหกรรม (10%)

ยิ่งคะแนนสูง ยิ่งแสดงถึงความแข็งแรงและความพร้อมในการเติบโต
""")

# ==========================================
# ANALYZE
# ==========================================

if st.button("🚀 วิเคราะห์ธุรกิจ"):

    score = 50

    profit = revenue - cost

    if revenue > 0:
        profit_margin = profit / revenue
    else:
        profit_margin = 0

    # Profitability

    if profit_margin > 0.30:
        score += 20

    elif profit_margin > 0.10:
        score += 10

    else:
        score -= 10

    # Liquidity

    if cash > revenue:
        score += 15

    elif cash > revenue * 0.5:
        score += 10

    elif cash < revenue * 0.3:
        score -= 15

    # Growth

    if growth > 10:
        score += 15

    elif growth > 0:
        score += 10

    else:
        score -= 15

    score += industry_score

    score = max(0, min(score, 100))

    # =====================================
    # OVERVIEW
    # =====================================

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "รายได้",
        f"{revenue:,.0f}"
    )

    c2.metric(
        "กำไร",
        f"{profit:,.0f}"
    )

    c3.metric(
        "การเติบโต",
        f"{growth}%"
    )

    # =====================================
    # SCORE
    # =====================================

    st.subheader("📈 ดัชนีสุขภาพธุรกิจ")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text":"Business Health Index"},
        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"#0B8457"},
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

    if score >= 80:

        st.success(
            "🟢 ระดับความเสี่ยงต่ำ"
        )

    elif score >= 60:

        st.warning(
            "🟠 ระดับความเสี่ยงปานกลาง"
        )

    else:

        st.error(
            "🔴 ระดับความเสี่ยงสูง"
        )

    # =====================================
    # ROOT CAUSE
    # =====================================

    st.markdown("---")
    st.subheader("🔍 สาเหตุสำคัญที่พบ")

    found = False

    if cash < revenue * 0.3:
        found = True
        st.write(
            "• เงินสดสำรองต่ำกว่าระดับที่แนะนำ"
        )

    if revenue < cost:
        found = True
        st.write(
            "• ต้นทุนสูงกว่ารายได้"
        )

    if growth < 0:
        found = True
        st.write(
            "• การเติบโตของลูกค้าลดลง"
        )

    if not found:
        st.write(
            "• ไม่พบความเสี่ยงสำคัญในปัจจุบัน"
        )

    # =====================================
    # RECOMMENDATION
    # =====================================

    st.markdown("---")

    st.subheader("💡 แนวทางที่แนะนำ")

    if growth < 0:
        st.write(
            "✅ เพิ่มกิจกรรมรักษาฐานลูกค้าเดิมและสร้างการกลับมาซื้อซ้ำ"
        )

    if cash < revenue * 0.3:
        st.write(
            "✅ เพิ่มสภาพคล่องและเงินสดสำรอง"
        )

    if revenue < cost:
        st.write(
            "✅ ทบทวนต้นทุนและปรับกลยุทธ์ราคา"
        )

    if not found:
        st.write(
            "✅ ดำเนินธุรกิจตามแผนปัจจุบันและติดตามผลอย่างต่อเนื่อง"
        )

    # =====================================
    # EXECUTIVE SUMMARY
    # =====================================

    st.markdown("---")

    st.subheader("📋 สรุปสถานะธุรกิจ")

    if score >= 80:

        st.success("""
ธุรกิจมีผลการดำเนินงานอยู่ในระดับดี

มีความสามารถในการทำกำไรและสภาพคล่องทางการเงินที่เหมาะสม
ควรติดตามผลอย่างต่อเนื่องและสร้างโอกาสการเติบโตเพิ่มเติม
""")

    elif score >= 60:

        st.warning("""
ธุรกิจสามารถดำเนินงานได้ตามปกติ

แต่ควรเฝ้าระวังความเสี่ยงบางประการ
และมีแผนรองรับล่วงหน้า
""")

    else:

        st.error("""
ธุรกิจมีความเสี่ยงในระดับสูง

ควรเร่งปรับปรุงด้านการเงิน การตลาด
หรือการดำเนินงานโดยเร็ว
""")
