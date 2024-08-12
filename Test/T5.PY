import sqlite3

# Connect to SQLite database
def connect_db():
    conn = sqlite3.connect("Ram.db")
    cur = conn.cursor()
    return conn, cur

# Create the table if it doesn't exist
def create_table():
    conn, cur = connect_db()
    cur.execute('''CREATE TABLE IF NOT EXISTS Ram (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    dob TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Load data from the database
def load_data():
    conn, cur = connect_db()
    cur.execute("SELECT * FROM Ram")
    rows = cur.fetchall()
    conn.close()
    return rows

# Save a new person to the database
def add_person(name, age, dob):
    conn, cur = connect_db()
    cur.execute("INSERT INTO Ram (name, age, dob) VALUES (?, ?, ?)", (name, age, dob))
    conn.commit()
    conn.close()

# Update a person's details in the database
def update_person(id, new_name, new_age, new_dob):
    conn, cur = connect_db()
    cur.execute("UPDATE Ram SET name = ?, age = ?, dob = ? WHERE id = ?", (new_name, new_age, new_dob, id))
    conn.commit()
    conn.close()

# Delete a person from the database
def delete_person(id):
    conn, cur = connect_db()
    cur.execute("DELETE FROM Ram WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Display data from the database
def display_data():
    rows = load_data()
    if not rows:
        print("No data available.")
        return
    for i, row in enumerate(rows, start=1):
        print(f"User {i}\n ID: {row[0]}\n Name: {row[1]}\n Age: {row[2]}\n DOB: {row[3]}")

# Main function to interact with the user
def main():
    create_table()
    
    while True:
        print("\n1. Display Details")
        print("2. Add Person")
        print("3. Update Person")
        print("4. Delete Person")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                display_data()
            case "2":
                name = input("Enter name: ").strip()
                age = int(input("Enter age: ").strip())
                dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
                add_person(name, age, dob)
                print("Person added successfully.")
            case "3":
                display_data()
                if load_data():
                    try:
                        user_id = int(input("Enter the ID of the user to update: ").strip())
                        new_name = input("Enter new name: ").strip()
                        new_age = int(input("Enter new age: ").strip())
                        new_dob = input("Enter new date of birth (YYYY-MM-DD): ").strip()
                        update_person(user_id, new_name, new_age, new_dob)
                        print("User updated successfully.")
                    except ValueError:
                        print("Invalid input. Please enter valid data.")
                else:
                    print("No data available to update.")
            case "4":
                display_data()
                if load_data():
                    try:
                        user_id = int(input("Enter the ID of the user to delete: ").strip())
                        delete_person(user_id)
                        print("User deleted successfully.")
                    except ValueError:
                        print("Invalid input. Please enter a valid ID.")
                else:
                    print("No data available to delete.")
            case "5":
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
