

fruits = ["apple", "banana","cherry"]
print(fruits[0])
fruits[1] = "blueberry" #Lists are changeable
print(fruits)

fruits.append("kiwi") #Append to end of list
print(fruits)
fruits.insert(1,"orange") #Append to a specific position in the List/array
print(fruits)
fruits.remove("kiwi") #Remove from a list. ONLY the first instance
print(fruits)
fruits.sort() #Sort a list (Default=ascending order)
print(fruits)
fruits.sort(reverse=True) #Sort a list (in descending order)
print(fruits)