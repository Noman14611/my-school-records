# main.py

import streamlit as st
from attendance import run_attendance_app
# from feeapp import run_fee_app      # ✅ Future ready
# from salaryapp import run_salary_app  # ✅ Future ready

# Title in sidebar
st.sidebar.title("📚 School Management System")

# Dropdown to select app
app = st.sidebar.selectbox("Select App", [
    "Attendance",
    # "Fee Submission",
    # "Teacher Salary"
])

# Load selected app
if app == "Attendance":
    run_attendance_app()
# elif app == "Fee Submission":
#     run_fee_app()
# elif app == "Teacher Salary":
#     run_salary_app()
