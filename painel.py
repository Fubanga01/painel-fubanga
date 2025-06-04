from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Monta pasta de arquivos estáticos (CSS, imagens, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define diretório de templates (HTML)
templates = Jinja2Templates(directory="templates")

# Rota GET: Carrega formulário
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota POST: Recebe dados do formulário
@app.post("/criar_conta")
async def criar_conta(
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...)
):
    print(f"🔧 Criando conta FAKE >>> Nome={nome} | Email={email} | Tel={telefone}")
    return JSONResponse(
        content={"status": "ok", "mensagem": f"Conta {nome} criada com sucesso!"}
    )
