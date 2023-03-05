import requests
from bs4 import BeautifulSoup
from datetime import datetime


with open('test2.html', encoding="utf-8") as p:
    pattern = p.read()
    liga_key = {}
    list_data = [{}]
    result_list = []
    s_1 = pattern.replace('SA÷1¬', 'smart_slice')
    s_2 = s_1.replace('allEventsCount', 'smart_slice')
    res = (s_2.split('smart_slice')[1]).split('¬')


    for i in res[:-2]:
        key = i.split('÷')[0]
        value = i.split('÷')[1]
        if '~ZA' in key:
            liga_key[key] = value
        elif '~AA' in key:
            list_data.append({key: value})
            list_data[-1].update(liga_key.items())
        else:
            list_data[-1].update({key: value})


    for i in list_data:
        if i.get('~AA'):
            timestap = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            country = (i.get('~ZA')).split(':')[0]
            liga = (i.get('~ZA')).split(':')[1]
            date_game = datetime.utcfromtimestamp(int(i.get('AD'))).strftime('%Y-%m-%d %H:%M:%S')
            team_1 = i.get('CX')
            key_tim_1 = i.get('JB')
            team_2 = i.get('FK')
            key_tim_2 = i.get('PY')
            result_list.append([timestap, country, liga, date_game, team_1, key_tim_1, team_2, key_tim_2])
    print(result_list)