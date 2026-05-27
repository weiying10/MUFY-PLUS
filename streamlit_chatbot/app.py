import streamlit as st
import pandas as pd
from datetime import datetime

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="Campus Companion",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📚 Campus Companion")
st.subheader("Your Student Productivity & Wellness Assistant")

# -----------------------------
# SIDEBAR MENU
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "Assignment Tracker",
        "Class Timetable",
        "Wellness Check-In",
        "Study Buddy Finder"
    ]
)

# ======================================================
# ASSIGNMENT TRACKER
# ======================================================
if menu == "Assignment Tracker":

    st.header("📝 Assignment & Exam Tracker")

    assignment_name = st.text_input("Assignment / Exam Name")
    deadline = st.date_input("Deadline")

    if st.button("Add Task"):

        task = {
            "Task": assignment_name,
            "Deadline": deadline
        }

        if "tasks" not in st.session_state:
            st.session_state.tasks = []

        st.session_state.tasks.append(task)

        st.success("Task Added Successfully!")

    st.subheader("Upcoming Tasks")

    if "tasks" in st.session_state:
        df = pd.DataFrame(st.session_state.tasks)
        st.table(df)
    else:
        st.info("No tasks added yet.")

# ======================================================
# CLASS TIMETABLE
# ======================================================
elif menu == "Class Timetable":

    st.header("📅 Class Timetable")

    class_name = st.text_input("Class Name")
    class_time = st.time_input("Class Time")

    if st.button("Add Class"):

        class_data = {
            "Class": class_name,
            "Time": class_time
        }

        if "classes" not in st.session_state:
            st.session_state.classes = []

        st.session_state.classes.append(class_data)

        st.success("Class Added!")

    st.subheader("Today's Classes")

    if "classes" in st.session_state:
        df = pd.DataFrame(st.session_state.classes)
        st.table(df)
    else:
        st.info("No classes added yet.")

# ======================================================
# WELLNESS CHECK-IN
# ======================================================
elif menu == "Wellness Check-In":

    st.header("💙 Mental Wellness Check-In")

    mood = st.selectbox(
        "How are you feeling today?",
        ["😊 Happy", "😐 Okay", "😴 Tired", "😔 Stressed"]
    )

    if st.button("Check In"):

        if mood == "😊 Happy":
            quote = "Keep going! Your positive energy matters."

        elif mood == "😐 Okay":
            quote = "One step at a time is still progress."

        elif mood == "😴 Tired":
            quote = "Rest is productive too. Don't forget to recharge."

        else:
            quote = "You're stronger than you think. Take things slowly."

        st.success("Check-In Complete!")
        st.write("### 🌟 Motivation Quote")
        st.info(quote)

# ======================================================
# STUDY BUDDY FINDER
# ======================================================
elif menu == "Study Buddy Finder":

    import folium
    from streamlit_folium import st_folium

    st.header("📍 Find Study Buddies Nearby")

    subject = st.selectbox(
        "What are you studying now?",
        [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "Account",
            "English"
        ]
    )

    st.write("### Students currently studying nearby")

    # Example coordinates (fake demo data)
    students = [
        {
            "name": "Ali",
            "subject": "Account",
            "location": [3.1390, 101.6869]
        },
        {
            "name": "Siti",
            "subject": "Mathematics",
            "location": [3.1405, 101.6880]
        },
        {
            "name": "Jason",
            "subject": "Physics",
            "location": [3.1380, 101.6875]
        },
        {
            "name": "Mei",
            "subject": "English",
            "location": [3.1410, 101.6890]
        }
    ]

    # Center map
    m = folium.Map(
        location=[3.1390, 101.6869],
        zoom_start=16
    )

    # Add markers
    for student in students:

        if student["subject"] == subject:

            folium.Marker(
                location=student["location"],
                popup=f"{student['name']} studying {student['subject']}",
                tooltip=student["name"]
            ).add_to(m)

    # Show map
    st_folium(m, width=700, height=500)

    st.success("You're not studying alone 💪")


#streamlit run app.py