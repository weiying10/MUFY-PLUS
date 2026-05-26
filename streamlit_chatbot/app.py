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

    st.header("🤝 Find Study Buddies")

    subject = st.selectbox(
        "What are you studying now?",
        [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "English"
        ]
    )

    if st.button("Find Study Partners"):

        fake_students = {
            "Mathematics": ["Ali", "Jason"],
            "Physics": ["Siti", "Daniel"],
            "Chemistry": ["Aina"],
            "Biology": ["Sarah"],
            "Computer Science": ["Kevin", "Mei"],
            "English": ["John"]
        }

        students = fake_students.get(subject, [])

        st.write(f"### Students studying {subject} now:")

        for student in students:
            st.write(f"✅ {student} is currently studying")

        st.success(
            "You're not studying alone anymore 💪"
        )


#streamlit run app.py