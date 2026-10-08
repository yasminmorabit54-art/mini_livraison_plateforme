from pydantic import BaseModel, Field


class ProduitCreate(BaseModel):
    nom: str = Field(min_length=1, max_length=100)
    prix: float = Field(gt=0, description="Prix en dirhams, strictement positif")
    stock: int = Field(ge=0, default=0)

class ProduitRead(ProduitCreate):
    id: int