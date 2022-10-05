#Dictionary/Dict is set of item that unordered, every dict item has key/value relationship

#Initialize Dict

Dict = {} #void dict

Dict_1 = {1:'Apple', 2:'Ball'}

Dict_2 = {'name':'Athoillah', 'age':23}

print('\n--- Print Dictionary ---')
print(Dict)
print(Dict_1)
print(Dict_2)

#Dict from List

keys = ['Name', 'Age', 'Degree', 'Mate']
values = ['Athoillah', '23', 'Bachelor', 'Firda']

d = dict(zip(keys, values))
print('\n--- Dictionary from List ---')
print(d)

#Acces key
print('\n--- Access Keys ---')
print(d.keys())

#Acces key
print('\n--- Access Values ---')
print(d.values())

#if we want values became None

f = dict.fromkeys(keys)
print('\n--- Dictionary from List became None ---')
print(f)

#Accessing Element, we can using [] and .get()
#.get() if key is nothing return None, [] if key is nothing return Error

my_dict = d
print('\n--- Accessing Value from Key using [] ---')
print(my_dict['Name'])

print('\n--- Accessing Value from Key using get() ---')
print(my_dict.get('Mate'))

#.items() make accessing key value in tupple

l = list(my_dict.items())
print('\n--- Accessing Key Value became Tupple ---')
print(l)

#Add dict and value using .update

my_dict.update({'Addres':'Mojokerto'})
print('\n--- Adding Key Value using .update() ---')
print(my_dict)

my_dict.update([('Hobby','Swimming')])
print('\n--- Adding Key Value using .update() but in List version ---')
print(my_dict)


#Update Value
my_dict['Addres'] = 'Bandung'
print('\n--- Change Value ---')
print(my_dict)

#Choose key values using .pop(key) and popitem(), .popitem() choose key randomly
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print('\n--- Choose key value ---')
print(squares.pop(4))

print('\n--- Choose key value using .popitem() return pair key and value ---')
print(squares.popitem())

squares.clear()
print('\n--- Delete Dict ---')
print(squares)


#Nested Dict

Pets = {
    'Rambo': {'Species':'Chicken', 'Age':5},
    'Wumbo' : {'Species':'Elephant', 'Age':15}
}

print('\n--- Accessing Nested Dict ---')
print(Pets['Rambo']['Species'])




