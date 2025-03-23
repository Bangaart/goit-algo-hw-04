def input_parcer(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_command(args,contacts):
    if not len(args) ==2:
        return "Please enter correct Name and Phone. Example: Arthur 0991112233"
    else:
        name, phone = args
        contacts[name] = phone
        return "Contact added"

def change_username(args, contacts):
    if not len(args) ==2:
        return "Please enter correct Name and Phone for changing. Example: Arthur 0991112233"
    else:
        name, phone = args
        if name in contacts:
            name, phone = args
            contacts[name] = phone
            return "Contact changed"
        else:
            return f"There is no such contact in the list yet. {add_command(args,contacts)}"

def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "No find such name"

def get_all(contacts):
    return [f"{key} : {value}\n" for key ,value in contacts.items()]

def main():
    contacts = {}
    print("Welcome to assistant bot")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = input_parcer(user_input)


        if command in ["exit", "close"]:
            print("Good bye")
            break
        elif command == "hello":
            print("How can i help you")
        elif command == "add":
            print(add_command(args, contacts))
        elif command == "change":
            print(change_username(args,contacts))
        elif command == "phone":
            print(get_phone(args,contacts))
        elif command == "all":
            print(*get_all(contacts))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
