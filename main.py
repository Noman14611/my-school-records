import streamlit as st
from attendance import run_attendance_app

st.sidebar.title("📚 School App")
app = st.sidebar.selectbox("Select App", ["Attendance"])

if app == "Attendance":
    run_attendance_app()
