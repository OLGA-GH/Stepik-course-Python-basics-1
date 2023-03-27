X = int(input())
H = int(input())
M = int(input())

X_init = H * 60 + M
X_wakeup = X_init + X
H_wakeup = X_wakeup // 60
M_wakeup = X_wakeup % 60

print(H_wakeup)
print(M_wakeup)
