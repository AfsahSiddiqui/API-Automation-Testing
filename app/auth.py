from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException

SECRET_KEY = "secretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(email: str):
    return jwt.encode({"sub": email}, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
