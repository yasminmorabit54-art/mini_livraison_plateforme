from fastapi import FastAPI

from app.routes import router  # Importation directe

app = FastAPI(title="Service Catalogue")

app.include_router(router)