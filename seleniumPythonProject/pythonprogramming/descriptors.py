#descriptors - control the accesss of the object attributes
#_get_()
#_set_()
#_delete()

class Desc:
    def __get__(self,instance,owner):
        print("getting the value")
        return 10

class Test:
    x = Desc();

 t = Test();
print(t.x)

Class mydesc:
    def __get__(self,instance,owner):
        return instance._value

    def __set__(self,instance,value):
        print("setting the value")
        instance._value = value

    def __delete__(self, instance):
        print("delete the name")


class Test:
    x = mydesc()

    p = Person()
    p.name =" harsha"
    del p.name

t = Test()
t.x = 100
print(t.x)