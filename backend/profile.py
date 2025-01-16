
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserProfile(BaseModel):
    email: str
    full_name: str
    profile_picture: str

router = APIRouter()

@router.get("/")
async def get_profile(token: str = Depends(oauth2_scheme)):
    # Dummy profile data for now
    user_data = {"email": "user@example.com", "full_name": "John Doe", "profile_picture": "https://example.com/avatar.jpg"}
    return user_data
        