with open("input.txt") as f:
    s = f.read()

winners = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

losers = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draws = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

pts = {"X": 1, "Y": 2, "Z": 3}

score1, score2 = 0, 0

for game in s.strip().split("\n"):
    o, m = game.split(" ")
    score1 += pts[m]

    if winners[o] == m:
        score1 += 0
    elif losers[o] == m:
        score1 += 6
    else:
        score1 += 3

    assert m in ["X", "Y", "Z"]
    if m == "X":
        score2 += pts[winners[o]]
    elif m == "Y":
        score2 += pts[draws[o]] + 3
    else:
        score2 += pts[losers[o]] + 6


print("Final score with initial system = ", score1)
print("Final score with new system = ", score2)