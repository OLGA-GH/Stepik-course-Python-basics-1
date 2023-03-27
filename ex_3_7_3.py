d_words = []
l_strings = []
errors = []

d_count = int(input())
for s in range(d_count):
    d_words.append(input().lower())
l_count = int(input())
for s in range(l_count):
    l_strings.append(input().lower())

for s in l_strings:
    for word in s.split(" "):
        if word.lower() not in d_words:
            errors.append(word.lower())
res = set(errors)
for error in res:
    print(error)
