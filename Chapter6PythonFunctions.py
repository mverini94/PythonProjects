
x = 5

def f():
    x = 10

f()
print(x)

'''
default arguments in functions
'''

def replaceToInt(repString, base):
    '''
    converts the repString to an int in the base
    and returns this int
    '''
    decimal = 0
    exponent = len(repString) - 1
    for digit in repString:
        decimal = decimal + int(digit) * base ** exponent
        exponent -= 1
        return decimal

replaceToInt("10s", 10)
