def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "There is no such contact in the phonebook."
        except ValueError:
            return "Enter the name and phone number separated by a space."
        except IndexError:
            return "Enter the name of the contact you want to see the phone number for."
    return wrapper

phonebook = {}

@input_error
def add_contact(name, phone):
    phonebook[name] = phone
    return f"{name}'s phone number {phone} has been added to the phonebook."

@input_error
def change_contact(name, phone):
    phonebook[name] = phone
    return f"{name}'s phone number has been updated to {phone} in the phonebook."

@input_error
def get_phone(name):
    return f"{name}'s phone number is {phonebook[name]}."

@input_error
def show_all():
    return "\n".join([f"{name}: {phone}" for name, phone in phonebook.items()])

def parse_command(command):
    words = command.lower().split()

    if words[0] == "hello":
        return "How can I help you?"

    if words[0] == "add":
        name, phone = words[1], words[2]
        return add_contact(name, phone)

    if words[0] == "change":
        name, phone = words[1], words[2]
        return change_contact(name, phone)

    if words[0] == "phone":
        name = words[1]
        return get_phone(name)

    if words[0] == "show" and words[1] == "all":
        return show_all()

    if words[0] in ["good", "bye", "close", "exit"]:
        return "Good bye!"
    
def main():
    print("Welcome to Phonebook assistant!")
    while True:
        command = input("Enter command: ")
        if command == ".":
            print("Good bye!")
            break
        response = parse_command(command)
        print(response)

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "There is no such contact in the phonebook."
        except ValueError:
            return "Enter the name and phone number separated by a space."
        except IndexError:
            return "Enter the name of the contact you want to see the phone number for."
    return wrapper


phonebook = {}

@input_error
def add_contact(name, phone):
    phonebook[name] = phone
    return f"{name}'s phone number {phone} has been added to the phonebook."


@input_error
def change_contact(name, phone):
    phonebook[name] = phone