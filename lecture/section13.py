# Section13
# typing game project


# imports -----------------------------------------------------------------------
import random                           # creating random shuffles and choices
import time                             # recording current time
# import winsound                         importing sound (window)
# import playsound
import sqlite3                          # importing db
import datetime                         # recording current date


# basic setting -----------------------------------------------------------------
words = []                              # list of random words
n = 1                                   # try count number
cor_cnt = 0                             # correct count number

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip().lower())
# print(words)


# INPUT STATEMENT----------------------------------------------------------------
input('READY? if so press enter')       # game start
start = time.time()                     # recording start time
print()

while n<= 5:
    random.shuffle(words)               # 'shuffle' module of 'random' package
    q = random.choice(words)

    print('question #{}'.format(n))
    print(q)

    x = input()                         # type value
    # print()

    if str(q).strip() == str(x).strip():    # !! matching word to input value
        print(' correct ')
        # winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        # PlaySound.PlaySound('./sound/good.wav', PlaySound.SND_FILENAME)
        cor_cnt += 1
    else:
        print(' incorrect ')
        # winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
    print()

    n += 1                              # next question
print()


# game result --------------------------------------------------------------------
end = time.time()                       # recording end time
et = end - start                        # game time
et = format(et, '.3f')                  # gametime format to 3 decimal points

if cor_cnt >= 3:                        # counting correct words to return pass v nonpass
    print('| good')
else:
    print('| not good enough')


# printing game result -----------------------------------------------------------
print('| game time: ', et, 'seconds')
print('| correct words: {}'.format(cor_cnt))

if __name__ == '__main__':              # run when file is original
    pass