print("Lets do some math!\n")
sum1 = int(input("Whats 2 + 2: "))
if sum1 == 4:
  print("Correct!")
while sum1 != 4:
  print("Wrong, Try again stupid")
  sum1 = int(input("\nWhats 2 + 2: "))

print("\nAlright, you passed question 1. Now lets do some subtraction!\n")
sum2 = int(input("Whats 2 - 2: "))
if sum2 == 0:
  print("Correct!")
while sum2 != 0:
  print("Wrong, Try again stupid")
  sum2 = int(input("\nWhats 2 - 2: "))

print("\nAlright that was question 2. Now lets do some multiplication!\n")
product1 = int(input("Whats 2 * 2: "))
if product1 == 4:
  print("Correct!")
while product1 != 4:
  print("Wrong, Try again stupid\n")
  product1 = int(input("Whats 2 * 2: "))

print("\nAlright that was question 3. Now last is division!\n")
product2 = int(input("Whats 2 / 2: "))
if product2 == 1:
  print("Correct!")
while product2 != 1:
  print("Wrong, Try again stupid\n")
  product2 = int(input("Whats 2 / 2: "))
print("\nYou did it! You passed the test!\n")
bonus = int(input("Bonus question, Whats 2 * ♾️: "))
print("\nWrong you must be punished\n")