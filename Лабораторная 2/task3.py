"""
3. Дано три числа. Знайти суму двох найбільших з них.
Іванова Дар'я 141 група
"""


def get(a: float, b: float, c: float):
    minim = min(a, b, c)
    maxim = max(a, b, c)
    cen = (a + b + c) - (maxim - minim)
    d = cen + maxim
    s = "сума= " + str(d)
    return s


def number(a: float, b: float, c: float):
    res = get(a, b, c)
    return res


if __name__ == '__main__':
    x = float(input("Введите a="))
    y = float(input("Введите b="))
    z = float(input("Введите c="))
    result = number(x, y, z)
    print(result)
