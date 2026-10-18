import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ZYRA Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 แดชบอร์ดภาพรวมธุรกิจ")

st.markdown("""
ติดตามผลการวิเคราะห์ ความเสี่ยง และแนวโน้มของธุรกิจ
เพื่อสนับสนุนการตัดสินใจของผู้ประกอบการ
""")

# =====================================
# SUMMARY KPIs
# =====================================

st.subheader("ภาพรวมปัจจุบัน")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Business Health Index",
    "82/100",
    "+2"
)

c2.metric(
    "ระดับความเสี่ยง",
    "ต่ำ"
)

c3.metric(
    "สถานะล่าสุด",
    "แข็งแรง"
)

c4.metric(
    "การเติบโต",
    "+12%"
)

# =====================================
# TREND CHART
# =====================================

st.markdown("---")

st.subheader("📈 แนวโน้มคะแนนสุขภาพธุรกิจ")

trend_data = pd.DataFrame({
    "รอบการวิเคราะห์":[
        "รอบ 1",
        "รอบ 2",
        "รอบ 3",
        "รอบ 4",
        "รอบ 5"
    ],
    "คะแนน":[
        68,
        72,
        74,
        80,
        82
    ]
})

fig = px.line(
    trend_data,
    x="รอบการวิเคราะห์",
    y="คะแนน",
    markers=True
)

fig.update_layout(
    height=400
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# ALERT CENTER
# =====================================

st.markdown("---")

st.subheader("⚠️ ศูนย์แจ้งเตือน")

st.warning(
    "ต้นทุนดำเนินงานเพิ่มขึ้นจากรอบก่อน 8%"
)

st.info(
    "ธุรกิจยังอยู่ในระดับความเสี่ยงต่ำ"
)

# =====================================
# EXECUTIVE SUMMARY
# =====================================

st.markdown("---")

st.subheader("📋 สรุปสำหรับผู้บริหาร")

st.success(
"""
ธุรกิจมีแนวโน้มปรับตัวดีขึ้นอย่างต่อเนื่อง

คะแนนสุขภาพธุรกิจเพิ่มขึ้นจาก 68 เป็น 82 คะแนน
สะท้อนถึงการเติบโตและการบริหารสภาพคล่องที่ดีขึ้น
"""
)

# =====================================
# HEALTH DIMENSIONS
# =====================================

st.markdown("---")

st.subheader("🩺 สุขภาพธุรกิจรายด้าน")

h1, h2, h3, h4 = st.columns(4)

h1.metric(
    "ด้านการเงิน",
    "88"
)

h2.metric(
    "ด้านการตลาด",
    "76"
)

h3.metric(
    "ด้านการดำเนินงาน",
    "81"
)

h4.metric(
    "ด้านการเติบโต",
    "74"
)

# =====================================
# BUSINESS STATUS
# =====================================

st.markdown("---")

status_data = pd.DataFrame(
    {
        "หมวด":[
            "การเงิน",
            "การตลาด",
            "การดำเนินงาน",
            "การเติบโต"
        ],
        "คะแนน":[
            88,
            76,
            81,
            74
        ]
    }
)

fig2 = px.bar(
    status_data,
    x="หมวด",
    y="คะแนน",
    color="คะแนน",
    color_continuous_scale="Greens"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
