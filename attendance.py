import streamlit as st
import json
import datetime
import os

ATTENDANCE_FILE = "attendance.json"

# Load data from file
def load_attendance():
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}  # corrupted file
    return {}

# Save data to file
def save_attendance(data):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Main function to run app
def run_attendance_app():
    st.title("📅 Student Attendance App")

    today = str(datetime.date.today())
    attendance = load_attendance()

    # Initialize today's record if not exists or invalid
    if today not in attendance or not isinstance(attendance[today], dict):
        attendance[today] = {"present": [], "absent": []}

    present_students = attendance[today]["present"]
    absent_students = attendance[today]["absent"]

    # Attendance form
    with st.form("attendance_form"):
        name = st.text_input("👤 Stude_
