import streamlit as st
import random

# ------------------ Setup ------------------
st.set_page_config(page_title="WaterBuddy", layout="centered")
st.title("💧 WaterBuddy: Your Daily Hydration Companion")

# ------------------ Age Groups & Goals ------------------
age_groups = {
    "Children (4–8)": 1200,
    "Teens (9–13)": 1700,
    "Adults (14–64)": 2500,
    "Seniors (65+)": 2000
}

# ------------------ Session State Init ------------------
if "total_intake" not in st.session_state:
    st.session_state.total_intake = 0
if "goal" not in st.session_state:
    st.session_state.goal = 0
if "age_group" not in st.session_state:
    st.session_state.age_group = ""

# ------------------ Age Selection ------------------
st.subheader("👤 Select Your Age Group")
age = st.selectbox("Choose your age group:", list(age_groups.keys()))
default_goal = age_groups[age]
custom_goal = st.number_input("Suggested goal (ml):", value=default_goal, step=100)
st.session_state.goal = custom_goal
st.session_state.age_group = age

# ------------------ Water Logging ------------------
st.subheader("🚰 Log Your Water Intake")
col1, col2 = st.columns(2)
with col1:
    if st.button("+250 ml"):
        st.session_state.total_intake += 250
with col2:
    manual_input = st.number_input("Manual entry (ml):", min_value=0, step=50)
    if st.button("Add manual amount"):
        st.session_state.total_intake += manual_input

# ------------------ Reset Button ------------------
if st.button("🔄 New Day / Reset"):
    st.session_state.total_intake = 0

# ------------------ Calculations ------------------
goal = st.session_state.goal
total = st.session_state.total_intake
remaining = max(goal - total, 0)
progress = min(int((total / goal) * 100), 100)

# ------------------ Visual Feedback ------------------
st.subheader("📊 Your Progress")
st.progress(progress)
st.write(f"**Total intake:** {total} ml")
st.write(f"**Remaining:** {remaining} ml")
st.write(f"**Progress:** {progress}% of your goal")

# ------------------ Motivational Messages ------------------
st.subheader("🎉 Motivation")
if progress >= 100:
    st.success("🏆 Amazing! You've hit your goal!")
elif progress >= 75:
    st.info("💪 You're almost there! Keep sipping!")
elif progress >= 50:
    st.info("😊 Halfway done! Great job!")
elif progress >= 25:
    st.info("👍 Good start! Stay hydrated!")
else:
    st.warning("👀 Let's get that bottle moving!")

# ------------------ Mascot Reaction ------------------
st.subheader("🐢 WaterBuddy Mascot")
if progress >= 100:
    st.image("https://cdn.pixabay.com/photo/2020/04/25/09/44/turtle-5090966_1280.png", caption="Mascot claps! 🐢")
elif progress >= 75:
    st.image("https://cdn.pixabay.com/photo/2020/04/25/09/44/turtle-5090964_1280.png", caption="Mascot waves! 🐢")
elif progress >= 50:
    st.image("https://cdn.pixabay.com/photo/2020/04/25/09/44/turtle-5090965_1280.png", caption="Mascot smiles! 🐢")
else:
    st.image("https://cdn.pixabay.com/photo/2020/04/25/09/44/turtle-5090963_1280.png", caption="Mascot encourages you! 🐢")

# ------------------ Daily Tips ------------------
tips = [
    "Drink a glass of water before each meal.",
    "Keep a bottle on your desk.",
    "Use a marked bottle to track intake.",
    "Start your day with a glass of water.",
    "Set hourly reminders to sip."
]
st.sidebar.title("💡 Daily Hydration Tip")
st.sidebar.write(random.choice(tips))
