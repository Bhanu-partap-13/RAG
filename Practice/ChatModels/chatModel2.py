from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-3-opus-20241218', temperature = 0.7, max_tokens = 1000)

result = model.invoke("Write a short poem about the beauty of nature.")

print(result.content)
