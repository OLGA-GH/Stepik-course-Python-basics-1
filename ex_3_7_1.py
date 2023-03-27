import itertools

n = int(input())
x_list = [input().split(";") for x in range(n)]
vs = [(x[0], x[2]) for x in x_list]

clubs = set(itertools.chain.from_iterable(vs))
res = {club: [0, 0, 0, 0, 0] for club in clubs}
for team1, gol1, team2, gol2 in x_list:
    res[team1][0] += 1
    res[team2][0] += 1
    if int(gol1) > int(gol2):
        res[team1][1] += 1
        res[team1][4] += 3
        res[team2][3] += 1
    elif int(gol1) < int(gol2):
        res[team2][1] += 1
        res[team2][4] += 3
        res[team1][3] += 1
    elif int(gol1) == int(gol2):
        res[team1][2] += 1
        res[team1][4] += 1
        res[team2][2] += 1
        res[team2][4] += 1
for club in clubs:
    print("{}:{}".format(club, " ".join(map(str, res[club]))))
