# main.py

import streamlit as st
from attendanceapp import run_attendance_app

st.sidebar.title("📚 School Management System")

app = st.sidebar.selectbox("Select App", [
    "Attendance"
])

if app == "Attendance":
    run_attendance_app()
