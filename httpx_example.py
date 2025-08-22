import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.text, response.status_code, response.json(), sep="\n")

data = {
    "userId": 1,
    "title": "Новая задача",
    "completed": False
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.text, response.status_code, response.json(), sep="\n")

data_multipart = {
    "username": "admin",
    "password": "123456787",
}

response = httpx.post("https://httpbin.org/post", data=data_multipart)
print(response.text, response.status_code, response.json(), sep="\n")

headers = {
    "Authorization": "Bearer my_secret_token",
}

response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.text, response.status_code, response.json(), sep="\n")


params = {
    "userId": 1,
}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.text, response.status_code, response.json(), sep="\n")


files = {
    "file": ("example.txt", open("example.txt", "rb"))
}

response = httpx.post("https://httpbin.org/post", files=files)

print(response.text, response.status_code, response.json(), sep="\n")

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
    print(response1.text, response2.text, sep="\n")


client = httpx.Client(headers=headers)
response = client.get("https://httpbin.org/get")
print(response.text, response.status_code, response.json(), sep="\n")

try:
    response1 = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    print(response1.text, response1.status_code, response1.json(), sep="\n")
    response1.raise_for_status()
except httpx.HTTPStatusError as e:
    print(e)


try:
    response1 = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout as e:
    print("Запрос превысил лимит времени")