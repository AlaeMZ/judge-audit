
import os
from dotenv import load_dotenv
import hashlib
from pathlib import Path 
load_dotenv()
import json

from google import genai

client = genai.Client()

def ask(model_name, prompt):

    interaction = client.interactions.create(
    model= model_name,
    input= prompt
)
    return interaction.output_text



def cached_ask(model_name, prompt):
    model_prompt=(f"{model_name}|{prompt}").encode()

    s=hashlib.sha256(model_prompt).hexdigest()
    folder_path = Path("data/cache")
    folder_path.mkdir(parents=True, exist_ok=True)

    file_path = folder_path / f"{s}.txt"


    if file_path.exists():
        with open(file_path,"r") as f:
            saved = f.read()
        print("cache hit")
        return saved

    print("Calling API")
    answer = ask(model_name, prompt)
    with open(file_path,"w") as f:
        f.write(answer)
    print("Calling API ...")
    return answer



    
