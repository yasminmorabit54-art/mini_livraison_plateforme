from fastapi import FastAPI
from app.routes import router # Importation directe

app = FastAPI(title="Service Catalogue")

# Mettre l'inclusion juste ici
app.include_router(router)

@app.get("/health", tags=["monitoring"])
async def health():
    return {"status": "ok", "service": "catalogue"}