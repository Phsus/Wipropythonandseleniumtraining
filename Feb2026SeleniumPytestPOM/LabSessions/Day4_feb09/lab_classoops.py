class Employee:

    emp_id = 0
    emp_name = ""
    emp_dept = ""

    

    def display_employee_details(self):
        print("Employee ID  :", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Department   :", self.emp_dept)



emp1 = Employee()

emp1.emp_id = 101
emp1.emp_name = "Rahul"
emp1.emp_dept = "IT"


emp1.display_employee_details()



emp2 = Employee()

emp2.emp_id = 102
emp2.emp_name = "Priya"
emp2.emp_dept = "HR"


emp2.display_employee_details()