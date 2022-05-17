"""
13. Дано ціле число N (> 0). Знайти квадрат даного числа, використовуючи для його обчислення наступну формулу:
N2 = 1 + 3 + 5 + ... + (2 • N - 1).
Після додавання до суми кожного доданка виводити поточне значення суми (в результаті будуть виведені квадрати всіх цілих
чисел від 1 до N).
Іванова Дар'я
"""


def get_n():
    n = int(input("Введите n="))
    return check(n)


def check(n):
    if n <= 0:
        return get_n()
    else:
        return n


def foo(n: int):
    i = 1
    m = 0
    while i <= n:
        m = m + ((2 * i)-1)
        print("Поточное значение суммы=", m)
        i += 1
    return m


def find():
    n = get_n()
    res = foo(n)
    return res


if __name__ == '__main__':
    result = find()
    print("Результат =", result)
