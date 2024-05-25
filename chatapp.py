import streamlit as st
import openai

# Replace with your OpenAI API key
API_KEY = "sk-proj-8LWMDzIfj4RPXlboMEftT3BlbkFJPIJgCdo5w3DDPcSeAlOW"
openai.api_key = API_KEY  # Set the API key

def generate_lyrics(genre, language, topic=None):
    """
    Generates song lyrics based on genre, language, and optionally a topic
    """
    prompt_text = f"I am an AI Song Lyricist. Write me a song in the {genre} genre in {language}."
    if topic:
        prompt_text += f" The song should be about {topic}."

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_text,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

st.title("AI Filipino Song Lyricist")

genre_options = ["O.P.M. (Original Pilipino Music)", "Hugot", "Pinoy Rock", "Kundiman", "Hip-Hop"]
language_options = ["Filipino", "English", "Hiligaynon"]
genre = st.selectbox("Choose Genre", genre_options)
language = st.selectbox("Choose Language", language_options)
topic = st.text_input("Enter Song Topic (Optional)")

if st.button("Generate Lyrics"):
    lyrics = generate_lyrics(genre, language, topic)
    st.write(f"**{genre} Song Lyrics ({language})**\n {lyrics}")
