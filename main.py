import streamlit as st

def main():
    st.set_page_config(page_title="Career GPS", layout="wide")
    st.title("📍 Career GPS")
    st.write("Use sidebar to navigate")
    st.markdown("Your personal AI mentor to help you navigate your career journey")

    if st.button("Get Started 🚀"):
       st.switch_page("auth")

if __name__ == "__main__":
    main()
