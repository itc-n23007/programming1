nisinsuu = ""
x = 23
while x != 0:
    x, y = divmod(x, 2)
    if y == 0:
        nisinsuu += "0"
    else:
        nisinsuu += "1"
print(nisinsuu[::-1])
