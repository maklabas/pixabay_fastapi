from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

from services import connect_pixabay

app = FastAPI()

templates = Jinja2Templates(directory="I:\\pixabay\\templates")


@app.get("/", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/result")
def read_item(request: Request):
    category = request.query_params.get("category")
    comments = request.query_params.get("comments")
    likes = request.query_params.get("likes")
    per_page = request.query_params.get("per_page")
    hits = connect_pixabay(per_page, category)["hits"]
    response = []
    for hit in hits:
        if hit.get("likes") > int(likes) and hit.get("comments") > int(comments):
            response.append(hit)
    return templates.TemplateResponse("result.html", {"request": request, "hits": response, "category": category})
