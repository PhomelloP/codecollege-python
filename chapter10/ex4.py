guest_book_path = 'guest_book.txt'

with open(guest_book_path, 'a') as guest_book:
    while True:
        name = input("Please enter your name (or type 'quit' to exit): ")
        if name.lower() == 'quit':
            print("Thank you for signing the guest book!")
            break
        guest_book.write(f"{name}\n")
        print(f"Welcome, {name}! Your name has been added to the guest book.")
