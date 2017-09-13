import string

phrase = 'purple cow'
text1 = 'The purple cow is soft and cuddly.'
text2 = 'Purple!!! Cow!!!'
text3 = 'purple@#$%cow'
text4 = 'Did you see a purple     cow?'
text5 = 'The farmer owns a really PURPLE cow.'
text6 = 'purple cow'

text7 = 'Purple cows are cool!'
text8 = 'The purple blob over there is a cow.'
text9 = 'How now brown cow.'
text10 = 'Cow!!! Purple!!!'
text11 = 'purplecowpurplecowpurplecow'
text12 = 'I like poison dart frogs.'

"""This program takes two strings, a phrase assumed to be words only any cap, and a text that might
include punctuation. It separates phrase and text into lists and returns true if phrase is in text, 
false otherwise."""

ntext = ''
phrase_list = phrase.lower().split(' ')
for letter in text9.lower():
    if letter in string.punctuation:
        ntext += ' '
    else:
        ntext += letter
text_list = ntext.split(' ')
while '' in text_list:
    text_list.remove('')
if phrase_list[0] not in text_list:
    print('You messed up')
print(phrase_list[:] == text_list[text_list.index(phrase_list[0]):text_list.index(phrase_list[0]) + len(phrase_list)])


