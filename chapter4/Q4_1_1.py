a = 0
b = 1
while True:
    print(a, end=",")
    a, b = b, a + b
    if b > 15:
        break
