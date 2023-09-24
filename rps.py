import random

pl1 = 0
pl2 = 0


def gamelogic(player_input):
    global pl1
    global pl2
    cards = ["rock", "paper", "sisor"]
    status = ["you won", "computer won"]
    player2 = random.randint(1, 3)
    if player_input == player2:
        print("drow")
    elif player_input == 1:
        print("you", cards[player_input-1])
        if player2 == 3:
            print("computer", cards[player2-1])
            print(status[0])
            pl1 = pl1 + 1
        else:
            print("computer", cards[player2-1])
            print(status[1])
            pl2 = pl2 + 1

    elif player_input == 2:
        print("you", cards[player_input-1])
        if player2 == 1:
            print("computer", cards[player2-1])
            print(status[0])
            pl1 = pl1 + 1
        else:
            print("computer", cards[player2-1])
            print(status[1])
            pl2 = pl2 + 1

    elif player_input == 3:
        print("you", cards[player_input-1])
        if player2 == 2:
            print("computer", cards[player2-1])
            print(status[0])
            pl1 = pl1 + 1
        else:
            print("computer", cards[player2-1])
            print(status[1])
            pl2 = pl2 + 1


def main():
    global pl1
    global pl2
    print("rock-paper-sisor")
    x = True
    while x:
        inp = int(input('rock(1),paper(2),sisor(3) quit(4): '))
        if inp not in (1, 2, 3, 4):
            print("invalid")
            return main()
        else:
            gamelogic(inp)
            print("you:", pl1)
            print("computer:", pl2)


main()
