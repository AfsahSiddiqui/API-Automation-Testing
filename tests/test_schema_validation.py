import requests
from jsonschema import validate
import logging

BASE_URL = "http://127.0.0.1:8000"
logger = logging.getLogger(__name__)

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["id", "email"]
}

def test_user_response_schema():
    logger.info("Fetching user with ID: 1")
    response = requests.get(f"{BASE_URL}/users/1")

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")
    
    assert response.status_code == 200
    validate(instance=response.json(), schema=user_schema)
