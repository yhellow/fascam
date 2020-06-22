# Section10
# exceptions / error

# error types: 
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError..
# 문법적으로 에러가 없지만 runtime 코드 실행 프로세스에서 발생하는 예외 처리 중요


# SyntaxError:
    # grammar error
    # missing/wrong syntax :, ', ", ], }, etc.
"""
    print('error)
    if True
        pass
"""


# NameError:
    # cannot find relevant variable 
"""
   here1 = 0 
   here2 = 9
   print(nothere)
"""


# ZeroDivisionError:
    # division by 0
"""
    print(10/0)
"""


# IndexError:
    # wrong index range
"""
    x = [10, 20, 30]
    print(x[0])
    print(x[3])
"""


# KeyError
    # nonexisting key recall
"""
    dic = {'name': 'chandler', 'age': 30, 'partner': 'monica'}
    print(dic['hobby'])
"""
dic = {'name': 'chandler', 'age': 30, 'partner': 'monica'}
    # to prevent KeyError safely use '.get()'
print(dic.get('hobby'))


# AttributeError
    # non existing module, class recall
"""
    import time
    print(time.time())
    print(time.month())
"""


# ValueError
    # nonexisting value recall
"""
    x = [1, 5, 9]
    x.remove(10)
    x.index(10)
"""


# FileNotFoundError
"""
    f = open('test.txt', 'r')
"""


# TypeError
    # datatype related error
"""
    x = [1, 2]
    y = (1, 2)
    z = 'test'

    print(x + y)
    print(x + z)
"""


# DEALING WITH ERRORS
# EAFP coding: easier to ask for forgiveness than permission
"""
    try: running codes that may return errors
    except: error1
    except: error2
    else: run if no errors were found
    finally: run regardless
"""


# e.g.1
    # specific except errors
friends1 = ['chandler', 'phoebe', 'rachel']

try: 
    z = 'chandler'
    x = friends1.index(z)
    print('{} was found {}'.format(z, x+1))
except ValueError:
    print('not found: ValueError')
else: 
    print('no errors were found')
print()


# e.g.2
    # catching unexpected errors
friends2 = ['monica', 'ross', 'joey']

try: 
    z = 'joe'
    x = friends2.index(z)
    print('{} was found {}'.format(z, x+1))
except:
    print('error')
print()


# e.g.3
    # 'finally'
friends3 = ['tag', 'julie', 'katie']

try: 
    z = 'richard'
    x = friends3.index(z)
    print('{} was found {}'.format(z, x+1))
except:
    print('error')
finally:
    print('still running')
print()


# e.g.4
    # often used coding pattern
    # run a code regardless of catching any errors
try: 
    print('try printing this')
finally:
    print('success or not print this too')
print()


# e.g.5
    # finally
friends5 = ['richard', 'katie', 'nicetoothguy']

try: 
    z = 'who'
    x = friends5.index(z)
    print('{} was found {}'.format(z, x+1))
except IndexError as i:             # as '': python spells out the error
    print(i)
except ValueError as e:             # as '': python spells out the error
    print(e)
except Exception:                   # put Exception last so the known errors are caught before and Exception is used as a safety net
    print('error')
finally:
    print('still running')
print()


# e.g.6
    # raise
    # formulating errors to catch these errors that may occur 

try:
    a = 'richard'
    if a == 'rich':
        print('access given')
    else: 
        raise ValueError
except ValueError:
    print('no access')
except Exception as f:
    print(f)
else:
    print('through')