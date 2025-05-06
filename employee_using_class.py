#define employee as a class
class Employee:
     # Initialize the Employee object with first name, last name, position, and salary
    def __init__(self,first_name,last_name,position,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary
    #this function shows the details of employees
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
    #this function is used for raising a salary of employee
    def give_raise(self,amount):
        self.salary += amount
        print(f"New Salary: {self.salary}")
    #this function is used for changing new position of employee
    def change_position(self, new_position):
        self.position = new_position
        print(f"New Position: {self.position}")
    #this function compute the annual salary of employee
    def get_annual_salary(self):
        return self.salary * 12
# Create Employee object with initial details   
Employee1 = Employee("John","Doe","Software Engineer",5000) 
Employee2 = Employee("John","smith","computer Engineer",6000)
Employee3 = Employee("John","paul","information technology",7000)

#showing employee1 details
print("Employee 1 Details:")
Employee1.display_info()
print("\nGiving raise to Employee 1")
#giving a raise to employees salary and show the updated salary
Employee1.give_raise(1000)
print("\nChanging position of Employee 1")
#giving a new position to employee and show the updated position
Employee1.change_position("Senior Software Engineer")
#showing tha annual salary 
print("\nAnnual Salary of Employee 1:")
print(Employee1.get_annual_salary())

#showing employee2 details
print("\nEmployee 2 Details:")
Employee2.display_info()
print("\nGiving raise to Employee 2")
#giving a raise to employees salary and show the updated salary
Employee2.give_raise(1500)
print("\nChanging position of Employee 2")
#giving a new position to employee and show the updated position
Employee2.change_position("Senior Software Engineer")
#showing tha annual salary 
print("\nAnnual Salary of Employee 2:")
print(Employee2.get_annual_salary())

#showing employee3 details
print("\nEmployee 3 Details:")
Employee3.display_info()
#giving a raise to employees salary and show the updated salary
print("\nGiving raise to Employee 3")
Employee3.give_raise(2000)
#giving a new position to employee and show the updated position
print("\nChanging position of Employee 3")
Employee3.change_position("Senior Software Engineer")
#showing tha annual salary 
print("\nAnnual Salary of Employee 3:")
print(Employee3.get_annual_salary())







