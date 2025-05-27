from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import string
import random

app = FastAPI()
url_map = {}

class URLItem(BaseModel):
    url: str

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.post("/shorten")
async def shorten_url(item: URLItem, request: Request):
    long_url = item.url
    short_id = generate_short_id()
    while short_id in url_map:
        short_id = generate_short_id()

    url_map[short_id] = long_url
    short_url = str(request.base_url) + short_id
    return {"short_url": short_url}

@app.get("/{short_id}")
async def redirect_to_long_url(short_id: str):
    long_url = url_map.get(short_id)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=long_url)
