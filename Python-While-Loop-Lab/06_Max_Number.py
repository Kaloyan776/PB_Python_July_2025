maxi = - 99999999999999999
while True:
    num = input()
    if num == "Stop":
        break
    conversion = int(num)
    if maxi < conversion:
        maxi = conversion

print(maxi)