from utils.history import load_history

df = load_history()

if df.empty:
    st.warning("ยังไม่มีข้อมูล")
    st.stop()

latest = df.iloc[-1]

score = latest["score"]
revenue = latest["revenue"]
cost = latest["cost"]
cash = latest["cash"]
growth = latest["growth"]

profit = revenue - cost
