import streamlit as st

# Import your apps
from attendance import run_attendance_app
from feeapp import run_fee_app
from salaryapp import run_salary_app

# Sidebar title
st.sidebar.title("📚 School Management System")

# Sidebar menu
app_option = st.sidebar.selectbox("Select App", [
    "Attendance",
    "Fee Submission",
    "Teacher Salary"
])

# Run selected app
if app_option == "Attendance":
    run_attendance_app()
elif app_option == "Fee Submission":
    run_fee_app()
elif app_option == "Teacher Salary":
    run_salary_app()
