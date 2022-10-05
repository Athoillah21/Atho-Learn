#Set is collection item that unordered, unchangeable and unidexed. We can add and delete but we can chage the value inside it
#Set started with {}, value in set is unique (Nothing duplicate)


#Make empty set, use set(), because if you make a = {} it will became dictionary

a = {}
print('\n--- Checking Data Type ---')
print(type(a))

b = set()
print('\n--- Checking Data Type ---')
print(type(b))


#Changing set, add or delete set dont use index

set = {1,3}

set.add(2)
print('\n--- Add Value using .add(value) ---')
print(set)

set.update([2,3,4])
print('\n--- Add Value using .update([value,value]) ---')
print(set)

set.update([4,5], [1,6,8])
print('\n--- Add Value using .update([value,value]) ---')
print(set)

set.discard(4)
print('\n--- Delete Value using .discard(value) ---')
print(set)

set.remove(5) #The difference discard and remove is, remove return error if the value aren't any (gaada)
print('\n--- Delete Value using .remove(value) ---')
print(set)

set.clear()
print('\n--- Delete Value using .clear() ---')
print(set)

#Set can use for mathematical set operations such as union, intersection, difference and symmetric difference

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#Union is adding all value into one set, use | operator
print('\n--- A Union B ---')
print(A | B)

#Intersection is separates only values ​​that are the same between two sets, use & operator
print('\n--- A Intersect B ---')
print(A & B)

#Difference is a set that has only values ​​that other sets do not have, using - operator
print('\n--- A Difference from B ---')
print(A - B)

#Symmetric Difference is sets that has value all over 2 set except the intersection, using ^ operator
print('\n--- A Symmetric Difference from B ---')
print(A ^ B)


