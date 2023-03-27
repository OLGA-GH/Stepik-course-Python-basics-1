sum_ = 0
sum_sqr = 0

while True:
    x = int(input())
    sum_ += x
    sum_sqr += x**2
    if sum_ == 0: break

print(sum_sqr)