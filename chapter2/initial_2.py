import random

befor = 0
ini_list = [chr(i) for i in range(97, 97 + 26)]
while True:
    x = random.choice(ini_list)
    if x == "a":
        befor += 1
    elif befor == 1 and x == "o":
        print("END")
        break
    elif befor == 1 and x != "o":
        befor -= 1
    print(x)
