
import streamlit as st

st.title("🎧 Student Music Interest Analyzer")
st.write("Understanding LIST vs SET using music genres")

# ------------------------------------
# LIST OF GENRES (FIXED OPTIONS)
# ------------------------------------
genres_list = [
    "Rock",
    "Pop",
    "Jazz",
    "Hip Hop",
    "Classical",
    "EDM",
    "Techno",
    "Retro",
    "Metal",
    "Drill"
]

st.subheader("🎵 Available Genres (LIST)")
st.write(genres_list)

# ------------------------------------
# STUDENT SELECTION (FROM LIST)
# ------------------------------------
st.header("🎧 Select Music Genres")

student1_selection = st.multiselect(
    "Student 1 - Select genres",
    genres_list,
    default=["Hip Hop"]
)

student2_selection = st.multiselect(
    "Student 2 - Select genres",
    genres_list,
    default=["EDM"]
)

# ------------------------------------
# CONVERT LIST TO SET
# ------------------------------------
student1_set = set(student1_selection)
student2_set = set(student2_selection)

# ------------------------------------
# DISPLAY SETS
# ------------------------------------
st.subheader("📌 Student Genre Sets (Unique Values)")

st.write("Student 1 Set:", student1_set)
st.write("Student 2 Set:", student2_set)

# ------------------------------------
# SET OPERATIONS
# ------------------------------------
st.header("🔍 Set Operations")

common_genres = student1_set & student2_set
all_genres = student1_set | student2_set
only_student1 = student1_set - student2_set
only_student2 = student2_set - student1_set

st.write("🤝 Common Genres:", common_genres)
st.write("🌍 All Unique Genres:", all_genres)
st.write("🎯 Only Student 1 Likes:", only_student1)
st.write("🎯 Only Student 2 Likes:", only_student2)

st.success("✅ Sorted!")
