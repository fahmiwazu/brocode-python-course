################## QUIZZZZ make rock paper scissors game in python
import random

while True:
    tangan = ["watu","kertas","gunting"]
    computer = random.choice(tangan)
    player = None

    while player not in tangan:
        player = input("watu, kertas, gunting? : ").lower()

    if player == computer:
        print("Computer :",computer)
        print("Player :",player)
        print("seri")
    elif player == "watu":
        if computer == "kertas":
            print("Computer :", computer)
            print("Player :", player)
            print("kalah")
        if computer == "gunting":
            print("Computer :", computer)
            print("Player :", player)
            print("menang")
    elif player == "kertas":
        if computer == "watu":
            print("Computer :", computer)
            print("Player :", player)
            print("menang")
        if computer == "gunting":
            print("Computer :", computer)
            print("Player :", player)
            print("kalah")
    elif player == "gunting":
        if computer == "kertas":
            print("Computer :", computer)
            print("Player :", player)
            print("menang")
        if computer == "watu":
            print("Computer :", computer)
            print("Player :", player)
            print("kalah")

    play_again = input("Play again ? ( Y / N ) :")

    if play_again !="Y":
        break

print("BYE!!")