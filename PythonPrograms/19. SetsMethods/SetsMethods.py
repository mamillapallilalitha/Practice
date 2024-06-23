# creating a set :
print(1) 
set = {"apple", "banana", "cherry", True, 1, 0}
print(set)
print()

print(2)
# length of a set :
fruits = {"apple", "banana", "cherry", "grapes"}
print(len(fruits))
print()

print(3)
# checking an element present in a set :
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)
print()

print(4)
# add() method : 
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
print()

print(5)
# update() method : 
fruits = {"apple", "banana", "cherry"}
fruit = {"pineapple", "mango", "papaya"}
fruits.update(fruit)
print(fruits)
print()

print(6)
# remove() method :
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)          # if the item not present in the set then it raise an error
print()

print(7)               
# discard() method : 
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)           # even if thr item not present in the set it does not raisr any error.
print()

print(8)        
# pop() method : 
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)
print(fruits) 
print()

print(9)
# this method will remove a random item, so we cannot be sure what item that gets removed
# clear() method : 
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
print()

print(10)
'''# del keyword : 
fruits = {"apple", "banana", "cherry"}
del fruits
print(fruits)
print()'''
#this will raise an error because the set no longer exists

print(11)
# for loop : 
fruits = {"apple", "banana", "cherry"}
for x in fruits:
  print(x)
  print()

print(12)
# join sets :
character = {"a", "b", "c"}
numeric = {1, 2, 3}
set3 = character.union(numeric) # we can also use '|' instead of 'union'
print(set3)
print()

print(13)
# to join multiple sets using union : 
character = {"a", "b", "c"}
numeric = {1, 2, 3}
string = {"John", "Elena"}
fruits = {"apple", "bananas", "cherry"}
myset = character.union(numeric,string,fruits)
print(myset)
print()

print(14)
#to join multiple sets using | :
character = {"a", "b", "c"}
numeric = {1, 2, 3}
string = {"John", "Elena"}
fruits = {"apple", "bananas", "cherry"}
myset = character | numeric | string | fruits
print(myset)
print()

print(15)
#intersection() method : 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) # instead of 'intersection' we can use '&'
print(set3)           #  # prints only duplicate values
print()

print(16) 
#differennce() method :
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) # we can use '-' instead of 'difference'.
print(set3) # this gives result of the first set without duplicate values.
print()

print(17)
# the difference_update() method changes the original set and keeps the items that are not present in both sets :
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
print()

print(18)
# The symmetric_difference() method will keep all the elements that are NOT present in both sets :
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) # we can use the ^ operator instead of the symmetric_difference() method.
print(set3)
print()

print(19)
# the symmetric_difference_update() method to keep the items that are not present in both sets and updates the original set :
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
print()

