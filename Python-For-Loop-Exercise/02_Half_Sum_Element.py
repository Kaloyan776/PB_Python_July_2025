num_count = int(input())
max_num = -999999999999999999
suma = 0
for number in range (1, num_count + 1, 1):
    user_input = int(input())
    if user_input > max_num:
        max_num = user_input
    suma = suma + user_input

other_nums_sum = suma - max_num

if max_num == other_nums_sum:
    print(f"Yes")
    print(f"Sum = {max_num}")
else:
    print(f"No")
    print(f"Diff = {abs(max_num - other_nums_sum)}")