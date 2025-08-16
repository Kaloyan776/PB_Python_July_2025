pens = int(input()) * 5.80
markers = int(input()) * 7.20
desinfectant = int(input()) * 1.20
discount = int(input()) / 100

suma = (pens + markers + desinfectant) * (1 - discount)

print(suma)