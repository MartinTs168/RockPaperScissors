import random
from colorama import Fore

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_move = random.choice([rock, paper, scissors])
print(f"The computer chose: {computer_move}")
if player_move == computer_move:
    print(Fore.YELLOW + "Draw")
elif (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) \
        or (player_move == scissors and computer_move == paper):
    print(Fore.GREEN + "You Win")
else:
    print(Fore.RED + "You Lose")