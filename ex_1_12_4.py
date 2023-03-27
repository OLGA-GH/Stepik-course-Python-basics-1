roomType = str(input())

if roomType == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print(float((p * (p - a) * (p - b) * (p - c)) ** 0.5))

elif roomType == "прямоугольник":
    a = int(input())
    b = int(input())
    print(float(a * b))

elif roomType == "круг":
    a = int(input())
    print(float(3.14 * (a**2)))
