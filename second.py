import math

_her = 1


def print_hi():
    while True:
        reply = raw_input("Enter texr:")
        if reply == 's':
            break
        print(int(reply) ** 57)
    print(99999)


def printP():
    __u = 1
    while __u:
        __u = 0
        print("0")
    else:
        print('1')


def printFor():
    _o = 0
    for x in [1, 2, 3]:
        _o += x
    else:
        print(_o)


def excel(N):
    def action(X):
        return X * N

    return action


def gena(M):
    for i in range(M):
        yield i ** 2


# ////////////////////
class Set:
    def __init__(self, value=[]):
        self.data = value[:]
        self.concat(value)

    def concat(self, value):
        for x in value:
            self.data.append(x)
        print(self.data)

    def __len__(self): return 70


# /////////////////////////
class SuperA(object):
    x = 1


class SuperB(SuperA): pass


class SuperC(SuperA):
    x = 2


class D(SuperB, SuperC): pass


# ////
class exceptr(): pass


def getErrors():
    raise exceptr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v = 0
    def tt():
        while True:
            global v
            v += 1
            if v == 5:
                return True


    print(tt())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
