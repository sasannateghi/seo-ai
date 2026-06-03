from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import analyze_site

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/analyze")
def analyze(request: URLRequest):
    return analyze_site(request.url)
