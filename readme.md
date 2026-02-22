[Assignment no.8.py](https://github.com/user-attachments/files/25465462/Assignment.no.8.py)[Assignment no.7.py](https://github.com/user-attachments/files/25465459/Assignment.no.7.py)[Assignment no.7.py](https://github.com/user-attachments/files/25465433/Assignment.no.7.py)[Assignment no.6.py](https://github.com/user-attachments/files/25465429/Assignment.no.6.py)[Assignment no.5.py](https://github.com/user-attachments/files/25465416/Assignment.no.5.py)[Assignment no. 4.py](https://github.com/user-attachments/files/25465399/Assignment.no.4.py)[Assignment no. 3.py](https://github.com/user-attachments/files/25465395/Assignment.no.3.py)Python programs:-
Assignment no 1
[Assignment no. 1.py](https://github.com/user-attachments/files/25465376/Assignment.no.1.py)
[Uploading Assignment #Creating the list 
phones=["iphone","onepluse","samsung","googlepixel"]
print(f"Original list :{phones}")

#Accessing the elements from list 
print(f"first element :{phones[0]}")
print(f"last element :{phones[-1]}")
print(f" 1 to 3 element :{phones[1:3]}")

#Insering the new element in the list 
phones.insert(2,"redmi")
print(f"After inserting element list :{phones}")

#Adding the element at last
phones.append("vivo")
print(f"After adding element list :{phones}")

#Removing the elements 
phones.remove("redmi")
print(f"After removing element list :{phones}")

#sorting the elements
phones.sort()
print(f"After sorting element list :{phones}")

#reverse list element 
phones.sort(reverse=True)
print(f"After reverse list element:{phones}")


Assignment no.2
[Assignment no. 2.py](https://github.com/user-attachments/files/25465389/Assignment.no.2.py)
#creating the set 
my_set_1={11,15,13,14}
my_set_2={12,16,14,18}
print(f"Set 1:{my_set_1}")
print(f"Set 2:{my_set_2}")

#Accessing the elements using for loop
for element in my_set_1:
    print(f" Is 12 in set 1:{12 in my_set_1}")

#Union of set 
union_set = my_set_1.union(my_set_2)
print(f"Union of set 1 and 2:{union_set}")

#Intersection of set
intersection_set = my_set_1.intersection(my_set_2)
print(f"intersection of set 1 and 2:{intersection_set}")

#Differnce of set 
difference_set_1_2 = my_set_1.difference(my_set_2)
difference_set_2_1 = my_set_2.difference(my_set_1)
print(f"Difference (set 1- set 2):{difference_set_1_2 }")
print(f"Difference (set 2- set 1):{difference_set_2_1 }")

Assignment no.3
[Assignment no. 3.py](https://github.com/user-attachments/files/25465397/Assignment.no.3.py)
#creating the tuple
phones=("iphone","onepluse","samsung","googlepixel")
print(f"Created tuple:{phones}")

#Accessing the elements from tuple
print(f"first element :{phones[0]}")
print(f"last element :{phones[-1]}")
print(f" 1 to 3 element :{phones[1:3]}")

#Nested tuple
mixed_tuple= ("cars",123,("BMW,BYD,Mercedes"))
print(f"Nested tuple:{mixed_tuple}")

#Accessing the tuple 
print(f"Nested tuple elements:{mixed_tuple[2]}")

#Accessing  the element form nested tuple
print(f"Nested tuple element:{mixed_tuple[2][5]}")

#Repeatation of tuple
phones=("iphone","onepluse","samsung","googlepixel")
repeated_tuple = phones *3
print(f"Nested tuple:{repeated_tuple}")

#Concatenation of tuple
more_phones = ("vivo","redmi")
combined_phone = phones + more_phones
print(f"concatenation of tuple:{combined_phone}")

Assignment no,4
[Assignment no. 4.py](https://github.com/user-attachments/files/25465411/Assignment.no.4.py)
#create the dictionary 
car = {'BMW':{'color':'White','year':'2020'},
       'Mercedes benz':{'color':'Red','year':'2022'},
       'Toyota':{'color':'Silver','year':'2024'}
       }
print(f"created dictionary:",car)

#Accessing the elements
BMW_details = car['BMW']
print(f"\n deatils of BMW ",BMW_details)

#updating the dictionary 
car['BMW'] = {'color':'golden','year':'2018'}
print(f"\n updated deatils of BMW ", car['BMW'])

#removing the elements from dictonary 
del car['Mercedes benz']
print(f"Dictionary after removing the mercedes benz",car)
      
#merging the dictonary 
new_car_add ={'BMW M3':{'color':'White','year':'2020'},
       'mercedes c class':{'color':'Red','year':'2022'}}
car.update(new_car_add)
print(f"dictonary after merging ",car)

Assignment no. 5
[Assignment no.5.py](https://github.com/user-attachments/files/25465418/Assignment.no.5.py)
#info of bankaccount
class bankaccount:
    def __init__(self, account_number,balance=0.0):
        self.account_number=account_number
        self.balance=balance

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited:{amount}.new balance{self.balance}")
        else:
            print(f"deposited amount must be positive")

    def withdraw(self,amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"withdraw:{amount}.******new balance{self.balance}")
            else:
                print(f"insufficient balance")
        else:
            print(f"withdraw amount must be positive")

    def check_balance(self):
        print(f"Account:{self.account_number} ******balance:{self.balance}")

#Example usage 
if __name__ == "__main__":
    account = bankaccount("123456789123",5000)
    account.check_balance
    account.deposite(1000)
    account.withdraw(500)
    account.check_balance()
    
Assignment no.6
[Assignment no.6.py](https://github.com/user-attachments/files/25465431/Assignment.no.6.py)
class library:
    def __init__(self,book_name,author,available=True):
        self.book_name=book_name
        self.author=author
        self.available=available

    def check_out(self):
        if self.available:
            self.available=False
            print(f"'{self.book_name}'has been checkout.")
        else:
            print(f"sorry,'{self.book_name}'is not available.")

    def return_book(self):
        if not self.available:
            self.available=True
            print(f"'{self.book_name}'has been return and now available.")
        else:
            print(f"'{self.book_name}'was not checkout.")

    def display_info(self):
        status="Available" if self.available else "checkout"
        print(F"book:{self.book_name},author:{self.author},status:{status}")

#example usage
book1 = library("1984","george orwall") 
book2 = library("the wall","jk",available=False)

book1.display_info()
book2.display_info()

book1.check_out()
book1.display_info()

book1.return_book()
book1.display_info()

Assignment no. 7
[Assignment no.7.py](https://github.com/user-attachments/files/25465460/Assignment.no.7.py)
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

Assignment no.8 

[Assignment no.8.py](https://github.com/user-attachments/files/25465470/Assignment.no.8.py)
# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# Subclass Car overrides move()
class Car(Vehicle):
    def move(self):
        print("Driving on the road")

# Subclass Bicycle overrides move()
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Demonstration of polymorphism
def show_movement(vehicle):
    vehicle.move()


# Example usage
car = Car()
bicycle = Bicycle()

# Calling move() directly
car.move()
bicycle.move()

print("\n--- Using polymorphism ---")
# Passing different objects to the same function
show_movement(car)
show_movement(bicycle)


Assignment no. 8
