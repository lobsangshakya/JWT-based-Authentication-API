from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth import verify_token
from models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token:str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException (
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid or expired soon"
        )
    return User(email = payload.get("email"))
