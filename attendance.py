# attendance.py

import streamlit as st
import json
import os
from datetime import date

# JSON file ka naam
ATTENDANCE_FILE = "attendance.json"

# File load karne ka function
def load_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

# File save karne ka function
def save_attendance(data):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Main function to run the app
def run_attendance_app():
    st.title("📋 Attendance App")

    today = str(date.today())
    attendance = load_attendance()

    # Aaj ka data agar nahi hai to bana lo
    if today not in attendance:
        attendance[today] = {"present": [], "absent": []}

    # Student input
    student_name = st.text_input("👤 Student ka naam likhein")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mark Present"):
            if student_name:
                if student_name not in attendance[today]["present"]:
                    attendance[today]["present"].append(student_name)
                # Agar pehle se absent me tha to hata do
                if student_name in attendance[today]["absent"]:
