import sys
import requests
import time

if len(sys.argv) < 2:
    print("Usage: joke_manager.py <fetch|report> [options]")
    sys.exit(1)

if sys.argv[1] == "fetch":
        #1. Defaults
    joke_type = "general"
    joke_count = 3

    #2. Parse -- type flag
    if "--type" in sys.argv:
        position = sys.argv.index("--type")
        try:
            joke_type = sys.argv[position + 1]
        except IndexError:
            print("Error: --type requires a value (general, programming, knock-knock)")
            sys.exit(1)

    #3. Parse --count flag (same pattern, but convert to int)
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
            
    #4. Fetch jokes 
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
    with open("/home/nounou/Desktop/programs/jokes.txt", "w") as f:
        for i, joke in enumerate(collected):
            f.write(f"{i+1}. {joke['setup']}\n")
            f.write(f"{joke['punchline']}\n")
            f.write("\n")

        print(f"Saved {joke_count} {joke_type} jokes to jokes.txt")


elif sys.argv[1] == "report":
    setup_number = 0
    punchline_number = 0
    total_setup_length = 0 
    total_punchline_length = 0
    longest_setup = ""
    shortest_punchline = None

    with open("/home/nounou/Desktop/programs/jokes.txt", "r") as f:
        for line in f:
            if line == "\n":
                continue
            if line[0].isdigit():
                setup_number += 1
                text = line.split(". ", 1)[1].strip()
                total_setup_length += len(text)
                if len(text) > len(longest_setup):
                    longest_setup = text
            else:
                punchline_number += 1
                text = line.strip()
                total_punchline_length += len(text)
                if shortest_punchline is None or len(text) < len(shortest_punchline):
                    shortest_punchline = text
    avg_setup = total_setup_length / setup_number
    avg_punchline = total_punchline_length / punchline_number

    print(f"Total jokes: {setup_number}")
    print(f"Average setup length: {avg_setup:.1f} charachters")
    print(f"Average punchline length: {avg_punchline:.1f} characters")
    print(f"Longest setup: {longest_setup}")
    print(f"Shortest punchline: {shortest_punchline}")

elif sys.argv[1] == "search":
    #Parse --keyword flag (required)
    if "--keyword" not in sys.argv:
        print("Error: --keyword is required")
        sys.exit(1)

    keyword_pos = sys.argv.index("--keyword")
    try:
        keyword = sys.argv[keyword_pos + 1]
    except IndexError:
        print("Error: --keyword requires a search term")
        sys.exit(1)

    #Parse --file flag (optional, default jokes.txt)
    filepath = "/home/nounou/Desktop/programs/jokes.txt"
    if "--file" in sys.argv:
        file_pos = sys.argv.index("--file")
        try:
            filepath = sys.argv[file_pos + 1]
        except IndexError:
            print("Error: --file requires a filename")
            sys.exit(1)
    #Search the file
    found = False
    joke_number = 0
    with open(filepath, "r") as f:
        for line in f:
            if line =="\n":
                continue
            if line[0].isdigit():
                joke_number += 1
                setup = line.split(". ", 1)[1].strip()
                #will check setup after reading punchline
            else:
                punchline = line.strip()
                if keyword.lower() in setup.lower() or keyword.lower() in punchline.lower():
                    found = True
                    print(f"{joke_number}. {setup}")
                    print(punchline)
                    print()
    if not found:
        print(f"No jokes found containing '{keyword}'")

else:
    print(f"Unknown command: {sys.argv[1]}")
    sys.exit(1)