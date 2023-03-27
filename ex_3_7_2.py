s1 = input()
s2 = input()
s3 = input()
s4 = input()

s1_chars_list = []
s2_chars_list = []
s3_chars_list = []
s4_chars_list = []

s3_chars_list_encoded = []
s4_chars_list_decoded = []

for char in s1:
    s1_chars_list.append(char)
for char in s2:
    s2_chars_list.append(char)
for char in s3:
    s3_chars_list.append(char)
for char in s4:
    s4_chars_list.append(char)

# encode
for char in s3_chars_list:
    index = s1_chars_list.index(str(char))
    s3_chars_list_encoded.append(s2_chars_list[index])

# decode
for char in s4_chars_list:
    index = s2_chars_list.index(str(char))
    s4_chars_list_decoded.append(s1_chars_list[index])

print("".join(s3_chars_list_encoded))
print("".join(s4_chars_list_decoded))
