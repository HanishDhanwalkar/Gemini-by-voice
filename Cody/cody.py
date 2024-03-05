import google.generativeai as genai
import os
from dotenv import load_dotenv

import multiprocessing
# import subprocess

from run_output import ChildRunner

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

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
								generation_config=generation_config,)
								# safety_settings=safety_settings)

convo = model.start_chat(history=[
])


if __name__ == '__main__':
		prompt = """
		You are a professional coder, well equipped with all the tools and programming languages. You follow all the coding practises and always come up with an optimised code both time and memory optimised. Just give code and nothing else, No explaination. Now give me code for: \n
		"""
		
		while True:
			msg = input("You: ")
			# msg = "write a hello world program in python"

			if msg == "q":
					break
			
			convo.send_message(prompt + msg)
			response = convo.last.text
			# print("bot:\n ", response)
			
			res= response.split("\n")
			res = res[1:-1]
			response = "\n".join(res)

			outputfile = "Cody\out.py"

			with open(outputfile, "w") as file:
					file.write(response)

			run_code = input("Do you want to run the code: (y/N) ")

			if (run_code.lower() == "y"):				
				os.system(f"""python -u {outputfile} """)
			
			elif (run_code.lower() == "n"):
					break
			else:
					print("invalid response")


		

		


