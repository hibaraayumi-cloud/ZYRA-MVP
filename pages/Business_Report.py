import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils.history import load_history

st.set_page_config(
    page_title="Business Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 รายงานสรุปสำหรับผู้บริหาร")

st.markdown("""
รายงานสรุปผลจากการวิเคราะห์ล่าสุด

จัดทำขึ้นเพื่อใช้ประกอบการตัดสินใจทางธุรกิจ
และติดตามสุขภาพธุรกิจในภาพรวม
""")

# =====================================
# LOAD DATA
# =====================================

df = load_history()

if df.empty:

    st.warning(
        """
ยังไม่มีข้อมูลการวิเคราะห์

กรุณาไปที่เมนู "Risk Analysis"
และวิเคราะห์ธุรกิจอย่างน้อย 1 ครั้ง
"""
    )

    st.stop()

# =====================================
# GET LATEST DATA
# =====================================

latest = df.iloc[-1]

business_type = latest["business_type"]

revenue = float(latest["revenue"])

cost = float(latest["cost"])

cash = float(latest["cash"])

growth = float(latest["growth"])

score = float(latest["score"])

profit = revenue - cost

if revenue > 0:
    profit_margin = (profit / revenue) * 100
else:
    profit_margin = 0

# =====================================
# HEALTH INDEX
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
# KPI SNAPSHOT
# =====================================

st.markdown("---")

st.subheader("📊 ตัวชี้วัดสำคัญ")

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "รายได้",
    f"{revenue:,.0f} บาท"
)

k2.metric(
    "กำไร",
    f"{profit:,.0f} บาท"
)

k3.metric(
    "อัตรากำไร",
    f"{profit_margin:.1f}%"
)

k4.metric(
    "การเติบโต",
    f"{growth:.0f}%"
)

# =====================================
# HEALTH STATUS
# =====================================

st.markdown("---")

st.subheader("🎯 ระดับความเสี่ยง")

if score >= 80:

    level = "ความเสี่ยงต่ำ"

    st.success(
        f"🟢 {level}"
    )

elif score >= 60:

    level = "ความเสี่ยงปานกลาง"

    st.warning(
        f"🟠 {level}"
    )

else:

    level = "ความเสี่ยงสูง"

    st.error(
        f"🔴 {level}"
    )

# =====================================
# EXECUTIVE SUMMARY
# =====================================

st.markdown("---")

st.subheader("📋 สรุปสำหรับผู้บริหาร")

if score >= 80:

    st.success(f"""
ธุรกิจประเภท {business_type}

มีดัชนีสุขภาพธุรกิจอยู่ที่ {score:.0f} คะแนน

สะท้อนถึงความสามารถในการดำเนินธุรกิจ
สภาพคล่อง และการเติบโตที่อยู่ในเกณฑ์ดี

สามารถรักษาแนวทางดำเนินงานปัจจุบัน
และมุ่งเน้นการสร้างการเติบโตเพิ่มเติมได้
""")

elif score >= 60:

    st.warning(f"""
ธุรกิจประเภท {business_type}

มีดัชนีสุขภาพธุรกิจอยู่ที่ {score:.0f} คะแนน

ยังสามารถดำเนินงานได้ตามปกติ

แต่ควรติดตามปัจจัยเสี่ยง
และบริหารต้นทุนอย่างต่อเนื่อง
""")

else:

    st.error(f"""
ธุรกิจประเภท {business_type}

มีดัชนีสุขภาพธุรกิจอยู่ที่ {score:.0f} คะแนน

ควรเร่งปรับปรุงด้านการเงิน
สภาพคล่อง และการดำเนินงาน
เพื่อลดความเสี่ยงในอนาคต
""")

# =====================================
# RISK SUMMARY
# =====================================

st.markdown("---")

st.subheader("⚠️ ประเด็นที่ควรติดตาม")

risk_list = []

if cash < revenue * 0.3:

    risk_list.append(
        "เงินสดสำรองต่ำกว่าระดับที่แนะนำ"
    )

if revenue < cost:

    risk_list.append(
        "ต้นทุนสูงกว่ารายได้"
    )

if growth < 0:

    risk_list.append(
        "การเติบโตของลูกค้าอยู่ในทิศทางลดลง"
    )

if len(risk_list) == 0:

    st.success(
        "ยังไม่พบประเด็นความเสี่ยงที่สำคัญ"
    )

else:

    for item in risk_list:

        st.warning(item)

# =====================================
# RECOMMENDATIONS
# =====================================

st.markdown("---")

st.subheader("💡 แนวทางที่แนะนำ")

if growth < 0:

    st.write(
        "✅ จัดทำกิจกรรมรักษาฐานลูกค้าและเพิ่มการกลับมาซื้อซ้ำ"
    )

if cash < revenue * 0.3:

    st.write(
        "✅ เพิ่มเงินสดสำรองเพื่อรองรับความผันผวน"
    )

if revenue < cost:

    st.write(
        "✅ ทบทวนต้นทุนและปรับปรุงประสิทธิภาพการดำเนินงาน"
    )

if len(risk_list) == 0:

    st.write(
        "✅ รักษากลยุทธ์ปัจจุบันและติดตามผลอย่างสม่ำเสมอ"
    )

# =====================================
# REPORT INFORMATION
# =====================================

st.markdown("---")

report_df = pd.DataFrame(
    {
        "รายการ": [
            "ประเภทธุรกิจ",
            "รายได้",
            "ต้นทุน",
            "เงินสดสำรอง",
            "การเติบโต",
            "คะแนนสุขภาพธุรกิจ"
        ],
        "ค่า": [
            business_type,
            f"{revenue:,.0f}",
            f"{cost:,.0f}",
            f"{cash:,.0f}",
            f"{growth:.0f}%",
            f"{score:.0f}"
        ]
    }
)

st.dataframe(
    report_df,
    use_container_width=True
)

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "ZYRA Executive Business Report | Real Analysis Data"
)
