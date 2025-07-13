import requests
import json

# Test health endpoint first
try:
    health_response = requests.get("http://localhost:8000/health")
    print(f"Health Status Code: {health_response.status_code}")
    print(f"Health Response: {health_response.text}")
except Exception as e:
    print(f"Health Error: {e}")

# Test root endpoint
try:
    root_response = requests.get("http://localhost:8000/")
    print(f"Root Status Code: {root_response.status_code}")
    print(f"Root Response: {root_response.text}")
except Exception as e:
    print(f"Root Error: {e}")

# Test auth test endpoint
try:
    auth_test_response = requests.get("http://localhost:8000/api/v1/auth/test")
    print(f"Auth Test Status Code: {auth_test_response.status_code}")
    print(f"Auth Test Response: {auth_test_response.text}")
except Exception as e:
    print(f"Auth Test Error: {e}")

# Test login endpoint
url = "http://localhost:8000/api/v1/auth/login"
data = {
    "username": "admin",
    "password": "admin123"
}

try:
    response = requests.post(url, data=data)
    print(f"Login Status Code: {response.status_code}")
    print(f"Login Response: {response.text}")
    if response.headers.get('content-type') == 'application/json':
        print(f"Login JSON: {response.json()}")
except Exception as e:
    print(f"Login Error: {e}")
