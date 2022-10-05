#Same like list, but unchangeable, started using ()

my_tupple = (1, 'Athoillah', [2, 'Firda']) #Nested List in Tupple
print('\n--- Print Tupple ---')
print(my_tupple)
print('\n--- Checking Data Type ---')
print(type(my_tupple))

#Tupple created in any version

my_tuple = ("hello")
print('\n--- Checking Data Type ---')
print(type(my_tuple))

# Creating a tuple having one element
my_tuple = ("hello",)
print('\n--- Checking Data Type ---')
print(type(my_tuple)) 

# Parentheses is optional
my_tuple = "hello",
print('\n--- Checking Data Type ---')
print(type(my_tuple))


#Accesing, Slicing, indexing, Deleting Tupple same as List

#Checking count value in tupple

buah = ('a','p','p','l','e')
print('\n--- Checking Count Value of a Tupple ---')
print(buah.count('p'))

#Membership Test

print('\n--- Checking Membership of a Tupple ---')
print('a' in buah)
print('b' in buah)