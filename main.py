from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser as Str
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from typing import List
from fastapi import FastAPI
import os

load_dotenv()


system_template = "translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages([
    
    ("system", system_template),
     ("user", "{text}")
    
])

model = ChatOpenAI(model = "gpt-4", temperature=0.1)

parser = Str()

chain = prompt_template| model | parser

app = FastAPI(
    title =" Translation App",
    version = "1.0",
    description = "A simple API server using Langchain's Runnable interface"
)

add_routes(app, chain, path= "/translate")

if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run(app, host="localhost", port=8050)