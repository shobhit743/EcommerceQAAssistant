import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()


os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"




model = ChatOpenAI(model="o3-mini")
result = model.invoke("Who are you?")
print(result.content)