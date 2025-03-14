from roles import *
class SignUp:

    def __init__(self):
        self.get_user_details()
        self.choose_position()

    def get_user_details(self):
        self.first_name = input("What is your first name: ").title()
        self.second_name = input("What is your last name: ").title()
        self.email = input("What is your email: ")

        if self.first_name == "" or self.second_name == "" or self.email == "":
            print("Please fill in all the fields.")
            self.get_user_details()

    def choose_position(self):
        job = {
            "Janitor": janitor,
            "Programmer": programmer,
            "Secretory": secretory,
            "Developer": Developer,
            "Manager": Manager
        }

        print("\nAvailable Positions:")
        for job in job:
            print(f"- {job}")

        while True:
            chosen_role = input("Select your position: ").strip().title()
            if chosen_role in job:
                self.position = job[chosen_role]
                break
            else:
                print("Invalid choice. Please select a valid position.")