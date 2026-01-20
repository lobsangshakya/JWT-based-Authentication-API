from pydantic import BaseModel

class User(BaseModel):
    email: str
    full_name : str | None = None
    
class UserInDB(User):
    hashed_password : str
    
class Token(BaseModel):
    access_token: str
    token_type: str