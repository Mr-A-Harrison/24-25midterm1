print("Welcome to my christmas tree creator!\n")


print("     🟩")
print("    🟩🟩")
print("   🟩🟩🟩")
print("  🟩🟩🟩🟩")
print(" 🟩🟩🟩🟩🟩")
print("🟩🟩🟩🟩🟩🟩")
print("    🟫🟫")
print("    🟫🟫")
def treeColor(lightcolor):
  if lightcolor=="red":
    print("     🟥")
    print("    🟩🟩")
    print("   🟥🟩🟥")
    print("  🟩🟩🟩🟩")
    print(" 🟥🟩🟥🟩🟥")
    print("🟩🟩🟩🟩🟩🟩")
    print("    🟫🟫")
    print("    🟫🟫 ",end="")
  if lightcolor=="blue":
    print("     🟦")
    print("    🟩🟩")
    print("   🟦🟩🟦")
    print("  🟩🟩🟩🟩")
    print(" 🟦🟩🟦🟩🟦")
    print("🟩🟩🟩🟩🟩🟩")
    print("    🟫🟫")
    print("    🟫🟫 ",end="")
  if lightcolor=="white":
    print("     ⬜")
    print("    🟩🟩")
    print("   ⬜🟩⬜")
    print("  🟩🟩🟩🟩")
    print(" ⬜🟩⬜🟩⬜")
    print("🟩🟩🟩🟩🟩🟩")
    print("    🟫🟫")
    print("    🟫🟫 ",end="")
  if lightcolor=="black":
    print("     ⬛")
    print("    🟩🟩")
    print("   ⬛🟩⬛")
    print("  🟩🟩🟩🟩")
    print(" ⬛🟩⬛🟩⬛")
    print("🟩🟩🟩🟩🟩🟩")
    print("    🟫🟫")
    print("    🟫🟫 ",end="")
  if lightcolor=="mix":
    print("     🟥")
    print("    🟩🟩")
    print("   🟦🟩🟦")
    print("  🟩🟩🟩🟩")
    print(" ⬜🟩⬜🟩⬜")
    print("🟩🟩🟩🟩🟩🟩")
    print("    🟫🟫")
    print("    🟫🟫 ",end="")
#light selector
lights=input("Do you want lights (yes or no): ")
if lights=="yes":
  lightcolor=input("What color lights (red, blue, white, black, mix): ")
  treeColor(lightcolor)
  print("\nwhats lookin good cookin 😼😼😼")
  present=int(input("How many presents you want dawg? "))
  if present>10:
    print("You are a greedy lil poop")
    treeColor(lightcolor)
    print("🪨🪨🪨🪨🪨\nyou get coal you turd")
  else:
    presents = []
    while present >= 1:
      presentnum = "🎁"
      present = present - 1
      presents.append(presentnum)
    treeColor(lightcolor)
    print(presents)
    print("Those presents look horrible type like 13323223 so you get coal next time PLEASE")
  star=input("Do you want a star or a skull?: ")
  if star=="star":
    print("     🌟")
  if star=="skull":
    print("     ☠️")
    treeColor(lightcolor)
if lights=="no":
  print("you're boring")
