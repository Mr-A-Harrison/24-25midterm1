import random
import math
import sympy

# I learned the [chr()], [ord()], sympy.isprime(), ''.join() functions from the site "Geeks for Geeks" ; I learned the list.append()/list=[], for loops, and len() from Ashley Harrison. The math is from https://www.onebigfluke.com/2013/11/public-key-crypto-math-explained.html


password = input("Enter Password: ")
# password = ""
while password != "" and password != "Default" and password != "default" and password != "\\\\dev_info" and password != "decrypt":
  print("\nThat is Incorrect\nPlease Try Again\n")
  password = input("Enter Password: ")

if password == "Default" or password == "default" or password == "" or password == "\\\\dev_info" or password == "decrypt":
  if password == "\\\\dev_info":
    m = input("\nEnter messege : ")

    p = sympy.randprime(1, 1_000)
    q = sympy.randprime(1, 1_000)
    NumN = p * q

    while p==q or q==p:
        p = sympy.randprime(1, 1_000)
        q = sympy.randprime(1, 1_000)
    print("\nPrivate Key: " + str(p) + " & " + str(q))
    NumN = p * q
    print("\nPublic Key : " + str(NumN))
    mL = [ord(c) for c in m]
    print(mL)
    mLr = random.choice(mL)
    num12 = p
    gcd = q
    ETFN = (p - 1) * (q - 1)
    print("\nEuler's Totient Function : " + str(ETFN) + "\n\n")
    listC = []
    mDlist = []
    ranlist = []

    for mLr in mL:
      print("mLr: " + str(mLr))
      rannum = sympy.randprime(1, 1_000)
      print("Rannum: " + str(rannum) +"\n")
      d = ((rannum**(ETFN - 1)) % ETFN)
      c = (mLr**rannum) % NumN
      mD = (c**d) % NumN
      while rannum == num12 or rannum == gcd or mD != mLr or mD == c:
        print("BEGIN")
        rannum = sympy.randprime(1, 1_000)
        d = ((rannum**(ETFN - 1)) % ETFN)
        c = (mLr**rannum) % NumN
        mD = (c**d) % NumN
        print(str(rannum))
        print("END\n")
        #BEGIN/x/END sybolizes the beginning and end of a loop; and mLr:x/Rannum:x shows that a new character is beggining the encryption proccess.
      listC.append (c)
      ranlist.append(rannum)
      mDlist.append (mD)
    FDml = [chr(mD) for mD in mDlist]
    FDm = ''.join(FDml)
    FCl = int(''.join([str(c) for c in listC]))
    print("\n")
    print("Random Prime: " + str(rannum))
    print("Modular Multiplicative Inverse : " + str(d))
    print("ranlist: " + str(ranlist))
    print(" ")
    print(" ")
    print("Public key (n: " + str(NumN) + "; e: " + str(rannum) + ")")
    print("private key (n: " + str(NumN) + "; d: " + str(d) + "; " + "p/q: " + str(p) + " & " + str(q) + ")")
    print(" ")
    print("Encrypted Messege : " + str(FCl))
    print("listC: " + str(listC))

  password = input("\nEnter Password: ")



# Keep in mind, the code is the same as the dev info, but the nitty gritty information isn't being shown, so it may take a while before showing any feedback.
  if password == "Default" or password == "default" or password == "":

    m = input("\nEnter messege : ")

    p = sympy.randprime(1, 1_000)
    q = sympy.randprime(1, 1_000)
    NumN = p * q

    while p==q or q==p:
        p = sympy.randprime(1, 1_000)
        q = sympy.randprime(1, 1_000)
    NumN = p * q
    mL = [ord(c) for c in m]
    mLr = random.choice(mL)
    num12 = p
    gcd = q
    ETFN = (p - 1) * (q - 1)
    listC = []
    mDlist = []
    ranlist = []

    for mLr in mL:
      rannum = sympy.randprime(1, 1_000)
      d = ((rannum**(ETFN - 1)) % ETFN)
      c = (mLr**rannum) % NumN
      mD = (c**d) % NumN
      while rannum == num12 or rannum == gcd or mD != mLr or mD == c:
        rannum = sympy.randprime(1, 1_000)
        d = ((rannum**(ETFN - 1)) % ETFN)
        c = (mLr**rannum) % NumN
        mD = (c**d) % NumN
      listC.append (c)
      mDlist.append (mD)
      ranlist.append(rannum)
    FDml = [chr(mD) for mD in mDlist]
    FDm = ''.join(FDml)
    FCl = int(''.join([str(c) for c in listC]))
    print("\n\nEncrypted Messege : " + str(FCl))
    print("\nlsitC: " + str(listC))

    password = input("\nEnter Password: ")



  if password == "Decrypt" or password == "decrypt":
    m = listC
    print("\n\nEncrypted Mesage: " + str(''.join([str(c) for c in listC])))
    print("\nPrivate Keys : " + str(p) + " & " + str(q))
    NumN = p * q
    ETFN = (p - 1) * (q - 1) 
    dlist = []
    print("ranlist: " + str(ranlist))
    for rannum in ranlist:
        d = ((rannum**(ETFN - 1)) % ETFN)
        print(rannum)
        dlist.append(d)
    print("dlist: " + str(dlist))
    mDlist = []
    for i in range(len(m)):
        mD = (m[i]**dlist[i]) % NumN
        mDlist.append(mD)
    print("mDlist: " + str(mDlist))
    mDF = ''.join([chr(mD) for mD in mDlist])
    print("Decrypted Messege : " + str(mDF))






