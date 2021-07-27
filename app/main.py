from fastapi import FastAPI, Request
from app.core import config
from app.blueprint.api_v1.api import router as api_router
from mangum import Mangum

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse('home.html', {'request': request})
    # return {"message" : f"This is our secret_key : {config.settings.secret_key}"}


app.include_router(api_router, prefix=config.settings.prefix)
handler = Mangum(app)