import streamlit as st

st.title("⚠️ Risk Analysis")

st.subheader("การวิเคราะห์ความเสี่ยง")

st.metric(
    "Overall Risk Score",
    "72/100"
)

st.warning(
    "ระดับความเสี่ยงปานกลาง"
)

st.markdown(
"""
### ปัจจัยเสี่ยง

- ต้นทุนเพิ่มขึ้น
- ลูกค้าเติบโตชะลอลง
- เงินสดสำรองต่ำกว่าระดับที่แนะนำ
"""
)
