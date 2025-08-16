n = int(input())
left_sum = 0
right_sum = 0


for number in range(1, 2 * n + 1, 1):
    num = int(input())
    if number <= 2 * n / 2:
        left_sum = left_sum + num
    else:
        right_sum = right_sum + num
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")