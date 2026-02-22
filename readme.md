python assignment 
Assignment no 1.
#Creating the list 
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

Assignment no. 2
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

Assignment no. 3
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

Assignment no. 4
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

Assignment no .5
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
    


                
