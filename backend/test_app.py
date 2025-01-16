
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Mock data for tests
mock_user_profile = {
    "email": "test.user@example.com",
    "full_name": "Test User",
    "profile_picture": "https://example.com/avatar.jpg",
}

mock_file_upload = {
    "filename": "example.pdf",
    "content": b"Mock file content",
    "content_type": "application/pdf",
}

@pytest.fixture
def test_client():
    return TestClient(app)

# Test the root endpoint
def test_root_endpoint(test_client):
    response = test_client.get("/")
    assert response.status_code == 404  # No root route exists

# Test the profile endpoint
def test_profile_endpoint(test_client):
    response = test_client.get("/user/")
    assert response.status_code == 200
    assert response.json()["email"] == mock_user_profile["email"]

# Test file upload endpoint with a valid file
def test_file_upload_valid(test_client):
    response = test_client.post(
        "/files/upload",
        files={"file": (mock_file_upload["filename"], mock_file_upload["content"], mock_file_upload["content_type"])},
    )
    assert response.status_code == 200
    assert response.json()["message"] == "File uploaded successfully"

# Test file upload endpoint with an invalid file type
def test_file_upload_invalid_type(test_client):
    response = test_client.post(
        "/files/upload",
        files={"file": ("example.txt", b"Mock file content", "text/plain")},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid file type"

# Test file upload endpoint with a file exceeding size limit
def test_file_upload_large_file(test_client):
    large_file_content = b"0" * (1.5 * 1024 * 1024 + 1)  # 1.5 MB + 1 byte
    response = test_client.post(
        "/files/upload",
        files={"file": ("large_example.pdf", large_file_content, "application/pdf")},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "File size exceeds 1.5 MB"

# Test login route for Google OAuth
def test_google_login_redirect(test_client):
    response = test_client.get("/auth/login/google")
    assert response.status_code == 200 or response.status_code == 307
