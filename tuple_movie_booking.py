import streamlit as st

st.title("🎬 Movie Ticket Booking System")
st.write("This app demonstrates LIST vs TUPLE using a real booking example")

# -------------------------------------------------
# MOVIES → LIST (CAN CHANGE)
# -------------------------------------------------
if "movies" not in st.session_state:
    st.session_state.movies = ["Inception", "Interstellar", "Avengers"]

movies = st.session_state.movies

# -------------------------------------------------
# SEATS → TUPLE (FIXED, ORDERED)
# -------------------------------------------------
seats = ("A1", "A2", "A3", "A4", "A5")

# -------------------------------------------------
# BOOKED SEATS → DICTIONARY
# -------------------------------------------------
if "booked" not in st.session_state:
    st.session_state.booked = {}

booked = st.session_state.booked

# -------------------------------------------------
# TABS
# -------------------------------------------------
tab1, tab2 = st.tabs(["🎥 Movie Manager", "🎟 Book Ticket"])

# =================================================
# TAB 1 — MOVIE MANAGER (LIST)
# =================================================
with tab1:
    st.header("🎥 Movie Manager (LIST)")

    st.subheader("Available Movies")
    st.write(movies)

    new_movie = st.text_input("Add a new movie")
    if st.button("Add Movie"):
        movies.append(new_movie)
        st.success("Movie added successfully!")
        st.write(movies)

    remove_movie = st.text_input("Remove a movie")
    if st.button("Remove Movie"):
        if remove_movie in movies:
            movies.remove(remove_movie)
            st.success("Movie removed successfully!")
        else:
            st.error("Movie not found")
        st.write(movies)

# =================================================
# TAB 2 — TICKET BOOKING (TUPLE + DICT)
# =================================================
with tab2:
    st.header("🎟 Ticket Booking")

    st.subheader("Available Movies")
    st.write(movies)

    movie = st.selectbox("Select movie", movies)

    st.subheader("Seat Layout (TUPLE — Fixed)")
    st.write(seats)

    seat = st.text_input("Enter seat number (A1–A5)")

    if st.button("Book Seat"):
        key = movie + "_" + seat

        if seat not in seats:
            st.error("❌ Invalid seat number")

        elif key in booked:
            st.error("❌ Seat already booked for this movie")

        else:
            booked[key] = "BOOKED"
            st.success(f"✅ Seat {seat} booked for {movie}")

    st.subheader("📌 Booked Seats")
    st.write(booked)
