import os
from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

def ask_llm(question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI FAQ assistant. Give short, clear answers."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content