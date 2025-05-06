class Employee:
    def __init__(self,first_name,last_name,position,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
    def give_raise(self,amount):
        self.salary += amount
        print(f"New Salary: {self.salary}")
    def change_position(self, new_position):
        self.position = new_position
        print(f"New Position: {self.position}")
    def get_annual_salary(self):
        return self.salary * 12
    
Employee1 = Employee("John","Doe","Software Engineer",5000) 
Employee2 = Employee("John","smith","computer Engineer",6000)
Employee3 = Employee("John","paul","information technology",7000)

print("Employee 1 Details:")
Employee1.display_info()
print("\nGiving raise to Employee 1")
Employee1.give_raise(1000)
print("\nChanging position of Employee 1")
Employee1.change_position("Senior Software Engineer")
print("\nAnnual Salary of Employee 1:")
print(Employee1.get_annual_salary())

print("\nEmployee 2 Details:")
Employee2.display_info()
print("\nGiving raise to Employee 2")
Employee2.give_raise(1500)
print("\nChanging position of Employee 2")
Employee2.change_position("Senior Software Engineer")
print("\nAnnual Salary of Employee 2:")
print(Employee2.get_annual_salary())

print("\nEmployee 3 Details:")
Employee3.display_info()
print("\nGiving raise to Employee 3")
Employee3.give_raise(2000)
print("\nChanging position of Employee 3")
Employee3.change_position("Senior Software Engineer")
print("\nAnnual Salary of Employee 3:")
print(Employee3.get_annual_salary())







