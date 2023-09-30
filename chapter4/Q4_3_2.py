def number(*args):
    result = []
    for i in args:
        result.append(i * i)
    return result


suji = [1, 2, 3, 4]
number(*suji)
