#imports
import random

#main
Dice = random.randint(1,6)
#print(Dice)


#Roll art

on = ("1\n _____\n|     |\n|  o  |\n|     |\n _____")
tw = ("2\n _____\n|o    |\n|     |\n|    o|\n _____")
th = ("3\n _____\n|o    |\n|  o  |\n|    o|\n _____")
fo = ("4\n _____\n|o   o|\n|     |\n|o   o|\n _____")
fi = ("5\n _____\n|o   o|\n|  o  |\n|o   o|\n _____")
si = ("6\n _____\n|o   o|\n|o   o|\n|o   o|\n _____")

Roll = random.choice([on, tw, th, fo, fi, si])
#print(Roll)

karma = 0

#Dubious Goober
head = random.choice(["(-3-)", "{v v}", "|'-'|", "\\^o^/", "[+uo]", "(ToT)", "{+x+}", "|;m;|", "\\6w6/", "[#v#]"])
body = random.choice(["+(_)+", "/{_}\\", "-|_|-", "</_\\>", "9[_]\\", "^(_)^", "v{_}v", "T|_|T", "l/_\\l", "o[_]o"])
legs = random.choice(["_| |_"," / \\", " \\ /", "_( )_", " ! !", " d b", " V V "])
print(head)
print(body)
print(legs)
print("Run the program until you get the character you want.")
input("\nAfter that press enter, or click a bunch of keys it don't matter.")
print("\n""\n")
#Rebos Lock (9 characters each)
RebosHead = (head)
RebosBody = (body)
RebosLegs = (legs)

print("            "+RebosHead+"\n            "+RebosBody+"\n            "+RebosLegs)
print("\nThis is your REBOS, you will be it's guide")

#Tutorial
print("\nYou will decide what to do with numbers between 1 and 6.")
numtorial = input("\nPlease enter a number between 1 and 6: ")
while not (numtorial == "1" or numtorial =="2" or numtorial =="3" or numtorial =="4" or numtorial =="5" or numtorial =="6"):
  numtorial = input("Try again, please enter a number between 1 and 6: ")
if numtorial == "1" or numtorial =="2" or numtorial =="3" or numtorial =="4" or numtorial =="5" or numtorial =="6":
 
  print("Okay, you understand, now I'll tell you about rolling.")
  rtest = input("Input the word \"roll\" to roll your dice. ")
while not rtest == "roll":
  rtest = input("Try again, input the word \"roll\" to roll your dice. ")
if rtest == "roll":
  print(Roll)

print("\nAre you ready to help REBOS?")
start = input("\"yes\"/\"no\": ")
while not start == "yes":
  start = input("I'll let you take your time, \"yes\"/\"no\": ")
if start == "yes":
  print("\nOkay, let's get started.")

print("\n\n REBOS has woken up, huge trees tower over THEIR head. REBOS is hungry, 3 objects are nearby that could help.")
print("1) decaying sword \n2) sharp stone \n3) crooked stick")

#First choice
#only decaying sword (1) has compete second decisions

print("what do you choose? Remember, you can also roll to let fate decide.")
first = input()
while first != ("roll") and (first != "1") and (first != "2") and (first != "3"):
  first = input("That is not an option. ")
if first == "roll":
  first = random.choice([on, tw, th,])
  print(first)


if first == "1" or first == on:
  print("REBOS pick up the decaying sword. It was laying by a skeletal figure, it seems that it was exposed to the elements for a long time.\n")
  decay_top = ("!")
  decay_han = ("+")
  print(head + decay_top)
  print(body + decay_han)
  print(legs)
  hand = ("decaying sword")
  karma = (karma + 1)
elif first == "2" or first == tw:
  print("REBOS pick up the sharp stone. It can peirce things easily, but it's small.\n")
  sharp_roc = ("o")
  print(head)
  print(body + sharp_roc)
  print(legs)
  hand = ("sharp stone")
  karma = (karma + 2)
elif first == "3" or first == th:
  print("REBOS pick up the crooked stick. It's blunt, andt here is a eerie feeling coming off of it.\n")
  crook_top = ("0")
  crook_han = ("l")
  print(head + crook_top)
  print(body + crook_han)
  print(legs)
  hand = ("crooked stick")
  karma = (karma + 3)
#Second choice (Sleep will end the run),(Crooked + Pig will end the run), (Sharp + Pig will end the run) (decay + leave will end the run))

print("REBOS now has a" , hand , "in hand. What should THEY do now?")
print("1) Get Sleep  \n2) Hunt a Pig \n3) Leave the Forest")
print("Rember, THEY are hungry this decision will be impactful.")
second = input()
while second != ("roll") and (second != "1") and (second != "2") and (second != "3"):
  second = input("That is not an option. ")
if second == "roll":
  second = random.choice([on, tw, th,])
  print(second)
elif second == "1" or second == on:
  karma = (karma + 1)
  if karma == 2:
    print("REBOS sleeps in the middle of the woods. \nThe fallen soldier, the original owner of the sword reanimates and claim's his blade.")
    print("\n\n" + head)
    print("He kills REBOS in the middle of the night")
    print("GAME OVER")
elif second == "2" or second == tw and karma == 1:
  karma = (karma + 2)
  if karma == 3:
    print("REBOS hunts for a pig. \nThe blade shatters on contact but the wound kills it.")
    print("\n\n" + head + "🐷")
    print(body + decay_han)
    print(legs)
    print("The meat is raw but it is filling. You have kept REBOS alive, at least for now.")
    print("VICTORY!")
elif second == "3" or second == thr and karma == 1:
  karma = (karma + 3)
  print("REBOS leaves the forest. \nAs THEY step out a rough skinned monster jumps out at REBOS from behind a tree.")
  print("\n\n" "         👹")
  print("      " + decay_han + body )
  print(head + "  " + legs)
  print("REBOS attempts to swing at the creature, but the sword shattered on contact no wounds were dealt.")
  print("GAME OVER")