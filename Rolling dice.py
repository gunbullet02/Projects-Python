import random

question = input('Would you like to roll the dice [y/n]?\n')

while question != 'n':
    if question == 'y':
        roll = random.randint(1, 6)
        roll = random.randint(1, 6)
        print(roll, roll)
        question = input('Would you like to roll the dice [y/n]?\n')
    else:
        print('Invalid response. Please type "y" or "n".')
        question = input('Would you like to roll the dice [y/n]?\n')

print('Good-bye!')