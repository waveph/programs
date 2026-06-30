import requests

url = "https://official-joke-api.appspot.com/random_joke"

for i in range(5):
	print()
	print(f"{i+1}.")
	
	try:
		response = requests.get(url, timeout=10)
		response.raise_for_status()
		data = response.json()

		print(data["setup"])
		print(data["punchline"])
	except requests.exceptions.ConnectionError:
		print("Error: no internet connection.")
	except requests.exceptions.Timeout:
		print("Error: Request timed out.")
	except Exception as e:
		print(f"Something went wrong: {e}")
	
