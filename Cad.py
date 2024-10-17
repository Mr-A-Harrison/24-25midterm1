import random

print("Welcome to rock, paper, scissors")

player_score = 0
computer_score = 0

options = ["Rock", "Paper", "Scissors"]

player_choice = input("Enter Rock, Paper, or Scissors: ")
if player_choice not in ["Rock", "Paper", "Scissors"]:
  print("Invalid try again")

  
computer_choice = random.choice(options)
print("Computer chose:" + computer_choice)


if computer_choice == player_choice:
  print("It's a tie!")
elif (computer_choice == "Rock" and player_choice == "Paper") :
  print("You Win!")
  player_score += 1
elif (computer_choice == "Scissors" and player_choice == "Rock"):
  print("You Win!")
  player_score += 1
elif(computer_choice == "Paper" and player_choice == "Scissors"):
  print("You Win!")
  player_score += 1
else:
  print("You Lose :(")
  computer_score += 1
if computer_score == 2:
    print("Game over you lose :(")
if player_score == 2:
    print("Game over you win!")

while player_score or computer_score < 2:
    options = ["Rock", "Paper", "Scissors"]
    player_choice = input("Enter Rock, Paper, or Scissors: ")
    if player_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid try again")
    computer_choice = random.choice(options)
    print("Computer chose:" + computer_choice)
    if computer_choice == player_choice:
        print("It's a tie!")
    elif (computer_choice == "Rock" and player_choice == "Paper") :
        print("You Win!")
        player_score += 1
    elif (computer_choice == "Scissors" and player_choice == "Rock"):
        print("You Win!")
        player_score += 1
    elif(computer_choice == "Paper" and player_choice == "Scissors"):
        print("You Win!")
        player_score += 1
    else:
        print("You Lose :(")
        computer_score += 1
    if computer_score == 2:
        print("Game over you lose :(")
    if player_score == 2:
        print("Game over you win!")