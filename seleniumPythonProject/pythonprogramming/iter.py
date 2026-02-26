a = [10,20,30,40,50]

iterator = iter(a)


print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

s = "hello"

iterator = iter(s)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


d = {'a':1,'b':2,'c':3}
for key, value in d.item():
    print(key, "-" , value)

def get_input():
    return input("enter value: ")

for value in iter (get_input , "quit"):
    print ("you entered:" , value)

print("Loop ended")