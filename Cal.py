import random

inp1 = input("Hello, in this game you will be guessing a number between 1 and 10 (type \"start\" to start, or type \"tutorial\" to learn how to play): ")

while inp1 != "start" and inp1 != "tutorial":
    inp1 = input("You have to write it exactly as it is written in the quotes, so try again: ")

if inp1 == "start":
    print("Im thinking of a number between 1 and 10")
    y = int(input("\nEnter a number between one and ten: "))
    x = random.randint(1, 10)
    while y != x:
        if y < x:
            print("The number was higher")
            print("Try again?")
        if y > x:
            print("The number was lower")
            print("Try again?")
        if y > 10 or y <= 0:
            print("I said between 1 and 10... you lose")
        y = int(input("\nEnter a number between one and ten: "))
        x = random.randint(1, 10)
    if y == x:
        print("You got it!")
        print("Good game!")
if inp1 == "tutorial":
    print("In this game, you will be guessing a number between 1 and 10.")
    print("You have unlimited tries to guess the number, but the goal is to get the highest amount of tries, as I have deduced that to be more diffcult than getting the least amount of tries.")
    inp1 = input("If you want to play, type \"start\": ")
    while inp1 != "start":
        inp1 = input("You have to write it exactly as it is written in the quotes, so try again: ")
    if inp1 == "start":
        print("Im thinking of a number between 1 and 10")
        y = int(input("\nEnter a number between one and ten: "))
        x = random.randint(1, 10)
        while y != x:
            if y < x:
                print("The number was higher")
                print("Try again?")
            if y > x:
                print("The number was lower")
                print("Try again?")
            if y > 10 or y <= 0:
                print("I said between 1 and 10... you lose")
            y = int(input("\nEnter a number between one and ten: "))
            x = random.randint(1, 10)
        if y == x:
            print("You got it!")
            print("Good game!")
    