# print("Hello Josh!")

'''
x = 1
if x == 1:
    # indent four spaces
    print("x is 1.")
'''

 # Exercise answer
 # print("Hello World!")

# define an integer
# myint = 7
# print(myint)

'''
# define float
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
'''

'''
# define string
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
'''

'''
# using double quotes for apostrophes instead of single quotes
mystring = "Don't worry about apostrophes"
print(mystring)
'''

'''
# simple operators on variables
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
'''

'''
# multiple assignmets
a, b = 3, 4
print(a, b)
'''

'''
# mixing does not work
one = 1
two = 2
hello = "hello"

print(one + two + hello)

'''

'''
# exercise input variables
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
'''

'''
# list
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)
'''

'''
# error accessing an index that does not exist
mylist = [1, 2, 3]
print(mylist[10])
'''

'''
# list exercises
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
'''

'''
# basic operations
number = 1 + 2 * 3 / 4.0
print(number)
'''

'''

# modulo
remainder = 11 % 3
print(remainder)

'''

'''
# two multiple operation = power relationship
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

'''

'''
# concatenation of strings with addition operator
helloworld = "hello" + " " + "world"
print(helloworld)
'''

'''
# multiplying string for repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)
'''

'''
# addition operator with lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
'''

'''
# multiply strings with multiplication operator
print([1, 2, 3] * 3)
'''

'''
# list exercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = [x_list + y_list]

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

'''

'''
# argument specifiers
name = "Josh"
print("Hello, %s!" % name)

'''

'''
# using tuple for two or more argument specifiers
name = "John"
age = 23
print("%s is %d years old." % (name, age))
'''

'''
# list format specifiers
mylist = [1, 2, 3]
print("A list: %s" % mylist)
'''

'''
# argument specifiers exercise

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

'''

'''
# string length double quotes
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))
'''

'''
# string index
astring = "Hello world!"
print(astring.index("o"))
'''

'''
astring = "Hello world!"
print(astring.count("l"))
'''

'''
astring = "Hello world!"
print(astring[3:7])
'''

'''
astring = "Hello world!"
print(astring[3:7:2])
'''

'''
astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])
'''

'''
astring = "Hello world!"
print(astring[::-1])
'''

'''
astring = "Hello world!"
print(astring.upper())
print(astring.lower())
'''

'''
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
'''

'''
astring = "Hello world!"
afewwords = astring.split(" ")
'''

'''

s = "Hey threa! what sho?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

'''

'''
x = 2
print(x == 2)
print(x == 3)
print(x < 3)
'''

'''
name = "John"
age = 22
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

'''

'''

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

'''

'''
statement = False
another_statement = True

if statement is True:
    pass

elif another_statement is True:
    pass

else:
    pass

'''

'''
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

'''

'''
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

'''

'''
print(not False)
print((not False) == (False))
'''

'''
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
'''

'''
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
'''

'''
for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)
'''

'''
count = 0
while count < 5:
    print(count)
    count += 1
'''

'''
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):

    if x % 2 == 0:
        continue
    print(x)

'''

'''
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))

for i in range(1, 10):
    if(i%5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
'''


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

'''
# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)

'''

'''
def my_function():
    print("Hello")

my_function()
'''


'''
def my_function_with_args(username, greeting):
    print("Hello, %s, From my Function, I wish you %s" %(username, greeting))

'''

'''
def sum_two_numbers(a,b):
    return a + b

sum_two_numbers(10,10)
'''

'''
def my_function():
    print("Hello Josh function!")

def my_function_with_args(username,greeting):
    print("Hello, %s, From Josh, I wish you %s" %(username, greeting))

def sum_two_numbers(a, b):
    return a + b

my_function()

my_function_with_args("Josh Josol", "A great year!")

x = sum_two_numbers(2,2)
print(x)
'''

'''
# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
'''

'''
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()
'''

'''
class NumberHolder:

    def __init__(self,number):
        self.number = number
'''

'''
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00
car1.name = "Fer"

car2.color = "blue"
car2.kind = "van"
car2.name = "Jump"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())
'''

'''
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
'''

'''
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781

}
print(phonebook)
'''

'''
phonebook = {"John" : 938477566, "Jack" : 938377264, "Jill" : 945662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
'''

'''
phonebook = {
    "John" : 938477566,
    "Jack" : 938477264,
    "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
'''

'''
phonebook = {
    "John" : 938477566,
    "Jack" : 93877264,
    "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)
'''

'''
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
    
}  
# your code goes here
phonebook["Jake"] = 938273443
del phonebook["Jill"]
# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")

'''

'''
import draw

def play_game():

    def main():
        result = play_game()
        draw.draw_game(result)

    if __name__ == '__main__':
        main()

'''

'''
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

bmi = np_weight / np_height ** 2

bmi > 23

bmi[bmi > 23]

print(bmi)
'''

'''
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg ** 2    
# Print out np_weight_lbs
print(np_weight_lbs)
'''


'''
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area:": [8.561, 17.10, 3.286, 9.597, 1.221], 
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)


brics.index = ["BR", "RU", "IN", "CH", "SA"]

print(brics)

'''

'''
import pandas as pd

cars = pd.read_csv('cars.csv')

print(cars)
'''

'''
import random

def lottery():

    for i in range(6):
        yield random.randint(1, 40)

    yield random.randint(1, 15)

for random_number in lottery():
        print("And the next number is ... %d!" % (random_number))

'''

'''

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, xa + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

'''

'''
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)
'''

'''
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)
'''

'''
numbers = [34.6, 203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [n for n in numbers if n > 0]
print(newlist)
'''

'''
def sum(a,b):
    return a + b

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)
'''

'''
l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))
'''


