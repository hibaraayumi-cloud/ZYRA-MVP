import streamlit as st

st.title("📊 Dashboard")

st.subheader("ภาพรวมธุรกิจ")

st.metric(
    "Business Health Index",
    "82/100"
)

st.success(
    "สถานะธุรกิจอยู่ในเกณฑ์ดี"
)

st.markdown(
"""
### สิ่งที่ต้องติดตาม

- สภาพคล่องทางการเงิน
- การเติบโตของลูกค้า
- ความสามารถในการทำกำไร
"""
)
