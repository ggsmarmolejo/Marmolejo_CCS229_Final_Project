import streamlit as st
import openai
import random

# Replace 'your_api_key' with your actual OpenAI API key
openai.api_key = "sk-proj-MXI9JdTLpSquQdIkGT3OT3BlbkFJYHKWnWxaFg8D3QpRHjrx"


def generate_lyrics(genre, theme, language, additional_prompt=None):
  prompts = [
    f"Genre: {genre}\nTheme: {theme}",
    f"Language: {language}",
  ]
  if additional_prompt:
    prompts.append(additional_prompt)
  final_prompt = "\n".join(prompts)
  response = openai.Completion.create(engine="text-davinci-003", prompt=final_prompt, max_tokens=150, n=1, stop=None, temperature=0.7)
  lyrics = response.choices[0].text.strip()
  return lyrics


st.title("Versify: Unleash Your Inner Songwriter")

genre_options = ["Pop", "Rock", "Hip-Hop", "Country", "Electronic"]
genre = st.selectbox("Choose a Genre:", genre_options)

theme_prompts = {
  "Bayanihan Anthem":  "Modern Pop, Tagalog lyrics celebrating community spirit",
  "Fiesta Fever":     "Latin Pop, Tagalog & English lyrics describing a Filipino fiesta",
  "OFW Ballad":      "Acoustic Ballad, Tagalog

theme = st.selectbox("Pick a Theme:", theme_prompts[genre])

language_options = ["English", "Filipino", "Hiligaynon"]
language = st.selectbox("Choose Your Language:", language_options)

additional_prompt = st.text_input("Add an Optional Prompt (e.g., specific imagery, metaphors)", key="prompt")

if st.button("Generate Lyrics"):
  lyrics = generate_lyrics(genre, theme, language, additional_prompt)
  st.write("Your AI-Generated Lyrics:")
  st.write(lyrics)
