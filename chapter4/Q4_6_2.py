import random


def generate_students_data(num_students=10):
    students_data = []
    for i in range(num_students):
        name = "n" + str(random.randint(10, 50))
        height = random.randint(150, 190)
        weight = random.randint(50, 80)
        students_data.append((name, height, weight))
        if i == 0:
            print("i,name,height,weight")
        if 0 <= i <= 9:
            print(i, name, height, weight)
        else:
            print(i, name, height, weight)
            print("FINISH")
        return students_data


students_data = generate_students_data(10)
