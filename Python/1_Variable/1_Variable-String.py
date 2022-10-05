#String

#Length of String
kata_1 = 'Muhammad Athoillah'
print('\n--- Length of String ---')
print(len(kata_1))

#Enumerate Function
list_enumerate = list(enumerate(kata_1))
print('\n--- Enumerate Function ---')
print(list_enumerate)

# Python string format() method
# default(implicit) order
default_order = "{}, {} and {}".format('Joko','Budi','Susi')
print('\n--- Default Order ---')
print(default_order)


# order using positional argument
positional_order = "{1}, {0} and {2}".format('Joko','Budi','Susi')
print('\n--- Positional Order ---')
print(positional_order)


# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='Joko',b='Budi',s='Susi')
print('\n--- Keyword Order ---')
print(keyword_order)



#.lower()
a = 'Athoillah'.lower()
print('\n--- Lower Function ---')
print(a)

#.upper()
b = 'Athoillah'.upper()
print('\n--- Upper Function ---')
print(b)

#.split()
c = 'Muhammad Athoillah'.split()
print('\n--- Split Function ---')
print(c)

#.find('word')
d = 'Muhammad Athoillah'.find('Atho')
print('\n--- Find Function ---')
print(d)

#.replace('old word','new word')
e = 'Muhammad Athoillah'
f = e.replace('Muhammad','Firda')
print('\n--- Replace Function ---')
print(f)
