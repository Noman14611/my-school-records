# main.py
import streamlit as st
from attendanceapp import run_attendance_app
# from feeapp import run_fee_app
# from salaryapp import run_salary_app

st.sidebar.title("📚 School Management System")

app = st.sidebar.selectbox("Select App", [
    "Attendance",
    # "Fee Submission",
    # "Teacher Salary"
])

if app == "Attendance":
    run_attendance_app()
# elif app == "Fee Submission":
#     run_fee_app()
# elif app == "Teacher Salary":
#     run_salary_app()
