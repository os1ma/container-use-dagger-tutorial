from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def hello_world():
    return '<h1>Hello World from FastAPI!</h1>'