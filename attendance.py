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

    # initialize today's attendance if not present
    if today not in attendance:
        attendance[today] = {"present": [], "absent": []}

    present_students = attendance[today]["present"]
    absent_students = attendance[today]["absent"]

    # Attendance form
    with st.form("attendance_form"):
        name = st.text_input("👤 Student Name")
        status = st.radio("Mark as", ["Present", "Absent"])
        submit = st.form_submit_button("✅ Mark Attendance")

        if submit:
            if not name:
                st.error("Please enter a name.")
            elif name in present_students or name in absent_students:
                st.warning(f"{name} already marked.")
            else:
                if status == "Present":
                    present_students.append(name)
                else:
                    absent_students.append(name)
                attendance[today] = {"present": present_students, "absent": absent_students}
                save_attendance(attendance)
                st.success(f"{name} marked as {status}")

    # Show results
    st.markdown(f"### ✅ Present Students ({len(present_students)})")
    for student in present_students:
        st.write("👤", student)

    st.markdown(f"### ❌ Absent Students ({len(absent_students)})")
    for student in absent_students:
        st.write("👤", student)
