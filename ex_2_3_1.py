a = int(input())
b = int(input())
c = int(input())
d = int(input())

for j in range(c, d + 1):
    if j == c:
        print("\t", end="")
    print(j, end="\t")

print()

for i in range(a, b + 1):
    if i != a:
        print()
    print(i, end="\t")
    for j in range(c, d + 1):
        print(i * j, end="\t")
