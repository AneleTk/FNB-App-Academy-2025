#Similar to lists, Tuples are a collection of ordered elements
#Unlike lists,Tuples are immutable once they are created

my_tuples = (1,2,3,4,5) #round brackets instead of square brackets

print(my_tuples)
print(my_tuples[0])
print(my_tuples[2])
print(my_tuples[-1]) #Negative indexing. Gives the last value in the list

tuple1 = (1,2,3)
tuple2 = (4,5,6)

conc_tuple = tuple1 + tuple2 #concatenate
print(conc_tuple) #or just print(tuple1 + tuple2)

rep_tuple = tuple1 * 3 #Repetition
print(rep_tuple)