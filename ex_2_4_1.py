a = input()
g = a.upper().count("g".upper())
c = a.upper().count("c".upper())
n = len(a)
perc_gc = float(((g + c) * 100) / n)
print(perc_gc)
