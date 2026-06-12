from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_read():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"message": "API rodando!"}

def test_register_car():
    json = {
        "modelo": "VrumVrum",
        "ano": 2020,
        "fabricante": "fabricar",
        "usado": False
    }
    response = client.post("/cars/", json=json)

    assert response.status_code == 200
    data = response.json()
    assert data["modelo"] == "VrumVrum"
    assert data["ano"] == 2020
    assert data["fabricante"] == "fabricar"

def test_all_car():
    response = client.get("/cars/")

    assert response.status_code == 200
    assert type(response.json()) == list

def test_get_car_error():
    response = client.get("/cars/999")
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found!"

def test_patch_car():

    json = {
        "usado": True
    }

    response = client.patch("/cars/1", json=json)

    assert response.status_code == 200

def test_delete_car():
    json = {
        "modelo": "VrumVrum",
        "ano": 2020,
        "fabricante": "fabricar",
        "usado": False
    }

    response1 = client.post("/cars/", json=json)

    assert response1.status_code == 200

    id = response1.json()["id"]

    response2 = client.delete(f"/cars/{id}")

    assert response2.status_code == 200

    assert response2.json()["message"] == "Carro deletado com sucesso!"
