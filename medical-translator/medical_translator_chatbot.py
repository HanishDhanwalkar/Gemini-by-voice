import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the `.env` file

api_key = os.getenv("API_KEY") # replace with your API_KEY
genai.configure(api_key= api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# safety_settings = [
# #   {
# #     "category": "HARM_CATEGORY_HARASSMENT",
# #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# #   },
# #   {
# #     "category": "HARM_CATEGORY_HATE_SPEECH",
# #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# #   },
# #   {
# #     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
# #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# #   },
# #   {
# #     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
# #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# #   },
# ]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,)
                              # safety_settings=safety_settings)

convo = model.start_chat(history=[
])

doc_prompt = """
    You are a professional medical translator. There are patients who speak various languages. These patients also tend to mix these languages when speaking. You have to help medical staffs by translating such patients in Hindi

    You will:
    - Identify the language for each statement and translate it to Hindi
    - Keep medical terms similar in sound using the patient's language
    - Translate the rest of the conversation with correct semantics.
    
    DO NOT add anything else other than Hindi translations

    Example:
    - For a statement: "
    आज आप कैसा महसूस कर रहे हैं?
    ههل تتناولين أي أدوية لضغط الدم، مثل الباراسيتامول؟
    " 
    - You'll translate it to: "
    How are you feeling today?
    Do you take any medications for your blood pressure, such as paracetamol?
    "
    - The rest of the sentence has been properly translated to Hindi
    """

pat_prompt = """
    You are a professional medical translator for a patient who doesn't speak doctors' languages. These doctor also tend to mix these languages when speaking. You have to help medical staffs by translating such patients in English

    You will:
    - Identify the language for each statement and translate it to English
    - Keep medical terms similar in sound using the patient's language
    - Translate the rest of the conversation with correct semantics.
    
    DO NOT add anything else other than English translations

    Example:
    - For a statement: "
    आज आप कैसा महसूस कर रहे हैं?
    ههل تتناولين أي أدوية لضغط الدم، مثل الباراسيتامول؟
    " 
    - You'll translate it to: "
    How are you feeling today?
    Do you take any medications for your blood pressure, such as paracetamol?
    "
    - The rest of the sentence has been properly translated to English
"""


while True:
    convo.send_message(doc_prompt)
    msg = input("D: ")
    if msg == "exit" or msg == "quit":
        break
    
    convo.send_message(msg)
    print("D (translated): ", convo.last.text)

    convo.send_message(pat_prompt)
    msg = input("P: ")
    if msg == "exit" or msg == "quit":
        break
    
    convo.send_message(msg)
    print("P (translated): ", convo.last.text)
    # print(convo.history)





#  आप कैसे हैं?