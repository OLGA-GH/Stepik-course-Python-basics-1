s = input()
s = s.lower()
s_list = s.split()
s_set = set(s_list)
for each in s_set:
    print(f"{each} {s_list.count(each)}")
