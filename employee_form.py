import streamlit as st
from datetime import date

st.title("Employee Data Entry Form")

current_project = st.text_input("Currently working on what project")
finish_date = st.date_input("When are you finished on current project?", min_value=date.today())

st.subheader("List all previous project experience")
experience = []
for i in range(3):
    cols = st.columns(2)
    with cols[0]:
        project_name = st.text_input(f"Project name {i+1}", key=f"project_{i}")
    with cols[1]:
        construction_type = st.selectbox(
            f"Construction type {i+1}", 
            ["Commercial", "Residential", "Industrial", "Healthcare", "Other"], 
            key=f"type_{i}"
        )
    if project_name:
        experience.append((project_name, construction_type))

job_title = st.selectbox("Job title", ["Superintendent", "Project Manager", "Field Engineer", "Assistant PM", "Other"])
coworkers = st.text_area("Coworkers you've worked with (first and last names, comma separated)")
location = st.text_input("Location of residence")
relocate = st.radio("Willing to relocate", ["Yes", "No", "Possibly"])

if st.button("Submit"):
    st.success("Employee data submitted successfully!")
    st.write("**Summary:**")
    st.write("Current Project:", current_project)
    st.write("Finish Date:", finish_date)
    st.write("Previous Experience:", experience)
    st.write("Job Title:", job_title)
    st.write("Coworkers:", coworkers)
    st.write("Location:", location)
    st.write("Willing to relocate:", relocate)
