# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


def apply_discount(product, discount):
    price = int(product['цена'] * (1.0 - discount))
    assert 0 <= price <= product['цена']
    return price


shoes = {'имя': 'Модные туфли', 'цена': 14900}


class FirstClass:
    title = "hi"

    def __init__(self):
        print("init suka")

    def setValue(self, value):
        self.title = value

    def printValue(self):
        print(self.title)

    def printTitle(self):
        print(FirstClass.title)


# отсечка
class super8:
    def hello(self):
        self.data1 = 'spam'


class sub(super):
    def hola(self):
        self.data2 = 'eggs'


'''
sf
'''


def sortin():
    data = []
    data.append(8)
    data.append(2)
    data.append(14)
    while data:
        index = len(data) - 1
        max = data[index]
        for i, v in enumerate(data):
            if max < v:
                max = v
                index = i
        print(max)
        del data[index]

    # Press the green button in the gutter to run the script.


def programmer():
    for i in range(1001):
        number = i
        if (number == 1 or (
                not (number // 10 in [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]) and ((number % 10) % 10 == 1))):
            print(str(number) + " программист")
        elif (not (number % 100 in [11, 12, 13, 14]) and (number % 10 in [2, 3, 4])):
            print(str(number) + " программиста")
        else:
            print(str(number) + " программистов")


def test(a, b=[]):
    b.append(a)
    print(b)


def test_s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    print(res)


def my_first_decorator(function):
    def excusmi(*args):
        print("Я получил аргументы")
        print(type(args))
        print("Заранее сори")
        function(*args)
        print("Ну случилось")
    return excusmi


class BadWord(object):
    def __init__(self):
        self.age = "Suka"

    @my_first_decorator
    def getWold(self):
        print(self.age)


if __name__ == '__main__':
    BadWord().getWold()
