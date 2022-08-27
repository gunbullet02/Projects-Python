sentence = input('Enter a sentence: ').lower()
words = sentence.split()

for i, word in enumerate(words):

    '''
    if first letter is a vowel
    '''

    if word[0] in 'aeiou':
        words[i] = words[i] + "ay"
    else:
        '''
        else get vowel position and postfix all the components
        present before that vowel to the end of the word along with "ay
        '''

        has_vowel = False

        for j, letter in enumerate(word):
            if letter in 'aeiou':
                words[i] = word[j:] + word[:j] + "ay"
                has_vowel = True
                break
        
        if(has_vowel == False):
            words[i] = words[i] + "ay"
    
pig_latin = ' '.join(words)
print("Pig Latin: ", pig_latin)