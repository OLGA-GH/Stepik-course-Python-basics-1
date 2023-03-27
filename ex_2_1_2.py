a = int(input())
b = int(input())
d = 1
i = True

while i:
    if (d % a == 0) and (d % b == 0):
        i = False
        print(d)
    else:
        d += 1
