# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Employee inherits from Person
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # Call Person's constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")


# Manager inherits from both Person and Employee
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Call Employee's constructor (which also calls Person's)
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager_info(self):
        self.display_employee_info()
        print(f"Department: {self.department}")

    def approve_leave(self, employee_name):
        print(f"Manager {self.name} approved leave for {employee_name}.")


# Example usage
# Person object
person1 = Person("Ram", 30)
person1.display_person_info()

print("\n--- Employee ---")
# Employee object
employee1 = Employee("Sham", 28, "E123", 50000)
employee1.display_employee_info()

print("\n--- Manager ---")
# Manager object
manager1 = Manager("Raj", 40, "M456", 80000, "IT")
manager1.display_manager_info()
manager1.approve_leave("Sham")
