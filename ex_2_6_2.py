x = int(input())
list_s = []

for i in range(1, x + 1):
    for n in range(0, i):
        if len(list_s) >= x:
            break
        list_s.append(i)

print(*list_s)
