import random

ini_list = [chr(i) for i in range(97, 97 + 26)]
while True:
    x = random.choice(ini_list)
    print(x)
    if x == "a":
        print("END")
        break
