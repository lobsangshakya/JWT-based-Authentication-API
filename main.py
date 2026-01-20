from fastapi import FastAPI, Depends, HTTPException, Form
from models import Token, User
from auth import create_access_token
from dependencies import get_current_user

app = FastAPI()

### DUMMY USER ###
FAKE_USERS_DB = {
    "test@example.com": {"full_name": "Lobsang Tsetan Shakya", "password": "Dummy@1"}
}

@app.post("/token", response_model=Token)
def login(email: str = Form(...), password: str = Form(...)):
    user = FAKE_USERS_DB.get(email)
    if not user or user["password"] != password:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = create_access_token(data={"sub": email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

@app.get("/")
def root():
    return {"message" : "JWT API is running successfully!"}