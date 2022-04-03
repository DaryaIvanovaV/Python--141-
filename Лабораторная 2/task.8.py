"""
8. Дано два цілих числа: D (день) і M (місяць), що визначають правильну дату невисокосного року.
Вивести значення D і M для дати, що передує зазначеній.
Іванова Дар'я 141 група
"""


def get(d: int, m: int):
    if d == 1 and m == 1:
        d = 31
        m = 12
    elif d == 1 and (m == 2 or m == 4 or m == 6 or m == 8 or m == 9 or m == 11):
        d = 32 - 1
        m -= 1
    elif d == 1 and m == 3:
        d = 29 - 1
        m -= 1
    elif d == 1 and (m == 5 or m == 7 or m == 10 or m == 12):
        d = 31 - 1
        m -= 1
    # проверка всех кроме первых дней
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 1 < d < 32:
            d -= 1
            m = m
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if 1 < d < 31:
            d -= 1
            m = m
    elif m == 2:
        if 1 < d < 29:
            d -= 1
            m = m
    s = "День= " + str(d) + "\nМесяц= " + str(m)
    return s


def check(d: int, m: int):
    while True:
        if 0 < m < 13:
            if m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                if 0 < d < 32:
                    break
                else:
                    print(d, "такого дня не существует")
                    d = int(input("Введите d(день)="))
            elif m == 1:
                if 0 < d < 32:
                    break
                else:
                    print(d, "такого дня не существует")
                    d = int(input("Введите d(день)="))
            elif m == 4 or m == 6 or m == 9 or m == 11:
                if 0 < d < 31:
                    break
                else:
                    print(d, "такого дня не существует")
                    d = int(input("Введите d(день)="))
            elif m == 2:
                if 0 < d < 29:
                    break
                else:
                    print(d, "такого дня не существует")
                    d = int(input("Введите d(день)="))
        else:
            print(m, "такого месяца не существует")
            m = int(input("Введите m(месяц)="))
    return d, m


def data(d: int, m: int):
    a, b = check(d, m)
    res = get(a, b)
    return res


if __name__ == '__main__':
    x = int(input("Введите d(день)="))
    y = int(input("Введите m(месяц)="))
    result = data(x, y)
    print(result)
