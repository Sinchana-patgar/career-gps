import streamlit as st

st.set_page_config(page_title="Login - Career GPS", page_icon="🔐")

# ── Session State Init ──────────────────────────
if "users" not in st.session_state:
    st.session_state.users = {}  # {username: password}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None

# ── If already logged in, redirect ──────────────
if st.session_state.logged_in:
    st.switch_page("main.py")

st.title("🔐 Career GPS")

tab1, tab2 = st.tabs(["Login", "Sign Up"])

# ── Login Tab ────────────────────────────────────
with tab1:
    st.subheader("Login")
    login_user = st.text_input("Username", key="login_user")
    login_pass = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login", use_container_width=True):
        if login_user in st.session_state.users and st.session_state.users[login_user] == login_pass:
            st.session_state.logged_in = True
            st.session_state.username = login_user
            st.success("Logged in successfully!")
            st.switch_page("main.py")
        else:
            st.error("Invalid username or password.")

# ── Sign Up Tab ──────────────────────────────────
with tab2:
    st.subheader("Create Account")
    new_user = st.text_input("Choose a username", key="signup_user")
    new_pass = st.text_input("Choose a password", type="password", key="signup_pass")
    confirm_pass = st.text_input("Confirm password", type="password", key="signup_confirm")

    if st.button("Sign Up", use_container_width=True):
        if not new_user or not new_pass:
            st.error("Username and password cannot be empty.")
        elif new_user in st.session_state.users:
            st.error("Username already exists.")
        elif new_pass != confirm_pass:
            st.error("Passwords do not match.")
        else:
            st.session_state.users[new_user] = new_pass
            st.success("Account created! Please log in.")
