from fastapi import FastAPI, Request
from pydantic import BaseModel
from gamechatbot.chatbox import chatty, A2chatty
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define a Pydantic model for the expected request body
class ChatRequest(BaseModel):
    querry: str

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"]  # Allow all headers
)
@app.post("/api/chatbotResponse")
async def get_response(request: ChatRequest):
    zendesk = False
    response = chatty(request.querry)
    try:
        if "[True]" in response:
            zendesk = True
            response = response.replace("[True]", "")
    except:
        pass
    response2 = A2chatty(response)
    print(response)
    # if response == None:
    #     return {"response":"ok"}
    return {"message": response, "option": response2,"zendesk":zendesk}

@app.post("/api/A2")
async def get_response_a2(request: ChatRequest):
    response = A2chatty(request.querry)
    return {"message": response}

