height = int(input())
width = int(input())
thickness = int(input())
percentage = float(input()) / 100

full_volume = height * width * thickness
full_volume_litres = full_volume * 0.001
needed_litres = full_volume_litres * (1 - percentage)

print(needed_litres)