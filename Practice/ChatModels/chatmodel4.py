from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Hum directly Text-Generation API use karenge (jo free mein chalti hai)
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3", 
    task="text-generation",
    max_new_tokens=100
)

# ChatHuggingFace ko hata diya gaya hai.
# Seedha llm.invoke() use karke prompt pass karenge:
result = llm.invoke("Write a very short poem on Mahatma Gandhi.")
print(result)
