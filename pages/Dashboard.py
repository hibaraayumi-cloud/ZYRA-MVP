import streamlit as st
import pandas as pd

st.title("📊 Dashboard")

st.subheader(
    "ภาพรวมผลการวิเคราะห์ธุรกิจ"
)

try:

    df = pd.read_csv(
        "data/analysis_history.csv"
    )

    if len(df) > 0:

        latest_score = df.iloc[-1]["score"]

        st.metric(
            "Business Health Index",
            f"{latest_score}/100"
        )

        st.line_chart(
            df["score"]
        )

    else:

        st.info(
            "ยังไม่มีประวัติการวิเคราะห์"
        )

except:

    st.info(
        "ยังไม่มีข้อมูล"
    )
