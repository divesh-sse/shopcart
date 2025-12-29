import streamlit as st

st.set_page_config(page_title="ATM Simulator", layout="centered")

st.title("🏧 ATM Machine Simulator")
st.write("Learn Nested If + While Logic in Real Life Scenario")

# ---------------- Instructions ----------------
with st.expander("📘 Instructions for Students (Read First)"):
    st.write("""
### How this ATM works
1️⃣ First **set your account balance** and **choose a PIN**  
2️⃣ Then try to login using the PIN  
3️⃣ You only get **3 attempts**  
4️⃣ After login:
- Press **Withdraw** to take money  
- Press **Check Balance** to see balance  
5️⃣ If wrong PIN entered 3 times → Card Blocked ❌
    """)

# -------------- Initialize session states --------------
if "balance" not in st.session_state:
    st.session_state.balance = None

if "password" not in st.session_state:
    st.session_state.password = None

if "attempts" not in st.session_state:
    st.session_state.attempts = 3

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------- Setup Section --------------
st.subheader("🛠️ Setup ATM Account")

if st.session_state.balance is None:
    balance = st.number_input("Enter Starting Balance", min_value=0, value=5000)
    password = st.text_input("Set ATM PIN", type="password")

    if st.button("Save & Activate ATM"):
        if password == "":
            st.error("PIN cannot be empty!")
        else:
            st.session_state.balance = balance
            st.session_state.password = password
            st.success("ATM Setup Successful! Scroll down to login 👇")

# -------------- If setup done, show login --------------
if st.session_state.balance is not None and not st.session_state.logged_in:

    st.subheader("🔐 Login to ATM")

    pin = st.text_input("Enter PIN", type="password")

    if st.button("Login"):
        if st.session_state.attempts == 0:
            st.error("❌ Card Blocked! Restart App to Reset.")
        elif pin == st.session_state.password:
            st.success("🎉 Login Successful!")
            st.session_state.logged_in = True
        else:
            st.session_state.attempts -= 1
            st.error(f"Wrong PIN! Attempts left: {st.session_state.attempts}")

            if st.session_state.attempts == 0:
                st.error("❌ Card Blocked!")

# -------------- After Login Section --------------
if st.session_state.logged_in:

    st.subheader("💳 ATM Menu")

    choice = st.radio("Choose Action", ["Check Balance", "Withdraw Money"])

    if choice == "Check Balance":
        st.info(f"💰 Your Balance: ₹{st.session_state.balance}")

    if choice == "Withdraw Money":
        amt = st.number_input("Enter amount to withdraw", min_value=1)

        if st.button("Withdraw"):
            if amt <= st.session_state.balance:
                st.session_state.balance -= amt
                st.success("Withdrawal Successful 💸")
                st.info(f"Remaining Balance: ₹{st.session_state.balance}")
            else:
                st.error("❌ Insufficient Balance")

# -------------- Reset Button --------------
st.divider()
if st.button("🔄 Reset ATM"):
    st.session_state.clear()
    st.experimental_rerun()
