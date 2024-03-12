import csv


def search(iid, data):
    for stroka in data:
        if stroka[2] == iid:
            return stroka
    return None


# открываем файл students.csv
with open('students.csv') as f:
    data = list(csv.reader(f, delimiter=';'))

    iid = input()
    while iid != 'СТОП':
        res = search(iid, data)
        if res is None:
            print('Ничего не найдено')
        else:
            print(f'Проект № {iid} делал: {res[1]} он(а) получил(а) оценку - {res[-1]}')
        iid = input()
