n = int(input())

lastDigit = n % 10
last2Digits = n % 100

if last2Digits < 10:
    if lastDigit == 0 or lastDigit >= 5:
        print(n, "программистов")
    if lastDigit == 1:
        print(n, "программист")
    if 1 < lastDigit < 5:
        print(n, "программиста")

if 10 <= last2Digits <= 20:
    print(n, "программистов")

if last2Digits > 20:
    if lastDigit >= 5 or lastDigit == 0:
        print(n, "программистов")
    if lastDigit == 1:
        print(n, "программист")
    if 1 < lastDigit < 5:
        print(n, "программиста")
