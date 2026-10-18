import streamlit as st
import pandas as pd

st.title("📊 Dashboard")

try:

    df = pd.read_csv(
        "data/analysis_history.csv"
    )

    if len(df) > 0:

        last_score = df.iloc[-1]["score"]

        st.metric(
            "Business Health Index",
            f"{last_score}/100"
        )

        st.subheader(
            "แนวโน้มคะแนนย้อนหลัง"
        )

        st.line_chart(
            df["score"]
        )

        st.subheader(
            "ประวัติการ
