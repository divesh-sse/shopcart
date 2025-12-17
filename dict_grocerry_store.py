import streamlit as st

st.title("🛒 Mini Grocery Store App")
st.write("A simple Streamlit app to understand Python Dictionaries")

# ---------------------------------------
# STORE DICTIONARY (KEY → VALUE)
# ---------------------------------------

if "store" not in st.session_state:
    st.session_state.store = {
        "rice": 45,
        "wheat": 38,
        "milk": 30,
        "oil": 180
    }

store = st.session_state.store

# ---------------------------------------
# TABS
# ---------------------------------------

tab1, tab2 = st.tabs(["🧑‍💼 Shopkeeper", "🛍 Customer"])

# =======================================
# SHOPKEEPER TAB
# =======================================
with tab1:
    st.header("🧑‍💼 Money Minded Shopkeeper ")

    st.subheader("📦 Current Store Items")
    st.write(store)

    st.subheader("➕ Add new Item ")

    item_name = st.text_input("Item name")
    item_price = st.number_input("Item price", min_value=1)

    if st.button("Add this "):
        store[item_name] = item_price
        st.success(f"{item_name} added successfully!")
        st.write("Updated Store:", store)

# =======================================
# CUSTOMER TAB
# =======================================
with tab2:
    st.header("🛍 yo Customerzz")

    st.subheader("🧾 Thats All i got man")
    st.write(store)

    item = st.text_input("Enter only one item name to buy")
    quantity = st.number_input("Enter quantity", min_value=1)

    if st.button("Generate Bill"):
        if item in store:
            price = store[item]
            total = price * quantity

            st.write("🛒 Item:", item)
            st.write("💰 Price per unit:", price)
            st.write("📦 Quantity:", quantity)
            st.success(f"🧾 Total Bill: ₹{total}")
        else:
            st.error("❌ Item not available in store")

