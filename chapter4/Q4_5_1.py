function = [sum, min, max]
num_list = range(1, 11)
for func in function:
    print("Function:{},Result:{}".format(func.__name__, func(num_list)))
