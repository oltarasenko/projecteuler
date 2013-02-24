"""
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""


def simple_multiplies(number):
    """
    Returns all simple dividers of the given number
    Params:
       number - positive integer
    Returns
       Array of simple dividers.


    >>> simple_multiplies(8)
    [2, 2, 2]

    >>> simple_multiplies(9)
    [3, 3]

    >>> simple_multiplies(2)
    [2]
    """
    simples = []
    for x in range(2, number + 1):
        while number % x == 0:
            number = number / x
            simples.append(x)
    return simples


def array_merger(arr1, arr2):
    """
    Simple util to merge two arrays into one.

    >>> array_merger([1, 2, 3], [3, 4])
    [1, 2, 3, 3, 4]

    >>> array_merger([1, 2, 3], [])
    [1, 2, 3]
    """
    if len(arr2) > 0:
        for x in arr2:
            arr1.append(x)
    return arr1


def array_multiplier(array):
    """
    Simple util to multiply all values in array

    >>> array_multiplier([1, 3, 2])
    6

    >>> array_multiplier([22, 2])
    44

    """
    res = 1
    for x in array:
        res *= x
    return res


def divider_finder(max_value):
    """
    Function which calculates the smaller number which can be divided
    by any number from range of 2....max_value

    Uses approach of finding unique simple dividers. So presents
    each number of the range as an array of simple dividers which are needed
    to get the minimal divider.

    Exampls of such split are:
    4 --> [2, 2]
    6 --> [2, 2, 3, 5]
    8 --> [2, 2, 2, 3, 5, 7]
    """
    checked_simples = []
    for num in range(2, max_value + 1):
        to_append = []
        for simple in simple_multiplies(num):
            if simple not in checked_simples:
                to_append.append(simple)
            else:
                checked_simples.pop(checked_simples.index(simple))
                to_append.append(simple)
        array_merger(checked_simples, to_append)
    return array_multiplier(checked_simples)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print divider_finder(20)
    #print simple_multiplies(2)
