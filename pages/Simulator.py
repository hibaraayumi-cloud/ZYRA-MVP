import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Business Simulator",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 เครื่องมือจำลองสถานการณ์ทางธุรกิจ")

st.markdown("""
ทดลองปรับตัวแปรทางธุรกิจเพื่อประเมินผลกระทบต่อ
สุขภาพธุรกิจและระดับความเสี่ยง

ช่วยสนับสนุนการตัดสินใจก่อนดำเนินการจริง
""")

st.markdown("---")

# =====================================
# CURRENT STATE
# =====================================

st.subheader("สถานการณ์ปัจจุบัน")

current_revenue = st.number_input(
    "รายได้ปัจจุบัน (บาท)",
    value=100000
)

current_cost = st.number_input(
    "ต้นทุนปัจจุบัน (บาท)",
    value=70000
)

current_growth = st.slider(
    "การเติบโตของลูกค้า (%)",
    -50,
    50,
    10
)

st.markdown("---")

# =====================================
# SCENARIO INPUT
# =====================================

st.subheader("จำลองสถานการณ์")

revenue_change = st.slider(
    "เปลี่ยนแปลงรายได้ (%)",
    -50,
    100,
    10
)

cost_change = st.slider(
    "เปลี่ยนแปลงต้นทุน (%)",
    -50,
    100,
    0
)

growth_change = st.slider(
    "เปลี่ยนแปลงการเติบโตของลูกค้า (%)",
    -50,
    100,
    0
)

# =====================================
# CALCULATION
# =====================================

new_revenue = current_revenue * (1 + revenue_change / 100)

new_cost = current_cost * (1 + cost_change / 100)

new_growth = current_growth + growth_change

profit = new_revenue - new_cost

# =====================================
# HEALTH SCORE
# =====================================

score = 50

if profit > 0:
    score += 20
else:
    score -= 15

if new_growth > 10:
    score += 15
elif new_growth > 0:
    score += 10
else:
    score -= 10

profit_margin = profit / new_revenue if new_revenue > 0 else 0

if profit_margin > 0.30:
    score += 15

elif profit_margin > 0.10:
    score += 10

score = max(0, min(score, 100))

# =====================================
# RESULTS
# =====================================

st.markdown("---")

st.subheader("📊 ผลการจำลอง")

c1, c2, c3 = st.columns(3)

c1.metric(
    "รายได้ใหม่",
    f"{new_revenue:,.0f}",
    f"{revenue_change}%"
)

c2.metric(
    "ต้นทุนใหม่",
    f"{new_cost:,.0f}",
    f"{cost_change}%"
)

c3.metric(
    "กำไรใหม่",
    f"{profit:,.0f}"
)

# =====================================
# SCORE GAUGE
# =====================================

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={
        "text": "คะแนนสุขภาพธุรกิจหลังปรับแผน"
    },
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
# INTERPRETATION
# =====================================

st.markdown("---")

st.subheader("📋 ผลการประเมิน")

if score >= 80:

    st.success(
        """
สถานการณ์จำลองแสดงให้เห็นว่าธุรกิจอยู่ในทิศทางที่ดี

การเปลี่ยนแปลงที่กำหนดช่วยเพิ่มศักยภาพในการเติบโต
และลดความเสี่ยงโดยรวมของธุรกิจ
"""
    )

elif score >= 60:

    st.warning(
        """
ธุรกิจมีแนวโน้มคงที่

ควรติดตามผลกระทบของรายได้ ต้นทุน
และการเติบโตของลูกค้าอย่างต่อเนื่อง
"""
    )

else:

    st.error(
        """
สถานการณ์จำลองสะท้อนถึงความเสี่ยงที่เพิ่มขึ้น

ควรทบทวนแผนการดำเนินงานก่อนตัดสินใจลงทุน
หรือขยายธุรกิจ
"""
    )

# =====================================
# RECOMMENDATION
# =====================================

st.markdown("---")

st.subheader("💡 ข้อเสนอแนะ")

if revenue_change > 0:

    st.write(
        "✅ การเพิ่มรายได้ส่งผลบวกต่อคะแนนสุขภาพธุรกิจ"
    )

if cost_change > 20:

    st.write(
        "⚠ ต้นทุนเพิ่มขึ้นในระดับสูง อาจส่งผลต่อกำไร"
    )

if new_growth < 0:

    st.write(
        "⚠ ควรจัดทำกิจกรรมรักษาฐานลูกค้า"
    )

if score >= 80:

    st.write(
        "✅ สามารถพิจารณาขยายธุรกิจได้"
    )
