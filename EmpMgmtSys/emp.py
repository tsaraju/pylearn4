class Employee:
    def __init__(self, eid, ename, department, salary, designation):
        self.eid = eid
        self.ename = ename
        self.department = department
        self.salary = salary
        self.designation = designation

    def  display_empinfo(self):
        print("Employee Information: ")
        print(f"Employee ID: {self.eid}")
        print(f"Employee Name: {self.ename}")
        print(f"Employee Department: {self.department}")
        print(f"Employee Salary: {self.salary}")
        print(f"Employee Designation: {self.designation}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary: {self.salary}")

    def calculate_annual_salary(self):
        print(f"Annual salary: {self.salary * 12}")

e1 = Employee(1, "Raju", "IT", 30000, "Developer")
e1.display_empinfo()
e1.update_salary(35000)
e1.calculate_annual_salary()

print()

e2 = Employee(2, "Ramu", "IT", 40000, "Sr. Developer")
e2.display_empinfo()
e2.update_salary(60000)
e2.calculate_annual_salary()

print()

e3 = Employee(3, "Rani", "IT", 35000, "Devops Engineer")
e3.display_empinfo()
e3.update_salary(45000)
e3.calculate_annual_salary()

print()

e4 = Employee(4, "Satish", "IT", 50000, "Manager")
e4.display_empinfo()
e4.update_salary(65000)
e4.calculate_annual_salary()

print()

e5 = Employee(5, "Srinu", "IT", 25000, "Test Engineer")
e5.display_empinfo()
e5.update_salary(35000)
e5.calculate_annual_salary()

print()
