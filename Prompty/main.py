import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the `.env` file 

api_key = os.getenv("API_KEY") # replace with your API_KEY
genai.configure(api_key= api_key)

# Set up the model
generation_config = {
  "temperature": 0.1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro",)
                              # generation_config=generation_config,)
                              # safety_settings=safety_settings)

convo = model.start_chat(history=[
])

print("TEXT 2 PROMPT")
while True:

    model = input("The generative model for which prompt is used: ")
    
    msg = input("Enter the text here: ")
    if msg == "q":
        break
    
    prompt = f"""You are a prompt generator machine whose sole job is to generate prompts for various models like stable diffusion, Dalle2, text to voice, SOra (the text to video generation) and any other LLM AI generative models.

    You will:
    Take the raw text as input and output the appropriate prompt for the generative models mentioned in the raw text as first word of the raw text.
    Output only the prompt and not explantions nor any other thongs that are not part of the prompt. Your job is to make the prompt more useful for the generative model by adding appropriate words which may help the model to generate better images.

    For example:
    raw text will be : Stable Diffusion, Generate an image of a dog underwater.
    you will return : A photorealistic image of a dog swimming underwater, sunlight filtering through the clear blue water, bubbles rising around the dog's happy face, detailed fur with water droplets clinging to it.

    You will make prompt for: {model}
    Your raw text is: {msg}
    """

    
    convo.send_message(prompt + msg)
    print("bot: ", convo.last.text)


