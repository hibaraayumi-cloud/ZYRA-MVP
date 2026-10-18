import streamlit as st
import pandas as pd
import plotly.express as px

from utils.history import load_history

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 แดชบอร์ดภาพรวมธุรกิจ")

st.markdown("""
ติดตามผลการวิเคราะห์ แนวโน้มความเสี่ยง
และสุขภาพธุรกิจจากข้อมูลจริงที่บันทึกในระบบ
""")

# ======================================
# LOAD DATA
# ======================================

df = load_history()

# ======================================
# NO DATA
# ======================================

if df.empty:

    st.warning(
        """
ยังไม่มีข้อมูลการวิเคราะห์

กรุณาไปที่เมนู "Risk Analysis"
และกดวิเคราะห์ธุรกิจอย่างน้อย 1 ครั้ง
"""
    )

    st.stop()

# ======================================
# LATEST DATA
# ======================================

latest = df.iloc[-1]

latest_score = latest["score"]

revenue = latest["revenue"]

cost = latest["cost"]

cash = latest["cash"]

growth = latest["growth"]

business_type = latest["business_type"]

profit = revenue - cost

# ======================================
# KPI OVERVIEW
# ======================================

st.subheader("ภาพรวมธุรกิจล่าสุด")

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Business Health Index",
    f"{latest_score:.0f}/100"
)

k2.metric(
    "กำไร",
    f"{profit:,.0f} บาท"
)

k3.metric(
    "การเติบโต",
    f"{growth}%"
)

k4.metric(
    "ประเภทธุรกิจ",
    business_type
)

# ======================================
# HEALTH STATUS
# ======================================

st.markdown("---")

st.subheader("🩺 สถานะสุขภาพธุรกิจ")

if latest_score >= 80:

    st.success(
        "ธุรกิจอยู่ในเกณฑ์แข็งแรง"
    )

elif latest_score >= 60:

    st.warning(
        "ธุรกิจอยู่ในกลุ่มเฝ้าระวัง"
    )

else:

    st.error(
        "ธุรกิจอยู่ในกลุ่มความเสี่ยงสูง"
    )

# ======================================
# TREND CHART
# ======================================

st.markdown("---")

st.subheader("📈 แนวโน้มคะแนนสุขภาพธุรกิจ")

trend_df = df.copy()

trend_df["analysis_no"] = list(
    range(
        1,
        len(df) + 1
    )
)

fig = px.line(
    trend_df,
    x="analysis_no",
    y="score",
    markers=True
)

fig.update_layout(
    xaxis_title="ครั้งที่วิเคราะห์",
    yaxis_title="คะแนน",
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================================
# SCORE DISTRIBUTION
# ======================================

st.markdown("---")

st.subheader("🎯 คะแนนรอบล่าสุด")

score_chart = pd.DataFrame(
    {
        "หมวด":[
            "Business Health"
        ],
        "คะแนน":[
            latest_score
        ]
    }
)

fig2 = px.bar(
    score_chart,
    x="หมวด",
    y="คะแนน",
    color="คะแนน",
    color_continuous_scale="Greens"
)

fig2.update_layout(
    height=350
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ======================================
# EXECUTIVE SUMMARY
# ======================================

st.markdown("---")

st.subheader("📋 สรุปสำหรับผู้บริหาร")

if latest_score >= 80:

    st.success(
        f"""
จากผลการวิเคราะห์ล่าสุด

ธุรกิจมีคะแนนสุขภาพธุรกิจอยู่ที่ {latest_score:.0f}/100

สะท้อนถึงความสามารถในการดำเนินธุรกิจ
สภาพคล่อง และการเติบโตที่อยู่ในระดับดี
"""
    )

elif latest_score >= 60:

    st.warning(
        f"""
จากผลการวิเคราะห์ล่าสุด

ธุรกิจมีคะแนนสุขภาพธุรกิจอยู่ที่ {latest_score:.0f}/100

ควรติดตามปัจจัยเสี่ยงด้านการเงิน
และการเติบโตอย่างต่อเนื่อง
"""
    )

else:

    st.error(
        f"""
จากผลการวิเคราะห์ล่าสุด

ธุรกิจมีคะแนนสุขภาพธุรกิจอยู่ที่ {latest_score:.0f}/100

ควรเร่งจัดการปัจจัยเสี่ยง
และปรับปรุงประสิทธิภาพการดำเนินงาน
"""
    )

# ======================================
# LAST ANALYSIS
# ======================================

st.markdown("---")

st.subheader("🗂 ผลการวิเคราะห์ล่าสุด")

show_df = pd.DataFrame(
    {
        "รายการ":[
            "ประเภทธุรกิจ",
            "รายได้",
            "ต้นทุน",
            "เงินสดสำรอง",
            "การเติบโตของลูกค้า",
            "คะแนนสุขภาพธุรกิจ"
        ],

        "ค่า":[
            business_type,
            f"{revenue:,.0f}",
            f"{cost:,.0f}",
            f"{cash:,.0f}",
            f"{growth}%",
            f"{latest_score:.0f}"
        ]
    }
)

st.dataframe(
    show_df,
    use_container_width=True
)

# ======================================
# HISTORY
# ======================================

st.markdown("---")

st.subheader("📚 ประวัติการวิเคราะห์")

st.dataframe(
    df.sort_values(
        "date",
        ascending=False
    ),
    use_container_width=True
)

# ======================================
# FOOTER
# ======================================

st.markdown("---")

st.caption(
    "ZYRA Dashboard | Connected to Analysis History"
)
