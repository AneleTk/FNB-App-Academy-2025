

fruits = ["apple", "banana", "cherry","date"]

for fruit in fruits:
        if fruit == "cherry":
            break #exits loop if cherry is found
        print(fruit)
        
print() #add a line/space in-between
        
for fruit in fruits:
        if fruit == "cherry":
            continue #Skips cherry
        print(fruit)
        
print()

for fruit in fruits:
        if fruit == "cherry":
            pass #Placeholder, no action is needed for cherry
        print(fruit)
print()       
#While-loop

count2 = 0

while count2 < 5:
    print(count2)
    count2+=1
    if count2 == 3:
        break
    