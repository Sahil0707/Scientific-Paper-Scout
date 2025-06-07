import shlex
from agent_host import process_command

def cli():
    print("Welcome to Scientific Paper Scout CLI (Gemini Edition) 🚀")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # smart split
        parts = shlex.split(user_input)
        command = parts[0]
        args = parts[1:]

        result = process_command(command, args)
        print(result)

if __name__ == "__main__":
    cli()
