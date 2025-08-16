# 06. Unique PIN codes // SOLVED!
max_num_for_first_num = int(input())
max_num_for_second_num = int(input())
max_num_for_third_num = int(input())

for first_num in range(2, max_num_for_first_num + 1, 2):
    for second_num in range(2, max_num_for_second_num + 1, 1):
        for third_num in range(2, max_num_for_third_num + 1, 2):
            if second_num == 2:
                print(f"{first_num} {second_num} {third_num}")
            elif second_num == 3:
                print(f"{first_num} {second_num} {third_num}")
            elif second_num == 5:
                print(f"{first_num} {second_num} {third_num}")
            elif second_num == 7:
                print(f"{first_num} {second_num} {third_num}")