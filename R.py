name=input("What's your name? ")
print("Lovely!")
Jewelry=input("What piece of jewelry do you like to wear the best? ")
print(Jewelry + " are trending right now, very chic! ")
gs=input("Do you prefer gold or silver? ")
if gs== "gold":
    print("gold is beautiful and it's like the sun! It's more of a warm tone too. ")
elif gs == "silver":
        print("silver is beautiful and it's like the moon! It's more of a cool tone too. ")
else: 
    print("me too ")
shoe=input("What's your favorite pair of shoes right now? ")
import random
x=random.randint(1,3)
if x == 1: 
    print("Those are my favorites as well! ")
elif x==2:
        print("I love those! ")
else:
    print("That's so stylish! ")
color=input("What color do you like wearing best? " )
print("I can tell that color looks amazing on you! ")

clothing=input("What piece of clothing do you like to wear most? ")
if clothing== "pants":
    print("You always need " + clothing + " to finish your fit! ")
elif clothing == "t-shirt": 
    print("A good " + clothing + " is always a must")
else:
    print(clothing + " is also what I like to wear the most! ")

bag= input("Do you like to wear a bag with your outfit? ")
if bag == "yes":
    print("Same! A good bag is always needed and very chic these days. ")
elif bag == "no":
    print("Yeah, sometimes bags aren't needed. ")
else:
    print("same. ")

print("Let's take a break from all the questions, let's play a game! ")
num1=int(input("Choose a number between 1 and 10: "))
if num1 >=5:
    print("Nice!")
elif num1<=4:
    print("Fabulous!")
else:
    print("not a valid number")
x=int(input("Multiply your number by 2: "))
if x== num1*2:
    print("Correct! " + str(x ) + " is the answer!")
else: 
    print("not correct, it should be " + str(num1*2) + " but that's okay!")
num2= int(input("Now guess my number between 1 and 10: "))
mynum= int(8)
if num2 == 8: 
    print("Correct, that was my number! ")
elif num2 !=8: 
    print("Not my number! My number is 8 ")
print("Now add my number to the number you got before, ")
num3=int(input("What is your new number? "))
if num3 ==(x+mynum):
    print("nice! ")
elif num3 != (x+mynum):
    print("That's not quite right, it should be " +(str(x+mynum)))

print("Now I have a new number, can you guess it? I'll give you a hint it's between 1 and 100. ")
n=int(18)
g=int(input("Guess my number: "))

while g != 18:
    if g > 18:
        print("my number is lower ")
        g=int(input("Guess my number: "))
    if g < 18:
        print("my number is higher ")
        g=int(input("Guess my number: "))


print("correct! that's my number, good job! ")

print("Hmmmm now let's see if you can do some basic math calculations... ")
num1=str(input("What is 2 times 4? "))
if num1 == str(2*4):
    print("correct")
elif num1 != str(2*4):
    print("incorrect, it's " + str(2*4))
num2=str(input("What is 4 times 6? "))
if num2 == str(4*6):
    print("correct")
elif num2 != str(4*6):
    print("incorrect, it's " + str(4*6))
num3=int(input("What is 9 divided by 3? "))
if num3 == (9/3):
    print("correct")
elif num3 != (9/3):
    print("incorrect, it's " + str(9/3) )


print( "Let's play one more game, these are fun! Let's play rock, paper, scissors. " )
rps= input("Enter rock, paper, or scissors: ")
if rps == "rock":
    print("paper, I beat you! ")
elif rps == "paper":
    print("scissors, I beat you! ")
elif rps == "scissors":
    print("rock, I beat you! ")

print("Good game, but I won! ")

rps2= input("Would you like to play again? ")
if rps2 == "no" :
    print("okay. ")
elif rps2 == "yes": 
    print("Yay!")
    rps= input("Enter rock, paper, or scissors: ")
    if rps == "rock":
        print("paper, I beat you! ")
    elif rps == "paper":
        print("scissors, I beat you! ")
    elif rps == "scissors":
        print("rock, I beat you! ")

    print("Good game, but I won again! ")
