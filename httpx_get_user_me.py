import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status code:", login_response.status_code)

get_me_headers = {
    "Authorization": f'Bearer {login_response_data["token"]["accessToken"]}',
}

get_me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=get_me_headers)
get_me_response_data = get_me_response.json()

print("Get me response:", get_me_response_data)
print("Status code:", get_me_response.status_code)
