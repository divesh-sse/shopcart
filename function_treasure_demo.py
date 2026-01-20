import streamlit as st

st.set_page_config(page_title="🏴‍☠️ Treasure Adventure", page_icon="💎")

# Initialize game state
if "stage" not in st.session_state:
    st.session_state.stage = "start"

st.title("🏴‍☠️ Treasure Adventure Game")
st.write("---")


def restart_game():
    st.session_state.stage = "start"


# ---------------- START ----------------
if st.session_state.stage == "start":
    st.subheader("🌄 Welcome to the Treasure Game!")
    st.write("You are standing at a **crossroad**.")
    st.write("Where do you want to go?")

    choice = st.radio("Choose your path:", ["🌲 Forest", "🏘️ Village"])

    if st.button("➡️ Continue"):
        if "Forest" in choice:
            st.session_state.stage = "forest"
        else:
            st.session_state.stage = "village"


# ---------------- FOREST ----------------
elif st.session_state.stage == "forest":
    st.subheader("🌲 Dark Forest")
    st.write("You enter a dark forest.")
    st.write("You see a **cave 🕳️** and a **river 🌊**.")

    choice = st.radio("What will you explore?", ["🕳️ Cave", "🌊 River"])

    if st.button("➡️ Continue"):
        if "Cave" in choice:
            st.session_state.stage = "cave"
        else:
            st.session_state.stage = "river"


# ---------------- CAVE ----------------
elif st.session_state.stage == "cave":
    st.subheader("🕳️ Mysterious Cave")
    st.write("Inside the cave, you see a **locked chest 🔒** and a **sleeping dragon 🐉**.")

    choice = st.radio("What will you do?", ["🔓 Open Chest", "🐉 Fight Dragon"])

    if st.button("➡️ Continue"):
        if "Open" in choice:
            st.success("💎 You found the TREASURE! You Win! 🎉")
            st.balloons()
            st.button("🔁 Restart Game", on_click=restart_game)
        else:
            st.error("🔥 The dragon wakes up and burns you! Game Over 😵")
            st.button("🔁 Restart Game", on_click=restart_game)


# ---------------- RIVER ----------------
elif st.session_state.stage == "river":
    st.subheader("🌊 Dangerous River")
    st.write("The river is flowing fast!")

    choice = st.radio("Your decision:", ["🏊 Swim", "⛵ Build Raft"])

    if st.button("➡️ Continue"):
        if "Swim" in choice:
            st.error("💀 You drown in the river. Game Over.")
            st.button("🔁 Restart Game", on_click=restart_game)
        else:
            st.success("🗺️ You cross safely and find hidden gold! You Win! 💰")
            st.button("🔁 Restart Game", on_click=restart_game)


# ---------------- VILLAGE ----------------
elif st.session_state.stage == "village":
    st.subheader("🏘️ Quiet Village")
    st.write("You meet an **old man 👴** near a hut.")

    choice = st.radio("What will you do?", ["💬 Talk", "🚶 Ignore"])

    if st.button("➡️ Continue"):
        if "Talk" in choice:
            st.session_state.stage = "old_man"
        else:
            st.error("😕 You miss valuable information. Game Over.")
            st.button("🔁 Restart Game", on_click=restart_game)


# ---------------- OLD MAN ----------------
elif st.session_state.stage == "old_man":
    st.subheader("👴 Wise Old Man")
    st.write("He gives you a **map 🗺️** and a **magic key 🗝️**.")

    choice = st.radio("Where will you go now?", ["🌲 Forest", "🏰 Castle"])

    if st.button("➡️ Continue"):
        if "Forest" in choice:
            st.success("💎 The key opens a hidden chest in the forest. You Win!")
            st.balloons()
            st.button("🔁 Restart Game", on_click=restart_game)
        else:
            st.error("🏰 The castle is cursed. You are trapped forever! 😱")
            st.button("🔁 Restart Game", on_click=restart_game)
