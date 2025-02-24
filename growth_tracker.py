import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

def daily_challenge():
    challenges = [
        "Learn something new today",
        "Practice gratitude",
        "Step out of your comfort zone",
        "Reflect on a recent failure and its lessons",
        "Set a small goal and achieve it"
    ]
    daily_challenge = st.selectbox("Today's Challenge", challenges)

    if st.button("Complete Challenge"):
        new_entry = pd.DataFrame({
            "Date": [datetime.now().strftime("%Y-%m-%d")],
            "Challenge": [daily_challenge],
            "Completed": ["Yes"]
        })
        progress_df = pd.DataFrame(columns=["Date", "Challenge", "Completed"])
        progress_df = pd.concat([progress_df, new_entry], ignore_index=True)
        progress_df.to_csv("progress.csv", index=False)
        st.success(f"Great job completing today's challenge: {daily_challenge}")

def mistake_journal():
    st.subheader("Mistake Journal")
    mistake = st.text_area("Reflect on a recent mistake and what you learned:")
    if st.button("Log Mistake"):
        st.info("Mistake logged. Remember, mistakes are opportunities for growth!")

def progress_tracker():
    st.subheader("Progress Tracker")
    progress = st.slider("Rate your growth today (1-10)", 1, 10, 5)
    if st.button("Log Progress"):
        st.success(f"Progress logged: {progress}/10")

def progress_visualization():
    st.header("Progress Over Time")
    try:
        progress_df = pd.read_csv("progress.csv")
        if not progress_df.empty:
            progress_df["Date"] = pd.to_datetime(progress_df["Date"])
            progress_df = progress_df.sort_values(by="Date")
            progress_df["Cumulative Completed"] = (progress_df["Completed"] == "Yes").cumsum()
            fig = px.line(progress_df, x="Date", y="Cumulative Completed", title="Challenges Completed Over Time")
            st.plotly_chart(fig)
    except FileNotFoundError:
        st.info("No progress data available yet.")