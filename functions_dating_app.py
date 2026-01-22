import streamlit as st

# ---------------- FUNCTIONS ---------------- #

def create_profile(name, age, interest, city):
    return {
        "name": name,
        "age": age,
        "interest": interest,
        "city": city
    }

def calculate_match_score(profile1, profile2):
    score = 0

    if profile1["interest"] == profile2["interest"]:
        score += 50

    if profile1["city"] == profile2["city"]:
        score += 30

    age_diff = abs(profile1["age"] - profile2["age"])
    if age_diff <= 2:
        score += 20

    return score

def is_match(score):
    return score >= 60


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="Campus Dating App", page_icon="💘")

st.title("💘 Campus Dating App")
st.write("Find out if it's a match based on simple compatibility rules!")

st.header("👤 Person 1 Details")
name1 = st.text_input("Name", key="name1")
age1 = st.number_input("Age", min_value=18, max_value=30, key="age1")
interest1 = st.selectbox("Interest", ["Music", "Sports", "Movies", "Travel", "Gaming"], key="int1")
city1 = st.selectbox("City", ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"], key="city1")

st.header("👤 Person 2 Details")
name2 = st.text_input("Name ", key="name2")
age2 = st.number_input("Age ", min_value=18, max_value=30, key="age2")
interest2 = st.selectbox("Interest ", ["Music", "Sports", "Movies", "Travel", "Gaming"], key="int2")
city2 = st.selectbox("City ", ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"], key="city2")

# ---------------- MATCH BUTTON ---------------- #

if st.button("💖 Check Match"):
    if name1 and name2:
        profile1 = create_profile(name1, age1, interest1, city1)
        profile2 = create_profile(name2, age2, interest2, city2)

        score = calculate_match_score(profile1, profile2)

        st.subheader("💘 Match Result")
        st.write(f"**Compatibility Score:** {score}")

        if is_match(score):
            st.success("🎉 It's a MATCH!")
            st.balloons()
        else:
            st.error("❌ Not a match. Keep swiping!")
    else:
        st.warning("⚠ Please enter both names!")
