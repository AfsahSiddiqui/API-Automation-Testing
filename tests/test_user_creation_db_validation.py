import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User
from app.auth import verify_password
from tests.conftest import BASE_URL, logger


engine = create_engine("sqlite:///./test.db")
Session = sessionmaker(bind=engine)

def test_create_user_and_validate_db(random_user):

    payload = random_user
    
    logger.info("Sending request to create user")
    response = requests.post(
        f"{BASE_URL}/users",
        json=payload
    )

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")

    assert response.status_code == 200
    assert response.json()["email"] == payload["email"]

    db = Session()

    logger.info("Querying the database to verify user creation")
    user = db.query(User).filter(User.email == payload["email"]).first()

    assert user is not None
    assert user.email == payload["email"]
    assert verify_password(payload["password"], user.hashed_password)

    logger.info("Verification completed")

    db.close()
