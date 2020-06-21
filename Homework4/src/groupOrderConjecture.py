def isPrime(x):
    flag = True
    i = 2
    while i < x:
        if x % i == 0:
            flag = False
            return flag
        i += 1
    return flag

def test(x):
    if not isPrime(x):
        print('输入不是质数')
        return
    group_d, group_tri = set(), set()

    for index in range(x):
        element_d = pow(index, 2) % x
        element_tri = pow(index, 3) % x
        group_d.add(element_d)
        group_tri.add(element_tri)

    return group_d, group_tri

group_d, group_tri = test(17)
print('平方之后群:{}'.format(group_d), '阶:{}'.format(len(group_d)))
print('立方之后群:{}'.format(group_tri), '阶:{}'.format(len(group_tri)))