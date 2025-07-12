
try:
    print(x)
except NameError:                       #if the exception is NameError (variable not defined)
    print("Variable x is not defined")
except:
    print("An exception occurred")
else:       #this block runs if no exceptions were raised in the try block
    print("Everything is fine, no exceptions occurred")
    
#finally:  #always runs after the try and except blocks, even if there was an exception
#   print("The 'try except' is finished")

x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")  #raises an exception if x is less than 0

