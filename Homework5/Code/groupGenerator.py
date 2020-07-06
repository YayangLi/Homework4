import numpy as np
def isPrimer(number):
    for j in range(2, number):
        if number % j == 0:
            return False
    return True

def primerChecker(numberRange):
    randList = np.random.choice(range(1, numberRange + 1), numberRange, replace=False)
    for i in range(numberRange):
        q = randList[i]
        p = 2 * q + 1
        if isPrimer(p) and isPrimer(q):
            return q, p

def addOperator(number1, number2, module):
    return (number1 + number2) % module

def getSubgroup(number, module):
    result = set()
    for i in range(1, module):
        times = i
        x = addOperator(number1=number, number2=number, module=module)
        while times > 0:
            times = times - 1
            x = addOperator(number1=number, number2=x, module=module)
            # print(x)
        result.add(x)
    return result


def generator(numberRange):
    q, p = primerChecker(numberRange=numberRange)
    print('q:{}'.format(q), 'p:{}'.format(p))
    randList = np.random.choice(range(1, p), p - 1, replace=False)
    # print(randList)
    for i in range(1, p):
        number = randList[i]
        result = getSubgroup(number=number, module=p)
        if len(result) == p - 1:
            print("生成元是:{}".format(number))
            break

    group_g = getSubgroup(number=number, module=p)
    return group_g

print(generator(100))


