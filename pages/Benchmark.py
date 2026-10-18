import streamlit as st
import pandas as pd

st.title("🏆 Industry Benchmark")

df = pd.DataFrame(
    {
        "ตัวชี้วัด": [
            "อัตรากำไร",
            "เงินสดสำรอง"
        ],
        "ธุรกิจของคุณ": [
            "28%",
            "350,000"
        ],
        "ค่าเฉลี่ยอุตสาหกรรม": [
            "18%",
            "180,000"
        ]
    }
)

st.dataframe(
    df,
    use_container_width=True
)
