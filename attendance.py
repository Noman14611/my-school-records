import streamlit as st
import json
import datetime
import os

ATTENDANCE_FILE = "attendance.json"

def load_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_attendance(data):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def run_attendance_app():
    st.title("📅 Student Attendance")

    today = str(datetime.date.today())
    attendance = load_attendance()
    present_students = attendance.get(today, [])

    with st.form("attendance_form"):
        name = st.text_input("👤 Student Name")
        submit = st.form_submit_button("✅ Mark Present")
        if submit:
            if name:
                if name not in present_students:
                    present_students.append(name)
                    attendance[today] = present_students
                    save_attendance(attendance)
                    st.success(f"{name} marked present!")
                else:
                    st.warning(f"{name} is already marked present.")
            else:
                st.error("Please enter a student name.")

    st.markdown(f"### 🎯 Present Today - *{today}*")

    if present_students:
        cols = st.columns(3)
        for idx, student in enumerate(present
