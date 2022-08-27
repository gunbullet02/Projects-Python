from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
Label(root, text = "Mad Libs Generator \n Have Fun!", font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One : ', font = 'arial 15 bold').place(x = 40, y = 80)

def madlib1():

    animals = input('Enter an animal species: ')
    profession = input('Enter a profession: ')
    cloth = input('Enter a type of clothing: ')
    things = input('Enter an object: ')
    name = input('Enter a name: ')
    place = input('Enter a name of a place: ')
    verb = input('Enter a verb in ing form: ')
    food = input('Food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

def madlib2():
    
    adjective = input('Enter an adjective: ')
    color = input('Enter a color: ')
    thing = input('Enter an object: ')
    place = input('Enter a location: ')
    person = input('Enter a persons name: ')
    adjective1 = input('Enter another adjective: ')
    insect = input('Enter an insect: ')
    food = input('Enter a food: ')
    verb = input('Enter a verb: ')

    print('Last night I dreamed I was a ' +adjective+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjective1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')

def madlib3():

    person = input('Enter a name of person: ')
    color = input('Enter a color: ')
    foods = input('Enter a name of a food: ')
    adjective = input('Enter an adjective: ')
    thing = input('Enter a thing: ')
    place = input('Enter a place: ')
    verb = input('Enter a verb: ')
    adverb = input('Enter an adverb: ')
    food = input('Enter another food: ')
    things = input('Enter a name of a thing: ')

    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  


    Button(root, text = 'The Photographer', font = 'arial 15', command = madlib1, bg = 'ghost white').place(x = 60, y = 120)
    Button(root, text = 'apple and apple', font = 'arial 15', command = madlib3, bg = 'ghost white').place(x = 70, y = 180)
    Button(root, text = 'The Butterfly', font = 'arial 15', command = madlib2, bg = 'ghost white').place(x = 80, y = 240)

    root.mainloop()