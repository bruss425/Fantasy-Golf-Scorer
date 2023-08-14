import requests

url = "https://golf-leaderboard-data.p.rapidapi.com/fixtures/2/2023"

headers = {
	"X-RapidAPI-Key": "b3e2fe7f33mshba762ec5a11343fp1cd6e4jsna308f09531ab",
	"X-RapidAPI-Host": "golf-leaderboard-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())