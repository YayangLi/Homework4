import numpy as np
def isPrime(x):
    flag = True
    i = 2
    while i < x:
        if x % i == 0:
            flag = False
            return flag
        i += 1
    return flag

def getSubGroup(x):
    if not isPrime(x):
        print('输入不是质数')
        return
    group = set()
    num = np.random.randint(1, x-1, size=1)[0]

    for index in range(x):
        element = pow(num, index) % x
        print(element)
        group.add(element)

    return group

print(getSubGroup(17))