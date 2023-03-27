# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
n = int(input())
result_dict = {}

for x in range(0, n):
    x = int(input())
    if x not in result_dict.keys():
        x_value = f(x)
        result_dict[x] = x_value
        print(x_value)
    else:
        print(result_dict[x])
