#Interfaces with chatgpt api to get response to question
from openai import OpenAI

with open("secretkey.txt", 'r') as file:
    secretkey = file.read()
    
client = OpenAI(api_key=secretkey)

def get_chatgpt_response(prompt):
    response = OpenAI.Completion.create(
        engine="gpt-3.5-turbo-16k",  # or the appropriate engine you want to use
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()