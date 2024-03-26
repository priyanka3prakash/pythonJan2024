"""
Purpose: Importance of Class Variables
    variables defined at the class level

"""

class Employee:
    """ Commmon base class for employees"""
    COMAPNY = 'MY COMPANY'
    emp_count = 0  # class variable
    emp_id = 0  # class variable
    
    
    def __init__(self, name, salary) -> None:
        """
        This is a constructor method
        :param name:
        :param salary:
        """
        print("\n New Employee joined")
        self.employee_name = name
        self.salary = salary
        Employee.emp_count += 1

    def total_employees_count(self):
        """
        This method is used to display the count of employees
        :return:
        """
        print(f"Total Employees count(before): {Employee.emp_count}")

        # self.emp_count += 1
        # print(f"self.emp_count               : {self.emp_count}")

        # print(f"Total Employees count(after): {Employee.emp_count}")

    def __del__(self) -> None:
        print(f'Employee is leaving...')
        Employee.emp_count -= 1

# print(vars(Employee))
# print()


# instantiation
# e1 = Employee()
# print(e1)
# print(vars(e1))
# print()


# print(dir(Employee))
# print(dir(e1))
        

# instantiation
e1 = Employee('Rohan', 234324)
print(vars(e1))

print(f"{e1.emp_count       =}")
print(f"{Employee.emp_count =}")
print()

e1.total_employees_count()

# Deletion of Instance
del e1

print('Last statement in the script')


emp2 = Employee('Mohana', 1231232)
emp2.total_employees_count()