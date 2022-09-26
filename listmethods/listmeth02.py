#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

#Challenge 01: Demo of an Method
fruits = ["strawberry", "blueberry","orange", "kiwi"]
veggie = ["lettace", "potato"]
print(fruits)
print(veggie)

fruits.append("tomato") # This is will add another fruit
veggie.append("onion") # This is will add another veggie
print(fruits)

fruits.pop() # This will remove fruit
veggie.pop()
print(fruits)
print(veggie)

