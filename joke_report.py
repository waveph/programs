with open("jokes.txt", "r") as f:
#    content = f.readlines()

    
    setup_number = 0
    punchline_number = 0
    setup_length_line = 0
    punchline_length_line = 0 


    for line in f:
        if line == "\n": 
            continue 
        if line[0].isdigit():
            setup_number += 1
            char = line.split(". ", 1)[1].strip()
            setup_length_line += len(char)
        else:
            punchline_number += 1
            char2 = line.strip()
            punchline_length_line += len(char2)

#            total_jokes = setup_number//2

    avg_setup = setup_length_line / setup_number
    avg_punchline = punchline_length_line / punchline_number
            
    print(f"Total number of jokes is : {setup_number}")
    print(f"Total of setups is : {setup_number}")
    print(f"average setup len: {avg_setup}")
    print(f"Average punchline len: {avg_punchline}")
