# IF used for Single Condition, if it doesn't find the condition, then it returns nothing

# if Condition:
#    Expression

print('\n--- IF Case 1 ---')

z = 4
if z % 2 == 0 :
    print('Checking ' + str(z))
    print('z is even')

print('\n--- IF Case 2 ---')

a = 7
b = 5
if a > b :
    print('a is bigger than b')


print('\n--- IF Case 3 ---')
nilai = int(input('Masukkan nilaimu: '))

if nilai >= 80 :
    print('Lolos KKM')


#Shorthand, it means simple version of the code above, used in Spark
# if condition1 : expression1

print('\n--- IF Case 2 : Shorthand ---')
if a > b : print('a is bigger than b')

print('\n--- IF Case 3 : Shorthand ---')
if nilai >= 80 : print('Lolos KKM')