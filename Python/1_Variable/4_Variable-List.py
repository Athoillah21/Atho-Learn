#List is a non-primitive data type that started by [], List can ordered and changeable

my_list = [1, 'Athoillah', [2, 'Firda']] #Nested List
print('\n--- Print List ---')
print(my_list)
print('\n--- Checking Data Type ---')
print(type(my_list))

#Accessing Element in List, started with 0

print('\n--- Checking Element ---')
print(my_list[2])

print('\n--- Checking Element in Nested ---')
print(my_list[2][1])

print('\n--- Checking Element with Negative number ---')
print(my_list[-1])

#Slicing Element in List

List_1 = [0,1,2,3,4,5,6,7,8,9,10]

print('\n--- Slicing Element Start to End ---')
print(List_1[:])

print('\n--- Slicing Element Value(Called) to Value(Not Called) ---')
print(List_1[2:5])

print('\n--- Slicing Element Null to Value(Not Called) ---')
print(List_1[:5])

print('\n--- Slicing Element Value(Called) to Value(Not Called) Multiple by Value ---')
print(List_1[1:8:2])

#Change Value

List_1[0] = 100
print('\n--- Change Value ---')
print(List_1)


List_1[1:4] = [100,200,300,400]
print('\n--- Change Value 2nd to 4th ---')
print(List_1)

#Add Value

odd = [1,3,5]

a = odd.append(7)
print('\n--- Append Value ---')
print(odd)

b = odd.extend([9, 11, 13])
print('\n--- Extend Value ---')
print(odd)

even = [2,4,8,10] #.insert(index define, insert value)
even.insert(2,6)
print('\n--- Insert Value ---')
print(even)

#Delete Element

kata_1 = ['p','r','o','b','l','e','m']
del kata_1[2]
print('\n--- Delete using del[index] ---')
print(kata_1)

kata_1.remove('p')
print('\n--- Delete using remove(value) ---')
print(kata_1)

print('\n--- Pop(index) ---')
print(kata_1.pop(4))

print('\n--- Clear All Value ---')
print(kata_1.clear())

#Sorting

nama = ['cinta', 'athoillah', 'firda', 'uhuy']

nama.sort()
print('\n--- Ascending Sort ---')
print(nama)

nama.reverse()
print('\n--- Descending Sort ---')
print(nama)