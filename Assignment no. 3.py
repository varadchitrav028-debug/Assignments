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
