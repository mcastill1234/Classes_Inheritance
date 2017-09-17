import string
import time
import datetime


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
text13 = 'purple colors are cool but purple cow is crazy'

"""This program takes two strings, a phrase assumed to be words only any cap, and a text that might
include punctuation. It separates phrase and text into lists and returns true if phrase is in text, 
false otherwise."""

ntext = ''
phrase_list = phrase.lower().split(' ')
for letter in text13.lower():
    if letter in string.punctuation:
        ntext += ' '
    else:
        ntext += letter
text_list = ntext.split(' ')
while '' in text_list:
    text_list.remove('')
for count in range(text_list.count(phrase_list[0])):
    start_index = text_list.index(phrase_list[0])
    if phrase_list[:] == text_list[start_index:start_index + len(phrase_list)]:
        # print(True)
        pass
    else:
        text_list.pop(start_index)
# print(False)

# print("Time in secods since the epoch: %s" %time.time())
# print("Current date and time: ", datetime.datetime.now())
# print("Or like this: ", datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
#
# print("Current year: ", datetime.date.today().strftime("%Y"))
# print("Month of year: ", datetime.date.today().strftime("%B"))
# print("Week number of the year: ", datetime.date.today().strftime("%W"))
# print("Day of year: ", datetime.date.today().strftime("%j"))
# print("Day of month: ", datetime.date.today().strftime("%d"))
# print("Day of week: ", datetime.date.today().strftime("%A"))

# dtobj = datetime.datetime.strptime("3 Oct 2016 17:00:10", "%d %b %Y %H:%M:%S")
# print(dtobj)

now = datetime.datetime(2016, 10, 12, 23, 59, 59)
somepast = datetime.datetime(2016, 10, 12, 23, 59,58)
ancient_time = datetime.datetime(1987, 10, 15)

print(now)
print(ancient_time)
print(now < ancient_time)
print(now > somepast)