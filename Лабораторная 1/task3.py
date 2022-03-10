"""
3. Дано два ненульових числа. Знайти суму, різницю, добуток і частку їх квадратів.
Іванова Дар'я 141 група
"""


def cheslo():
    a = float(input("введите a="))
    b = float(input("введите b="))
    if a != 0:
        c = a**2
    else:
        print("Ошибка")
    if b != 0:
        d = b ** 2
    else:
        print("Ошибка")
    sum = float(c+d)
    rez = float(c-d)
    dob = float(c*d)
    chast = float(c/d)
    return "sum(сума)=" + str(sum) + "\nrez(різниця)=" + str(rez) + "\ndob(добуток)=" + str(dob) + "\nchast(частка)=" + str(chast)


print(cheslo())
