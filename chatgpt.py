#Interfaces with chatgpt api to get response to question

from openai import OpenAI

with open("secretkey.txt", 'r') as file:
    secretkey = file.read()

client = OpenAI(api_key=secretkey)

def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{"role":"system", "content": "answer the question"},
                    {"role":"user", "content": prompt}
          ],
          temperature=0.7,
          max_tokens=150,
          top_p=1
    )
    
    print(response.choices[0].message.content)
    return response.choices[0].message.content
