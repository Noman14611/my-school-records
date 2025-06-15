import streamlit as st
import json
import os

SALARY_FILE = "teachers_salary.json"

def load_salaries():
    if os.path.exists(SALARY_FILE):
        with open(SALARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_salaries(data):
    with open(SALARY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def run_salary_app():
    st.title("👨‍🏫 Teacher Salary Management")

    data = load_salaries()

    st.subheader("Add Teacher Salary")
    with st.form("salary_form"):
        name = st.text_input("Teacher Name")
        month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July",
                                       "August", "September", "October", "November", "December"])
        salary = st.number_input("Salary Amount", min_value=0)
        submit = st.form_submit_button("Add Salary")
        if submit:
            data.append({"name": name, "month": month, "salary": salary})
            save_salaries(data)
            st.success("Salary added!")

    st.subheader("All Salaries")
    for item in data:
        st.write(f"{item['name']} - {item['month']} : Rs. {item['salary']}")
