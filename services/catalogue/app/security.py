import os
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2 = OAuth2PasswordBearer(tokenUrl="token")
SECRET = os.environ.get("JWT_SECRET", "changez-moi-en-seance-8")


def utilisateur_courant(token: str = Depends(oauth2)) -> dict:
    # TODO (TP8) : décoder le jeton avec jwt.decode(token, SECRET, algorithms=["HS256"])
    # et renvoyer le payload ; lever HTTPException(401) si le jeton est expiré ou invalide.
    _ = (jwt, SECRET, token)  # Utilisé fictivement pour éviter le warning d'import inutilisé
    raise HTTPException(status_code=501, detail="À implémenter au TP8")


def exiger_role(role: str):
    # TODO (TP8) : renvoyer une dépendance qui vérifie user["role"] et lève 403 sinon.
    def _verifier(user: Annotated[dict, Depends(utilisateur_courant)]) -> dict:
        _ = (role, user)
        raise HTTPException(status_code=501, detail="À implémenter au TP8")

    return _verifier