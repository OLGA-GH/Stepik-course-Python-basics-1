s = input()

currChar = s[0]
currCount = 0
result = ""

for ch in s:
    if ch != currChar:
        result += currChar + str(currCount)
        currChar = ch
        currCount = 1
    else:
        currCount += 1
result += currChar + str(currCount)

print(result)
