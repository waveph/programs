import sys
import requests
import time

# 1 . set defaults
joke_type = "general"
joke_count = 3

# 2. override from cli if provided
if len(sys.argv) > 1:
	joke_type = sys.argv[1]
if len(sys.argv) > 2:
	joke_count = int(sys.argv[2])

# 3. buil url

url = f"https://official-joke-api.appspot.com/random_joke"
collected = []

# 4 . fetch
while len(collected) < joke_count:
    time.sleep(1.5)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        joke = response.json()
        
        if joke["type"] == joke_type:
            collected.append(joke)
            print(f"found {len(collected)}/{joke_count} {joke_type} jokes ...")
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"API error: {e}")
        print("Waiting 5 seconds before retrying...")
        time.sleep(5)

# 5 . print-data is a list of jokes, loop through it
#for i in range(len(data)):
#	joke = data[i]	
#	print(f"{i+1}. {joke['setup']}")
#	print(joke['punchline'])
#	print()
	
for i, joke in enumerate(collected):
	print(f"{i+1}. {joke['setup']}")
	print(joke['punchline'])
	print()

# 6. write into a txt
with open("jokes.txt", "w") as f:
	for i, joke in enumerate(collected):
		f.write(f"{i+1}. {joke['setup']}\n")
		f.write(f"{joke['punchline']}\n")
		f.write("\n")





	
