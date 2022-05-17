"""
18. Дано ціле число N (> 0). Використовуючи операції ділення без остачі і взяття залишку від ділення, вивести всі його
цифри, починаючи з самої правої (розряду одиниць).
Іванова Дар'я
"""


def get_n():
    n = int(input("Введите n="))
    return check(n)


def check(n):
    if n < 0:
        return get_n()
    elif 0 < n < 10:
        return n
    else:
        return n


def foo(n: int):
    while n % 10 != 0:
        print(n % 10)
        check(n)
        n = n // 10
    return n


def find():
    n = get_n()
    res = foo(n)
    return res


if __name__ == '__main__':
    result = find()
