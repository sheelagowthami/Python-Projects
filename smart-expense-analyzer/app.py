import streamlit as st

# ---------------- USER NAME ----------------
st.title("📊 Smart Expense Analyzer")

name = st.text_input("Enter your name")

if name:
    st.write(f"Welcome, {name} 👋")

# ---------------- SESSION STORAGE ----------------
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# ---------------- MENU ----------------
menu = st.sidebar.selectbox(
    "Menu", ["Add Expense", "View Expenses", "Analysis"]
)

# ---------------- ADD EXPENSE ----------------
if menu == "Add Expense":
    st.subheader("➕ Add New Expense")

    category = st.selectbox(
        "Select Category",
        ["Food", "Travel", "Shopping", "Bills", "Other"]
    )

    amount = st.number_input("Enter Amount (₹)", min_value=0.0)

    if st.button("Add Expense"):
        if not name:
            st.error("❌ Please enter your name first")
        elif amount > 0:
            st.session_state.expenses.append({
                "name": name,
                "category": category,
                "amount": amount
            })
            st.success("✅ Expense added successfully!")
        else:
            st.error("❌ Please enter a valid amount")

# ---------------- VIEW EXPENSES ----------------
elif menu == "View Expenses":
    st.subheader("📄 Your Expenses")

    user_expenses = [
        item for item in st.session_state.expenses if item["name"] == name
    ]

    if not user_expenses:
        st.warning("⚠ No expenses found for you")
    else:
        total = 0
        for item in user_expenses:
            st.write(f"{item['category']} - ₹{item['amount']}")
            total += item["amount"]

        st.markdown(f"### 💰 Total Spending: ₹ {total}")

# ---------------- ANALYSIS ----------------
elif menu == "Analysis":
    st.subheader("📊 Your Spending Analysis")

    user_expenses = [
        item for item in st.session_state.expenses if item["name"] == name
    ]

    if not user_expenses:
        st.warning("⚠ No data to analyze")
    else:
        category_total = {}

        for item in user_expenses:
            cat = item["category"]
            amt = item["amount"]

            category_total[cat] = category_total.get(cat, 0) + amt

        st.write("### Category-wise Spending:")
        for cat, amt in category_total.items():
            st.write(f"{cat}: ₹{amt}")

        st.write("### 📈 Spending Chart")
        st.bar_chart(category_total)

        max_category = max(category_total, key=category_total.get)
        st.success(f"💸 Highest Spending: {max_category}")
