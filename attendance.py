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
    students = attendance.get(today, [])

    name = st.text_input("Student Name")
    if st.button("Mark Present"):
        if name and name not in students:
            students.append(name)
            attendance[today] = students
            save_attendance(attendance)
            st.success(f"{name} marked present!")

    st.subheader(f"Present Today ({today})")
    st.write(students)
