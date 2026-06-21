import streamlit as st
from pages import grammar_fun, home, translation
PAGES = {
    "Home": home,
    #"Image Comprehension": image_comprehension,
    "Grammar and Fun": grammar_fun,
    "Reading and Translation": translation
}

def main():
    st.sidebar.title('Navigation')
    selection=st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()