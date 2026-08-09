from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenAI(model = 'gemini-2.5-flash', temperature = 0.7, max_output_tokens = 1000)

result = model.invoke("Write a short poem about the beauty of nature.")

print(result.content) # content prints the raw bytes
