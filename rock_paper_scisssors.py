import random
from colorama import Fore

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_games_won = 0
player_games_won = 0
drawn_games = 0
while True:
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
        drawn_games += 1
    elif (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) \
            or (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You Win")
        player_games_won += 1
    else:
        print(Fore.RED + "You Lose")
        computer_games_won += 1
    print(Fore.WHITE + f"You: {player_games_won} || Computer: {computer_games_won} || Draws: {drawn_games}")
    if input("Play again? [y/n]: ").lower() == "n":
        break

