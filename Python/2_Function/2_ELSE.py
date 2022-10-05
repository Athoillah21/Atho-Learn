# Else used for 2 condition
# if condition :
#   expression
# else :
#   expression

print('\n--- ELSE Case 1 ---')

number = int(input('Enter Number: '))

# if number % 2 == 0 :
#     print('Number is even')
# else :
#     print('Number is odd')

print('\n--- ELSE Case 2 ---')

nilai = int(input('Masukkan Nilaimu: '))

if nilai >= 80:
    print('Lulus')
else:
    print('Tidak Lulus')

print('\n--- ELSE Case 3 ---')

belanja = int(input('Masukkan Angka Belanjamu: '))
if belanja >= 100000:
    diskon = 0.2*belanja
    harga = belanja - diskon
    print(f'Harga setelah Diskon {harga}')
else:
    print('Anda Tidak Dapat Diskon')

#Shorthand Else, most used for Spark
# expression1 if condition1 else expression2

print('\n--- ELSE Case 1 : Shorthand ---')

print('Number is even') if number % 2 == 0 else print('Number is odd')

print('\n--- ELSE Case 2 : Shorthand ---')

print('Lulus') if nilai >= 80 else print('Tidak Lulus')