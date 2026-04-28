from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Produto

app = FastAPI(title="Sistema de Loja")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/produtos/cadastro")
def cadastrar_produto(request: Request):
    return templates.TemplateResponse("produtos/cadastro.html", {"request": request})

@app.post("/produtos")
def criar_produto(
    request: Request,
    nome: str = Form(...),
    preco: float = Form(...),
    estoque: int = Form(...),
    categoria_id: int = Form(...),
    db: Session = Depends(get_db)
):
    novo_produto = Produto(nome=nome, preco=preco, estoque=estoque, categoria_id=categoria_id)
    db.add(novo_produto)
    db.commit()
    return RedirectResponse(url="/produtos", status_code=303)

@app.get("/listar_produtos")
def listar_produtos(request: Request, db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    return templates.TemplateResponse("produtos/listar.html", {"request": request, "produtos": produtos})

@app.get("/produtos/{id}/deletar")
def deletar_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id_produto == id).first()
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/produtos", status_code=303)
