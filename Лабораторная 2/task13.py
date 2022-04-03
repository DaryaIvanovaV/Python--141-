"""
13. За довжинами трьох відрізків, введених користувачем, визначити можливість існування
трикутника, складеного з цих відрізків. Якщо такий трикутник існує, то визначити, чи є він
різнобічним, рівнобедреним або рівностороннім.
Іванова Дар'я 141 група
"""


def check(a: float, b: float, c: float):
    while True:
        if a + b > c and b + c > a and a + c > b:
            break
        else:
            print("Треугольник не существует")
            a = int(input("Введите a="))
            b = int(input("Введите b="))
            c = float(input("Введите c="))
    return a, b, c


def get(a: float, b: float, c: float):
    s = ""
    if a == b == c:
        s += "Треугольник равносторонний"
    elif a != b and a != c and b != c:
        s += "Треугольник  разносторонний"
    elif a == b != c or a == c != b or b == c != a:
        s += "Треугольник равнобедренный"
    return s


def triangle(a: float, b: float, c: float):
    n, m, d = check(a, b, c)
    res = get(n, m, d)
    return res


if __name__ == '__main__':
    x = float(input("Введите a="))
    y = float(input("Введите b="))
    z = float(input("Введите c="))
    result = triangle(x, y, z)
    print(result)
