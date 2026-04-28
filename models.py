from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(100), nullable=False)

    produtos = relationship("Produto", back_populates="categorias")

    def __repr__(self):
        return f"Categoria = ID: {self.id_categoria} | Nome: {self.nome} | Descrição: {self.descricao}"


class Produto(Base):
    __tablename__ = "produtos"
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id_categoria"))

    categorias = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Produto = ID: {self.id_produto} | Nome: {self.nome} | Preço: {self.preco} | Estoque: {self.estoque} ID Categoria: {self.categoria_id}"