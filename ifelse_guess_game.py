import streamlit as st
import random

st.title("🎮 Guess The Number Game")
st.write("Guess a number between 1 and 10. You get 6 chances!")

# -------------------------
# SESSION STATE
# -------------------------
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)

if "attempts" not in st.session_state:
    st.session_state.attempts = 6

if "game_over" not in st.session_state:
    st.session_state.game_over = False


# -------------------------
# GAME UI
# -------------------------
if st.session_state.game_over:
    st.warning("Game is already over. Click Play Again to restart.")


guess = st.number_input("Enter your guess:", 1, 10, step=1)

if st.button("Submit Guess") and not st.session_state.game_over:

    st.session_state.attempts -= 1

    if guess == st.session_state.secret:
        st.success(f"🎉 Correct Guess! You Win! The number was {st.session_state.secret}")
        st.session_state.game_over = True

    elif guess > st.session_state.secret:
        st.warning("Too High!")
    else:
        st.warning("Too Low!")

    st.info(f"Attempts left: {st.session_state.attempts}")

    # If attempts finished → GAME OVER
    if st.session_state.attempts == 0 and not st.session_state.game_over:
        st.error(f"❌ Game Over! You used all attempts. Number was {st.session_state.secret}")
        st.write(f"The number was: {st.session_state.secret}")
        st.session_state.game_over = True


# -------------------------
# RESET BUTTON
# -------------------------
if st.button("Play Again"):
    st.session_state.secret = random.randint(1, 10)
    st.session_state.attempts = 6
    st.session_state.game_over = False
    st.success("Game Reset! Try Again 😊")
