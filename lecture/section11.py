# Section11
# excel, csv
# managing external files
    # r, w csv files
# package install
    # excel files: xsl, xlsx    
    # csv: mime - text/csv


# CSV ----------------------------------------------------------------------------
    # fileVariable = csv.reader(file) / fileVariable = csv.DictReader(file)
    # fileVariable = csv.writer(file) / fileVariable.writerow(rowValue) / fileVariable.writerows(rowValue)

import csv                          # to read csv files

import sys
# import pprint
from importlib import reload
reload(sys)
print(sys.getdefaultencoding())

print()
# str.decode('oxb9').encode('utf-8')



# e.g.1
with open('./resource/sample1.csv', encoding= 'korean') as f:      
        # add encoding= 'language' to decode new language 
    reader = csv.reader(f)          # note difference with txt file: 'read = f.read()'
    next(reader)                    # header skip: next(pushes the cursor for one take)

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)
print()



# e.g.2
    # reading csv files with modified import 
with open('./resource/sample2.csv', encoding='korean') as f:    
    reader = csv.reader(f, delimiter= '|')      # delimiter= '|' to separate the strings with |              
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()


    for c in reader:
        print(c)                    # | didn't separate the cells and recalled entire line as a single string
print()



# e.g.3
    # dictionary change
with open('./resource/sample2.csv', encoding='korean') as f:
    reader = csv.DictReader(f, delimiter= '|')      #reader for dictionaries: assigning the key to each value

    for c in reader:                                # for each row 
        for k, v in c.items():                      # printing each key value one by one
            print(k, v)
        print('-----------------------------')



# e.g.4
    # inserting rows with for loops
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
with open('./resource/sample3.csv', 'w') as f:       # 'with open() as X:' and '
    wt = csv.writer(f)                               # .writer()' both adds a new line
                                                     # fix with adding a 'newline= ''' into 'open()'
    for v in w: 
        wt.writerow(v)



# e.g.5
    # inserting rows without for loops
with open('./resource/sample4.csv', 'w') as f:
    wt = csv.writer(f)
    wt.writerows(w)             # writerow: inspecting filters foreach row / writerows: no need for filters
print()



# XSL, XLSX ----------------------------------------------------------------------------
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas used most: because uses the most used (openpyxl, xlrd) within
# pip install xlrd
# pip install openpyxl
# pip install pandas
    # fileVariable = pd.read_excel('file')
    # fileVariable.to_excel()
import pandas as pd
    # options to put in 'pd.read_excel()'
    # sheetname= sheet name or nubmer, header= assiging header, skiprow= the number of the row to skip
xlsx = pd.read_excel('./resource/sample.xlsx')
    # data check
print(xlsx.head())          # head(): showing the first rows
print()
print(xlsx.tail())          # tail(): showing the last rows
print()
print(xlsx.shape)           # shape(): rows, columns
print()

# writing excel or csv
xlsx.to_excel('./resource/result.xlsx', index= False)       # index= true/false: giving index to the rows
xlsx.to_csv('./resource/result.csv', index= False)       # index= true/false: giving index to the rows
