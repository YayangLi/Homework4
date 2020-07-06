import numpy as np
'''
 generator of Z*p
'''
def primeGenerator(numberRange):
    while True:
        randomNumber = np.random.randint(0, numberRange, size=1)[0]
        if isPrimer(number=randomNumber):
            return randomNumber

def isPrimer(number):
    for j in range(2, number):
        if number % j == 0:
            return False
    return True
# print('质数:{}'.format(primeGenerator(numberRange=100)))

def addOperator(number1, number2, module):
    return (number1 + number2) % module

def mutiplyOperator(number1, number2, module):
    return (number1 * number2) % module


def getSubgroup(number, module):
    result = set()
    for i in range(1, module):
        times = i
        x = mutiplyOperator(number1=number, number2=number, module=module)
        while times > 0:
            times = times - 1
            x = addOperator(number1=number, number2=x, module=module)
            # print(x)
        result.add(x)
    return result

def getGenerator(module):
    randList = np.random.choice(range(1, module), module - 1, replace=False)
    # print(randList)
    for i in range(1, module):
        number = randList[i]
        result = getSubgroup(number=number, module=module)
        if len(result) == module - 1:
            print("生成元是:{}".format(number))
            break

def main():
    getGenerator(module=11)

if __name__ == '__main__':
    main()


# x = getSubgroup(number=5, module=11)
# print('元素为:{}'.format(x))
# print('阶:{}'.format(len(x)))
