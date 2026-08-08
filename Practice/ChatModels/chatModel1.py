from langchain_openai import ChatOpenAI
from dotenv   import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4', temperature = 0.7, max_tokens = 1000)

result = model.invoke("Write a short poem about the beauty of nature.")

print(result)