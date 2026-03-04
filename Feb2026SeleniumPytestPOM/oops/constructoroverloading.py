class Numbers:
    def __init__(self,*args):
        self.values = args

n = Numbers(10,20,30)
print(n.values)

m = Numbers(3,4)
print(m.values)

p = Numbers(3)
print(p.values)