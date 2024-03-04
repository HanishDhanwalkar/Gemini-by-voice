# rewinding a request/response pair OR regenerating 
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  
api_key = os.getenv("API_KEY") # replace with your API_KEY
genai.configure(api_key= api_key)

# Set up the model
generation_config = {
  "temperature": 0.1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,)
                              # safety_settings=safety_settings)
convo = model.start_chat(history=[])

while True:
    
    msg = input("You: ")
    if msg == "q":
        break

    if msg == "regenerate":
        convo.rewind()

    os.system('cls')
    print(f"You: {msg}")
    
    convo.send_message(msg)
    print("bot: ", convo.last.text)

    
    

    # print(convo.history)

