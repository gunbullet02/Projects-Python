import random

print("Password Generator")

chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%^&*().,?123456789"

number=input("number of password?")
number=int(number)

length=input("Password length?")
length=int(length)

print("\nHere is your random generated password:")

for pwd in range(number):
    password=""
    for c in range(length):
        password +=random.choice(chars)
        print(password)
