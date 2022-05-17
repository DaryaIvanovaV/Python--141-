"""
8. Дано дійсне A та ціле число N (> 0). Вивести 1 – A + A^2 – A^3 + ... + (–1)^N*A^N.
Іванова Дар'я
"""


def get_a():
    a = float(input("Введите a="))
    return a


def get_n():
    n = int(input("Введите n(степень)="))
    return check(n)


def check(n):
    if n <= 0:
        return get_n()
    else:
        return n


def foo(a: float, n: int):
    i = 1
    m = 1
    while i <= n:
        m = m + ((-1) ** i) * (a ** i)
        i += 1
    return m


def find():
    a = get_a()
    n = get_n()
    res = foo(a, n)
    return res


if __name__ == '__main__':
    result = find()
    print(result)
