"""
По варіантах - завдання #1
1.Назви та ПІП керівників в файл rectors.csv
По варіантах - завдання #2
3.З посадою керівника Ректор
Завдання 3
Ускладніть програму з другого завдання можливістю фільтрування за будь-яким з наявних значень поля
Іванова Дар'я
"""
import requests
import csv


def get_region():
    c = ["01", "05", "07", "12", "14", "18", "21", "23", "26", "32", "35", "44", "46", "48", "51", "53", "56", "59", "61",
         "63", "65", "68", "71", "73", "74", "80", "85"] # коды регионов
    print("Выбирите код региона из списка:" + str(c))
    region = str(input("Введите код региона:"))
    return check(region, c)


def check(region, c):
    i = region in c # смотрим есть ли код ргиона который ввели в списке
    if i is False:
        print("Код не верный. Введите другой код:")
        return get_region()
    else:
        return region


def req(region):
    r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=' + region + '&exp=json')
    try:
        universities: list = r.json()
    except Exception as ex:
        return print("Не удалось получить доступ к учреждениям региона {}".format(region)), exit(0)
    return universities


def zvo(universities, region):
    with open('universities.csv', mode='w', encoding='CP1251') as f: # Зберегти всі дані у файл universities.csv у форматі csv CP1251 - чтобы убрать иероглефы
        writer = csv.DictWriter(f, fieldnames=universities[0].keys())
        writer.writeheader()
        writer.writerows(universities)

    with open('universities' + region + '.csv', mode='w', encoding='CP1251') as fw: # Збережіть ті ж дані у файл universities_<код регіону>.csv, наприклад universities_80.csv
        writer = csv.DictWriter(fw, fieldnames=universities[0].keys())
        writer.writeheader()
        writer.writerows(universities)


def posad():
    varian = 0
    while varian != 1 and varian != 2 and varian != 3 and varian != 4 and varian != 5 and varian != 6 and varian != 7:
        varian = int(input("""
Выберите номер для фильтра должности управляющих :
1: Керівник
2: Декан
3: Директор
4: Начальник
5: Ректор
6: В.о. ректора
7: В.о. директора
"""))
        if varian == 1:
            f = "Керівник"
        elif varian == 2:
            f = "декан"
        elif varian == 3:
            f = "директор"
        elif varian == 4:
            f = "начальник"
        elif varian == 5:
            f = "Ректор"
        elif varian == 6:
            f = "В.о. ректора"
        elif varian == 7:
            f = "В.о. директора"
        fl = 'university_director_post' # где нужно искать
        flt = " З посадою " + f # будет ввыводиться на экран для удобнсти
        return f, fl, flt


def filt(universities, region, f, fl, flt):
    try:
        fltr = [{k: row[k] for k in ['university_name', 'university_name_en', 'university_director_fio', fl]} for row in list(filter(lambda x: x[fl].casefold() == f.casefold(), universities))]
    except Exception as ex:
        return print("цей регіон {} не має університетів " + str(flt).format(region)), 0
    if len(fltr) == 0:
        return print("цей регіон {} не має університетів " + str(flt).format(region)), 0
    return fltr, 1


def zvo_filt(fltr, i):
    if i == 1:
        with open('rectors.csv', mode='w', encoding='CP1251') as fw:
            writer = csv.DictWriter(fw, fieldnames=fltr[0].keys())
            writer.writeheader()
            writer.writerows(fltr)
        return print("Успешная загрузка")
    else:
        return print("Загрузка не удалась")


def main():
    region = get_region()
    universities = req(region)
    zvo(universities, region)
    f, fl, flt = posad()
    fltr, i = filt(universities, region, f, fl, flt)
    zvo_filt(fltr, i)


main()
