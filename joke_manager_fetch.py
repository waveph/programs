import sys
import requests
import time

#1. Defaults
joke_type = "general"
joke_count = 3

#2. Check for subcommand
if len(sys.argv) < 2 or sys.argv[1] != "fetch":
    print("Usage: joke_manager.py fetch --type <type> --count <number>")
    sys.exit(1)

#3. Parse -- type flag
if "--type" in sys.argv:
    position = sys.argv.index("--type")
    try:
        joke_type = sys.argv[position + 1]
    except IndexError:
        print("Error: --type requires a value (general, programming, knock-knock)")
        sys.exit(1)

#4. Parse --count flag (same pattern, but convert to int)
if "--count" in sys.argv:
    position = sys.argv.index("--count")
    try:
        joke_count = int(sys.argv[position + 1])
    except IndexError:
        print("Error: --count requires a number")
        sys.exit(1)
    except ValueError:
        print("Error: --count must be a valid integer")
        sys.exit(1)
        
#5. Fetch jokes 
url = f"https://official-joke-api.appspot.com/random_joke"
collected = []

while len(collected) < joke_count:
    time.sleep(1.5)
    try: 
        response = requests.get(url, timeout = 10)
        response.raise_for_status()
        joke = response.json()

        if joke["type"] == joke_type:
            collected.append(joke)
            print(f"Found {len(collected)}/{joke_count} {joke_type} jokes ...")
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e}")
        print("Waiting 5 seconds before trying again...")
        time.sleep(5)


#6. Save to jokes.txt
with open("jokes.txt", "w") as f:
    for i, joke in enumerate(collected):
        f.write(f"{i+1}. {joke['setup']}\n")
        f.write(f"{joke['punchline']}\n")
        f.write("\n")

print(f"Saved {joke_count} {joke_type} jokes to jokes.txt")


