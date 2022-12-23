import openai
import os
from dotenv import load_dotenv

class Question:
  def __init__(self, prompt, model="text-davinci-003", max_tokens=256, temperature=0.5):
    self.prompt = prompt
    self.model = model
    self.max_tokens = max_tokens
    self.temperature = temperature

  def get_answer(self):
    load_dotenv()
    openai.organization = os.getenv("ORG_KEY")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    answer = openai.Completion.create(
      model=self.model,
      prompt=self.prompt,
      max_tokens=self.max_tokens,
      temperature=self.temperature,
    )

    for i in answer['choices']:
      return i['text']

q = Question('write python code that will loop through a list')
a = q.get_answer()
print(a)
    
