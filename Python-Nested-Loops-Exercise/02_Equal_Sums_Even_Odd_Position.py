start_num = int(input())
end_num = int(input())

for num in range(start_num, end_num + 1):
    even_sum = 0
    odd_sum = 0
    temp_num = num

    for i in range(6, 0, -1):
        digit = temp_num % 10
        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        temp_num //= 10

    if even_sum == odd_sum:
        print(num, end=" ")