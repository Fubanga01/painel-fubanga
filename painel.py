from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/criar_conta")
async def criar_conta(request: Request):
    form = await request.form()
    nome = form.get("nome")
    email = form.get("email")
    telefone = form.get("telefone")

    print(f"Criando conta: Nome={nome}, Email={email}, Telefone={telefone}")

    return JSONResponse(content={"status": "ok", "mensagem": f"Conta {nome} criada com sucesso!"})