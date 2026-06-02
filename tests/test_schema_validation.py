import requests
from jsonschema import validate
from tests.conftest import BASE_URL, logger

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["id", "email"]
}

def test_user_response_schema(auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token['token']}"
    }
    logger.info(f"Fetching user with ID: '{auth_token['user_id']}' to validate response schema")
    response = requests.get(
        f"{BASE_URL}/users/{auth_token['user_id']}",
        headers=headers
    )

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")
    
    assert response.status_code == 200
    validate(instance=response.json(), schema=user_schema)

