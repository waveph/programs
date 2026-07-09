import sys


if len(sys.argv) < 2:
    print("Usage: joke_manager.py <fetch|report> [options]")
    sys.exit(1)

if sys.argv[1] == "fetch":
    print("Fetch command goes here")
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

else:
    print(f"Unknown command: {sys.argv[1]}")
    sys.exit(1)