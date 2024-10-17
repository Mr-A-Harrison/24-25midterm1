from colorama import Fore; import random #Learned colorama off of github
cards = [1,2,3,4,5,6,7,8,9,10,11]
player = []; dealer = []
def drawCard(person):
  card = random.randint(0,len(cards)-1)
  newcard = cards.pop(card)
  person.append(newcard)
def printCards(person):
  result = ""
  if person == dealer and sum(dealer) < 17 and sum(player) <= 21:
    for n in person[1:len(person)]:
      result += str(n) + ", "
  else:
    for n in person:
      result += str(n) + ", "
  return result[0:len(result)-2]
print("Welcome to" + Fore.RED, "Twenty" + Fore.RESET + "-" + Fore.BLACK + "one" + Fore.RESET + "!")
drawCard(dealer); drawCard(dealer)
if sum(dealer) > 17:
  print(Fore.RED + "\nDealer's cards: ?, " + printCards(dealer[1:len(dealer)]))
else:
  print(Fore.RED + "\nDealer's cards: ?, " + printCards(dealer))
print(Fore.RESET + "? + " + str(sum(dealer[1:len(dealer)])) + "/21")
drawCard(player); drawCard(player)
print(Fore.BLACK + "\nPlayer's cards:", printCards(player))
if sum(player) == 21:
  print(Fore.GREEN + str(sum(player)) + "/21")
else:
  print(Fore.RESET + str(sum(player)) + "/21")
hos = input(Fore.RED + "Hit " + Fore.RESET + "or " + Fore.BLACK + "Stay?\n" + Fore.RESET)
while hos == "Hit" or hos == "hit":
  print("You decided to " + Fore.RED + "hit" + Fore.RESET + "!")
  if sum(dealer) > 17:
    print(Fore.RED + "\nDealer's cards: ?, " + printCards(dealer[1:len(dealer)]))
  else:
    print(Fore.RED + "\nDealer's cards: ?, " + printCards(dealer))
  print(Fore.RESET + "?, " + str(sum(dealer[1:len(dealer)])) + "/21")
  drawCard(player)
  print(Fore.BLACK + "\nPlayer's cards:", printCards(player))
  if sum(player) > 21:
    print(Fore.RED + str(sum(player)) + "/21")
  if sum(player) < 21:
    print(Fore.RESET + str(sum(player)) + "/21")
  if sum(player) == 21:
    print(Fore.GREEN + str(sum(player)) + "/21")
  if sum(player) > 21:
    hos = "stay"
  else:
    hos = input(Fore.RED + "Hit " + Fore.RESET + "or " + Fore.BLACK + "Stay?\n" + Fore.RESET)
if hos == "Stay" or hos == "stay":
  if sum(player) > 21:
    print("You bust!")
  else:
    print("You decided to " + Fore.BLACK + "stay" + Fore.RESET + "!")
  if sum(player) > 21:
    print("\nThe game is over!")
    print(Fore.RED + "\nDealer's cards: ", printCards(dealer))
    print(Fore.RESET + str(sum(dealer)) + "/21")
    print(Fore.BLACK + "\nPlayer's cards:", printCards(player))
    print(Fore.RED + str(sum(player)) + "/21")
    print(Fore.RESET + "\nThe player busts! The dealer wins!")
  else:
    while sum(dealer) < 17 and sum(player) <= 21:
      drawCard(dealer)
      print(Fore.RED + "\nDealer's cards: ?,", printCards(dealer[1:len(dealer)]))
      print(Fore.RESET + "? + " + str(sum(dealer[1:len(dealer)])) + "/21")
      print(Fore.BLACK + "Player's cards:", printCards(player))
      if sum(player) == 21:
        print(Fore.GREEN + str(sum(player)) + "/21")
      else:
        print(Fore.RESET + str(sum(player)) + "/21")
    if sum(dealer) >= 17 and sum(dealer) <= 21:
      print("\nThe game is over!")
      print(Fore.RED + "\nDealer's cards:", printCards(dealer))
      if sum(dealer) == 21:
        print(Fore.GREEN + str(sum(dealer)) + "/21")
      else:  
        print(Fore.RESET + str(sum(dealer)) + "/21")
      print(Fore.BLACK + "\nPlayer's cards:", printCards(player))
      if sum(player) == 21:
        print(Fore.GREEN + str(sum(player)) + "/21")
      else:
        print(Fore.RESET + str(sum(player)) + "/21")
      if sum(player) <= 21:
        if sum(dealer) > sum(player):
          print("\nThe dealer wins!")
        if sum(dealer) == sum(player):
          print("\nBoth players push!")
        if sum(dealer) < sum(player):
          print("\nThe player wins!")
  if sum(dealer) > 21:
    print("\nThe game is over!")
    print(Fore.RED + "\nDealer's cards:", printCards(dealer))
    print(str(sum(dealer)) + "/21")
    print(Fore.BLACK + "\nPlayer's cards:", printCards(player))
    print(Fore.RESET + str(sum(player)) + "/21")
    print("\nThe dealer busts! The player wins!")