def printdata():
    print("hello world")

printdata()

def printdata(Name):
    print("hello", Name)

printdata("Tina")
printdata("Rita")

def sq(num):
    result = num * num
    return result

square = sq(3)
print('square',square)

def func_pass():
    pass

func_pass()

def cal(a,b):
    return a-b, a+b, a*b

add , sub , mul = cal(10 ,12)
print(add)
print(sub)
print(mul)

def areaofrect(len, width):
    return len * width

def areaofsq(side):
    return side*side

value = (areaofrect(4,8))
sq = (areaofsq(value))
print(sq)

def even(limit):
    for i in range(2, limit + 1 , 2):
        print(i)
    even(10)
    even(11)

def even(limit):
    if limit % 2 ==0:
        return "even"
    else:
        return "odd"

    print(even(10))
    print(even(11))

