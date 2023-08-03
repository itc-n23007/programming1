list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
list2 = []
for i in list:
    if len(i) <= 6:
        list2.append(i)
print(list2)
