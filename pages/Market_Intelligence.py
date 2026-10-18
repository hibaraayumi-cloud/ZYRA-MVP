import streamlit as st
import pandas as pd
import plotly.express as px

from utils.weather import get_weather_data

st.set_page_config(
    page_title="Market Intelligence",
    page_icon="📈",
    layout="wide"
)

st.title("📈 ข่าวสารและแนวโน้มตลาด")

st.markdown("""
ติดตามปัจจัยภายนอกที่อาจส่งผลกระทบต่อธุรกิจ

ระบบต้นแบบ ZYRA เชื่อมโยงข้อมูลภายนอก
เพื่อใช้ประกอบการประเมินความเสี่ยงและโอกาสทางธุรกิจ
""")

# =====================================
# MARKET OVERVIEW
# =====================================

st.subheader("🌍 ภาพรวมสภาวะแวดล้อมทางธุรกิจ")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Market Demand",
    "+12%"
)

c2.metric(
    "Consumer Confidence",
    "74/100"
)

c3.metric(
    "Economic Risk",
    "Medium"
)

c4.metric(
    "Inflation Impact",
    "+3.1%"
)

# =====================================
# WEATHER DATA
# =====================================

st.markdown("---")

st.subheader("🌦 ข้อมูลสภาพอากาศปัจจุบัน")

weather = get_weather_data()

if weather:

    w1, w2, w3, w4 = st.columns(4)

    w1.metric(
        "อุณหภูมิ",
        f"{weather['temperature']} °C"
    )

    w2.metric(
        "ความชื้น",
        f"{weather['humidity']} %"
    )

    w3.metric(
        "ปริมาณฝน",
        f"{weather['rain']} mm"
    )

    w4.metric(
        "ความเร็วลม",
        f"{weather['wind']} km/h"
    )

    if weather["rain"] > 10:

        st.warning(
            "พบปริมาณฝนค่อนข้างสูง ควรติดตามผลกระทบต่อการดำเนินงาน"
        )

    elif weather["temperature"] > 35:

        st.warning(
            "อุณหภูมิอยู่ในระดับสูง อาจกระทบต้นทุนด้านพลังงานและการผลิต"
        )

    else:

        st.success(
            "ยังไม่พบความเสี่ยงด้านสภาพอากาศที่มีนัยสำคัญ"
        )

else:

    st.error(
        "ไม่สามารถเชื่อมต่อข้อมูลสภาพอากาศได้"
    )

# =====================================
# MARKET TREND
# =====================================

st.markdown("---")

st.subheader("📊 แนวโน้มตลาด")

trend_data = pd.DataFrame({
    "เดือน":[
        "ม.ค.",
        "ก.พ.",
        "มี.ค.",
        "เม.ย.",
        "พ.ค.",
        "มิ.ย."
    ],

    "ดัชนีความต้องการ":[
        65,
        68,
        71,
        75,
        78,
        82
    ]
})

fig = px.line(
    trend_data,
    x="เดือน",
    y="ดัชนีความต้องการ",
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
# EXTERNAL RISK MONITOR
# =====================================

st.markdown("---")

st.subheader("⚠️ ปัจจัยเสี่ยงภายนอก")

risk_df = pd.DataFrame({
    "ปัจจัย": [
        "สภาพอากาศ",
        "เศรษฐกิจ",
        "กำลังซื้อ",
        "ต้นทุนพลังงาน"
    ],

    "ระดับความเสี่ยง": [
        "ต่ำ",
        "ปานกลาง",
        "ต่ำ",
        "ปานกลาง"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True
)

# =====================================
# MANAGEMENT INSIGHT
# =====================================

st.markdown("---")

st.subheader("📋 ข้อสรุปสำหรับผู้บริหาร")

st.info(
"""
ภาพรวมปัจจัยภายนอกยังอยู่ในระดับที่เอื้อต่อการดำเนินธุรกิจ

อย่างไรก็ตาม ผู้ประกอบการควรติดตาม
แนวโน้มด้านเศรษฐกิจ ต้นทุน และสภาพอากาศ
อย่างต่อเนื่อง เพื่อใช้ประกอบการวางแผนระยะยาว
"""
)

# =====================================
# DATA SOURCES
# =====================================

st.markdown("---")

st.subheader("📚 แหล่งข้อมูล")

st.markdown("""
ข้อมูลในระบบพัฒนาจาก

- Open-Meteo Weather API
- ข้อมูลสาธารณะด้านเศรษฐกิจ
- ข้อมูลแนวโน้มตลาด

อ้างอิง:
https://open-meteo.com
""")

st.caption(
    "ZYRA Market Intelligence Module | Version 2.0"
)
