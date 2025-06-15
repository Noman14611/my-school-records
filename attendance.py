# attendanceapp.py

import streamlit as st
import json
import os
from datetime import date

ATTENDANCE_FILE = "attendance.json"

def load_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_attendance(data):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def run_attendance_app():
    st.title("📋 Attendance Tracker")

    today = str(date.today())
    attendance = load_attendance()

    if today not in attendance:
        attendance[today] = {"present": []}
        save_attendance(attendance)

    name = st.text_input("👤 Student Name")
    if st.button("✅ Mark Present"):
        if name:
            if name not in attendance[today]["present"]:
                attendance[today]["present"].append(name)
                save_attendance(attendance)
                st.success(f"{name} marked present.")
            else:
                st.warning(f"{name} already marked.")

    st.subheader("📅 Today's Present Students")
    st.write(attendance[today]["present"])
