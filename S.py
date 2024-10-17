#This code will make you kill yourself

import random
import math

ans1 = input("Welcome to a game. Accept?\n")
if ans1 == "yes" or ans1 == "okay" or ans1 == "ok":
    print("You will continue")
    wrong1 = input("Enter a word: ")
    if wrong1 == "3.14":
        print("You will continue")
        wrong2 = input("Enter the outcome: ")
        while wrong2 != "I win?": #Judah wrote this, I copied it on other parts of the project
            wrong2= input("Enter the outcome: ")
        if wrong2 == "I win?":
            print("Wrong! You lose! Now try again properly this time.")
    if wrong1 != "3.14" and wrong1 != "pie" and wrong1 != "Pie":
        print(random.choice(["WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "WHY DID YOU PUT IN A WORD!?!?! PIE!!!!!!", "The answer is 3.14"]))
    if wrong1 == "pie" or wrong1 == "Pie":
        print(random.choice(["The number, idiot", "The number, idiot", "The number, idiot", "The number, idiot", "stupid", "That's a food, not a number", "Not the damn food!", "...", "Delicious, but wrong"]))
elif ans1 == "Accept" or ans1 == "accept":
    print("You will continue")
    right1 = random.randint(1, 10)
    right2 = int(input("A number between 1 and 10 will appear. Guess what it is: "))
    print(right1)
    if right2 == right1:
        print("You will continue")
        right3 = random.randint(1, 100)
        right4 = int(input("A number between 1 and 100 will appear. Guess what it is: "))
        print(right3)
        if right4 == right3:
            print("Correct! You lose! Now try again properly this time.")
        else:
            print("Wrong! You lose! Now try again properly this time.")
    else:
        print("Wrong! You lose! Now try again properly this time.")
elif ans1 == "why":
    print("YOU WIN!!!!!!")
elif ans1 == "3.14":
    print("Ha")
elif ans1 == "I wanna do math" or ans1 == "math":
    mat1 = input("Really? ")
    if mat1 == "math":
        print("What is the square root of 5 + 9^2?")
        sqrt1 = int(input())
        if sqrt1 == 86:
            print("Correct! You lose! Now try again properly this time.")
    elif mat1 == "yes":
        print("no")
    elif mat1 == "no":
        num1 = int(input("Enter a Number: "))
        num2 = int(input("Enter a number: "))
        num3 = random.randint(1, 100)
        print("I will squareroot these two numbers then add them")
        innt = float(input("Guess the answer: \n"))
        num4 = (math.sqrt(num1) + math.sqrt(num2))
        if innt == num4:
            print("You thought it was", str(num4) + ", but it was actually", str(num3) + ("!"))
            print("...")
            print(num3, "was not the actual answer.\nOh well...")
            input()
            while num3 != 100:
                print(num3)
                num3 += 1
            print(100)
elif ans1 == "name":
    name1 = input("What is your name?\n")
    if name1 == "Judah":
        print("Have fun...")
    elif name1 == "cooper" or name1 == "Cooper":
        print("Do your coding you loser")
    elif name1 == "ash" or name1 == "Ash" or name1 == "Ashley" or name1 == "ashley":
        print("Have fun grading whatever this is...")
        x = 0
        while x != 100:
            print(random.choice(["Imagine this is code", "This is totally code", "Code", "01000011 01101111 01100100 01100101", "01010110 01100101 01110010 01111001 00100000 01101100 01101111 01101110 01100111 00100000 01100011 01101111 01100100 01100101", ""]))
            x += 1
    elif name1 == "Skye" or name1 == "skye":
        print("The best name, no bias at all")
    else:
        print(name1 + "\nHave fun!")
elif ans1 == "number game":
    while ans1 == "number game":
        right1 = random.randint(1, 10)
        right2 = (input("A number between 1 and 10 will appear. Guess what it is: "))
        print(right1)
        if right2 == right1:
            print("Good Job!")
elif ans1 == "key":
    print("yes, okay, ok\n\t3.14, pie, Pie\n\t\tI win?\nAccept, accept\nwhy\n3.14\nI wanna do math, math\n\tmath\n\t\t86\n\tyes\n\tno")
    print("name\n\tJudah\n\tcooper, Cooper\n\tash, Ash, Ashley, ashley\nnumber game\npie, Pie\nelse: nothing")
elif ans1 == "pie" or ans1 == "Pie":
    print("Got ahead of yourself, but it's not an answer")
else:
    rannum = random.randint(1, 10)
    if rannum == 1:
        print("You know what, I give up")
    if rannum == 2:
        input("Why are you like this\n")
        print("Just restart")
    if rannum == 3:
        print("no")
    if rannum == 4:
        input("...\n")
        print("leave")
    if rannum in range(5, 11): #Mr. Harrison wrote this
        no1 = input("Fine, here's a question.\nWhat is the reason for your pitful existance?\n")
        while no1 != "nothing" and no1 != "Nothing":
            no1 = input("What is the reason for your pitful existance?\n")
        if no1 == "nothing" or no1 == "Nothing":
            print(random.choice(["Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Correct! You loser! Now try again properly this time.", "Type in \"key\" next time"]))