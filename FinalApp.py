import streamlit as st
import subprocess

# Set page background color to a gradient
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #f6c5ea, #d6a4a4);
        color: #ffffff;
        padding: 0 50px;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 18px;
        margin-bottom: 20px;
    }
    .description {
        font-size: 16px;
        margin-bottom: 20px;
    }
    .button {
        background-color: #ffffff;
        color: #000000;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
        margin-top: 20px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #cccccc;
    }
    .animation {
        width: 100%;
        max-width: 800px;
        margin-bottom: 50px;
    }
    .image {
        width: 100%;
        max-width: 600px;
        border-radius: 10px;
        margin-bottom: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
st.title("🚀 Revolutionizing Technologies by OpenAI 🚀")
st.markdown("""
    OpenAI has been at the forefront of developing groundbreaking AI technologies that have the potential to revolutionize various industries. 
    Here, we explore some of the most revolutionary technologies developed by OpenAI.
""")

# Whisper AI section
st.markdown('<h2 class="title">Whisper AI</h2>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🔍 Explore our state-of-the-art speech recognition model that can transcribe and translate speech from multiple languages 🔍</p>', unsafe_allow_html=True)
st.image("https://cdn.dribbble.com/users/214929/screenshots/4967879/ai-loader-opt.gif", use_column_width=True, caption="Whisper AI")

if st.button("🎙 Try Whisper AI", key="whisper_ai"):
    subprocess.Popen(["streamlit", "run", "Whisper_final.py"])
    # st.experimental_set_query_params(next_app="app_b_url")

# ChatBot section
st.markdown('<h2 class="title">ChatBot</h2>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🤖 Experience our AI-powered conversational agent that can assist you with various tasks and answer your questions 🤖</p>', unsafe_allow_html=True)
st.image("https://media.licdn.com/dms/image/C5612AQHaxX-jdKUrqg/article-cover_image-shrink_600_2000/0/1566196946786?e=2147483647&v=beta&t=IAZdJ6-ZapLN_4Nvw76uDC4gaoaFaUFVZ3gmWUzY1qc", use_column_width=True, caption="ChatBot")

if st.button("💬 Start ChatBot", key="chatbot"):
    subprocess.Popen(["streamlit", "run", "Chatbot_final.py"])
    # st.experimental_set_query_params(next_app="app_c_url")
