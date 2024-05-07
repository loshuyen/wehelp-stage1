from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="ASDFGsdfasdfSFSDeee")

# @app.middleware("http")
# def add_session(request:Request, call_next):
#     response = call_next(request)
#     return response

@app.get("/")
def get_home(request:Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/signin")
def verify_user(request:Request, username: Annotated[str, Form()]=None, password: Annotated[str, Form()]=None):
    if not (username or password):
        return RedirectResponse("/error?message=請輸入帳號和密碼", status_code=302)
    if (username == "test" and password == "test"):
        request.session["SIGNED-IN"] = True
        return RedirectResponse("/member", status_code=302)
    return RedirectResponse("/error?message=帳號或密碼錯誤", status_code=302)

@app.get("/error")
def error_msg(request:Request, message):
    return templates.TemplateResponse(request=request, name="message.html", context={"message": message, "title": "失敗頁面"})

@app.get("/member")
def loggedIn(request:Request):
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        return templates.TemplateResponse(request=request, name="member.html")
    return RedirectResponse("/")

@app.get("/signout")
def sign_out(request:Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse("/")

@app.get("/square/{number}")
def square_number(request:Request, number:int):
    return templates.TemplateResponse(request=request, name="message.html", context={"message": number ** 2, "title": "正整數平方計算結果"})