import streamlit as st
import openai
import subprocess
import importlib

# Set the desired OpenAI version
desired_openai_version = "0.28.0"

# Check if the installed OpenAI version matches the desired version
if openai.__version__ != desired_openai_version:
    # Print a warning message indicating the version mismatch
    st.warning(f"The installed OpenAI version ({openai.__version__}) does not match the desired version ({desired_openai_version}).")

    # Install the desired OpenAI version using pip
    st.info(f"Installing OpenAI version {desired_openai_version}...")
    subprocess.call(['pip', 'install', f'openai=={desired_openai_version}'])

    # Check if the installation was successful
    try:
        importlib.reload(openai)
        st.success(f"OpenAI version {desired_openai_version} installed successfully.")
    except ImportError:
        st.error(f"Failed to install OpenAI version {desired_openai_version}. Please check your pip installation and try again.")
else:
    # OpenAI version matches the desired version
    st.success(f"OpenAI version {desired_openai_version} is already installed.")

# Set your OpenAI API key
api_key = "sk-proj-2Pj9vlSlHfcw8B5JHkOOT3BlbkFJ3GU3Q2wnepA3Ib2GWe8o"
openai.api_key = api_key

st.title("ChatGPT")

# Initialize conversation history in session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Function to display conversation history
def display_conversation(history):
    for message in history:
        # Use the same background color for both "You:" and "ChatGPT:" messages
        background_color = "#24c404"  # Light green for both "You:" and "ChatGPT:" messages
        if message == "-----":
            # Set background color to None for horizontal line
            st.markdown('<hr style="border-top: 1px solid #d3d3d3; margin: 10px 0px; background-color: None;">', unsafe_allow_html=True)
        else:
            # Use the selected background color to set the background of the conversation text
            st.markdown(f'<div style="background-color: {background_color}; padding: 10px; margin-bottom: 10px; border-radius: 10px;">{message}</div>', unsafe_allow_html=True)

# User input
user_input = st.text_input("You:", "")

# Send request to the correct endpoint when user sends a message
if st.button("Send"):
    if user_input.strip() != "":
        # Add user input to conversation history under "You:"
        st.session_state.conversation_history.append("You: " + user_input)

        # Get AI response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate chat-based model
            messages=[
                {"role": "user", "content": user_input}
            ],
            max_tokens=500,
            temperature=0.9,
        )
        ai_response = response.choices[0].message.content.strip()

        # Add AI response to conversation history under "ChatGPT:"
        st.session_state.conversation_history.append("ChatGPT: " + ai_response)

        # Add horizontal line after "ChatGPT:" response
        st.session_state.conversation_history.append("-----")

# Display conversation history
display_conversation(st.session_state.conversation_history)

# Link to OpenAI API documentation
st.markdown("[OpenAI API Documentation](https://beta.openai.com/docs/)")
