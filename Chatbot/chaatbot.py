import google.generativeai as genai
import PIL.Image

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the `.env` file 

api_key = os.getenv("API_KEY") # replace with your API_KEY
genai.configure(api_key= api_key)

model = genai.GenerativeModel('models/gemini-pro')
chat = model.start_chat()

messages = [{'role':'user', 'parts': ['hello']}]
response = model.generate_content(messages) # "Hello, how can I help"
messages.append(response.candidates[0].content)
messages.append({'role':'user', 'parts': ['How does quantum physics work?']})
response = model.generate_content(messages)

print(response.text)