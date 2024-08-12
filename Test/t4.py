def display_details():
    pass


def load_file():
    pass

def add_person(details):
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    details.append({"name": name, "age":age})


details = load_file()


while True:
    print("Data Entry")
    print("1. Add a person")
    print("2. Display details")

    choice = input("Enter your choice : ")
    if choice == '1':
        add_person(details)

    elif choice == '2':
        display_details(details)