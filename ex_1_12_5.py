a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print(a)
    print(b)
    print(c)

if a == b and a > c:
    print(a)
    print(c)
    print(b)

if a == b and a < c:
    print(c)
    print(a)
    print(b)

if c == b and c > a:
    print(c)
    print(a)
    print(b)

if c == b and a > c:
    print(a)
    print(c)
    print(b)

if a == c and a > b:
    print(a)
    print(b)
    print(c)

if a == c and a < b:
    print(b)
    print(a)
    print(c)

if b < a > c and b != c:
    print(a)
    if b > c:
        print(c)
        print(b)

    else:
        print(b)
        print(c)


if a < b > c and a != c:
    print(b)
    if a > c:
        print(c)
        print(a)

    else:
        print(a)
        print(c)


if a < c > b and a != b:
    print(c)
    if a > b:
        print(b)
        print(a)

    else:
        print(a)
        print(b)
