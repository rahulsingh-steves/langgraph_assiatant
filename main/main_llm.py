from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


MODEL_NAME = os.getenv("MODEL_NAME")

client = Groq()

def llm_intake(prompt:str):
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
          {
                "role": "user",
                "content": prompt
            }
        ],
)

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")