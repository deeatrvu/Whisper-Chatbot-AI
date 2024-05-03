import streamlit as st

import openai
import subprocess
import importlib

# Set the desired OpenAI version
desired_openai_version = "1.25.1"

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

api_key = "sk-proj-2Pj9vlSlHfcw8B5JHkOOT3BlbkFJ3GU3Q2wnepA3Ib2GWe8o"
openai.api_key = api_key

from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="sk-proj-2Pj9vlSlHfcw8B5JHkOOT3BlbkFJ3GU3Q2wnepA3Ib2GWe8o")  # Replace "YOUR_API_KEY" with your actual API key

# Title and description
st.title("🔊 Whisper AI Transcriber & Translator 🌐")
st.write("Welcome to Whisper AI, where your audio speaks volumes! Whisper AI offers state-of-the-art transcription and translation services.")

# File upload
audio_file = st.file_uploader("Upload your audio file", type=["mp3", "wav"])

# Checkboxes for transcription and translation
transcribe_enabled = st.checkbox("Transcribe")
translate_enabled = st.checkbox("Translate")

if audio_file:

    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav', start_time=0)

    # Perform transcription if enabled
    if transcribe_enabled:
        st.write("Transcription Output:")
        try:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",  # Use the appropriate model
                file=audio_file,
            )
            transcribed_text = transcription.text
            st.write(transcription.text)
        except Exception as e:
            st.error(f"Transcription failed: {str(e)}")

    # Perform translation if enabled
    if translate_enabled:
        # Language selection dropdown
        target_language = st.selectbox("English",
                                       ["English"])

        # Translate audio
        st.write("Translation Output:")
        # try:
        #     translation = client.audio.translations.create(
        #         model="whisper-1",  # Use the appropriate model
        #         file=audio_bytes,
        #         target_language=target_language
        #     )
        #     st.write(translation.text)

        try:
            translation = client.audio.translations.create(
                model="whisper-1",
                file=audio_file
            )
            # st.write(translation["choices"][0]["text"].strip())
            st.write(translation.text)
        except Exception as e:
            st.error(f"Translation failed:{str(e)}")