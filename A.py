import random

print("Hello")
welcome = input("Would u like to play??? y/n ")
if welcome == "y":
  print("Ok, welcome to the game ")
  card1 = random.randint(1,11)
  card2 = random.randint(1,11)
  cards3 = card1 + card2
  print("Your total is: ", cards3)
  dealer1 = random.randint(1,11)
  dealer2 = random.randint(1,11)
  dealers3 = dealer1 + dealer2
  print("The dealers total is: ", dealers3)
  question1 = input("Would you like to hit or stand? h/s ")
  if question1 == "h":
    card3 = random.randint(1,11)
    cards4 = card1 + card2 + card3
    print("Your total is: ", cards4)
    dealer3 = random.randint(1,11)
    dealers4 = dealer1 + dealer2 + dealer3
    print("The dealers total is: ", dealers4)
    if dealers4 > 21:
      print("YOU WIN, the dealer busted")
      exit()
    if cards4 > 21:
      print("YOU LOSE, you busted")
      exit()
    if cards4 >= dealers4 or cards4 <= dealers4:
      question2 = input("Would you like to hit or stand? h/s ")
      if question2 == "h":
        card4 = random.randint(1,11)
        cards5 = card1 + card2 + card3 + card4
        print("Your total is: ", cards5)
        dealer4 = random.randint(1,11)
        dealers5 = dealer1 + dealer2 + dealer3 + dealer4
        print("The dealers total is: ", dealers5)
        if dealers5 > 21:
          print("YOU WIN, the dealer busted")
          exit()
        if cards5 > 21:
          print("YOU LOSE, you busted")
          exit()
        if cards5 >= dealers5 or cards5 <= dealers5:
          question3 = input("Would you like to hit or stand? h/s ")
          if question3 == "h":
            card5 = random.randint(1,11)
            cards6 = card1 + card2 + card3 + card4 + card5
            print("Your total is:", cards6)
            dealer5 = random.randint(1,11)
            dealers6 = dealer1 + dealer2 + dealer3 + dealer4 + dealer5
            print("The dealers total is:", dealers6)
            if dealers6 > 21:
              print("YOU WIN, the dealer busted")
              exit()
            if cards6 > 21:
              print("YOU LOSE, you busted")
              exit()
            if cards6 >= dealers6 or cards6 <= dealers6:
              question4 = input("Would you like to hit or stand? h/s ")
elif welcome == "n":
  print("Ok, bye")
  exit()
elif question1 == "s":
  if dealers3 < 17:
    dealer3 = random.randint(1,11)
    dealers4 = dealer1 + dealer2 + dealer3
    print("The dealers total is:", dealers4)
    if dealers4 > cards3 and dealers4 < 21:
      print("DEALER WINS, YOU LOSE")
      exit()
elif question2 == "s":
  if dealers4 < 17:
    dealer4 = random.randint(1,11)
    dealers5 = dealer1 + dealer2 + dealer3 +dealers4
    print("The dealers total is:", dealers5)
    if dealers5 > cards4 and dealers5 < 21:
      print("DEALER WINS, YOU LOSE")
      exit()