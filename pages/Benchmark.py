import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Benchmark",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 เปรียบเทียบกับค่าเฉลี่ยอุตสาหกรรม")

st.markdown("""
เปรียบเทียบผลการดำเนินงานของธุรกิจกับค่าเฉลี่ยในอุตสาหกรรม
เพื่อระบุจุดแข็ง จุดที่ควรพัฒนา และโอกาสในการแข่งขัน
""")

# ======================================
# SELECT BUSINESS TYPE
# ======================================

business_type = st.selectbox(
    "เลือกประเภทธุรกิจ",
    [
        "ร้านอาหาร",
        "ค้าปลีก",
        "เกษตรกรรม"
    ]
)

# ======================================
# SAMPLE BENCHMARK DATA
# ======================================

if business_type == "ร้านอาหาร":

    your_data = {
        "อัตรากำไร (%)": 28,
        "เงินสดสำรอง": 350,
        "การเติบโตของลูกค้า": 12
    }

    industry_data = {
        "อัตรากำไร (%)": 18,
        "เงินสดสำรอง": 180,
        "การเติบโตของลูกค้า": 5
    }

elif business_type == "ค้าปลีก":

    your_data = {
        "อัตรากำไร (%)": 22,
        "เงินสดสำรอง": 300,
        "การเติบโตของลูกค้า": 8
    }

    industry_data = {
        "อัตรากำไร (%)": 15,
        "เงินสดสำรอง": 150,
        "การเติบโตของลูกค้า": 4
    }

else:

    your_data = {
        "อัตรากำไร (%)": 20,
        "เงินสดสำรอง": 250,
        "การเติบโตของลูกค้า": 10
    }

    industry_data = {
        "อัตรากำไร (%)": 12,
        "เงินสดสำรอง": 120,
        "การเติบโตของลูกค้า": 3
    }

# ======================================
# TABLE
# ======================================

benchmark_df = pd.DataFrame({
    "ตัวชี้วัด": list(your_data.keys()),
    "ธุรกิจของคุณ": list(your_data.values()),
    "ค่าเฉลี่ยอุตสาหกรรม": list(industry_data.values())
})

st.subheader("📊 ตารางเปรียบเทียบ")

st.dataframe(
    benchmark_df,
    use_container_width=True
)

# ======================================
# CHART
# ======================================

chart_df = pd.DataFrame({
    "ตัวชี้วัด":
        list(your_data.keys()) +
        list(industry_data.keys()),

    "คะแนน":
        list(your_data.values()) +
        list(industry_data.values()),

    "ประเภท":
        ["ธุรกิจของคุณ"] * 3 +
        ["ค่าเฉลี่ยอุตสาหกรรม"] * 3
})

fig = px.bar(
    chart_df,
    x="ตัวชี้วัด",
    y="คะแนน",
    color="ประเภท",
    barmode="group",
    color_discrete_sequence=[
        "#0B8457",
        "#ADB5BD"
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================================
# INSIGHT
# ======================================

st.markdown("---")

st.subheader("🔍 วิเคราะห์ผล")

for key in your_data:

    if your_data[key] > industry_datast.success(
            f"{key}: สูงกว่าค่าเฉลี่ยอุตสาหกรรม"
        )

    else:

        st.warning(
            f"{key}: ต่ำกว่าค่าเฉลี่ยอุตสาหกรรม"
        )

# ======================================
# MANAGEMENT VIEW
# ======================================

st.markdown("---")

st.subheader("📋 ข้อสรุปสำหรับผู้บริหาร")

better = 0

for key in your_data:

    if your_data[key] > industry_databetter += 1

if better >= 2:

    st.success(
        """
ธุรกิจมีผลการดำเนินงานสูงกว่าค่าเฉลี่ยอุตสาหกรรม

สามารถใช้จุดแข็งดังกล่าวเป็นฐานในการขยายธุรกิจ
และเพิ่มความสามารถในการแข่งขันในระยะยาว
"""
    )

else:

    st.warning(
        """
ธุรกิจยังมีตัวชี้วัดบางส่วนต่ำกว่าค่าเฉลี่ยอุตสาหกรรม

ควรให้ความสำคัญกับการเพิ่มประสิทธิภาพการดำเนินงาน
และปรับปรุงความสามารถในการทำกำไร
"""
    )
