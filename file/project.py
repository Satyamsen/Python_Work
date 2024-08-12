import json

def load_file():
    try:
        file=open('details_of_user','r')
        json.load(file)
    except FileNotFoundError:
        return []

def sever_op(details):
    file = open('details_of_user','w')
    json.dump(details,file)

def display_data(details):
    a=(enumerate(details,start=1))
    for i,j in a:
        print(f"User {i}\n name : {j['name']}\n age : {j['age']}\n dob : {j['dob']}")
    

def add_person(details):
    name=input("Enter name : ")
    age=input("Enter age : ")
    dob=input("Enter dob : ")
    details.append({'name':name,'age':age,'dob':dob})
    sever_op(details)
    
def update_person(details):
    display_data(details)
    
    if details:
        try:
            a = int(input("Enter the user number to update: ")) - 1
            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_dob = input("Enter new dob: ")
            
            details[a]['name'] = new_name
            details[a]['age'] = new_age
            details[a]['dob'] = new_dob
            
            sever_op(details)
            print("User updated successfully.")
        except (IndexError, ValueError):
            print("Invalid input. Please try again.")
    else:
        print("No data available to update.")
        

def delete_person(details):
    display_data(details)
    
    if details:
        try:
            index = int(input("Enter the user number to delete: ")) - 1
            del details[index]
            sever_op(details)
            print("User deleted successfully.")
        except (IndexError, ValueError):
            print("Invalid input. Please try again.")
    else:
        print("No data available to delete.")


details = load_file()

def main ():
    while True:
        print("1. Display Details")
        print("2. Add Person")
        print("3. Update Person")
        print("4. Delete a person")
        print("5. Exit")

        choice = input("Enter your choice : ")

        match choice:
            case "1":
                display_data(details)
            case "2":
                add_person(details)
            case "3":
                update_person(details)
            case "4":
                delete_person(details)
            case "5":
                break
            

if __name__=="__main__":
    main()