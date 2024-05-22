import streamlit as st
import openai

# Replace with your actual OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

async def generate_starter_description(starter):
  """Generates a creative description of the chosen starter Pokemon."""
  prompt_text = f"""Write a compelling description of a Pokemon trainer embarking on their journey in the Hoenn region, with their trusty {starter} by their side. Highlight the unique strengths and personality of the starter."""

  response = await openai.Completion.create(
      engine="text-davinci-003",  # Use a powerful language model
      prompt=prompt_text,
      max_tokens=150,  # Control description length
      n=1,
      stop=None,
      temperature=0.7  # Adjust for creativity vs. informativeness
  )

  return response.choices[0].text.strip()

async def generate_starter_recommendation():
  """Guides the user through prompts to recommend a Hoenn starter."""
  st.title("Hoenn Region Starter Recommendation")

  # Level 1 Prompt: Playstyle Preference
  playstyle_options = {
      "Balanced": "I enjoy using a variety of Pokemon types and strategies.",
      "Offensive": "I prefer to take down opponents quickly with powerful attacks.",
      "Defensive": "I value building a strong team that can withstand attacks.",
  }
  playstyle = st.selectbox("What kind of trainer are you?", list(playstyle_options.keys()))
  playstyle_description = playstyle_options[playstyle]

  # Level 2 Prompt: Specific Preferences (Optional)
  additional_prompts = st.checkbox("Do you have any preferences for specific types or looks?")
  if additional_prompts:
    type_preference = st.selectbox("Do you have a favorite type?", ["Grass", "Fire", "Water"])
    look_preference = st.text_input("Describe any visual preferences (color, appearance): (Optional)")
    additional_text = f"\nAdditionally, I tend to prefer {type_preference} type Pokemon, and ideally, my starter would look {look_preference} (if applicable)." if look_preference else f"\nAdditionally, I tend to prefer {type_preference} type Pokemon."
  else:
    additional_text = ""

  # Combine prompts and call GPT-3 for generation
  full_prompt = f"""Based on the information below, recommend a suitable starter Pokemon for a trainer in the Hoenn region:

  *Playstyle:* {playstyle_description}
  {additional_text}"""

  response = await openai.Completion.create(
      engine="text-davinci-003",
      prompt=full_prompt,
      max_tokens=150,
      n=1,
      stop=None,
      temperature=0.7
  )

  recommended_starter = response.choices[0].text.strip()

  # Generate starter description
  starter_description = await generate_starter_description(recommended_starter)

  return recommended_starter, starter_description

async def app():
  recommended_starter, starter_description = await generate_starter_recommendation()

  st.write(f"*Recommended Starter:* {recommended_starter.capitalize()}")
  st.image(f"images/{recommended_starter.lower()}.png", width=200)  # Add starter images
  st.write(starter_description)

  st.write("*Learn More About the Starters:*")
  st.text(
      """
      - Treecko (Grass): A quick and agile Pokemon that evolves into a powerful Grass/Ground type.
      - Torchic (Fire): A spirited and energetic Pokemon that evolves into a blazing Fire/Fighting type.
      - Mudkip (Water): A laid-back and easygoing Pokemon that evolves into a strong Water/Ground type.
      """
  )

# Run the app
if _name_ == "_main_":
  import asyncio
  asyncio.run(app())
