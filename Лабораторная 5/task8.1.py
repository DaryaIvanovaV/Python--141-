"""
8. Описати функцію AddRightDigit (D, K), що додає до цілого позитивного числа K праворуч цифру D (D - вхідний параметр
цілого типу, що лежить в діапазоні 0-9, K - параметр цілого типу, який є одночасно вхідним і вихідним). За допомогою
цієї функції послідовно додати до цього числа K праворуч дані цифри D1 і D2, виводячи результат кожного додавання.
Іванова Дар'я
"""


def get_k():
    k = int(input("Введите k (k>0)="))
    return check_k(k)


def get_d1():
    d1 = int(input("Введите d1 (d1 от 0 до 9)="))
    return check_d1(d1)


def get_d2():
    d2 = int(input("Введите d2 (d2 от 0 до 9)="))
    return check_d2(d2)


def check_d1(d1):
    if 0 < d1 > 9:
        return get_d1()
    else:
        return d1


def check_d2(d2):
    if 0 < d2 > 9:
        return get_d2()
    else:
        return d2


def check_k(k):
    if k < 0:
        return get_k()
    else:
        return k


def foo(k: int):
    a = k
    d1 = get_d1()
    a = a * 10 + d1
    b = k
    d2 = get_d2()
    b = b * 10 + d2
    return a, b

def AddRightDigit():
    k = get_k()
    res1, res2 = foo(k)
    return res1, res2


if __name__ == '__main__':
    result1, result2 = AddRightDigit()
    print("k(c d1)=", result1, "k(c d2)=", result2)
