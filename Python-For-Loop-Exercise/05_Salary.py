open_tabs = int(input())
salary = int(input())
check = True

for number in range (1, open_tabs + 1, 1):
    tab = input()
    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f"You have lost your salary.")
        check = False
        break
if check:
    print(salary)