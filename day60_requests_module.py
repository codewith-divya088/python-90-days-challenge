# Day 60 - Requests Module in Python

import requests

# sending GET request
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# checking status code
print("Status Code:", response.status_code)

# converting response to JSON
data = response.json()

print("\nUser Details:")
print("Name:", data["name"])
print("Email:", data["email"])
print("City:", data["address"]["city"])
