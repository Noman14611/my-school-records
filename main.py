import streamlit as st
from fee_submission import run_fee_submission
from attendance import run_attendance_app
from teachers_salary import run_salary_app

st.set_page_config(page_title="School Management App", layout="wide")
st.sidebar.title("📚 School Management System")

app = st.sidebar.selectbox("Select App", ["Fee Submission", "Attendance", "Teacher Salary"])

if app == "Fee Submission":
    run_fee_submission()
elif app == "Attendance":
    run_attendance_app()
elif app == "Teacher Salary":
    run_salary_app()
