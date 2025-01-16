from fastapi import APIRouter, Request
from authlib.integrations.starlette_client import OAuth

router = APIRouter()

oauth = OAuth()
oauth.register(
    name="google",
    client_id="YOUR_GOOGLE_CLIENT_ID",
    client_secret="YOUR_GOOGLE_CLIENT_SECRET",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    client_kwargs={"scope": "openid email profile"},
)

@router.get("/login/google")
async def google_login(request: Request):
    redirect_uri = request.url_for("google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/login/google/callback")
async def google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)
    return {"user_info": user_info}