import os
import httpx
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi import FastAPI, WebSocket, Request, Form
from starlette import status
from app_gpt import chatgpt

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    """
    Страница ввода Ключа
    """
    return FileResponse("templates/get_key.html")


@app.post("/postdata")
def postdata(api_token=Form()):
    """
    Сохранение ключа в переменные виртуального окружения
    :param api_token: Ключ.
    :return: перенаправление на страницу чата с GPT
    """

    # Сохраняем введенное значение API_TOKEN в переменную окружения
    os.environ['OPENAI_API_KEY'] = api_token
    return RedirectResponse('/message', status_code=status.HTTP_302_FOUND)


@app.get("/message", response_class=HTMLResponse)
def read_index(request: Request):
    """
    Страница чата
    """
    # Render the HTML template
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Сокет для обработки сообщения, он подключается в форме шаблона через JS.
    Отправляет сообщение пользователя в подключенную модель.
    Возвращает сообщение от модели
    """

    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        text = chatgpt(data)
        await websocket.send_text(text)



