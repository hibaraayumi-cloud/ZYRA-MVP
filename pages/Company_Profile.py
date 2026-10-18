import streamlit as st

st.set_page_config(
    page_title="Company Profile",
    page_icon="🏢",
    layout="wide"
)

# =====================================
# HEADER
# =====================================

st.title("🏢 ZYRA")

st.subheader(
    "Business Health Intelligence Platform"
)

st.markdown("""
ZYRA เป็นแพลตฟอร์มวิเคราะห์สุขภาพธุรกิจ
และระบบแจ้งเตือนความเสี่ยงล่วงหน้าสำหรับผู้ประกอบการ SME

โดยใช้ข้อมูลทางธุรกิจร่วมกับปัจจัยภายนอก
เพื่อช่วยให้ผู้ประกอบการตัดสินใจได้อย่างมีประสิทธิภาพมากขึ้น
""")

# =====================================
# VISION
# =====================================

st.markdown("---")

st.subheader("🎯 วิสัยทัศน์")

st.success("""
เป็นแพลตฟอร์ม Business Intelligence
สำหรับผู้ประกอบการ SME ไทย

ที่ช่วยให้ผู้ใช้งานมองเห็นความเสี่ยงก่อนเกิดปัญหา
และสนับสนุนการตัดสินใจเชิงธุรกิจด้วยข้อมูล
""")

# =====================================
# PROBLEM
# =====================================

st.markdown("---")

st.subheader("⚠️ ปัญหาที่ต้องการแก้ไข")

st.markdown("""
ผู้ประกอบการจำนวนมากมักทราบปัญหาเมื่อเกิดผลกระทบขึ้นแล้ว เช่น

• รายได้ลดลง

• ลูกค้าลดลง

• สภาพคล่องไม่เพียงพอ

• ต้นทุนเพิ่มขึ้น

ทำให้ไม่สามารถวางแผนรับมือได้ทันท่วงที
""")

# =====================================
# SOLUTION
# =====================================

st.markdown("---")

st.subheader("💡 วิธีการแก้ปัญหา")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### วิเคราะห์ข้อมูลธุรกิจ

- รายได้
- ต้นทุน
- เงินสด
- การเติบโตของลูกค้า
""")

with col2:

    st.info("""
### วิเคราะห์ความเสี่ยง

- ความเสี่ยงด้านการเงิน
- ความเสี่ยงด้านการตลาด
- ความเสี่ยงด้านการดำเนินงาน
- ความเสี่ยงภายนอก
""")

# =====================================
# VALUE PROPOSITION
# =====================================

st.markdown("---")

st.subheader("🚀 คุณค่าที่ส่งมอบ")

st.success("✅ ประเมินสุขภาพธุรกิจ")

st.success("✅ แจ้งเตือนความเสี่ยงล่วงหน้า")

st.success("✅ เปรียบเทียบกับอุตสาหกรรม")

st.success("✅ วิเคราะห์แนวโน้มตลาด")

st.success("✅ จำลองสถานการณ์ก่อนตัดสินใจ")

# =====================================
# TARGET MARKET
# =====================================

st.markdown("---")

st.subheader("🎯 กลุ่มลูกค้าเป้าหมาย")

st.markdown("""
### ระยะเริ่มต้น

• ร้านอาหาร

• ธุรกิจค้าปลีก

• ธุรกิจเกษตร

---

### ระยะขยาย

• SME

• Startup

• ที่ปรึกษาธุรกิจ

• หน่วยงานที่สนับสนุนผู้ประกอบการ
""")

# =====================================
# PRODUCT MODULES
# =====================================

st.markdown("---")

st.subheader("🧩 โมดูลหลักของระบบ")

modules = [
    "Dashboard",
    "Risk Analysis",
    "Early Warning Center",
    "Benchmark",
    "Market Intelligence",
    "Business Simulator",
    "Business Report"
]

for module in modules:

    st.write(
        "✅",
        module
    )

# =====================================
# DIFFERENTIATION
# =====================================

st.markdown("---")

st.subheader("🏆 ความแตกต่างจากเครื่องมือทั่วไป")

st.info("""
โปรแกรมบัญชีทั่วไปช่วยบันทึกข้อมูลย้อนหลัง

Dashboard ทั่วไปช่วยแสดงผลข้อมูล

แต่ ZYRA มุ่งเน้น

• การประเมินสุขภาพธุรกิจ

• การแจ้งเตือนล่วงหน้า

• การวิเคราะห์ความเสี่ยง

• การสนับสนุนการตัดสินใจ
""")

# =====================================
# ROADMAP
# =====================================

st.markdown("---")

st.subheader("📅 แผนพัฒนา")

st.markdown("""
### Version 2.0

✅ Dashboard

✅ Benchmark

✅ Early Warning

✅ Market Intelligence

✅ Simulator

---

### Version 3.0

🔜 Economic Intelligence

🔜 AI Recommendation

🔜 External Data Integration

🔜 Automated Executive Report

---

### Version 4.0

🔜 Business Copilot

🔜 Predictive Analytics

🔜 Industry Risk Engine
""")

# =====================================
# FUTURE DATA SOURCES
# =====================================

st.markdown("---")

st.subheader("📚 แหล่งข้อมูลที่รองรับ")

st.markdown("""
• ข้อมูลทางธุรกิจจากผู้ใช้งาน

• Open-Meteo Weather API

• ข้อมูลเศรษฐกิจสาธารณะ

• Google Trends (อนาคต)

• Exchange Rate APIs (อนาคต)
""")

# =====================================
# CONTACT
# =====================================

st.markdown("---")

st.subheader("📌 Project Information")

st.caption(
    "ZYRA Business Health Intelligence Platform"
)

st.caption(
    "Prototype Version 2.0"
)
