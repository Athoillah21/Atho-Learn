# IF ELIF ELSE, used for many condition

# if condition1:
#   expression1
# elif condition2:
#   expression2
# else:
#   expression3


print('\n--- ELIF Case 1 ---')

harga = int(input('Masukkan Pembelianmu: '))

if 0 <= harga <= 100000:
    diskon = 0.05
elif 100000 < harga <= 200000:
    diskon = 0.1
elif 200000 < harga <= 300000:
    diskon = 0.2
else:
    diskon = 0.5

harga_akhir = harga - (diskon*harga)
print(f'Diskonmu adalah: {diskon*100} %')
print(f'Harga Akhirmu Menjadi: {harga_akhir}')

print('\n--- ELIF Case 2 ---')

name = input('Masukkan nama peliharaanmu: ')
species = input('Masukkan jenis peliharaanmu: ')

if species == "dog":                      #condition1
    print(name, "sound barks")            #expression1
elif species == "duck":                   #condition2
    print(name, "sound quacks")           #expression2
elif species == "cat":                    #condition3
    print(name, "sound meows")            #expression3
elif species == "cow":                    #condition4
    print(name, "sound moos")             #expression4
else: 
    print("I do not know what is this...") #expression5


no = 9

print('\n--- ELIF Case 3 ---')

if 5 < no < 7:                      #cond1
    print('diantara 5 dan 7')       #ex1
elif 8 < no < 10:                   #cond2
    print('diantara 8 dan 10')      #ex2
else:                               #
    print('Jauh')                   #ex3

# Shorthand, expression1 if condition1 else (expression2 if condition2 else expression3)
# ex1 if cond1 else ((ex2 if cond2 else (ex3 if con3 else ex4))

print('\n--- ELIF Case 3 : Shorthand ---')

print('diantara 5 dan 7') if 5 < no < 7 else (print('diantara 8 dan 10') if 8 < no < 10 else print('Jauh'))

#Short Circuit
#Ternary operator
