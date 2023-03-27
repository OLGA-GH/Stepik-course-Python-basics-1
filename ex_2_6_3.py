list_s = list(map(int, input().split(" ")))
x = int(input())


def get_indices(list_s, x):
    return [i for i in range(len(list_s)) if list_s[i] == x]


res_list = get_indices(list_s, x)

if len(res_list) > 0:
    print(*res_list)
else:
    print("Отсутствует")
