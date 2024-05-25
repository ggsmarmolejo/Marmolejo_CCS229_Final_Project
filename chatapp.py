import os
import openai
import streamlit as st

# Replace with your OpenAI API key
AsyncOpenAI(api_key=st.secrets["sk-proj-MVqgbWMTu0w84QRAK3hST3BlbkFJh8HvHgu3lpcQqY7VUBbE"]) 
openai.api_key = API_KEY

def generate_lyrics(genre, language, topic=None):
    """
    Generates song lyrics based on genre, language, and optionally a topic
    """
    prompt_text = f"I am an AI Song Lyricist. Write me a song in the {genre} genre in {language}."
    if topic:
        prompt_text += f" The song should be about {topic}."

    model = "gpt-3.5-turbo"
    response = client.chat.completions.create(
        prompt=prompt_text,
        model=model,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message.content

st.title("AI Filipino Song Lyricist")

genre_options = ["O.P.M. (Original Pilipino Music)", "Hugot", "Pinoy Rock", "Kundiman", "Hip-Hop"]
language_options = ["Filipino", "English", "Hiligaynon"]
genre = st.selectbox("Choose Genre", genre_options)
language = st.selectbox("Choose Language", language_options)
topic = st.text_input("Enter Song Topic (Optional)")

if st.button("Generate Lyrics"):
    lyrics = generate_lyrics(genre, language, topic)
    st.write(f"**{genre} Song Lyrics ({language})**\n {lyrics}")
