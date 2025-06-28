#Similar to lists, (unordered)
#Unlike lists, sets are unique and do not allow for duplicates
#They are immutable in that duplicates are not allowed, however, items can be added/deleted
#Common uses:Removing duplicate data from a list. i.e Union, Intersection, Difference

my_set = {1,2,3,4,5,} #Curly braces
print(my_set)
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)

set1 = {1,2,3}
set2 = {3,4,5}

#Union adds both sets together and removes duplicates
union_set = set1.union(set2)
print(union_set)

#intersection
inter_set = set1.intersection(set2)
print(inter_set)

#Difference
diff_set = set1.difference(set2)
print(diff_set)