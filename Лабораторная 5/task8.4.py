"""
8. Описати функцію Arctg1 (x, ε) дійсного типу (параметри x, ε - дійсні, | x | <1, ε>0),
знаходить наближене значення функції arctg (x):
arctg (x) = x - x3 / 3 + x5 / 5 - ... + (-1) n · x2 · n + 1 / (2 · n + 1) + ....
В сумі враховувати всі складові, модуль яких більше ε. За допомогою Arctg1 знайти наближене значення arctg (x) для
даного x при шести даних ε.
Іванова Дар'я
"""
from math import fabs


def check(x1, e1):
    n = 1
    a = 1
    r = x1
    while fabs(a) >= e1:
        a = ((-1**n)*(x1**((2*n)+1)))/((2*n)+1)
        if fabs(a) >= e1:
            r = r + a
        n += 1
    return a


def Arctg1(x1, e1):
    res = check(x1, e1)
    return res


if __name__ == '__main__':
    x = float(input("x="))
    while fabs(x) > 1:
        x = float(input("x="))
    for i in range(6):
        e = float(input("e= "))
        while e < 0:
            e = float(input("e= "))
        result = Arctg1(x, e)
        print(result)
