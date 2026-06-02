import pytest
import requests
from tests.conftest import BASE_URL, logger


@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        ("own", 200),
        (2, 403),
        (5, 403),
        (99999, 404),
    ]
)
def test_user_authorization(auth_token, user_id, expected_status):

    headers = {
        "Authorization": f"Bearer {auth_token['token']}"
    }

    # replace "own" dynamically
    if user_id == "own":
        logger.info("Testing access to own user info")
        user_id = auth_token["user_id"]
    
    else:
        logger.info(f"Testing access to user info with ID: {user_id}")

    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        headers=headers
    )

    assert response.status_code == expected_status
