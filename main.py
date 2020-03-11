import random
from collections import OrderedDict
from database import dictionary as dict

lists = list(dict.items())
option = random.choice(lists)
word = list(option[0])
word2 = list(OrderedDict.fromkeys(word))
glist = []
chances = 12
while(len(glist) != len(word2) and chances > 0) :
    for i in word :
        if i in glist:
            print(i)
        else :
            print('_')
    print('Hint is : {}'.format(option[1]))
    print('You have {} chances'.format(chances))
    if(chances > 0) :
        letter = input('Guess any letter ')
        if (letter.isalpha()) :
            if len(letter) != 1 :
                print('Enter only 1 character ')
            else :
                if letter in word :
                    glist.append(letter)
                else :
                    chances -= 1
                    print('Wrong attempt. You have {} chances left '.format(chances))
        else :
            print('Only letters are alowed')

if (chances == 0) :
    print('You Lose. The word was {} '.format(option[0]))
else :
    for i in word :
        print(i)
    print('You WON !!! Congratulations')