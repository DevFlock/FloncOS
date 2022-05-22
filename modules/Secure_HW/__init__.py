from ..Security import Secure
from fastapi import APIRouter, Security

app = APIRouter()

@app.get("/sec")
async def root(api_key: str = Security(Secure(["123"]))):
    return {"Hello": "world", "api_key": api_key}

def setup():
    return app