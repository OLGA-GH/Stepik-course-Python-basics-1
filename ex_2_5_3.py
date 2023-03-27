s = [int(i) for i in input().split()]
s.sort()
prev_ch = ""

if len(s) > 1:
    for i in s:
        if (s.count(i) > 1) and (prev_ch != i):
            print(i, end=" ")
            prev_ch = i
