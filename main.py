import streamlit as st
from attendance import run_attendance_app

st.set_page_config(page_title="School App")
st.sidebar.title("App Selector")
choice = st.sidebar.selectbox("Choose", ["Attendance"])

if choice == "Attendance":
    run_attendance_app()
