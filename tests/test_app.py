from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_account():
    response = client.post(
        "/accounts/",
        json={"name": "Conta Pessoal", "type": "personal", "balance": 100},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Conta Pessoal"
    assert data["type"] == "personal"
    assert data["balance"] == 100


def test_create_category():
    response = client.post(
        "/categories/",
        json={"name": "Aluguel", "type": "expense"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Aluguel"
    assert data["type"] == "expense"


def test_create_transaction():
    # ensure account and category exist
    client.post(
        "/accounts/",
        json={"name": "Conta Empresa", "type": "company", "balance": 0},
    )
    client.post(
        "/categories/",
        json={"name": "Venda", "type": "income"},
    )
    response = client.post(
        "/transactions/",
        json={
            "amount": 500,
            "description": "Venda de produto",
            "category_id": 2,
            "account_origin_id": 2,
            "account_dest_id": None,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 500
    assert data["description"] == "Venda de produto"
