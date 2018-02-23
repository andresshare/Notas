"""
Strings
"""

cadena = "I'm String"

print(len(cadena))
print(cadena[0])
print (cadena[-1])
print(cadena[1:4])
print(cadena[:5])

palabra = 'python'
palabra = 'super'+palabra[:2]
print(palabra)

#string
print("Today I had {0} cups of {1}".format(3,"coffee"))
print('{:<20}'.format("text"))
print('{:>20}'.format("text"))

print("'I\'m a string in Python")

message = 'text1'

''' IF'''

if message == 'text':
    print('Hi')
else:
    print('bye')

    '''staments'''

lista = [1, 2.5, 'Code', [5, 6], 4]
print lista[0]  # 1
print lista[1]  # 2.5
print lista[2]  # DevCode
print lista[3]  # [5,6]
print lista[3][0]  # 5
print lista[3][1]  # 6
print lista[1:3]  # [2.5, 'Code']
print lista[1:6]  # [2.5, 'Code', [5, 6], 4]
print lista[1:6:2]  # [2.5, [5, 6]]
