from fixtures import fixtures
from record import record_result
from record import record_link_error

def main():
    with open('link.txt') as l:
        print('Парсер запущен, ожидайте')
        count = 0
        count_error = 0
        for i in [i.rstrip() for i in l.readlines() if len(i) > 3]:
            try:
                 # variable = i.split('/')
                 # res = fixtures(variable[4], variable[5])
                 # res = fixtures(variable[4], variable[5])
                 count += 1
                 res = fixtures(i)
                 record_result(res)
                 print(f'Ссылка №{count} - {i} (выполнено)')
            except Exception as e:
                count_error += 1
                record_link_error(i)
                print(f"Произошла ошибка - {e}. По ссылке {i}")
        print(f'Парсинг завершен, обработано {count} ссылок, из которых {count_error} завершилось ошибкой')



if __name__ == '__main__':
    main()