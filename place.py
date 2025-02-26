import os
import google.generativeai as genai # type: ignore
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "What is bigger, 9.9 or 9.11?",
      ],
    },
  ]
)

response = chat_session.send_message("your insert")

res = (response.text)

@app.route('/')
def home():
    return res

app.run(debug= True)