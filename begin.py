# Variables --
num = 6  # Integer type
num2 = 6.0  # Double type
string = "hello"  # String type
string2 = "hello"  # String type

a, b = 0, 1  # Assign multiple values to variables on one line
c = d = 1  # Multiple assignment

dict1 = {"Sarah": 18, "Charlie": 18}  # Dictionaries -- key/value pairs
dict2 = {}  # Empty Dictionary
dict3 = dict()  # Empty Dictionary

set1 = set()
# Empty set (similar to empty array)
set2 = {"1", "2", "3"}  # Set- no order, can add/change

list1 = []  # Empty List
list2 = [1, 2, 3, 4]  # List--mutable, ordered
list3 = [[1, 2], [3, 4], [5, 6]]  # List in a list- Like a 2D array
list4 = ["1", 1]  # List with different data types

tup1 = ()  # Empty tuple
tup2 = tuple()  # Empty tuple
tup3 = ("hello", "world")  # Tuple- ordered,cannot change
tup4 = ("hello", "world", 1)  # Tuples- ordered, cannot add/remove

# ACESSING ELEMENTS OF LISTS AND TUPLES
for i in range(3):
    print (list4[i], tup4[i])  # So, both use index to access an element at
    # a particular index

# DICTIONARIES
test_dict = {}  # Create an empty dictionary
test_dict["Sarah"] = 18  # Assign a value to a key
test_dict["Charlie"] = 18  # Assign a value to a key

print (test_dict)  # Print the entire ditionary
print (test_dict["Sarah"])  # Print the value of a particular key
print (test_dict.keys())  # Print all of the keys (as a list)
print (test_dict.values())  # Print all of the values (as a list)

# Since the test_dict.keys() and .values() are lists, they are iterable:
for i in test_dict.keys():
    print (i)

# INPUT/OUTPUT
# print()
print ("Hello World!")
print ("Hello World!")
print (6)
print (6 + "Hello World")  # NO! Can't concatenate int and string types
print (str(6) + "Hello World")

# input()
e = input()  # Read in a value
f = input().strip()  # Remove leading and trailing spaces. You can also specify
# a string for strip() to remove (e.g. strip("\t"))

g = input().split()  # Splits the input on spaces. You can also specify a string
# for split() to work on (e.g., string.split(""))

# stdin.readline() and stdout.write()
# You must use an import to use these-
import sys

h = sys.stdin.readline()  # Take input. You can still use strip(), split(), etc
sys.stdout.write("hello, world")  # Like print() but all parameters MUST br string type

# ASIDE CONVERTING TO STR
# You can use str(num) or you can use `num` (backward single quotes)
#If all you want to use from sys is stdin.readline() and/or stdout.write(, you
#can do the following

 #from sys import stfin.readline(), stdout.write()
 k = stdin.readline()
 stdout.write("hello world")

 #It is fastest to read in all the input at once and parse it yourself
 all_input = sys.stdin.readline().split("\n")

 #LOOPS
 #For loops
 for i in range(10):
     print(i) #Prints the value of i. i will range from 0 to 9 inclusive

for i in range(1, 10):
    print(i) #Print i (1 <= i < 10)

for i in range (1, 10)[::-1]:
    print(i) #Prints 9, 8, 7, 6, 5, 4, 3, 2, 1
            #following: reversed(range (1,10))

for i in reversed(range(1,10))::
    print(i)

#Or the following:
for i in range(9,0,-1): #Note that we needed to use 9 and 0 because
                        #just as before, it includes the start value not the end value
print(i)

#You can also use similar syntax to iterate over some data structures
for i in list2:
    print(i) #In this case, the values of i are the elements of the list in order

#This is the same as the following, but cleaner:
for i in range(len(list2)):
    print(list2[i])

#WHILE
while True:
    #Do something
    print(1)

while num < 10:
    #Do something
    print(1)

while user_name == "Charlie":
    #Do something
    print(1)

#ASIDE: OPERATORS
#Use == for equal
#Use != for not equal
#Use < for less than
#Use <= for less than or equal to
#Use > for greater than
#Use >= for greater than or equal to
#Use and for and
#Use or for or
#Use + for addition/concatenation
#Use - for subtraction (even works some suprising places, like on sets)
#Use / for division
#Use // for floor division
#Use * for multiplication
#Use ** for exponentiation
#Use % for mod

#ADD BITWISE OPERATORS LATER!

#We also have assignment operators, which you use when you want to modify the
#value of an existing variable: +=, -=, /=, //=, *=, **=, %=, and bitwise too

#Break
while True:
    #....
    if num >= 10:
        break

 #FUNCTIONS



