class Parent1:
    pass

class Parent2:
    pass

class child(Parent1 , Parent2):
    pass

class Father:

    def driving(self):
        print("Father has the skills to drive")

class Mother:

    def cooking(self):
        print("Mother has the skills to cook")

class Child(Father , Mother):

    def Bothskills(self):
        print("chinld has the skills to study")
        print("child has both skills of driving and cooking")

c = Child()
c.driving()
c.cooking()
c.Bothskills()
