"""
13. Дані координати двох протилежних вершин прямокутника: (x1, y1), (x2, y2). Сторони
прямокутника паралельні до осів координат. Знайти периметр і площу даного прямокутника.
Іванова Дар'я 141 група
"""


def rectangle():
    x1 = float(input("введите x1="))
    y1 = float(input("введите y1="))
    x2 = float(input("введите x2="))
    y2 = float(input("введите y2="))
    a = float(x2-x1)
    b = float(y2-y1)
    p = float(2*(a+b))
    s = float(a*b)
    return "p(периметр прямоугольника)=" + str(p) + "\ns(площадь прямоугольника)=" + str(s)

print(rectangle())
