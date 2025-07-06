#Dictionaries are mutable. New key pairs can be added, existing ones can be modified

my_dict = {"apple": 3, 'banana': 5, 'orange': 2} #similar to sets, dictionaries use curly-braces


print (my_dict['apple'])

my_dict['grapes'] = 4 #new pair added

print(my_dict)

my_dict['banana'] = 7 #key pair modified

print(my_dict)