from app.routes import _db


def test_lister_produits(client):
    _db.clear()

    response = client.get("/produits")

    assert response.status_code == 200
    assert response.json() == []


def test_creer_produit(client):
    _db.clear()

    response = client.post(
        "/produits",
        json={
            "nom": "Laptop",
            "prix": 5000,
            "stock": 10,
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["nom"] == "Laptop"
    assert data["prix"] == 5000
    assert data["stock"] == 10
    assert "id" in data


def test_consulter_produit(client):
    _db.clear()

    create_response = client.post(
        "/produits",
        json={
            "nom": "Laptop",
            "prix": 5000,
            "stock": 10,
        },
    )

    produit_id = create_response.json()["id"]

    response = client.get(f"/produits/{produit_id}")

    assert response.status_code == 200
    assert response.json()["id"] == produit_id


def test_consulter_produit_inexistant(client):
    _db.clear()

    response = client.get("/produits/9999")

    assert response.status_code == 404


def test_modifier_produit(client):
    _db.clear()

    create_response = client.post(
        "/produits",
        json={
            "nom": "Laptop",
            "prix": 5000,
            "stock": 10,
        },
    )

    produit_id = create_response.json()["id"]

    response = client.put(
        f"/produits/{produit_id}",
        json={
            "nom": "Laptop Pro",
            "prix": 7000,
            "stock": 5,
        },
    )

    assert response.status_code == 200
    assert response.json()["id"] == produit_id
    assert response.json()["nom"] == "Laptop Pro"


def test_supprimer_produit(client):
    _db.clear()

    create_response = client.post(
        "/produits",
        json={
            "nom": "Laptop",
            "prix": 5000,
            "stock": 10,
        },
    )

    produit_id = create_response.json()["id"]

    response = client.delete(f"/produits/{produit_id}")

    assert response.status_code == 204

    response = client.get(f"/produits/{produit_id}")

    assert response.status_code == 404


def test_validation_prix_invalide(client):
    _db.clear()

    response = client.post(
        "/produits",
        json={
            "nom": "Laptop",
            "prix": 0,
            "stock": 10,
        },
    )

    assert response.status_code == 422