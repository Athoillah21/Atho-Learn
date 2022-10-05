#Type of Number

#Float
x = 5e3
y = 2E-4
z = -7.7e10
print('\n--- Float Type ---')
print(type(x))
print(type(y))
print(type(z))


#Rounding

result_1 = round(4.5678, 2) #Rounding to 2 decimal
print('\n--- Rounding to 2 Decimal ---')
print(result_1)

my_float = 4.5678
my_str_1 = f'{my_float:.2f}' #Another way to rounding
print('\n--- Rounding to 2 Decimal ---')
print(my_str_1)

#Complex

x = 3+5j
y = 5j
z = -5j
print('\n--- Complex Type ---')
print(type(x))
print(type(y))
print(type(z))

#Casting

nomor = 10
print('\n--- Original Value ---')
print(nomor)
print(type(nomor))

#int()
a = int(nomor)
print('\n--- Casting to Integer ---')
print(a)
print(type(a))

#float()
b = float(nomor)
print('\n--- Casting to Float ---')
print(b)
print(type(b))

#str()
c = str(10)
print('\n--- Casting to String ---')
print(c)
print(type(c))

#bool()
d = bool(10)
print('\n--- Casting to Boolean ---')
print(d)
print(type(d))