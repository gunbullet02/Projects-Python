'''

5
x = 5
x + 1

'''


'''

name = input("Enter your name: ")
print("Welcome " + name)

'''

'''
hours = input("Enter Number of Hours: ")
try:
    int(hours)
    rate = input("Enter Rate: ")
    int(rate)
    grossPay = int(hours) * int(rate)
    int(grossPay)
    print("Gross Pay: ")
    print(grossPay)

except:
    print("Error please enter numeric input.")


'''



'''
width = 17
height = 12.0

print(width / 2) # float
print(width / 2.0) # float
print(height / 3) # float
print(1 + 2 * 5) # int

'''

'''
temperature = float(input('Enter temperature in celsius : '))
temperature2 = 1.8 * temperature + 32
print(temperature2)

'''

'''
score = input("Enter your score between 0.0 and 1.0: ")
try:
    float(score)
    if float(score) >= 0.9 and float(score) <= 1.0:
        print("A")
    elif float(score) >= 0.8 and float(score) <= 0.9:
        print("B")
    elif float(score) >= 0.7 and float(score) <= 0.8:
        print("C")
    elif float(score) >= 0.6 and float(score) <= 0.7:
        print("D")
    elif float(score) > 0 and float(score) <= 0.6:
        print("F")
    else:
        print("Invalid score please enter numeric input. ")
except:
    print("Error please enter numeric input. ")
'''

'''
counting = 0
total = 0
average = 0
movingOn = True
while movingOn:
    num1 = ('Enter a number:\n')
    line = input(num1)
    try:
        line = float(line)
        counting = counting + 1
        total = total + line
        average = total / counting
    except:
        if line == 'Done' or line == 'done':
            break
        else:
            print ('Invalid input')
            continue
print (counting, total, average)
'''

from tkinter import N


largest = None
smallest = None
counting = 0
total = 0
while True:
    try:

        number = input("Enter a number: ")
        if number == "done":
            break
        number = int(number)
        counting += 1
        total = number + total
        if largest == None and smallest == None:
            largest = number
            smallest = number
        if largest == None or number > largest:
            largest = number
        if smallest == None or number < smallest:
            smallest = number
    
    except:
        print("Invalid input.")

print("The maximum number is: {}".format(largest))
print("The minimum number is : {}".format(smallest))
print("The total number is : {}".format(total))
print("The count number is: {}".format(counting))