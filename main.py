import streamlit as st
from attendance import run_attendance_app
from attendance import run_attendance_app

run_attendance_app()

st.sidebar.title("📘 School App")
page = st.sidebar.selectbox("Select App", ["Attendance"])

if page == "Attendance":
    run_attendance_app()
