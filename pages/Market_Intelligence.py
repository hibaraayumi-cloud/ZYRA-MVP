import streamlit as st
import pandas as pd
import plotly.express as px

from utils.weather import get_weather_data
from utils.history import load_history

st.set_page_config(
    page_title="Market Intelligence",
    page_icon="📈",
    layout="wide"
)

st.title("📈 ข่าวสารและแนวโน้มตลาด")

st.markdown("""
รวบรวมปัจจัยภายนอกที่อาจส่งผลต่อธุรกิจ

ประกอบด้วย

• สภาพอากาศ

• ปัจจัยเศรษฐกิจ

• แนวโน้มตลาด

• ความเสี่ยงภายนอก

เพื่อใช้ประกอบการตัดสินใจทางธุรกิจ
""")

# =====================================
# LOAD BUSINESS DATA
# =====================================

df = load_history()

if df.empty:

    st.warning(
        """
ยังไม่มีข้อมูลการวิเคราะห์

กรุณาไปที่หน้า Risk Analysis
และวิเคราะห์ธุรกิจอย่างน้อย 1 ครั้ง
"""
    )

    st.stop()

latest = df.iloc[-1]

business_type = latest["business_type"]

score = float(latest["score"])

# =====================================
# WEATHER
# =====================================

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

else:

    st.error(
        "ไม่สามารถโหลดข้อมูลสภาพอากาศได้"
    )

# =====================================
# WEATHER RISK
# =====================================

st.markdown("---")

st.subheader("⚠️ ความเสี่ยงด้านสภาพอากาศ")

weather_risk = "ต่ำ"

if weather:

    if weather["rain"] > 10:

        weather_risk = "สูง"

        st.error(
            "ปริมาณฝนสูง อาจส่งผลต่อการดำเนินงาน"
        )

    elif weather["temperature"] > 35:

        weather_risk = "ปานกลาง"

        st.warning(
            "อุณหภูมิสูง อาจเพิ่มต้นทุนด้านพลังงาน"
        )

    else:

        st.success(
            "ไม่พบความเสี่ยงด้านสภาพอากาศที่มีนัยสำคัญ"
        )

# =====================================
# MARKET OVERVIEW
# =====================================

st.markdown("---")

st.subheader("🌍 ภาพรวมปัจจัยภายนอก")

m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "Market Demand",
    "+12%"
)

m2.metric(
    "Consumer Confidence",
    "74/100"
)

m3.metric(
    "Economic Outlook",
    "Stable"
)

m4.metric(
    "Weather Risk",
    weather_risk
)

# =====================================
# MARKET TREND
# =====================================

st.markdown("---")

st.subheader("📊 แนวโน้มสภาพตลาด")

market_df = pd.DataFrame({

    "เดือน":[
        "ม.ค.",
        "ก.พ.",
        "มี.ค.",
        "เม.ย.",
        "พ.ค.",
        "มิ.ย."
    ],

    "Market Index":[
        65,
        68,
        72,
        75,
        79,
        82
    ]
})

fig = px.line(
    market_df,
    x="เดือน",
    y="Market Index",
    markers=True
)

fig.update_layout(
    height=420
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# EXTERNAL RISK
# =====================================

st.markdown("---")

st.subheader("🛡 External Risk Monitor")

risk_df = pd.DataFrame({

    "ปัจจัย":[
        "สภาพอากาศ",
        "ภาวะเศรษฐกิจ",
        "กำลังซื้อ",
        "ต้นทุนพลังงาน"
    ],

    "ระดับความเสี่ยง":[
        weather_risk,
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
# INDUSTRY INSIGHT
# =====================================

st.markdown("---")

st.subheader("🏭 วิเคราะห์ตามประเภทธุรกิจ")

if business_type == "Restaurant":

    st.info(
        """
ธุรกิจร้านอาหารควรติดตาม

• ต้นทุนวัตถุดิบ

• กำลังซื้อผู้บริโภค

• จำนวนนักท่องเที่ยว

• ค่าใช้จ่ายด้านพลังงาน
"""
    )

elif business_type == "Retail":

    st.info(
        """
ธุรกิจค้าปลีกควรติดตาม

• กำลังซื้อ

• อัตราเงินเฟ้อ

• แนวโน้มการใช้จ่าย

• การแข่งขันในตลาด
"""
    )

else:

    st.info(
        """
ธุรกิจเกษตรควรติดตาม

• ปริมาณฝน

• อุณหภูมิ

• แนวโน้มราคาพืชผล

• ต้นทุนการผลิต
"""
    )

# =====================================
# MARKET OPPORTUNITY
# =====================================

st.markdown("---")

st.subheader("🚀 โอกาสทางธุรกิจ")

if score >= 80:

    st.success(
        """
ผลวิเคราะห์ชี้ว่าธุรกิจมีความพร้อม

สามารถขยายกิจการ
เพิ่มฐานลูกค้า
หรือขยายช่องทางจำหน่ายได้
"""
    )

else:

    st.warning(
        """
ควรมุ่งเน้นการเสริมความแข็งแรงภายในธุรกิจก่อน
แล้วจึงวางแผนการขยายตัว
"""
    )

# =====================================
# MANAGEMENT SUMMARY
# =====================================

st.markdown("---")

st.subheader("📋 สรุปสำหรับผู้บริหาร")

if weather_risk == "สูง":

    st.warning(
        """
ควรติดตามความเสี่ยงจากสภาพอากาศอย่างใกล้ชิด
เนื่องจากอาจส่งผลกระทบต่อการดำเนินงาน
ห่วงโซ่อุปทาน และต้นทุนการผลิต
"""
    )

else:

    st.success(
        """
ปัจจัยภายนอกโดยรวมยังอยู่ในระดับปกติ

สามารถใช้ข้อมูลสภาพตลาด
และสภาพแวดล้อมทางธุรกิจ
ประกอบการตัดสินใจเชิงกลยุทธ์ได้
"""
    )

# =====================================
# SOURCES
# =====================================

st.markdown("---")

st.subheader("📚 แหล่งข้อมูล")

st.markdown("""
ข้อมูลในระบบรองรับการเชื่อมต่อจาก

• Open-Meteo Weather API

• ข้อมูลเศรษฐกิจสาธารณะ

• ข้อมูลแนวโน้มตลาด

อ้างอิง:
https://open-meteo.com
""")

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "ZYRA Market Intelligence | External Environment Analysis"
)
