filename="guest.txt"

name=input("what is your name?")

with open(filename,"w") as file_object:
    file_object.write(f"{name}\n")