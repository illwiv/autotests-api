import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string",
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload, )
login_response_data = login_response.json()

print("Login response:", login_response_data)

auth_user_headers = {
    "Authorization": f'Bearer {login_response_data["token"]["accessToken"]}',
}

client = httpx.Client(base_url="http://127.0.0.1:8000", timeout=2, headers=auth_user_headers)

get_user_me_response = client.get("/api/v1/users/me")
get_user_me_data = get_user_me_response.json()

print('Get user me data:', get_user_me_data)
