class Pupil:
    def __init__(self, name, age, english, math, physics, chemistry, cs):
        self.name = name
        self.age = age
        self.english = english
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.cs = cs

class PupilManagementSystem:
    def __init__(self):
        self.pupils = []

    def create_pupil_record(self):
        name = input("Enter pupil's name: ")
        age = input("Enter pupil's age: ")
        english = input("Enter English score: ")
        math = input("Enter Math score: ")
        physics = input("Enter Physics score: ")
        chemistry = input("Enter Chemistry score: ")
        cs = input("Enter Computer Science score: ")
        pupil = Pupil(name, age, english, math, physics, chemistry, cs)
        self.pupils.append(pupil)
        print("Pupil record created successfully.")

    def display_all_pupil_records(self):
        if not self.pupils:
            print("No pupil records found.")
        else:
            print("All Pupil Records:")
            for idx, pupil in enumerate(self.pupils, start=1):
                print(f"{idx}. Name: {pupil.name}, Age: {pupil.age}, English: {pupil.english}, Math: {pupil.math}, Physics: {pupil.physics}, Chemistry: {pupil.chemistry}, CS: {pupil.cs}")

    def search_pupil_record(self):
        name = input("Enter pupil's name to search: ")
        found = False
        for pupil in self.pupils:
            if pupil.name.lower() == name.lower():
                print(f"Name: {pupil.name}, Age: {pupil.age}, English: {pupil.english}, Math: {pupil.math}, Physics: {pupil.physics}, Chemistry: {pupil.chemistry}, CS: {pupil.cs}")
                found = True
                break
        if not found:
            print("Pupil record not found.")

    def modify_pupil_record(self):
        name = input("Enter pupil's name to modify: ")
        for pupil in self.pupils:
            if pupil.name.lower() == name.lower():
                pupil.name = input("Enter new name: ")
                pupil.age = input("Enter new age: ")
                pupil.english = input("Enter new English score: ")
                pupil.math = input("Enter new Math score: ")
                pupil.physics = input("Enter new Physics score: ")
                pupil.chemistry = input("Enter new Chemistry score: ")
                pupil.cs = input("Enter new Computer Science score: ")
                print("Pupil record modified successfully.")
                break
        else:
            print("Pupil record not found.")

    def delete_pupil_record(self):
        name = input("Enter pupil's name to delete: ")
        for pupil in self.pupils:
            if pupil.name.lower() == name.lower():
                self.pupils.remove(pupil)
                print("Pupil record deleted successfully.")
                break
        else:
            print("Pupil record not found.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Create pupil record")
            print("2. Display all pupil records")
            print("3. Search pupil record")
            print("4. Modify pupil record")
            print("5. Delete pupil record")
            print("6. Back to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_pupil_record()
            elif choice == "2":
                self.display_all_pupil_records()
            elif choice == "3":
                self.search_pupil_record()
            elif choice == "4":
                self.modify_pupil_record()
            elif choice == "5":
                self.delete_pupil_record()
            elif choice == "6":
                break
            else:
                print("Invalid choice.")

    def class_result(self):
        if not self.pupils:
            print("No pupil records found.")
        else:
            print("Class Result:")
            print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Name", "Age", "English", "Math", "Physics", "Chemistry", "CS"))
            for pupil in self.pupils:
                print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(pupil.name, pupil.age, pupil.english, pupil.math, pupil.physics, pupil.chemistry, pupil.cs))

    def pupil_report_card(self):
        name = input("Enter pupil's name to generate report card: ")
        found = False
        for pupil in self.pupils:
            if pupil.name.lower() == name.lower():
                print("Pupil Report Card:")
                print(f"Name: {pupil.name}")
                print(f"Age: {pupil.age}")
                print(f"English: {pupil.english}")
                print(f"Math: {pupil.math}")
                print(f"Physics: {pupil.physics}")
                print(f"Chemistry: {pupil.chemistry}")
                print(f"CS: {pupil.cs}")
                found = True
                break
        if not found:
            print("Pupil record not found.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Report")
            print("2. Admin")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                while True:
                    print("\nReport Menu:")
                    print("1. Class result")
                    print("2. Pupil report card")
                    print("3. Back to main menu")

                    report_choice = input("Enter your choice: ")

                    if report_choice == "1":
                        self.class_result()
                    elif report_choice == "2":
                        self.pupil_report_card()
                    elif report_choice == "3":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "2":
                self.admin_menu()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    system = PupilManagementSystem()
    system.main_menu()
