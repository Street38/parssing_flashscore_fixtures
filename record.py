import csv


def record_html(html):  # Сохраняем забранный HTML в файл, для дальнейшей работы с ним
    with open('test2.html', mode='w', newline='', encoding="utf-8") as r:
        r.write(html)


def record_result(list_value):
    with open('result.csv', mode='a', newline='', encoding="utf-8") as r:
        writer = csv.writer(r, delimiter=";")
        for i in list_value:
            writer.writerow(i)


def record_link_error(list_value):
    with open('link_error.csv', mode='a', newline='', encoding="utf-8") as r:
        writer = csv.writer(r, delimiter=";")
        writer.writerow(list_value.split(','))
