import streamlit as st

st.set_page_config(
    page_title="ZYRA",
    page_icon="📈",
    layout="wide"
)

# =====================================
# HERO SECTION
# =====================================

st.title("📈 ZYRA")

st.markdown("""
# Business Health Intelligence Platform

แพลตฟอร์มวิเคราะห์สุขภาพธุรกิจ ความเสี่ยง และโอกาสในการเติบโตสำหรับผู้ประกอบการ SME

ZYRA ช่วยเปลี่ยนข้อมูลธุรกิจให้กลายเป็นข้อมูลเชิงลึกที่นำไปใช้ได้จริง
ผ่านระบบวิเคราะห์ความเสี่ยง การแจ้งเตือนล่วงหน้า และการประเมินสุขภาพธุรกิจ
""")

st.success(
    "เปลี่ยนข้อมูลทางธุรกิจให้เป็นสัญญาณเตือนเชิงกลยุทธ์"
)

st.markdown("---")

# =====================================
# VALUE PROPOSITION
# =====================================

st.subheader("🎯 ZYRA ช่วยอะไรได้บ้าง")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("""
### สุขภาพธุรกิจ

ประเมินความแข็งแรงของธุรกิจผ่าน
Business Health Index
""")

with c2:

    st.info("""
### ความเสี่ยง

ตรวจจับสัญญาณเตือนล่วงหน้า
ก่อนเกิดผลกระทบทางธุรกิจ
""")

with c3:

    st.info("""
### การตัดสินใจ

สนับสนุนผู้ประกอบการด้วย
ข้อมูลและคำแนะนำเชิงวิเคราะห์
""")

st.markdown("---")

# =====================================
# SYSTEM MODULES
# =====================================

st.subheader("🧩 โมดูลหลักของระบบ")

m1, m2, m3 = st.columns(3)

with m1:

    st.success("""
✅ Dashboard

✅ Risk Analysis

✅ Benchmark
""")

with m2:

    st.success("""
✅ Market Intelligence

✅ Simulator

✅ Business Report
""")

with m3:

    st.success("""
✅ Early Warning Center

✅ Trend Analysis

✅ Executive Summary
""")

st.markdown("---")

# =====================================
# FEATURE HIGHLIGHTS
# =====================================

st.subheader("🚀 จุดเด่นของระบบ")

st.markdown("""
### 1. Business Health Index

ประเมินสุขภาพธุรกิจจาก

- รายได้
- ต้นทุน
- สภาพคล่อง
- การเติบโต
- ปัจจัยเฉพาะอุตสาหกรรม

---

### 2. Early Warning System

ตรวจจับความเสี่ยง เช่น

- เงินสดสำรองต่ำ
- ต้นทุนสูงเกินไป
- การเติบโตของลูกค้าลดลง

---

### 3. Industry Benchmark

เปรียบเทียบผลการดำเนินงานกับค่าเฉลี่ยอุตสาหกรรม

---

### 4. Business Simulator

จำลองผลกระทบของการตัดสินใจทางธุรกิจก่อนใช้งานจริง
""")

st.markdown("---")

# =====================================
# TARGET CUSTOMERS
# =====================================

st.subheader("🏪 กลุ่มเป้าหมาย")

target_df = {
    "กลุ่มธุรกิจ": [
        "ธุรกิจค้าปลีก",
        "ร้านอาหาร",
        "ธุรกิจเกษตร",
        "SME",
        "Startup"
    ]
}

st.table(target_df)

st.markdown("---")

# =====================================
# BUSINESS PROCESS
# =====================================

st.subheader("⚙️ กระบ
