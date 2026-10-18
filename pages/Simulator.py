import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from utils.history import load_history
from utils.scoring import calculate_score

st.set_page_config(
    page_title="Business Simulator",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 เครื่องมือจำลองสถานการณ์ทางธุรกิจ")

st.markdown("""
ทดลองปรับตัวแปรทางธุรกิจ
เพื่อประเมินผลกระทบก่อนตัดสินใจจริง
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
และวิเคราะห์ธุรกิจอย่างน้อย 1 ครั้ง
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
# CURRENT STATE
# =====================================

st.subheader("📊 ข้อมูลปัจจุบัน")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "รายได้",
    f"{revenue:,.0f}"
)

c2.metric(
    "ต้นทุน",
    f"{cost:,.0f}"
)

c3.metric(
    "เงินสดสำรอง",
    f"{cash:,.0f}"
)

c4.metric(
    "การเติบโต",
    f"{growth:.0f}%"
)

# =====================================
# SCENARIO
# =====================================

st.markdown("---")

st.subheader("⚙️ จำลองสถานการณ์")

revenue_change = st.slider(
    "ปรับรายได้ (%)",
    -50,
    100,
    10
)

cost_change = st.slider(
    "ปรับต้นทุน (%)",
    -50,
    100,
    0
)

growth_change = st.slider(
    "ปรับการเติบโตของลูกค้า (%)",
    -50,
    100,
    0
)

# =====================================
# NEW VALUES
# =====================================

new_revenue = revenue * (
    1 + revenue_change / 100
)

new_cost = cost * (
    1 + cost_change / 100
)

new_growth = growth + growth_change

industry_value = 0

sim_score = calculate_score(
    new_revenue,
    new_cost,
    cash,
    new_growth,
    business_type,
    industry_value
)

new_profit = new_revenue - new_cost

# =====================================
# RESULT
# =====================================

st.markdown("---")

st.subheader("📈 ผลการจำลอง")

r1, r2, r3 = st.columns(3)

r1.metric(
    "รายได้ใหม่",
    f"{new_revenue:,.0f}",
    f"{revenue_change}%"
)

r2.metric(
    "ต้นทุนใหม่",
    f"{new_cost:,.0f}",
    f"{cost_change}%"
)

r3.metric(
    "กำไรใหม่",
    f"{new_profit:,.0f}"
)

# =====================================
# SCORE
# =====================================

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=sim_score,
    title={
        "text":"คะแนนสุขภาพธุรกิจหลังปรับแผน"
    },
    gauge={
        "axis":{"range":[0,100]},
        "bar":{"color":"#0B8457"},
        "steps":[
            {
                "range":[0,40],
                "color":"#dc3545"
            },
            {
                "range":[40,60],
                "color":"#fd7e14"
            },
            {
                "range":[60,80],
                "color":"#ffc107"
            },
            {
                "range":[80,100],
                "color":"#198754"
            }
        ]
    }
))

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# COMPARISON
# =====================================

st.markdown("---")

st.subheader("📊 เปรียบเทียบก่อนและหลัง")

compare_df = pd.DataFrame({

    "รายการ":[
        "รายได้",
        "ต้นทุน",
        "การเติบโต"
    ],

    "ปัจจุบัน":[
        revenue,
        cost,
        growth
    ],

    "หลังจำลอง":[
        new_revenue,
        new_cost,
        new_growth
    ]
})

st.dataframe(
    compare_df,
    use_container_width=True
)

# =====================================
# SUMMARY
# =====================================

st.markdown("---")

st.subheader("📋 ผลการประเมิน")

if sim_score >= 80:

    st.success(
        """
สถานการณ์จำลองสะท้อนว่าธุรกิจมีแนวโน้มแข็งแรงขึ้น

สามารถพิจารณาขยายธุรกิจ
หรือดำเนินกลยุทธ์เชิงรุกได้
"""
    )

elif sim_score >= 60:

    st.warning(
        """
สถานการณ์จำลองยังอยู่ในระดับปกติ

ควรติดตามต้นทุนและการเติบโต
อย่างใกล้ชิด
"""
    )

else:

    st.error(
        """
สถานการณ์จำลองสะท้อนถึงความเสี่ยงที่เพิ่มขึ้น

ควรทบทวนกลยุทธ์ก่อนดำเนินการจริง
"""
    )

# =====================================
# RECOMMENDATION
# =====================================

st.markdown("---")

st.subheader("💡 ข้อเสนอแนะ")

if revenue_change > 0:

    st.success(
        "การเพิ่มรายได้ส่งผลบวกต่อคะแนนสุขภาพธุรกิจ"
    )

if cost_change > 20:

    st.warning(
        "ต้นทุนเพิ่มขึ้นในระดับสูง อาจส่งผลต่อความสามารถในการทำกำไร"
    )

if new_growth < 0:

    st.warning(
        "ควรวางแผนรักษาฐานลูกค้าอย่างจริงจัง"
    )

if sim_score >= 80:

    st.success(
        "สถานการณ์ดังกล่าวสามารถใช้เป็นแนวทางในการวางแผนธุรกิจได้"
    )

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "ZYRA Business Simulator | Scenario Planning Module"
)
