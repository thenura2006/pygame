import random


def toss():
    print('hand-cricket')

    while True:
        toss_bet = input("head(1) or tale(2): ")
        coin_side = random.randint(1, 3)
        if toss_bet in (1, 2):
            if toss_bet == coin_side:
                print("you won toss")
            else:
                print("computer won toss")
        else:
            print("")
