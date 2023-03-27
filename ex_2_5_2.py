a = [int(i) for i in input().split()]
if len(a) > 1:
    for i in range(len(a)):
        print(a[i - 1] + a[i + 1 - len(a)], end=" ")
else:
    print(a[0], end=" ")
