def sum_list(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

my_list = [8, 2, 3, 0, 7]
print(sum_list(my_list))

def max_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(max_of_three(20, 35, 19))