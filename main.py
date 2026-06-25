import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import InferenceClient

load_dotenv()

client=InferenceClient(api_key=os.environ.get('HF_TOKEN'))

class MessageStructure(BaseModel):
    role:str
    content:str

app = FastAPI()

@app.post("/prompt/")
async def create_message(message:MessageStructure):
    
    promt = [
        {
            "role":message.role,
            "content":message.content
        }
    ]

    request = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=promt,
        max_tokens=500
    )

    return {'asnwer':request.choices[0].message.content}
