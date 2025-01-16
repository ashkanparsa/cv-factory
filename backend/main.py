
from fastapi import FastAPI
from auth import router as auth_router
from profile import router as profile_router
from file_upload import router as file_upload_router

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Web App API"}

# Include routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(profile_router, prefix="/user", tags=["Profile"])
app.include_router(file_upload_router, prefix="/files", tags=["File Upload"])
