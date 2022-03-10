"""
9. Дано двозначне число. Знайти суму і добуток його цифр.
Іванова Дар'я 141 група
"""


def dvozcheslo():
    a = float(input("введите a="))
    if a > 9 and a <= 99:
        b = a//10
        c = a%10
    else:
        print("Ошибка")
    sum = int(b+c)
    dob = int(b*c)
    return "sum(сума)=" + str(sum) + "\ndob(добуток)=" + str(dob)


print(dvozcheslo())
