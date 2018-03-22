from sys import argv

#user  print
print("Hello world")
print("Hello again")
print("I like type this")
print("This is fun")
print("Yay! Printing")
print("I'd much rather  you 'not'")
print('I "said" do not touch this')
print("*"*50)
#chickens
print("Now will  now count my chickens")

print("Hens", 25 + 30 / 6)
print("Rooters", 100 - 25 * 3 % 4)
print("Now I will count the eggs:")
print(3+2+1-5+4 % 2-1/4+6)
print("is it true that  3+2<5-7?")
print(3 + 2 < 5 - 7)
print("what is 3+2?", 3 + 2)
print("What is 5 -7", 5 - 7)
print("Oh,that's why it's False")
print("How about some more")
print("Is it greater", 5 > -2)
print("is it grater or equal",  5 <= -2)
print("*"*50)
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are:", cars, "cars_available")
print("There are only", drivers, "drivers_available")
print("There will be", cars_not_driven, "empty_cars_today")
print("We can transport", carpool_capacity, "people today")
print("We have",  passengers  ,  "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
print("*"*50)

my_name = "Ander"
my_age = 37
my_height = 74
my_weight = 180
my_eyes = 'Blues'
my_teeh = "White"
my_hair = "Browm"

print("Let's talk about %s"% my_name)
print("He's %d inches tall"% my_height)
print("He's %d 'pound heavy"%my_weight)
print("Actually that'not too heavy")
print("He's got %s  eyes and %s hair"%(my_eyes,my_hair))
print("His teeth are usually %s depending on the coffe" % my_teeh)

#this line is tricky
print("If I add %d %d and %d I get %d"%(my_age, my_height, my_weight, my_age + my_height + my_weight))
print("*"*50)
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s"%(binary, do_not)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s'." % y)


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print (joke_evaluation % hilarious)
w = "This is the left  side of"
e = "a string with a right side"

print(w + e)

print("mary had a little lamb")
print("its fleece was white as %s" % 'snow')
print("And everyweather that Mary went")
print("." * 10)


end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11+end12)

formatter = " %r %r %r %r "

print(formatter  % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print( formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
         "I had this thing",
         "That you could type up right",
         "but it didn't sing",
         "So I said goodnight."
 ))

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days", days)
print("Here are the months:", months)
print("""
There's something going on here
With the three double-quotes
Well be able to type as much as we like
Even 4 lines if we want, or 5, or 6, 
""")

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm\\ a\\cat"

fat_cat = """
I'll do a list
\t* Cat food
\t* Fishies
\t*Catnip\n\t* Grass
"""
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print(fat_cat)

# while True:
#     for i in["/", "-", "|", ",", "\\"," | "]:
#         print("%s\r" %i)

age = input("How old are you?")
print("So,you're %r old,%r tall and %r heavy" % (age, height, weight))

script, first, second, third = argv
print("The script is called:",script)
print("You first variable is:", first)
print("your second variable is:", second)
print("your third variable is:", third)






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
