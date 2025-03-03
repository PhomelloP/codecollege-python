class Stack_Overflowed:
    "Stores Team info"
    def _init_(self,Age,Majors,Skill="Infinite"):
        self.Age=Age
        self.Majors=Majors
        self.Skill=Skill

    def Overflower_information(self):
        print(f"\n  Meet {self.Name} A young {self.Age}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

Lindo= Stack_Overflowed(Age=23,Majors="Cyber Security",Skill="Leadership")
Courtney= Stack_Overflowed(19,"WebDev","CreativeTech")
Ulrich= Stack_Overflowed(20,"Machine Learning","Technical")
Tom=Stack_Overflowed(20,"Data Science","Communication")

print(f"Lindo IS: {Lindo.Age} and plans to specialize in{Lindo.Majors}, Her strenth is {Lindo.Skill}")
print("------")

print(f"Courtney is: {Courtney.Age}")
print("------")


# class StackOverFlow:
#     # Fixed variable (team name)
#     def init(self, member1, member2, member3, member4, member5, team_name = "StackOverflowed"):
#         # Instance variables for team members
#         self.member1 = member1
#         self.member2 = member2
#         self.member3 = member3
#         self.member4 = member4
#         self.member5 = member5
#         self.team_name = team_name

#     # Method to change the surname of the first member
#     def change_to_surname(self, surname):
#         self.member1 = surname

#     # Method to change the name of any team member
#     def change_member_name(self, member_num, surname):
#         if member_num == 1:
#             self.member1 = surname
#         elif member_num == 2:
#             self.member2 = surname
#         elif member_num == 3:
#             self.member3 = surname
#         elif member_num == 4:
#             self.member4 = surname
#         elif member_num == 5:
#             self.member4 = surname
#         else:
#             print("Invalid member number!")

#     # Method to display team details
#     def display_team_info(self):
#         print(f"Team Name: {self.team_name}")
#         print(f"Member 1: {self.member1}")
#         print(f"Member 2: {self.member2}")
#         print(f"Member 3: {self.member3}")
#         print(f"Member 4: {self.member4}")
#         print(f"Member 5: {self.member5}")


# Create a team with initial member names
# team = StackOverFlow("Lindo", "Courteney", "Ulrich", "Tom", "Phomello")

# Display initial team details
# team.display_team_info()

# Change the surname of the first member (Lindo)
# team.change_to_surname("Yende")