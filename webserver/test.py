import requests

data = {
    "room_number": 101,
    "current_occupancy": 5
}
response = requests.post("http://localhost:8000/data", json=data)
print(response.json())