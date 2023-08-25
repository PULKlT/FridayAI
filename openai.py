import os
import openai
from config import apikey

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "you are a helpful assistant"
    },
    {
      "role": "user",
      "content": "hi friday"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)