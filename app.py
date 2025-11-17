import streamlit as st
import random

# ------------------ Setup ------------------
st.set_page_config(page_title="WaterBuddy", layout="centered")

# ------------------ Session State Init ------------------
if "page" not in st.session_state:
    st.session_state.page = "onboarding"
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "age_group" not in st.session_state:
    st.session_state.age_group = ""
if "goal_ml" not in st.session_state:
    st.session_state.goal_ml = 0
if "total_intake" not in st.session_state:
    st.session_state.total_intake = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "history" not in st.session_state:
    st.session_state.history = []
if "average_intake" not in st.session_state:
    st.session_state.average_intake = 0

# ------------------ Age Groups ------------------
age_groups = {
    "Child (4–8 years)": {"goal_ml": 1200, "goal_l": "1.2L", "cups": "4–5 cups"},
    "Teen (9–13 years)": {"goal_ml": 1700, "goal_l": "1.7L", "cups": "6–7 cups"},
    "Adult (14–64 years)": {"goal_ml": 2250, "goal_l": "2.25L", "cups": "8–10 cups"},
    "Senior (65+ years)": {"goal_ml": 1850, "goal_l": "1.85L", "cups": "6–8 cups"}
}

# ------------------ Onboarding Page ------------------
if st.session_state.page == "onboarding":
    st.title("💧 WaterBuddy")
    st.markdown("### Welcome to WaterBuddy – Your intelligent hydration companion for healthier habits.")
    
    st.text_input("👋 What should we call you?", key="user_name")
    age = st.selectbox("Choose your age group:", list(age_groups.keys()))
    st.session_state.age_group = age
    goal_info = age_groups[age]
    st.session_state.goal_ml = goal_info["goal_ml"]
    
    st.markdown(f"**Recommended Goal:** {goal_info['goal_l']} per day ({goal_info['cups']})")
    
    st.markdown("🔒 **100% Private:** All your data stays on your device. No sign-ups, no tracking…")
    
    with st.expander("💡 Why Hydration Matters"):
        st.markdown("- **Energy & Focus**: Water helps your brain work better and keeps you alert")
        st.markdown("- **Temperature Control**: Regulates body temperature through sweating")
        st.markdown("- **Skin Health**: Keeps your skin healthy and glowing")
        st.markdown("- **Physical Performance**: Supports muscle function and recovery")
    
    st.markdown("🧠 **Why WaterBuddy is different:** Simple, age-based guidance with friendly motivation. No logins, no clutter.")
    
    if st.button("🚀 Start My Hydration Journey"):
        st.session_state.page = "dashboard"

# ------------------ Dashboard Page ------------------
elif st.session_state.page == "dashboard":
    st.title("💧 WaterBuddy")
    st.markdown(f"Hello, **{st.session_state.user_name}**! 🌟")
    
    if st.button("🔄 New Day"):
        st.session_state.total_intake = 0
        st.session_state.history = []
    
    # Progress
    goal = st.session_state.goal_ml
    total = st.session_state.total_intake
    remaining = max(goal - total, 0)
    progress = min(int((total / goal) * 100), 100)
    
    st.subheader("📊 Today's Progress")
    st.progress(progress)
    st.write(f"**{total / 1000:.1f}L of {goal / 1000:.1f}L goal**")
    st.write(f"**{remaining} ml remaining**")
    st.write(f"Let's get started, {st.session_state.user_name}! Your body will thank you 💧")
    
    # Stats
    st.subheader("📈 Your Stats")
    st.write("😴 Status: Thirsty" if total == 0 else "😊 Status: Hydrated")
    st.write(f"🔥 Day Streak: {st.session_state.streak} days")
    st.write(f"🥤 Total Today: {len(st.session_state.history)} drinks")
    st.write(f"📊 Average: {st.session_state.average_intake} ml")
    
    # Quick Add
    st.subheader("🚰 Quick Add Water")
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("Glass\n200ml"):
        st.session_state.total_intake += 200
        st.session_state.history.append(200)
    if col2.button("Can\n330ml"):
        st.session_state.total_intake += 330
        st.session_state.history.append(330)
    if col3.button("Bottle\n500ml"):
        st.session_state.total_intake += 500
        st.session_state.history.append(500)
    if col4.button("Large Bottle\n750ml"):
        st.session_state.total_intake += 750
        st.session_state.history.append(750)
    
    # Tips
    st.subheader("💡 Daily Hydration Tips")
    tips = [
        "Try drinking a glass of water before each meal 🍽️",
        "Keep your water bottle on your desk or workspace 💼",
        "Start your day with a glass of water ☀️",
        "Use a marked bottle to track intake 📏",
        "Set hourly reminders to sip ⏰"
    ]
    st.write(random.choice(tips))
    
    # History
    st.subheader("📅 Today's History")
    if not st.session_state.history:
        st.write("No water logged yet today.")
        st.write("Tap above to log your first drink!")
    else:
        for i, amount in enumerate(st.session_state.history, 1):
            st.write(f"Drink {i}: {amount} ml")
    
    # Weekly Overview (Placeholder)
    st.subheader("📆 7 Day Overview")
    st.bar_chart([0, 0, 0, 0, 0, 0, total])

    # Settings
    with st.sidebar:
        st.title("⚙️ Settings")
        st.text_input("Name", value=st.session_state.user_name, key="user_name")
        st.selectbox("Age Group", options=list(age_groups.keys()), index=list(age_groups.keys()).index(st.session_state.age_group), key="age_group")
        st.write(f"Daily Goal: {st.session_state.goal_ml / 1000:.2f} Liters")
        new_goal = st.number_input("Adjust Goal (ml)", value=st.session_state.goal_ml, step=50)
        st.session_state.goal_ml = new_goal
        st.markdown("🔒 All data is stored locally on your device.")
        if st.button("❌ Reset Profile"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.session_state.page = "onboarding"
