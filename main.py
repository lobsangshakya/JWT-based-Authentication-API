from fastapi import FastAPI, Depends, HTTPException
from models import LoginRequest, TokenResponse, User
from auth import create_access_token
from dependencies import get_current_user

app = FastAPI()

#### DUMMY USER ###
FAKE_USER = {
    "email" : "dummy@example.com",
    "password" : "Admin@123"
}

@app.post("/login", response_model = TokenResponse)
def login(data: LoginRequest):
    if data.email != FAKE_USER["email"] or data.password != FAKE_USER['password']:
        raise HTTPException(status_code = 401, detail = "INVALID CREDENTIALS")
    token = create_access_token({'email': data.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
def protested_route(current_user: User = Depends(get_current_user)):
    return {
        "message" : "Access granted",
        "user" : current_user.email
    }