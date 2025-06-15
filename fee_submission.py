import streamlit as st
import json
import pandas as pd
import os

STUDENT_FILE = "students.json"

def load_students():
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as f:
            return json.load(f)
    return []

def save_students(data):
    with open(STUDENT_FILE, "w") as f:
        json.dump(data, f, indent=2)

def export_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("student_fee_data.xlsx", index=False)
    st.success("Excel file exported as student_fee_data.xlsx")

def run_fee_submission():
    st.title("💳 Student Fee Submission")

    students = load_students()

    menu = st.radio("Options", ["Add Student", "View/Edit/Delete Students", "Export to Excel"])

    if menu == "Add Student":
        with st.form("add_form"):
            name = st.text_input("Student Name")
            student_class = st.text_input("Class")
            roll_no = st.text_input("Roll Number")
            fee = st.number_input("Monthly Fee", min_value=0)
            fee_status = st.selectbox("Fee Status", ["Paid", "Due"])
            submitted = st.form_submit_button("Add")
            if submitted:
                students.append({
                    "name": name,
                    "class": student_class,
                    "roll_no": roll_no,
                    "fee": fee,
                    "status": fee_status
                })
                save_students(students)
                st.success("Student added successfully!")

    elif menu == "View/Edit/Delete Students":
        st.subheader("Student Records")
        for i, student in enumerate(students):
            st.write(f"### {student['name']} - {student['class']} (Roll: {student['roll_no']})")
            col1, col2, col3 = st.columns(3)
            with col1:
                new_status = st.selectbox("Fee Status", ["Paid", "Due"], key=f"status{i}", index=["Paid", "Due"].index(student["status"]))
            with col2:
                if st.button("Update", key=f"update{i}"):
                    students[i]["status"] = new_status
                    save_students(students)
                    st.success("Updated!")
            with col3:
                if st.button("Delete", key=f"delete{i}"):
                    students.pop(i)
                    save_students(students)
                    st.success("Deleted!")
                    st.experimental_rerun()

    elif menu == "Export to Excel":
        export_to_excel(students)
