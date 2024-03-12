import csv


# открываем файл students.csv
with open('students.csv') as f, open('student_new.csv', 'w') as nf:
    data = list(csv.reader(f, delimiter=';'))
    chel = 'Гарный Никита'
    # print(*data, sep='\n')

    # ищем в файле нужного пользователя
    a = []
    for stroka in data[1:]:
        if chel in stroka:
            print(f'Ты получил: {stroka[-1]}, за проект - {stroka[2]}')
        if stroka[-1] != '':
            a.append(int(stroka[-1]))
    mean = round(sum(a) / len(a), 3)

    # перезаписываем данные, заполняя пропуски
    res = csv.writer(nf, delimiter=';')
    for stroka in data:
        if stroka[-1] == '':
            stroka[-1] = str(mean)
        res.writerow(stroka)
