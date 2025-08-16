n = int(input())
suma = 0
for num1 in range(0, n + 1, 1):
    for num2 in range(0, n + 1, 1):
        for num3 in range(0, n + 1, 1):
            if num1 + num2 + num3 == n:
                suma+=1
print(suma)