"""Module for Task 4."""

import handler

def parse_input(user_input: str) -> tuple:
    """Parses user input and returns command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    """Main function."""
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "all":
            print(handler.get_all_contacts())

        elif command == "add":
            print(handler.add_contact(*args))

        elif command == "change":
            print(handler.change_contact(*args))

        elif command == "phone":
            print(handler.get_phone(*args))

        elif command in ["exit", "close"]:
            print("Goodbye!")
            break

        else:
            print("Invalid command. Usage: hello | all | add [name] [phone] | change [name] [phone] | phone [name] | exit | close")

if __name__ == "__main__":
    main()
