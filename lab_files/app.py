import os
from dotenv import load_dotenv

from utilities import get_cryptids

from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from mssql_python import connect
from datetime import datetime

import chainlit as cl

load_dotenv()

@cl.on_chat_start
async def start():
    # Display header
    header = """
# CRYPTOZOOLOGY RESEARCH TERMINAL
*Documenting the Undocumented • Est. 1973*
    """
    await cl.Message(content=header).send()
    
    # Welcome message
    welcome = """
Welcome to the Cryptozoology Research Terminal.

This system provides access to our research database, field observations, and specimen analysis tools.

How may I assist with your research today?
    """
    await cl.Message(content=welcome).send()

    openai = AzureChatOpenAI(
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        streaming=True
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "ai",
                """ 
                You are a leading cryptozoologist here to help answer questions about cryptids. Your goal is to help users identify and learn about different
                cryptids based on the data provided. Use the returned data to provide detailed information, including descriptions, habitats, sightings,
                and any other relevant details found in the returned data. Ensure your responses are informative and engaging. Remember, you are only able to use the 
                data returned to you and cannot derive answers from other information. If the information provided to you does not yield a good match, please tell the
                user that and to try another question.
                """,
            ),
            (
                "human",
                """
                Please use the following cryptids for your answer and only these cryptids: 
                {cryptids}               
                """
            ),
            (
                "human",                
                "{question}"
            ),
        ]
    )

    # Use an agent retriever to get similar sessions
    retriever = RunnableLambda(get_cryptids, name="GetCryptids").bind() 

    runnable = {"cryptids": retriever, "question": RunnablePassthrough()} | prompt | openai | StrOutputParser()
    cl.user_session.set("runnable", runnable)

@cl.on_message  
async def on_message(message: cl.Message):

    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    runnable = cl.user_session.get("runnable")  # type: Runnable
    cb = cl.LangchainCallbackHandler()
    cb._schema_format = "original+chat"

    response_message = cl.Message(content="")
    thinking_msg = cl.Message(content="Analyzing cryptozoological database...")
    await thinking_msg.send()

    for chunk in await cl.make_async(runnable.stream)(
        input=message.content,
        #config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await response_message.stream_token(chunk)
    


    await response_message.send()
