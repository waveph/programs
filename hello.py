import sys

#if len(sys.argv) > 1:
#    name = " ".join(sys.argv[1:])
#else:
#    name = "there"

#print(f"hello {name}")

greetings = {"en": "hello", "ar": "marhaba", "fr": "bonjour"}

if "--language" in sys.argv:

#	position = sys.argv.index("--language")
	position = -1
	for i in range(len(sys.argv)):
		if sys.argv[i] == "--language":
			position = i
	
	try:
		language_code = sys.argv[position + 1]
	except IndexError:
		print("Error: --language requires a value(en,ar,fr)")
		sys.exit(1)

	greeting = greetings.get(language_code, "hello")
	name = " ".join(sys.argv[position + 2:]) or "there"
	
	if language_code not in greetings:
		print(f"Warning: '{language_code}' is not supported. Using English.")
	
	print(f"{greeting} {name}")

else:
	name= " ".join(sys.argv[1:]) or "there"
	print(f"hello {name}")

