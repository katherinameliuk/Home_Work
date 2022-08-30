WIN_DICTONARY = {"rock": ["scissors", "rock"], "scissors": ["paper", "scissors"], "paper": ["rock", "paper"]}

def game(player_1: str, player_2: str, player_3: str):
    if player_1 == player_2 == player_3:
        print("Tie")
    elif player_2 in WIN_DICTONARY[player_1]:
        print(f"{player_1} is winner")
    elif player_2 not in WIN_DICTONARY[player_1]:
        print(f"{player_2} is winner")
    elif player_3 in WIN_DICTONARY[player_1]:
        print(f"{player_1} is winner")
    elif player_3 not in WIN_DICTONARY[player_1]:
        print(f"{player_3} is winner")


game("scissors", "paper", "rock")
game("rock", "scissors", "paper")
game("paper", "rock", "scissors")

game("paper", "scissors", "scissors")
game("paper", "rock", "rock")
game("rock", "paper", "paper")
game("rock", "scissors", "scissors")
game("scissors", "paper", "paper")
game("scissors", "rock", "rock")

game("scissors", "scissors", "scissors")
game("paper", "paper", "paper")
game("rock", "rock", "rock")