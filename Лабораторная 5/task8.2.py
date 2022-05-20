"""
8. Описати функцію Quarter (x, y) цілого типу, яка визначає номер координатної чверті, в якій знаходиться точка з
ненульовими дійсними координатами (x, y). За допомогою цієї функції знайти номери координатних чвертей для трьох точок
з даними ненульовими координатами.
Іванова Дар'я
"""


def check(x: int, y: int):
    s = " "
    if x > 0 and y > 0:
        s += "Первая координатная четверть"
        return s
    elif x < 0 and y > 0:
        s += "Вторая координатная четверть"
        return s
    elif x < 0 and y < 0:
        s += "Третья координатная четверть"
        return s
    elif x > 0 and y < 0:
        s += "Четвертая координатная четверть"
        return s
    elif x == 0 and y == 0:
        s += "Центр координат"
        return s
    else:
        s += "Принадлижат оси x,y"
        return s


def Quarter(x: int, y: int):
    res = check(x, y)
    return res


if __name__ == '__main__':
    for i in range(3):
        a = int(input("Введте x="))
        b = int(input("Введите y="))
        result = Quarter(a, b)
        print(result)
