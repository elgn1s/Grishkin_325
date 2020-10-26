from random import *


def vvod(s):
    return input(s)


def vivod(elem):
    print(elem)


a1 = int(vvod('A1 '))
a2 = int(vvod('A2 '))
b1 = int(vvod('B1 '))
b2 = int(vvod('B2 '))


def createTuple(c, d):
    new_list = []
    for i in range(11):
        new_list.append(randint(c, d))
    return tuple(new_list)


tuple1 = createTuple(a1, a2)
tuple2 = createTuple(b1, b2)

vivod(tuple1)
vivod(tuple2)


def concatTuple(t1, t2):
    return t1 + t2


tuple3 = concatTuple(tuple1, tuple2)

vivod(tuple3)


def countZero(t):
    return t.count(0)


zero = countZero(tuple3)
vivod(zero)
