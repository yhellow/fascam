# Section09
# file read and write
    # read = r / write = w (overwrite original file) / append = a (modify original or create original file)


# READ
    # recallName = open('./filedirectory/fileName', 'mode')
    # with open('./filedirectory/fileName', 'mode') as recallname


# 1
    # usual open() function
f = open('./resource/review.txt', 'r')
content1 = f.read()
print(content1)
print(dir(f))
f.close()                   # '.close()' needed after opening a file (반드시 close 리소스 반환)

print()
print('---------------------------------------')
print()


# 2
    # with loop
with open('./resource/review.txt', 'r') as f:   # with closes the resource without 'close()'
    content2 = f.read()
    print(content2)
    print(list(content2))
    print(iter(content2))

print()
print('---------------------------------------')
print()


# 3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        # print(c)                                # print each line and print separately
        print(c.strip())

print()
print('---------------------------------------')
print()


# 4
with open('./resource/review.txt', 'r') as f:
    content4 = f.read()
    print('>', content4)
    content4 = f.read()
    print('>', content4)                        # cursor is at the end of file 'review.txt', therefore blank

print()
print('---------------------------------------')
print()


# 5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='****')
        line = f.readline()

print()
print('---------------------------------------')
print()


# 6
with open('./resource/review.txt', 'r') as f:
    content6 = f.readlines()                    # readlines: each line is saved into a list
    # print(content6)
    for c in content6:
        print(c, end= '&&&')

print()
print('---------------------------------------')
print()


# 7
    # mean of the scores in 'score.txt'
score = []
with open('./resource/score.txt', 'r') as f:
    for eachline in f:
        score.append(int(eachline))
    print(score)

print('average is: {:6.4}'.format(sum(score)/len(score)))       # note decimal point

print()
print('---------------------------------------')
print('---------------------------------------')
print()




# WRITE
    # recallName = open('./filedirectory/fileName', 'mode')
    # with open('./filedirectory/fileName', 'mode') as recallname


# 1
    # write mode
with open('./resource/text1.txt', 'w') as f:
    f.write('new file made from write mode\n')


# 2
    # append mode
with open('./resource/text1.txt', 'a') as f:
    f.write('appended line from append mode')


# 3 
from random import randint
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')


# 4
    # writelines: saves list as file
with open('./resource/text3.txt', 'w') as f:
    list = ['chandler\n', 'monica\n', 'phoebe\n']
    f.writelines(list) 


# 5
    # printing on the new write mode file instead of on the console
with open('./resource/text4.txt', 'w') as f:
    print('test printer 1', file=f)
    print('test printer 2', file=f)