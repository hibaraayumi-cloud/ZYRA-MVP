import streamlit as st

st.title("📈 Market Intelligence")

st.metric(
    "Market Demand Index",
    "+12%"
)

st.success(
    "แนวโน้มความต้องการของตลาดเพิ่มขึ้น"
)

st.markdown(
"""
### แหล่งข้อมูล

- Google Trends
- ข่าวเศรษฐกิจ
- ข้อมูลตลาดสาธารณะ

ข้อมูลในเวอร์ชันต้นแบบใช้เพื่อสาธิตแนวคิดของระบบ
"""
)
