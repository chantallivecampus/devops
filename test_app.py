import pytest
from app import app

# Créer un client de test
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test de la route principale "/"
def test_home(client):
    response = client.get("/")
    assert response.data == b"Hello, Docker!"
    assert response.status_code == 200

# Test de l'addition
def test_addition(client):
    response = client.get("/add/3/4")
    assert response.data == b"7"
    assert response.status_code == 200

# Test de la soustraction
def test_subtraction(client):
    response = client.get("/subtract/10/4")
    assert response.data == b"6"
    assert response.status_code == 200

# Test de la multiplication
def test_multiplication(client):
    response = client.get("/multiply/3/5")
    assert response.data == b"15"
    assert response.status_code == 200

def test_division(client):
    response = client.get("/divide/10/2")
    assert response.data == b"5.0"
    assert response.status_code == 200


# Test de la division par zéro
def test_division_by_zero(client):
    response = client.get("/divide/10/0")
    assert response.data == b"Cannot divide by zero"
    assert response.status_code == 400

