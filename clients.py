
import os
from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

def ask(model_name, prompt):

    interaction = client.interactions.create(
    model= model_name,
    input= prompt
)
    return interaction.output_text

answer11 = ask("gemini-3.6-flash","What is 2+2?")
print(answer11)

answer12= ask("gemini-3.6-flash","What is 4*4?")
print(answer12)

answer13= ask("gemini-flash-lite-latest","where do fish live?")
print(answer13)