# salaryapp.py

import streamlit as st
import json
import os

SALARY_FILE = "teacher_salaries.json"

def load_salaries():
    if os.path.exists(SALARY_FILE):
        with open(SALARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_salaries(data):
    with open(SALARY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def run_salary_app():
    st.title("👨‍🏫 Teacher Salary Manager")

    salaries = load_salaries()
    name = st.text_input("👨‍🏫 Teacher Name")
    amount = st.number_input("💰 Salary Amount", min_value=0)
    month = st.selectbox("📆 Month", [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])

    if st.button("💾 Submit Salary"):
        if name and amount > 0:
            salaries.append({"name": name, "amount": amount, "month": month})
            save_salaries(salaries)
            st.success("✅ Salary saved successfully.")

    st.subheader("📜 Salary Records")
    for record in salaries:
        st.write(f"{record['name']} - {record['amount']} PKR ({record['month']})")
