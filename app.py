import streamlit as st

st.set_page_config(
    page_title="My Webpage",
    page_icon="👋",
    layout="wide"
)

# Add custom CSS to set background color and header colors
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6e6fa;  /* Light lavender background color */
    }
    .header {
        color: #4b0082;  /* Indigo color for header */
        font-weight: bold;
        font-size: 24px;
    }
    .question {
        color: #2e8b57;  /* Sea Green color for questions */
        font-weight: bold;
    }
    .css-1d391kg {
        background-color: #dcdcdc;  /* Light gray background color for sidebar */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.header("🌟Growth Mindset Challenge!🌟")
# Define the pages
if "page" not in st.session_state:
    st.session_state.page = "Home"

page = st.sidebar.selectbox("Select a Page", ["Home", "Quiz"], index=["Home", "Quiz"].index(st.session_state.page), key="page_select")
st.sidebar.write("💫Learning hub💫")
st.sidebar.write("🔆Happy Coding🔆")
st.sidebar.subheader("created by Rabia Rizwan")


if page != st.session_state.page:
    st.session_state.page = page

if st.session_state.page == "Home":
    # Home Page
    st.header("Welcome To The Web Page!")
    st.subheader("Hi, I am Rabia :wave:")
    st.title("Web Developer From Pakistan")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings...")

    # ---What I Do----
    st.write("---")
    st.header("WHAT I DO?")
    st.write(
        """Hi! I’m Rabia Rizwan, a certified Frontend Web Developer, Graphic Designer, and Video Editor/Animator 🎨💻🎥. 
        \n I create sleek, user-friendly websites with Next.js, React, and more, and bring your ideas to life with stunning designs and animations.
        🌐✨ .
        \n In my portfolio, you’ll find a diverse range of exciting projects that showcase my creativity and commitment to quality. 
        My focus is on delivering high-quality work on time, every time ⏰
        \n ✔ Let's create something amazing together🚀!"""
    )

    if st.button("Start Quiz"):
        st.session_state.page = "Quiz"

elif st.session_state.page == "Quiz":
    # Quiz Page
    st.markdown('<h1 class="header">This is a Quiz Game!👨🎰</h1>', unsafe_allow_html=True)
    st.write("This Quiz Made By Rabia Rizwan!🥰")

    #---Question 1-----
    answer1 = st.selectbox("1. Which famous poet is considered the spiritual father of Pakistan?", ['Faiz Ahmed Faiz', 'Mirza Ghalib', 'Allama Iqbal', 'Ahmad Faraz'], key="q1")
    if answer1 == 'Allama Iqbal':
        st.balloons()  # Balloons will only execute if the answer is correct
        st.success("Right Answer ✔")
    else:
        st.error("Incorrect Answer!")

    #-----Question 2-----
    answer2 = st.selectbox("2. In which year was eBay founded?", ['1992', '1993', '1994', '1995'], key="q2")
    if answer2 == '1995':
        st.success("Right answer ✔")
    else:
        st.error("Incorrect Answer!")

    #---Question 3-----
    answer3 = st.selectbox("3. Which resolution, passed in 1940, laid the foundation for the creation of Pakistan?", ['Delhi Resolution', 'Karachi Resolution', 'Lahore Resolution', 'Lucknow Resolution'], key="q3")
    if answer3 == 'Lahore Resolution':
        st.success("Right answer ✔")
    else:
        st.error("Incorrect Answer!")

    #----Question 4-----
    answer4 = st.selectbox("4. Which Pakistani city is known as the 'City of Gardens'?", ['Islamabad', 'Karachi', 'Lahore', 'Peshawar'], key="q4")
    if answer4 == 'Lahore':
        st.success("Right answer ✔")
    else:
        st.error("Incorrect Answer!")

    #----Question 5-----
    answer5 = st.selectbox("5. In which year did Pakistan become a nuclear power?", ['1995', '1997', '2000', '1998'], key="q5")
    if answer5 == '1998':
        st.success("Right answer ✔")
    else:
        st.error("Incorrect Answer!")


        