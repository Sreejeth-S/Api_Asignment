import pytest
from utils import config
from utils.api_client import APIClient
from utils.config import Auth, order_id
from utils.test_data import NEW_ORDER, UPDATE_ORDER


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


# Generating the authtoken and passing the token to all the below functions
@pytest.fixture(scope="module")
def auth_token(api_client):
    response = api_client.post("/api-clients/", data=Auth)
    assert response.status_code == 201
    return response.json()["accessToken"]


# Verifying the authtoken is present or not
def test_get_auth(auth_token):
    assert auth_token is not None


# Sumbitting an order
# Passed authtoken & NEW_ORDER(JSON taken from test_data.py) in headers
def test_submit_order(api_client, auth_token):
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    response = api_client.post("/orders", data=NEW_ORDER, headers=headers)
    orderId = response.json()["orderId"]
    config.order_id = orderId  # Storing the order_id in config.py to reuse in below functions
    print(f"Order id after submission: {config.order_id}")  # Verifying whether the order_id is getting stored or not

    assert response.json()["created"] == bool("True")
    assert response.status_code == 201  # 201 Created


# Updating the order
# Passed authtoken & UPDATE_ORDER(JSON taken from test_data.py) in headers
# Passed the order_id which is stored in config.py
def test_update_order(api_client, auth_token):
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    print(config.order_id)  # Checking whether the order_id is getting pulled from config or not
    response = api_client.patch(f"/orders/{config.order_id}", data=UPDATE_ORDER, headers=headers)

    assert response.status_code == 204  # 204 No Content


# Getting the order
# Passed authtoken & order_id from config.py
def test_get_an_order(api_client, auth_token):
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    response = api_client.get(f"/orders/{config.order_id}", headers=headers)
    print(response.json())
    updated_name = UPDATE_ORDER.get('customerName')  # Fetching the updated name from test_data.py -> UPDATE_ORDER

    assert response.status_code == 200
    assert response.json()["customerName"] == updated_name  # Verifying the updated name


# Deleting the order
def test_delete_an_order(api_client, auth_token):
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    response = api_client.delete(f"/orders/{config.order_id}", headers=headers)

    assert response.status_code == 204  # 204 No Content
