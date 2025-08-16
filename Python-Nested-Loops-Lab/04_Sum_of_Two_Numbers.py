beginning = int(input())
ending = int(input())
magic_num = int(input())
combination_count = 0
check = True

for num1 in range(beginning, ending + 1, 1):
    for num2 in range(beginning, ending + 1, 1):
        combination_count+=1
        if num1 + num2 == magic_num:
            print(f"Combination N:{combination_count} ({num1} + {num2} = {magic_num})")
            check = False
            break
    if not check:
        break
if check:
    print(f"{combination_count} combinations - neither equals {magic_num}")