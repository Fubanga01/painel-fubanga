from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Diretórios de assets e templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Página principal com o formulário
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint para receber dados do formulário
@app.post("/criar_conta", response_class=JSONResponse)
async def criar_conta(request: Request):
    form = await request.form()
    nome = form.get("nome")
    email = form.get("email")
    telefone = form.get("telefone")

    print(f"[✔] Criando conta FAKE >>> Nome={nome} | Email={email} | Tel={telefone}")

    return JSONResponse(content={
        "status": "ok",
        "mensagem": f"Conta fake de {nome} criada com sucesso!"
    })
