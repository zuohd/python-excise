'''
unit test-for function/class or module validation

test result:
1.unit test passed means tested funcion is correct
2.unit test unpassed means tested function has bug or test condition is wrong.

'''
import doctest


def myAdd(x, y):
    '''
    get the added result
    :param x: first number
    :param y: second number
    :return: result which two num added

    example:
    >>> print(myAdd(1,2))
    3
    '''
    return x + y


def mySub(x, y):
    return x - y


# print(myAdd(1, 2))

doctest.testmod()
