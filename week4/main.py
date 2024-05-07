from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="QWERFGhsfdghe5rtgerteRT")

templates = Jinja2Templates(directory="templates")

@app.middleware("http")
async def handle_session(request: Request, call_next):
    response = await call_next(request)
    return response
@app.get("/")
def get_home (request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html"
    )
@app.get("/square/{number}")
def calc_square (request: Request, number: int):
    result = number ** 2
    return templates.TemplateResponse(request=request, name="square.html", context={"result":result})
@app.get("/member")
def get_member (request: Request):
    try:
        if not request.session['SIGNED-IN']:
            return RedirectResponse("/")
    except:
        return RedirectResponse("/")
    return templates.TemplateResponse(
        request=request, name="member.html"
    )
@app.get("/error")
def get_failure (request: Request, message):
    return templates.TemplateResponse(
        request=request, name="failure.html", context={"message": message}
    )
@app.post("/signin")
def sign_in (request: Request, username: Annotated[str, Form()] = None, password: Annotated[str, Form()] = None):
    if not (username or password):
        return RedirectResponse("/error?message=請輸入帳號、密碼", status_code = 302)
    if username == "test" and password == "test":
        request.session['SIGNED-IN'] = True
        return RedirectResponse("/member", status_code = 302)
    return RedirectResponse("/error?message=帳號、或密碼輸入錯誤", status_code = 302)
@app.get("/signout")
def sign_out(request: Request):
    request.session['SIGNED-IN'] = False
    return RedirectResponse("/")