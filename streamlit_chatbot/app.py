import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_calendar import calendar

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

        if "tasks" not in st.session_state:
            st.session_state.tasks = []

        st.session_state.tasks.append({
            "title": assignment_name,
            "start": str(deadline),
            "color": "#ff6b6b"
        })

        st.success("Task Added!")

    st.subheader("📅 Assignment Calendar")

    if "tasks" in st.session_state:

        calendar_options = {
            "initialView": "dayGridMonth",
            "height": 650,
        }

        calendar(
            events=st.session_state.tasks,
            options=calendar_options
        )

    else:
        st.info("No assignments added yet.")

# ======================================================
# CLASS TIMETABLE
# ======================================================
elif menu == "Class Timetable":

    st.header("📚 Class Timetable")

    # User inputs
    class_name = st.text_input("Class Name")

    class_day = st.date_input("Class Date")

    start_time = st.text_input(
        "Start Time (24-hour format, example: 08:00)"
    )

    end_time = st.text_input(
        "End Time (24-hour format, example: 10:00)"
    )

    # Add class button
    if st.button("Add Class"):

        # Create storage if not exists
        if "classes" not in st.session_state:
            st.session_state.classes = []

        try:

            # Convert input into datetime
            start_datetime = datetime.strptime(
                f"{class_day} {start_time}",
                "%Y-%m-%d %H:%M"
            )

            end_datetime = datetime.strptime(
                f"{class_day} {end_time}",
                "%Y-%m-%d %H:%M"
            )

            # Add event into calendar
            st.session_state.classes.append({
                "title": class_name,
                "start": start_datetime.isoformat(),
                "end": end_datetime.isoformat(),
                "color": "#4dabf7"
            })

            st.success("Class Added Successfully!")

        except:
            st.error(
                "Invalid time format. Please use HH:MM format."
            )

    # Display timetable calendar
    st.subheader("🗓️ Weekly Timetable")

    if "classes" in st.session_state:

        calendar_options = {
            "initialView": "timeGridWeek",
            "slotMinTime": "07:00:00",
            "slotMaxTime": "22:00:00",
            "height": 700,
        }

        calendar(
            events=st.session_state.classes,
            options=calendar_options
        )

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