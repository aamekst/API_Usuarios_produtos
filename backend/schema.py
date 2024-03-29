from pydantic import BaseModel

class ProdutosSchema(BaseModel):
    id: int
    item: str
    peso: float
    numero_caixas: int

class UsuariosSchema(BaseModel):
    id: int
    usuario: str
    password: str
    email: str
    name: str

