from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Using a highly reliable supported model
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3", 
    task="text-generation",
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("Write a very short poem on Mahatma Gandhi.")
print(result.content)
# the code is not working