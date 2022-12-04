def rock_paper_scissors(player1, player2, pt_2=False):
    flat_points = {
        'x': 1,
        'y': 2,
        'z': 3,
    }

    outcomes = {
        'ax': 3,
        'ay': 6,
        'az': 0,
        'bx': 0,
        'by': 3,
        'bz': 6,
        'cx': 6,
        'cy': 0,
        'cz': 3,
    }

    if pt_2:
        if player2 == 'y':
            player2 = chr(ord(player1) + 23)
        else:
            for plays, points in outcomes.items():
                if player2 == 'z' and points == 6 and plays[0] == player1:
                    player2 = plays[1]
                    break
                elif player2 == 'x' and points == 0 and plays[0] == player1:
                    player2 = plays[1]
                    break

    match = player1 + player2
    return outcomes[match] + flat_points[player2]


with open("input.txt", "r") as f:
    games = f.read()

games = games.lower().split("\n")

my_score = 0
my_new_score = 0

for game in games:
    their_play, my_play = game.split(" ")

    # part 1
    my_score += rock_paper_scissors(their_play, my_play)

    # part 2
    my_new_score += rock_paper_scissors(their_play, my_play, pt_2=True)

print(f"First answer: {my_score}")
print(f"Second answer: {my_new_score}")
