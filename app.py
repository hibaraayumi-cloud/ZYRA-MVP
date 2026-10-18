import streamlit as st
import plotly.graph_objects as go

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="ZYRA",
    page_icon="📈",
    layout="wide"
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📈 ZYRA")

st.sidebar.caption(
    "Business Health Intelligence Platform"
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
ระบบวิเคราะห์สุขภาพธุรกิจ
และความเสี่ยงเชิงธุรกิจ
สำหรับผู้ประกอบการ SME
"""
)

st.sidebar.markdown("---")

st.sidebar.success("เวอร์ชัน 2.0")

# =====================================
# HEADER
# =====================================

st.title("📈 ZYRA")

st.markdown("""
### ระบบวิเคราะห์สุขภาพธุรกิจและสัญญาณเตือนความเสี่ยงสำหรับ SME

ZYRA ช่วยประเมินสถานะทางธุรกิจ วิเคราะห์ความเสี่ยง
และเสนอแนวทางดำเนินการเบื้องต้นจากข้อมูลธุรกิจ
เพื่อสนับสนุนการตัดสินใจของผู้ประกอบการ
""")

st.markdown("---")

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

# =====================================
# GUIDE
# =====================================

with st.expander("ℹ วิธีคำนวณคะแนน"):

    st.markdown("""
คะแนนสุขภาพธุรกิจ (Business Health Index)

ประกอบด้วย

- ความสามารถในการทำกำไร 40%
- สภาพคล่องทางการเงิน 30%
- การเติบโตของลูกค้า 20%
- ปัจจัยเฉพาะอุตสาหกรรม 10%

คะแนนยิ่งสูง แสดงถึงความแข็งแรงของธุรกิจ
""")

# =====================================
# INDUSTRY INPUT
# =====================================

st.markdown("---")

industry_bonus = 0

if business_type == "Restaurant":

    st.subheader("🍽 ตัวชี้วัดธุรกิจร้านอาหาร")

    food_cost = st.slider(
        "สัดส่วนต้นทุนวัตถุดิบ (%)",
        20,
        80,
        35
    )

elif business_type == "Retail":

    st.subheader("🏪 ตัวชี้วัดธุรกิจค้าปลีก")

    inventory_turnover = st.slider(
        "อัตราการหมุนเวียนสินค้า",
        1,
        20,
        8
    )

elif business_type == "Agriculture":

    st.subheader("🌾 ตัวชี้วัดธุรกิจเกษตร")

    crop_price_trend = st.slider(
        "แนวโน้มราคาพืชผล (%)",
        -30,
        30,
        0
    )

# =====================================
# INPUTS
# =====================================

st.markdown("## ข้อมูลธุรกิจ")

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
    "เงินสดสำรองสำหรับดำเนินธุรกิจ (บาท)",
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
# ANALYZE
# =====================================

if st.button("🚀 วิเคราะห์ธุรกิจ"):

    score = 50

    profit = revenue - cost

    if revenue > 0:
        profit_margin = profit / revenue
    else:
        profit_margin = 0

    # ------------------------
    # PROFITABILITY
    # ------------------------

    if profit_margin > 0.30:
        score += 20

    elif profit_margin > 0.10:
        score += 10

    else:
        score -= 10

    # ------------------------
    # LIQUIDITY
    # ------------------------

    if cash > revenue:
        score += 15

    elif cash > revenue * 0.5:
        score += 10

    elif cash < revenue * 0.3:
        score -= 15

    # ------------------------
    # CUSTOMER GROWTH
    # ------------------------

    if growth > 10:
        score += 15

    elif growth > 0:
        score += 10

    else:
        score -= 15

    # ------------------------
    # INDUSTRY LOGIC
    # ------------------------

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

    # =====================================
    # KPI SNAPSHOT
    # =====================================

    st.markdown("---")
    st.subheader("📊 ภาพรวมตัวชี้วัด")

    k1, k2, k3 = st.columns(3)

    k1.metric(
        "รายได้",
        f"{revenue:,.0f}"
    )

    k2.metric(
        "กำไร",
        f"{profit:,.0f}"
    )

    k3.metric(
        "การเติบโตของลูกค้า",
        f"{growth}%"
    )

    # =====================================
    # BUSINESS HEALTH
    # =====================================

    st.markdown("---")
    st.subheader("🩺 สุขภาพธุรกิจรายด้าน")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("การเงิน", 88)
    c2.metric("การตลาด", 76)
    c3.metric("การดำเนินงาน", 81)
    c4.metric("การเติบโต", 74)

    # =====================================
    # RISK DASHBOARD
    # =====================================

    st.markdown("---")
    st.subheader("🛡 แผงควบคุมความเสี่ยง")

    financial_risk = 100
    marketing_risk = 100
    operational_risk = 100

    if cash < revenue * 0.3:
        financial_risk -= 50

    if growth < 0:
        marketing_risk -= 50

    if revenue < cost:
        operational_risk -= 50

    r1, r2, r3 = st.columns(3)

    r1.metric("ความเสี่ยงด้านการเงิน", financial_risk)
    r2.metric("ความเสี่ยงด้านการตลาด", marketing_risk)
    r3.metric("ความเสี่ยงด้านการดำเนินงาน", operational_risk)

    # =====================================
    # BUSINESS HEALTH INDEX
    # =====================================

    st.markdown("---")
    st.subheader("📈 ดัชนีสุขภาพธุรกิจ")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Business Health Index"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#0B8457"},
            "steps": [
                {"range": [0, 40], "color": "#dc3545"},
                {"range": [40, 60], "color": "#fd7e14"},
                {"range": [60, 80], "color": "#ffc107"},
                {"range": [80, 100], "color": "#198754"}
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # OVERALL STATUS
    # =====================================

    st.subheader("🎯 ระดับความเสี่ยงโดยรวม")

    if score >= 80:

        st.success(
            "🟢 ความเสี่ยงต่ำ"
        )

    elif score >= 60:

        st.warning(
            "🟠 ความเสี่ยงปานกลาง"
        )

    else:

        st.error(
            "🔴 ความเสี่ยงสูง"
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
สามารถเติบโตต่อได้ภายใต้การติดตามความเสี่ยงอย่างสม่ำเสมอ
""")

    elif score >= 60:

        st.warning("""
ธุรกิจยังสามารถดำเนินงานได้ตามปกติ

อย่างไรก็ตาม ควรติดตามปัจจัยเสี่ยงบางประการ
และวางแผนป้องกันล่วงหน้า
""")

    else:

        st.error("""
ธุรกิจมีความเสี่ยงในระดับสูง

ควรเร่งปรับปรุงประสิทธิภาพการดำเนินงาน
และบริหารสภาพคล่องโดยเร็ว
""")

    # =====================================
    # EARLY WARNING
    # =====================================

    st.markdown("---")
    st.subheader("⚠️ สัญญาณเตือนความเสี่ยง")

    risk_found = False

    if growth < 0:

        st.error(
            "อัตราการเติบโตของลูกค้าอยู่ในทิศทางลดลง"
        )

        risk_found = True

    if cash < revenue * 0.3:

        st.error(
            "เงินสดสำรองต่ำกว่าระดับที่แนะนำ"
        )

        risk_found = True

    if revenue < cost:

        st.error(
            "ต้นทุนสูงกว่ารายได้"
        )

        risk_found = True

    if not risk_found:

        st.success(
            "ยังไม่พบความเสี่ยงที่มีนัยสำคัญ"
        )

    # =====================================
    # ROOT CAUSE
    # =====================================

    st.markdown("---")
    st.subheader("🔍 สาเหตุสำคัญของความเสี่ยง")

    if cash < revenue * 0.3:
        st.write("• เงินสดสำรองต่ำกว่าระดับที่เหมาะสม")

    if revenue < cost:
        st.write("• ต้นทุนการดำเนินงานสูงกว่ารายได้")

    if growth < 0:
        st.write("• ฐานลูกค้ากำลังลดลง")

    if not risk_found:
        st.write("• ยังไม่พบปัจจัยเสี่ยงที่สำคัญ")

    # =====================================
    # RECOMMENDATION
    # =====================================

    st.markdown("---")
    st.subheader("💡 แนวทางที่แนะนำ")

    if growth < 0:
        st.write("✅ จัดทำกิจกรรมรักษาฐานลูกค้า")

    if cash < revenue * 0.3:
        st.write("✅ เพิ่มเงินสดสำรองสำหรับดำเนินธุรกิจ")

    if revenue < cost:
        st.write("✅ ปรับปรุงต้นทุนและทบทวนกลยุทธ์ราคา")

    if not risk_found:
        st.write("✅ ดำเนินธุรกิจตามแผนปัจจุบันและติดตามผลต่อเนื่อง")

    # =====================================
    # GROWTH OPPORTUNITY
    # =====================================

    st.markdown("---")
    st.subheader("🚀 โอกาสในการเติบโต")

    if business_type == "Restaurant":

        st.info(
            "ควรเพิ่มสัดส่วนลูกค้าประจำและบริหารต้นทุนวัตถุดิบให้มีประสิทธิภาพมากขึ้น"
        )

    elif business_type == "Retail":

        st.info(
            "ควรเพิ่มอัตราการหมุนเวียนสินค้าและพัฒนาช่องทางการขาย"
        )

    elif business_type == "Agriculture":

        st.info(
            "ควรติดตามแนวโน้มราคาพืชผลและกระจายช่องทางจำหน่าย"
        )

    # =====================================
    # INDUSTRY BENCHMARK
    # =====================================

    st.markdown("---")

    st.subheader("🏆 เปรียบเทียบกับค่าเฉลี่ยอุตสาหกรรม")

    if business_type == "Restaurant":

        st.write("""
- ต้นทุนวัตถุดิบเฉลี่ยอุตสาหกรรม : 35%
- ธุรกิจที่มีผลการดำเนินงานดี : ต่ำกว่า 35%
""")

    elif business_type == "Retail":

        st.write("""
- อัตราหมุนเวียนสินค้าเฉลี่ย : 8 รอบ
- ธุรกิจที่มีผลการดำเนินงานดี : มากกว่า 10 รอบ
""")

    elif business_type == "Agriculture":

        st.write("""
- แนวโน้มราคาพืชผลเฉลี่ย : 0%
- ค่าบวกสะท้อนแนวโน้มที่ดีขึ้น
""")

    st.markdown("---")

    st.caption(
        "ZYRA Business Health Intelligence Platform | Prototype Version 2.0"
    )
