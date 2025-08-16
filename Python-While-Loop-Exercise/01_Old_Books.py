search_book = input()
user_guess = ""
counter = 0
check = True

while search_book != user_guess:
    user_guess = input()
    if user_guess == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        check = False
        break
    counter += 1
if check:
    print(f"You checked {counter - 1} books and found it.")