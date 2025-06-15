# main.py

import streamlit as st
from attendanceapp import run_attendance_app
from salaryapp import run_salary_app

st.set_page_config(page_title="School Management System", layout="centered")

st.sidebar.title("🏫 School Management System")
app = st.sidebar.selectbox("📂 Select Module", ["Attendance", "Teacher Salary"])

if app == "Attendance":
    run_attendance_app()
elif app == "Teacher Salary":
    run_salary_app()
