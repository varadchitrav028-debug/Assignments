python assignment 
Assignment no 1.

[Assignment no. 1.py](https://github.com/user-attachments/files/25160105/Assignment.no.1.py)
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
