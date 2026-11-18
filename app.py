import streamlit as st
st.set_page_config(page_title = "Student Profile Portal",page_icon = "🎓",layout='centered')
st.title("Student Profile Portal")
st.caption("Developed by Chaithra B H")

st.info("Fill in your details and click View My Profile.")

name = st.text_input(
    "Student Name",
    placeholder="Enter your name"
)

roll = st.text_input(
    "USN / Roll Number",
    placeholder="Enter roll number"
)

department = st.selectbox(
    "Department",
    ["CSE", "ISE", "ECE", "EEE", "ME", "Civil", "Other"]
)

year = st.radio(
    "Current Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

if st.button("View My Profile"):
    if name and roll:
        st.success("Profile submitted successfully!")
        st.write("Name:", name)
        st.write("Roll Number:", roll)
        st.write("Department:", department)
        st.write("Year:", year)
    else:
        st.warning("Please fill in all details."
