def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    else:
        print "result is", result
    finally:
        print "executing finally clause"

def divideNew(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    except TypeError:
        divideNew(int(x), int(y))
    else:
        print "result is", result
    finally:
        print "executing finally clause"


divide(3, 0)
# divide('3', '4')
print divideNew('3', '4')


print "-------------------------------"

"""
def FancyDivide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception, e:
        print e


FancyDivide([0, 2, 4], 0)
"""



def FancyDivide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [SimpleDivide(item, denom)
            for item in list_of_numbers]


def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError, e:
        return 0

print FancyDivide([0, 2, 4], 0)


def getRatios(v1, v2):
    """
    Assumes: v1 and v2 are lists of equal length of numbers
    ReturnsL a list containing the meaningful values of
    v1[i]/v2[i]
    """
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError ,e:
            print e
            ratios.append(float('NaN')) #NaN = Not a Number
        except:
            raise ValueError('getRatios called with bad arg')
    return ratios

try:
    print getRatios([1.0,2.0,7.0,6.0],
                    [1.0,2.0,0.0,3.0])
    print getRatios([],[])
    print getRatios([1.0,2.0], [3.0])
except ValueError, msg:
    print msg



