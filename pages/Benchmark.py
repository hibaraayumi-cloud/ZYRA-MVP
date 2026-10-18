import streamlit as st
import pandas as pd
import plotly.express as px

from utils.history import load_history

st.set_page_config(
    page_title="Benchmark",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 เปรียบเทียบกับค่าเฉลี่ยอุตสาหกรรม")

st.markdown("""
เปรียบเทียบผลการดำเนินงานของธุรกิจกับค่าเฉลี่ยในอุตสาหกรรม

เพื่อค้นหาจุดแข็ง จุดที่ควรพัฒนา
และโอกาสในการแข่งขัน
""")

# =====================================
# LOAD DATA
# =====================================

df = load_history()

if df.empty:

    st.warning(
        """
ยังไม่มีข้อมูลการวิเคราะห์

กรุณาไปที่เมนู Risk Analysis
และวิเคราะห์อย่างน้อย 1 ครั้ง
"""
    )

    st.stop()

latest = df.iloc[-1]

business_type = latest["business_type"]

revenue = float(latest["revenue"])

cost = float(latest["cost"])

cash = float(latest["cash"])

growth = float(latest["growth"])

# =====================================
# CALCULATE ACTUAL METRICS
# =====================================

profit = revenue - cost

if revenue > 0:

    profit_margin = (
        profit / revenue
    ) * 100

    cash_ratio = (
        cash / revenue
    ) * 100

else:

    profit_margin = 0
    cash_ratio = 0

# =====================================
# INDUSTRY BENCHMARK
# =====================================

if business_type == "Restaurant":

    industry_profit = 18
    industry_cash = 35
    industry_growth = 5

elif business_type == "Retail":

    industry_profit = 15
    industry_cash = 30
    industry_growth = 4

else:

    industry_profit = 12
    industry_cash = 25
    industry_growth = 3

# =====================================
# BENCHMARK TABLE
# =====================================

st.subheader("📊 ตารางเปรียบเทียบ")

benchmark_df = pd.DataFrame({

    "ตัวชี้วัด": [
        "อัตรากำไร (%)",
        "สัดส่วนเงินสดสำรอง (%)",
        "การเติบโตของลูกค้า (%)"
    ],

    "ธุรกิจของคุณ": [
        round(profit_margin, 1),
        round(cash_ratio, 1),
        round(growth, 1)
    ],

    "ค่าเฉลี่ยอุตสาหกรรม": [
        industry_profit,
        industry_cash,
        industry_growth
    ]
})

st.dataframe(
    benchmark_df,
    use_container_width=True
)

# =====================================
# CHART
# =====================================

st.markdown("---")

st.subheader("📈 เปรียบเทียบผลการดำเนินงาน")

chart_df = pd.DataFrame({

    "ตัวชี้วัด": [
        "อัตรากำไร",
        "อัตรากำไร",
        "เงินสดสำรอง",
        "เงินสดสำรอง",
        "การเติบโต",
        "การเติบโต"
    ],

    "คะแนน": [
        profit_margin,
        industry_profit,
        cash_ratio,
        industry_cash,
        growth,
        industry_growth
    ],

    "ประเภท": [
        "ธุรกิจของคุณ",
        "ค่าเฉลี่ยอุตสาหกรรม",
        "ธุรกิจของคุณ",
        "ค่าเฉลี่ยอุตสาหกรรม",
        "ธุรกิจของคุณ",
        "ค่าเฉลี่ยอุตสาหกรรม"
    ]
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

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# PERFORMANCE SCORING
# =====================================

st.markdown("---")

st.subheader("📌 ผลการประเมิน")

score_count = 0

if profit_margin > industry_profit:

    score_count += 1

    st.success(
        "อัตรากำไรสูงกว่าค่าเฉลี่ยอุตสาหกรรม"
    )

else:

    st.warning(
        "อัตรากำไรต่ำกว่าค่าเฉลี่ยอุตสาหกรรม"
    )

if cash_ratio > industry_cash:

    score_count += 1

    st.success(
        "สภาพคล่องสูงกว่าค่าเฉลี่ยอุตสาหกรรม"
    )

else:

    st.warning(
        "สภาพคล่องต่ำกว่าค่าเฉลี่ยอุตสาหกรรม"
    )

if growth > industry_growth:

    score_count += 1

    st.success(
        "การเติบโตสูงกว่าค่าเฉลี่ยอุตสาหกรรม"
    )

else:

    st.warning(
        "การเติบโตต่ำกว่าค่าเฉลี่ยอุตสาหกรรม"
    )

# =====================================
# COMPETITIVE POSITION
# =====================================

st.markdown("---")

st.subheader("🎯 ตำแหน่งทางการแข่งขัน")

if score_count == 3:

    st.success(
        """
ธุรกิจมีผลการดำเนินงานเหนือกว่าค่าเฉลี่ยอุตสาหกรรมในทุกด้าน

ถือเป็นจุดแข็งสำคัญในการแข่งขัน
"""
    )

elif score_count >= 2:

    st.info(
        """
ธุรกิจมีผลการดำเนินงานดีกว่าค่าเฉลี่ยอุตสาหกรรมในหลายด้าน

ยังมีโอกาสพัฒนาบางส่วนเพิ่มเติม
"""
    )

else:

    st.warning(
        """
ธุรกิจยังมีผลการดำเนินงานต่ำกว่าค่าเฉลี่ยอุตสาหกรรมหลายด้าน

ควรวางแผนปรับปรุงเพื่อเพิ่มความสามารถในการแข่งขัน
"""
    )

# =====================================
# MANAGEMENT SUMMARY
# =====================================

st.markdown("---")

st.subheader("📋 สรุปสำหรับผู้บริหาร")

st.info(
f"""
ประเภทธุรกิจ : {business_type}

อัตรากำไรปัจจุบัน : {profit_margin:.1f}%

สภาพคล่องปัจจุบัน : {cash_ratio:.1f}%

อัตราการเติบโตของลูกค้า : {growth:.1f}%

ผลการวิเคราะห์แสดงให้เห็นว่าธุรกิจมีความสามารถในการแข่งขันในระดับที่สามารถต่อยอดได้
โดยควรติดตามตัวชี้วัดที่ยังต่ำกว่าค่าเฉลี่ยอุตสาหกรรมอย่างใกล้ชิด
"""
)

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "ZYRA Industry Benchmark Engine | Connected to Real Business Data"
)
