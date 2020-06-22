# prints.py module


def prt1():
    print('sth significant')

def prt2():
    print('sth insignificant')


# testing the package file only within the file as a test:
    # doesn't run on other files that import this package
if __name__ == '__main__':
    prt1()
    prt2()