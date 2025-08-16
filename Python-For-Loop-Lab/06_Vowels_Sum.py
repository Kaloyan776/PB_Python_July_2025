text = input()
suma = 0

for char in text:
    if char == 'a':
        suma = suma + 1
    elif char == 'e':
        suma = suma + 2
    elif char == 'i':
        suma = suma + 3
    elif char == 'o':
        suma = suma + 4
    elif char == 'u':
        suma = suma + 5

print(suma)