n_count = int(input())
commands = []
location = [0, 0]

for s in range(n_count):
    commands.append(input())

for each in commands:
    command = each.split(" ")
    if command[0] == "север":
        location[1] += int(command[1])
    elif command[0] == "юг":
        location[1] -= int(command[1])
    elif command[0] == "восток":
        location[0] += int(command[1])
    elif command[0] == "запад":
        location[0] -= int(command[1])


print(location[0], location[1])
