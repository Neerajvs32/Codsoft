import os
import random

def draw_choice(choice):
    if choice == "rock":
        return """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    elif choice == "paper":
        return """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
    elif choice == "scissors":
        return """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    else:
        return "Invalid choice"

choices = ["rock", "paper", "scissors"]

def determine_winner(player, opp):
    if player == opp:
        return("It's a tie game!")
    elif ((player == "rock" and opp == "scissors") or 
          (player == "paper" and opp == "rock") or
          (player == "scissors" and opp == "paper")):
        return ("You won, congratulations!")
    else:
        return("You lost, sorry!")

playing, invalid = True, False
while playing:
    if not invalid:
        print("Choose rock, paper or scissors")
    else:
        print("Invalid input, please type rock, paper or scissors")
        invalid = False
    print("Or enter q to quit")
    player_choice = input().lower()
    opp_choice = random.choice(choices)
    
    if player_choice in choices:
        print("You chose:\n" + draw_choice(player_choice))
        print("The opponent chose:\n" + draw_choice(opp_choice))
        print(determine_winner(player_choice, opp_choice))
    elif player_choice == "q": 
        playing = False
    else:
        invalid = True

    if playing and not invalid:
        replay = input("Wanna play again? Type yes to replay\nor enter anything else to end the game\n").lower()
        print()
        playing = replay == "yes"
    
    os.system('cls' if os.name == 'nt' else 'clear')  

print("Thanks for playing!")