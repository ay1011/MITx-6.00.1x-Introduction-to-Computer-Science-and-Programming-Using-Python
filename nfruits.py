def nfruits(aDict, aStr):
    """
    Assumes: Python cannot eat more of a certain fruit than he has
    :param aDict:A non-empty dictionary containing type of fruit
                 and its quantity initially with Python
                 when he leaves home (length < 10)
    :param aStr: A string pattern of the fruits eaten by Python
                 on his journey as observed by Cobra.
    :return:     Maximum quantity out of the different types of fruits
                 that is available with Python when he has reached the campus.
    """
    # Create copy of dictionary
    aDict_copy = aDict.copy()
    for i in range(len(aStr)):
        # Reduce number of fruit just eaten
        aDict_copy[aStr[i]] -= 1
        # If not last fruit, add 1 to all other fruits
        if i < len(aStr) - 1:
            # Add 1 to all other fruits
            for key in aDict_copy.keys():
                aDict_copy[key] += 1
            # Minus 1 from fruit just eaten
            aDict_copy[aStr[i]] -= 1
    # Return maximum quantity of fruit
    return max(aDict_copy.values())

# Test
print nfruits({'C': 10, 'D': 7, 'J': 10, 'M': 8, 'L': 6, 'P': 6, 'T': 10, 'V': 8}, 'TTCM')


"""
def nfruits(aDict, aStr):
    '''
    Assumes: Python cannot eat more of a certain fruit than he has
    :param aDict:A non-empty dictionary containing type of fruit
                 and its quantity initially with Python
                 when he leaves home (length < 10)
    :param aStr: A string pattern of the fruits eaten by Python
                 on his journey as observed by Cobra.
    :return:     Maximum quantity out of the different types of fruits
                 that is available with Python when he has reached the campus.
    '''
    # Create copy of dictionary
    aDict_copy = aDict.copy()
    for i in range(len(aStr)):
        # Reduce number of fruit just eaten
        aDict_copy[aStr[i]] -= 1
        # If not last fruit, add 1 to all other fruits
        if i < len(aStr) - 1:
            # Add 1 to all other fruits
            for key in aDict_copy.keys():
                aDict_copy[key] += 1
            # Minus 1 from fruit just eaten
            aDict_copy[aStr[i]] -= 1
    # Return maximum quantity of fruit
    return max(aDict_copy.values())"""

"""
def nfruits(aDict, pattern):
    '''
        aDict: dictionary with the quantity of each fruit carried by Python
        pattern: string with the pattern of fruits eaten by Python

        retunrs: the maximum of the quantities of fruits of each type
    '''
    if len(pattern) == 1:
        aDict[pattern] -= 1
        return max(aDict.values())
    else:
        fruit = pattern[0]
        for key in aDict:
            if key == fruit:
                aDict[key] -= 1
            else:
                aDict[key] += 1
        return nfruits(aDict, pattern[1:])
"""


"""def nfruits(quantity, pattern):
    ''' Python Loves Fruits implementation.
        For full description look into assignment.
        Arguments:
        quantity -> dict
        non-empty dictionary containing type of fruit and its
        quantity initially with Python when he leaves home

        pattern -> str
        string pattern of the fruits eaten by Python on his journey
        as observed by Cobra
        Return value:
        return -> int
        maximum quantity out of the different types of fruits
        that is available with Python when he has reached the campus
    '''

    def eat(fruit):
        ''' Update quantity dictionary to
            decrease quantity of eaten fruit
        '''
        quantity[fruit] -= 1

    def buy_all_but(fruit):
        ''' Returns dictionary which reflects
            quantities after shopping.
            Uses fairly advanced dict comprehension technique.
            However, lecturer have used list comprehension
            in his slides already.

            We create new dictionary where we increment all quantities except
            for fruit Python have just eaten
        '''
        return {
            key: quantity[key] + 1 if key != fruit else quantity[key]
            for key in quantity
        }

    assert 0 < len(quantity) < 10, 'Length of quantity must be in 1 to 9 range'

    # while on journey to campus
    journey = pattern[:-1]
    for fruit in journey:
        # Python eats one fruit
        eat(fruit)
        # And buys one fruit of each other type
        quantity = buy_all_but(fruit)

    # just on reaching the campus
    in_campus = pattern[-1]
    # we eat last fruit
    eat(in_campus)
    # return the maximum quantity out of the different types
    # of fruits that is available with Python
    return max(quantity.values())"""