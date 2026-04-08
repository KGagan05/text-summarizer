from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from summarizer import summarize_text

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/summarize", response_class=HTMLResponse)
def summarize(request: Request, text: str = Form(...)):

    summary = summarize_text(text)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summary,
        "input_text": text
    })