from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# llm = ChatGroq(
#     groq_api_key= os.environ["GROQ_API_KEY"],
#     model="gemma2-9b-it",  # Can be replace with our preferred model
#     temperature=0.3
# )

llm = ChatOpenAI(
    api_key = os.environ['OPEN_AI_KEY'],

    model = 'gpt-4.1-2025-04-14',

    temperature = 0

)