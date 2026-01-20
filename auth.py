from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 30

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

def verify_token(token:str):
    try:
        payload = jwd.decode(token, SECRET_KEY, algorithm = [ALGORITHM])
        return payload
    except JWTError:
        return None