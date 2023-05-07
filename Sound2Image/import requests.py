import requests

url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": "ed81fe4aba8e41f28536c55f1ecdb7b0",
    "client_secret": "cf68d5e7365b406f916c166400e743e6"
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access token:", access_token)
else:
    print("Error:", response.status_code, response.text)
