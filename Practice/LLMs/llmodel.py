from langchain_openai import OpenAI
from dotenv   import load_dotenv
# dot env is used to store the configurations settings and secrets from the env file
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.9)
# object ban gya

result = llm.invoke("What is the capital of France?")   
#invoke method communicate krta h particular model k sath and return krta h response

print(result)