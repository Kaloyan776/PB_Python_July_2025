import math
name_of_figure = input()
if name_of_figure == "square":
    length = float(input())
    print(f"{(length * length):.3f}")
elif name_of_figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    print(f"{(side1 * side2):.3f}")
elif name_of_figure == "circle":
    radius = float(input())
    print(f"{(math.pi * radius * radius):.3f}")
elif name_of_figure == "triangle":
    width = float(input())
    height = float(input())
    print(f"{((width * height) / 2):.3f}")