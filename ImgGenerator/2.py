import google.generativeai as genai
import PIL.Image

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the `.env` file 

api_key = os.getenv("API_KEY") # replace with your API_KEY
genai.configure(api_key= api_key)

model = genai.GenerativeModel('models/gemini-pro')
result = model.generate_content('Tell me a story about a magic backpack')

print(result.text)
