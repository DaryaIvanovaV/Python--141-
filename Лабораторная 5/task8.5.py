"""
8. Описати функцію Count2(x) – кількість різних простих дільників числа х. Скласти програму пошуку тих чисел в наборі з
6 чисел, що мають k різних простих дільників.
Іванова Дар'я
"""


def check(x1):
    b = 1
    d = 0
    while b <= x1:
        if x1 % b == 0:
            d += 1
        b += 1
    return d


def Count2(x1):
    res = check(x1)
    return res


if __name__ == '__main__':
    k = int(input("Введте k="))
    a = 0
    while a != 6:
        x = list(map(int, input("Введите 6 цифр в строку(через пробел): ").split()))
        a = len(x)
    for i in range(6):
        result = Count2(x[i])
        if k == result:
            print(x[i])
        else:
            print("x делителей не равно k")
