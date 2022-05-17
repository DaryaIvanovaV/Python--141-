"""
9. Дано ціле число N (> 0). Знайти число, отримане при прочитанні числа N справа наліво та добуток його цифр.
Іванова Дар'я
"""


def get_n():
    n = int(input("Введите n="))
    return check(n)


def check(n):
    if 0 < n < 10:
        return get_n()
    else:
        return n


def foo(n: int):
    reverse = 0
    p = n
    dob = 1
    while p != 0:
        m = p % 10
        reverse = reverse * 10 + m
        p = int(p / 10)
        dob = dob * m
    return reverse, dob


def find():
    n = get_n()
    res, res2 = foo(n)
    return res, res2


if __name__ == '__main__':
    result, result2 = find()
    print("Переверная цифра=", result, "Добуток чисел=", result2)
