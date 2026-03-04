print (len("python"))
print (len([1,2,3]))
print (len({1,2,3}))

class calculator:
    def add(self , a,b= 0, c=0):
        return a+b+c

c = calculator()
print(c.add(5))
print(c.add(5,10.5))
print(c.add(5, 10,15))


class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def sound(self):
        print("dog barks")


a =Dog()
a.sound()
