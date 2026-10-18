import streamlit as st
import pandas as pd
import plotly.express as px

from utils.history import load_history

st.set_page_config(
    page_title="Early Warning Center",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 ศูนย์เตือนความเสี่ยงล่วงหน้า")

st.markdown("""
ติดตามความเสี่ยงที่อาจส่งผลกระทบต่อธุรกิจ

ระบบจะวิเคราะห์ข้อมูลจากผลการประเมินล่าสุด
และจัดลำดับความสำคัญของความเสี่ยงที่ควรติดตาม
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
และทำการวิเคราะห์อย่างน้อย 1 ครั้ง
"""
    )

    st.stop()

latest = df.iloc[-1]

revenue = float(latest["revenue"])

cost = float(latest["cost"])

cash = float(latest["cash"])

growth = float(latest["growth"])

score = float(latest["score"])

# =====================================
# ALERT GENERATION
# =====================================

alerts = []

critical = 0
high = 0
medium = 0

if cash < revenue * 0.3:

    alerts.append({
        "risk":
            "เงินสดสำรองต่ำกว่าระดับที่แนะนำ",

        "level":
            "วิกฤต",

        "impact":
            "อาจกระทบต่อสภาพคล่องของธุรกิจ"
    })

    critical += 1

if revenue < cost:

    alerts.append({
        "risk":
            "ต้นทุนสูงกว่ารายได้",

        "level":
            "สูง",

        "impact":
            "มีโอกาสเกิดการขาดทุน"
    })

    high += 1

if growth < 0:

    alerts.append({
        "risk":
            "การเติบโตของลูกค้าติดลบ",

        "level":
            "สูง",

        "impact":
            "เสี่ยงต่อการสูญเสียรายได้ในอนาคต"
    })

    high += 1

if score < 60:

    alerts.append({
        "risk":
            "คะแนนสุขภาพธุรกิจต่ำกว่าเกณฑ์",

        "level":
            "ปานกลาง",

        "impact":
            "ควรติดตามแนวโน้มธุรกิจอย่างใกล้ชิด"
    })

    medium += 1

# =====================================
# ALERT OVERVIEW
# =====================================

st.subheader("📌 ภาพรวมความเสี่ยง")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "ความเสี่ยงวิกฤต",
    critical
)

c2.metric(
    "ความเสี่ยงสูง",
    high
)

c3.metric(
    "ความเสี่ยงปานกลาง",
    medium
)

c4.metric(
    "คะแนนสุขภาพธุรกิจ",
    f"{score:.0f}"
)

# =====================================
# RISK LEVEL CHART
# =====================================

st.markdown("---")

chart_df = pd.DataFrame({
    "หมวด": [
        "วิกฤต",
        "สูง",
        "ปานกลาง"
    ],

    "จำนวน": [
        critical,
        high,
        medium
    ]
})

fig = px.bar(
    chart_df,
    x="หมวด",
    y="จำนวน",
    color="หมวด",
    color_discrete_sequence=[
        "#dc3545",
        "#fd7e14",
        "#ffc107"
    ]
)

fig.update_layout(
    height=400
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# ALERT DETAIL
# =====================================

st.markdown("---")

st.subheader("⚠️ รายการความเสี่ยง")

if len(alerts) == 0:

    st.success(
        "ยังไม่พบสัญญาณความเสี่ยงที่มีนัยสำคัญ"
    )

else:

    alert_df = pd.DataFrame(alerts)

    st.dataframe(
        alert_df,
        use_container_width=True
    )

# =====================================
# ROOT CAUSE ANALYSIS
# =====================================

st.markdown("---")

st.subheader("🔍 วิเคราะห์สาเหตุ")

causes = []

if cash < revenue * 0.3:

    causes.append(
        "เงินสดสำรองต่ำเมื่อเทียบกับรายได้"
    )

if revenue < cost:

    causes.append(
        "โครงสร้างต้นทุนสูงเกินไป"
    )

if growth < 0:

    causes.append(
        "จำนวนลูกค้าลดลง"
    )

if len(causes) == 0:

    st.success(
        "ไม่พบสาเหตุที่น่ากังวลในปัจจุบัน"
    )

else:

    for c in causes:

        st.write(
            "•",
            c
        )

# =====================================
# RECOMMENDATIONS
# =====================================

st.markdown("---")

st.subheader("💡 แนวทางที่แนะนำ")

recommendations = []

if cash < revenue * 0.3:

    recommendations.append(
        "เพิ่มเงินสดสำรองและจัดทำแผนบริหารสภาพคล่อง"
    )

if revenue < cost:

    recommendations.append(
        "ทบทวนต้นทุนและเพิ่มประสิทธิภาพการดำเนินงาน"
    )

if growth < 0:

    recommendations.append(
        "จัดทำกิจกรรมรักษาฐานลูกค้าและสร้างการซื้อซ้ำ"
    )

if len(recommendations) == 0:

    recommendations.append(
        "ดำเนินธุรกิจตามแผนปัจจุบันและติดตามผลอย่างต่อเนื่อง"
    )

for r in recommendations:

    st.success(
        f"✅ {r}"
    )

# =====================================
# TREND
# =====================================

st.markdown("---")

st.subheader("📈 แนวโน้มคะแนนสุขภาพธุรกิจ")

trend_df = df.copy()

trend_df["analysis_no"] = range(
    1,
    len(trend_df) + 1
)

fig2 = px.line(
    trend_df,
    x="analysis_no",
    y="score",
    markers=True
)

fig2.update_layout(
    xaxis_title="ครั้งที่วิเคราะห์",
    yaxis_title="คะแนน",
    height=400
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================
# MANAGEMENT SUMMARY
# =====================================

st.markdown("---")

st.subheader("📋 สรุปสำหรับผู้บริหาร")

if len(alerts) == 0:

    st.success(
        """
ธุรกิจยังไม่พบสัญญาณความเสี่ยงที่มีนัยสำคัญ

ควรติดตามผลการวิเคราะห์อย่างต่อเนื่อง
เพื่อป้องกันความเสี่ยงในอนาคต
"""
    )

else:

    st.warning(
        f"""
ตรวจพบความเสี่ยงจำนวน {len(alerts)} รายการ

ควรดำเนินการตามข้อเสนอแนะของระบบ
เพื่อป้องกันผลกระทบที่อาจเกิดขึ้น
"""
    )

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "ZYRA Early Warning Center | Real-Time Internal Risk Monitoring"
)
