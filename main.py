import pickle
import os

# Student Management System - Python Component
def add_record():
    with open("students.dat", "ab") as f:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        record = {"roll": roll, "name": name, "marks": marks}
        pickle.dump(record, f)
    print("Record added successfully!")

def display_high_scorers():
    print("\n--- Students scoring above 90% ---")
    found = False
    if not os.path.exists("students.dat"):
        print("No records found.")
        return
    
    with open("students.dat", "rb") as f:
        while True:
            try:
                rec = pickle.load(f)
                if rec['marks'] > 90:
                    print(f"Name: {rec['name']} | Roll: {rec['roll']} | Marks: {rec['marks']}%")
                    found = True
            except EOFError:
                break
    if not found:
        print("No students found with > 90% marks.")

def main_menu():
    while True:
        print("\n1. Add Student\n2. View High Scorers (>90%)\n3. Exit")
        ch = input("Choice: ")
        if ch == '1': add_record()
        elif ch == '2': display_high_scorers()
        elif ch == '3': break
        else: print("Invalid Choice.")

if __name__ == "__main__":
    main_menu()
