import requests

BASE_URL = "https://reqres.in"

def test_get_user_list():
    response = requests.get(f"{BASE_URL}/api/users?page=2")
    assert response.status_code == 200
    assert len(response.json()['data']) > 0

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/api/users/2")
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2

def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/api/users/23")
    assert response.status_code == 404

def test_create_user():
    payload = {
        "name": "Mukul",
        "job": "QA Engineer"
    }
    response = requests.post(f"{BASE_URL}/api/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Mukul"

def test_update_user():
    payload = {
        "name": "Mukul Updated",
        "job": "Lead QA"
    }
    response = requests.put(f"{BASE_URL}/api/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "Lead QA"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/api/users/2")
    assert response.status_code == 204
