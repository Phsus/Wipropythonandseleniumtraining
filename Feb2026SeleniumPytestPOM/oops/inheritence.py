class Employee:
    def __init__(self,name,empid):
        self.name = name
        self.empid = empid

    def empdetails(self):
        print(self.name,self.empid)



class Manager(Employee):

    def approve_leave(self):
        print("leave approved")


m = Manager("john" , "7878")
m.empdetails()
m.approve_leave()
