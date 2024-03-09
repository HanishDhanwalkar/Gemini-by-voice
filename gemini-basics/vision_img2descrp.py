import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the `.env` file 

api_key = os.getenv("API_KEY") # replace with your API_KEY
genai.configure(api_key= api_key)

model = genai.GenerativeModel('gemini-pro-vision')
prompt = """
Describe the given picture first based on what you see.
Then create a short story based on your understanding of the picture.

Output should have both the description and the short story as two separate items 
with relevant headings
"""

import PIL.Image

img = PIL.Image.open('gemini-basics\data\imgs\cat_pc.jpeg')

response = model.generate_content(contents=[prompt, img])

# print(response)

print(response.text)