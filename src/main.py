# coding: utf-8
"""Web server module."""

from fastapi import FastAPI, status, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.config import get_configs

class Signal(BaseModel):
    """Class representing incoming http signal."""

    client_host: str
    client_IP: str
    user_agent: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def homepage():
    return {"message": "Welcome to Protector API"}


@app.post("/check_incomming_http_traffic", status_code=status.HTTP_201_CREATED)
async def check_http_traffic(request:Request, signals: Signal):
    """."""
    settings = get_configs()
    try:
        settings.get('origin_allow', request.headers.get('X-Origin'))
   
    except AttributeError as _:
        raise HTTPException(503, detail="Incoming came from unknow host")

    incomming_http_signals = signals.model_dump()
    
    if 'bot' in incomming_http_signals['user_agent'] or incomming_http_signals['client_host']=='http://blacklist.host':
        raise HTTPException(403, detail="Bot Detected")


    return {"status": "Granted"}