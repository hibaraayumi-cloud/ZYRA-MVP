import streamlit as st

st.set_page_config(
    page_title="ZYRA Company Profile",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 เกี่ยวกับ ZYRA")

st.markdown("""
## Business Health Intelligence Platform

ZYRA เป็นแพลตฟอร์มวิเคราะห์สุขภาพธุรกิจและความเสี่ยงสำหรับผู้ประกอบการ SME

ระบบได้รับการออกแบบเพื่อช่วยให้ผู้ประกอบการสามารถมองเห็นสัญญาณเตือนล่วงหน้า
วิเคราะห์ความเสี่ยง และวางแผนการดำเนินธุรกิจโดยใช้ข้อมูลเป็นฐานในการตัดสินใจ
""")

st.markdown("---")

st.subheader("🎯 ปัญหาที่ต้องการแก้ไข")

st.warning("""
ผู้ประกอบการจำนวนมากรับรู้ปัญหาทางธุรกิจเมื่อผลกระทบเกิดขึ้นแล้ว

เช่น

• รายได้ลดลง

• สภาพคล่องไม่เพียงพอ

• ต้นทุนเพิ่มขึ้น

• จำนวนลูกค้าลดลง

ทำให้ไม่สามารถวางแผนรับมือได้อย่างทันท่วงที
""")

st.markdown("---")

st.subheader("✅ แนวทางการแก้ปัญหาของ ZYRA")

col1, col2 = st.columns(2)

with col1:

    st.success("""
1. วิเคราะห์สุขภาพธุรกิจ

2. ประเมินความเสี่ยง

3. แจ้งเตือนล่วงหน้า

4. เปรียบเทียบกับอุตสาหกรรม
""")

with col2:

    st.success("""
5. วิเคราะห์แนวโน้มตลาด

6. จำลองสถานการณ์ทางธุรกิจ

7. สรุปผลสำหรับผู้บริหาร

8. แนะนำแนวทางปรับปรุง
""")

st.markdown("---")

st.subheader("🧩 โมดูลหลักของระบบ")

modules = [
    "Dashboard",
    "Risk Analysis",
    "Benchmark",
    "Market Intelligence",
    "Business Simulator"
]

for m in modules:
    st.write("✅", m)

st.markdown("---")

st.subheader("🎯 กลุ่มเป้าหมาย")

st.info("""
• ธุรกิจค้าปลีก

• ร้านอาหาร

• ธุรกิจเกษตร

• ผู้ประกอบการ SME

• Startup ระยะเริ่มต้น
""")

st.markdown("---")

st.subheader("🚀 คุณค่าที่ระบบมอบให้")

st.success("""
จากการรายงานผลย้อนหลัง

สู่

การวิเคราะห์เชิงคาดการณ์และแจ้งเตือนความเสี่ยงล่วงหน้า

เพื่อช่วยให้ผู้ประกอบการตัดสินใจได้เร็วขึ้นและมีข้อมูลรองรับมากขึ้น
""")

st.markdown("---")

st.subheader("🏆 จุดเด่นของ ZYRA")

st.write("✅ Industry-Specific Analytics")

st.write("✅ Business Health Index")

st.write("✅ Early Warning System")

st.write("✅ Business Simulator")

st.write("✅ Market Intelligence")

st.write("✅ Industry Benchmark")

st.markdown("---")

st.caption(
    "ZYRA Business Health Intelligence Platform | Company Profile"
)
