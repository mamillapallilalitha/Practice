'''print(1)
# creating tuple :
fruits = ("apple", "banana", "cherry")
print(fruits)
print()

print(2)
# tuple allows duplicates : 
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)
print()

print(3)
# length of a tuple : 
fruits = ("apple", "banana", "cherry")
print(len(fruits))
print()

print(4)
# creating tuple with one item : 
fruits = ("apple",)
print(type(fruits))
print()

print(5)
# data types tuple :
strings = ("apple", "banana", "cherry")
numeric = (1, 5, 7, 9, 3)
boolean = (True, False, False)
print(strings)
print(numeric)
print(boolean)
print()

print(6)
# multiple data types : 
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print()

print(7)
# tuple type : 
fruits = ("apple", "banana", "cherry")
print(type(fruits))
print()

print(8)
#Using the tuple() method to make a tuple:
fruits = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(fruits)
print()

print(9)
# indexing of a tuple : 
fruits = ("apple", "banana", "cherry")
print(fruits[0])
print()

print(10)
# negative indexing : 
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
print()

print(11)
#range of indexing : 
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
print()

print(12)
# adding a tuple value to a tuple :
fruits = ("apple", "banana", "cherry")
y = ("orange",)
fruits += y
print(fruits)
print()

print(13)
# assigning values to a list :
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print()

print(14)
# for loop to a tuple :
fruits = ("apple", "banana", "cherry")
for x in fruits:
 print(x)
print()

print(15)
# while loop to a tuple :
fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
 print(fruits[i])
 i = i + 1
print()

print(16)
# joining of tuple with + operator :
character = ("a", "b" , "c")
number = (1, 2, 3)
tuple3 = character + number
print(tuple3)
print()

print(17)
# multiply to tuples :
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
print()'''

print(18)

tuple = ("apple", "banana", 1, 2)
print(tuple)