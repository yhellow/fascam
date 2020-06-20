# Section04-2
# string, string operations, slicing


# string commands
str1 = "A cheeseburger"
str2 = "has cheese"
str3 = ""
str4 = " "
str5 = str()
str6 = str('stringcheese')
    # length of the string
print(len(str1), len(str2))
    # includes spaces
print(len(str3), len(str4))
    # 'str()' is an empty string
    # even for strings that only include alphabets, '' or "" has to be inside 'str()'
print(len(str5), len(str6))
print()


# escape strings
esc_str1 = "\"android\" is a type of cheeseburger"
esc_str2 = "go from \t one tab \t to another"
    # '\"'
print(esc_str1)
    # '\t'
print(esc_str2)
print()


# raw string
    # starts with a lowercase 'r'
    # '' or "" both work
raw_s1 = r"C:\Programs\Test\Bin"
raw_s2 = r"\\a\\a"
    # escape doesn't run on a raw string
print(raw_s1)
print(raw_s2)
print()


# multiline
    # have to command the escape '\' for python to recognize multilines
multi1 = \
"""
multiline 
tester
"""
print(multi1) 
print()


# string operations
so1 = "*"
so2 = "abc"
so3 = "def"
so4 = "cheeseburger"
    # addition of a string joins the strins
print(so2 + so3)
    # multiplication of a string is a repetition of the string
print(so1 * 100)
    # cannot add string with integer
# print(so1 + 3)
    # !! multiplication with an integer works but addition with integer doesn't 
    # 'in' operation: is '' included in the variable
print('a' in so4)
print('c' in so4)
    # 'not in' operation: is '' not included in the variable
print('a' not in so4)
print('c' not in so4)
print()


# changing string data type
    # for integers, '' or "" doesn't have to be inside 'str()'
    # to add integers with strings, the integer has to be inserted as a string data type
print(str(77))
print(str(10.4))
print(str(77) + 'a')
print()


# string functions
# python string fuctions: https://www.w3schools.com/python/python_ref_string.asp
"""
    capitalize()	Converts the first character to upper case
    casefold()	Converts string into lower case
    center()	Returns a centered string
    count()	Returns the number of times a specified value occurs in a string
    encode()	Returns an encoded version of the string
    endswith()	Returns true if the string ends with the specified value
    expandtabs()	Sets the tab size of the string
    find()	Searches the string for a specified value and returns the position of where it was found
    format()	Formats specified values in a string
    format_map()	Formats specified values in a string
    index()	Searches the string for a specified value and returns the position of where it was found
    isalnum()	Returns True if all characters in the string are alphanumeric
    isalpha()	Returns True if all characters in the string are in the alphabet
    isdecimal()	Returns True if all characters in the string are decimals
    isdigit()	Returns True if all characters in the string are digits
    isidentifier()	Returns True if the string is an identifier
    islower()	Returns True if all characters in the string are lower case
    isnumeric()	Returns True if all characters in the string are numeric
    isprintable()	Returns True if all characters in the string are printable
    isspace()	Returns True if all characters in the string are whitespaces
    istitle()	Returns True if the string follows the rules of a title
    isupper()	Returns True if all characters in the string are upper case
    join()	Joins the elements of an iterable to the end of the string
    ljust()	Returns a left justified version of the string
    lower()	Converts a string into lower case
    lstrip()	Returns a left trim version of the string
    maketrans()	Returns a translation table to be used in translations
    partition()	Returns a tuple where the string is parted into three parts
    replace()	Returns a string where a specified value is replaced with a specified value
    rfind()	Searches the string for a specified value and returns the last position of where it was found
    rindex()	Searches the string for a specified value and returns the last position of where it was found
    rjust()	Returns a right justified version of the string
    rpartition()	Returns a tuple where the string is parted into three parts
    rsplit()	Splits the string at the specified separator, and returns a list
    rstrip()	Returns a right trim version of the string
    split()	Splits the string at the specified separator, and returns a list
    splitlines()	Splits the string at line breaks and returns a list
    startswith()	Returns true if the string starts with the specified value
    strip()	Returns a trimmed version of the string
    swapcase()	Swaps cases, lower case becomes upper case and vice versa
    title()	Converts the first character of each word to upper case
    translate()	Returns a translated string
    upper()	Converts a string into upper case
    zfill()	Fills the string with a specified number of 0 values at the beginning
"""

# string command e.g.
a = "cheeseburger"
b = "CHEESEBURGER"
print(a.islower())
print(b.islower())
print(a.endswith('r'))
    # letter cases matter
print(b.endswith('r'))
print(a.capitalize())
print(a.replace('cheese', 'chicken'))
    # reversed() work on lists 
    # use ('').join() to join a list into a single string
print(list(reversed(b)))
print(('').join(list(reversed(b))))
print()


# slicing: printing partial strings
    # the first letter is number 0
    # [a:b] : returns letters from a to b-1, length is b-a
print(a[0:3])
print(a[0:11])
print(a[0:12]) 
    # to make this easier
print(a[0:len(a)])
    # blanks assume start to end
    # !! no direction
print(a[:])
    # third option: skipping letters
    # positive slicing
print(a[::2])
print(a[1::2])
print(a[::1])
    # minus
    # takes out n letters from '-n'
print(a[0:-2])
print()
    # negative slicing
print(a[::-1])
print(a[::-2])
print()


# deleting immutables
    # del immutableVar

