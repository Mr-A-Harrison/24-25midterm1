import random
card1 = random.randint(1,10)
card2 = random.randint(1,10)
print("you got a " + str(card1) + " and a " + str(card2) + ".")
dealer = random.randint(1,10)
print("dealer got a " + str(dealer))
hidden = random.randint(1,10)
dealertotal = dealer + hidden
total = card1 + card2
if card1 + card2 > 21:
    print("You busted")
elif card1 + card2 == 21:
    print("You win!")
else:
    print("You currently have " + str(total))
turn1 = input("Hit? Y/N ")
new1 = random.randint(1,10)
new2 = random.randint(1,10)
new3 = random.randint(1,10)
if turn1 =="Y":
    print("\nYou got a " + str(new1))
    total = total + new1
    print("You now have " + str(total))
    if total > 21:
        print("You busted")
    elif total == 21:
        print("You win!")
if turn1 == "N":
    print("Dealer has a " + str(dealer) + " and a " + str(hidden))
    print("This equals " + str(dealertotal))
else:
    turn2 = input("Hit again? Y/N ")
    if turn2 == "Y":
        print("\n You got a " + str(new2))
        total = total + new2
        print("You now have " + str(total))
    elif total > 21:
        print("You busted")
    elif total == 21:
        print("You win!")
    if turn2 == "N":
        print("Dealer has a " + str(dealer) + " and a " + str(hidden))
        print("This equals " + str(dealertotal))
    turn3 = input("Hit again? Y/N ")
    if turn3 == "Y":
        print("\n You got a " + str(new3))
        total = total + new3
        print("You now have " + str(total))
    elif total > 21:
        print("You busted")
    elif total == 21:
        print("You win!")
    if turn3 == "N" or turn2 == "N" or turn1 == "N":
        print("Dealer has a " + str(dealer) + " and a " + str(hidden))
        print("This equals " + str(dealertotal))
    if dealertotal >= 17:
        print("\n=== FINAL SCORE ===")
        print("Your score: " + str(total))
        print("Dealer score: " + str(dealertotal))
    if dealertotal <= 16:
        print("Dealer hits")
        dealernew1 = random.randint(1,10)
        print("Dealer now has " + str(dealertotal + dealernew1))
        dealertotal = dealertotal + dealernew1
    if dealertotal >= 21:
        print("\n=== FINAL SCORE ===")
        print("Your score: " + str(total))
        print("Dealer score: " + str(dealertotal))
    if dealertotal <= 16:
        print("Dealer hits")
        dealernew2 = random.randint(1,10)
        print("Dealer now has " + str(dealertotal + dealernew2))
        dealertotal = dealertotal + dealernew2
    if dealertotal <= 16:
        print("Dealer hits")
        dealernew3 = random.randint(1,10)
        print("Dealer now has " + str(dealertotal + dealernew3))
        dealertotal = dealertotal + dealernew3
    elif dealertotal >= 17:
        print("\n=== FINAL SCORE ===")
        print("Your score: " + str(total))
        print("Dealer score: " + str(dealertotal))
        print("\n=== FINAL SCORE ===")
        print("Your score: " + str(total))
        print("Dealer score: " + str(dealertotal))
    if dealertotal > total:
        print("You lose :(")