# attendanceapp.py

import streamlit as st
import json
import os
from datetime import date

ATTENDANCE_FILE = "attendance.json"

def load_attendance():
    try:
        if os.path.exists(ATTENDANCE_FILE):
            with open(ATTENDANCE_FILE, "r") as f:
                return json.load(f)
        else:
            # File doesn't exist yet, return empty dict
            return {}
    except:
        return {}

def save_attendance(data):
    try:
        with open(ATTENDANCE_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        st.error(f"File write error: {e}")

def run_attendance_app():
    st.title("📋 Attendance App (Present Only)")

    today = str(date.today())
    attendance = load_attendance()

    # Ensure today's entry exists
    if today not in attendance:
        attendance[today] = {"present": []}
        save_attendance(attendance)  # 👈 Save empty structure so file is created

    student_name = st.text_input("👤 Student ka Naam")

    if st.button("✅ Mark Present"):
        if student_name:
            if student_name not in attendance[today]["present"]:
                attendance[today]["present"].append(student_name)
                save_attendance(attendance)
                st.success(f"{student_name} marked Present ✅")
            else:
                st.info(f"{student_name} already marked Present")

    st.markdown("## 📅 Aaj ki Attendance")
    st.write("✅ **Present Students:**", attendance[today]["present"])
