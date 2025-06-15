# attendance.py

import streamlit as st
import json
import os
from datetime import date

# Attendance data file
ATTENDANCE_FILE = "attendance.json"

# Load or initialize attendance data
def load_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_attendance(data):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def run_attendance_app():
    st.title("📋 Attendance App")

    today = str(date.today())
    attendance = load_attendance()

    if today not in attendance:
        attendance[today] = {"present": [], "absent": []}

    student_name = st.text_input("👤 Enter Student Name")
    if st.button("✅ Mark Present"):
        if student_name and student_name not in attendance[today]["present"]:
            attendance[today]["present"].append(student_name)
            if student_name in attendance[today]["absent"]:
                attendance[today]["absent"].remove(student_name)
            save_attendance(attendance)
            st.success(f"{student_name} marked as Present.")
    
    if st.button("❌ Mark Absent"):
        if student_name and student_name not in attendance[today]["absent"]:
            attendance[today]["absent"].append(student_name)
            if student_name in attendance[today]["present"]:
                attendance[today]["present"].remove(student_name)
            save_attendance(attendance)
            st.warning(f"{student_name} marked as Absent.")

    st.markdown("## 📅 Today's Attendance")
    st.write("✅ Present Students:", attendance[today]["present"])
    st.write("❌ Absent Students:"
