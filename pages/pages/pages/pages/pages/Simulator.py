import streamlit as st

st.title("🔮 Business Simulator")

increase = st.slider(
    "หากรายได้เพิ่มขึ้น (%)",
    0,
    50,
    10
)

new_score = 80 + increase * 0.5

st.metric(
    "คะแนนสุขภาพธุรกิจที่คาดการณ์",
    round(new_score)
)

st.info(
    "ใช้สำหรับประเมินผลกระทบก่อนตัดสินใจทางธุรกิจ"
)
