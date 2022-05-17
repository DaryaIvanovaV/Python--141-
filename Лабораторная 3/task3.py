"""
3. Визначити, чи є задане натуральне число паліндромом, тобто таким, десяткова запис якого читається однаково зліва
направо і справа наліво.
Іванова Дар'я
"""


def get_n():
    n = int(input("Введите n(от 10)="))
    return check(n)


def check(n):
    if 0 < n < 10:
        return get_n()
    else:
        return n


def foo(n: int):
    reverse = 0
    p = n
    while p != 0:
        m = p % 10
        reverse = reverse * 10 + m
        p = int(p / 10)
    s = " "
    if n == reverse:
        s += "палиндром"
    else:
        s += "НЕ палиндром"
    return s


def palindrom():
    n = get_n()
    res = foo(n)
    return res


if __name__ == '__main__':
    result = palindrom()
    print(result)
