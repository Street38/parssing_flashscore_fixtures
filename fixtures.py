import requests
from datetime import datetime

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def fixtures(id):
    liga_key = {}
    list_data = [{}]
    result_list = []
    # url = 'https://d.flashscore.com/x/feed/pnf_Iw7eKK25'                                                              # News
    # url = f'https://www.flashscore.com/team/{team}/{id}/fixtures/'
    url = f'https://www.flashscore.com/r/?t=3&id={id}'
    response = requests.get(url, headers=headers)
    s_1 = (response.text).replace('SA÷1¬', 'smart_slice')
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
            key_team_request = id
            # team_request = team
            timestap = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            country = (i.get('~ZA')).split(':')[0]
            liga = (i.get('~ZA')).split(':')[1]
            date_game = datetime.utcfromtimestamp(int(i.get('AD'))).strftime('%Y-%m-%d %H:%M:%S')
            # team_1 = i.get('CX')
            # key_tim_1 = i.get('JB')
            # team_2 = i.get('FK')
            # key_tim_2 = i.get('PY')
            result_list.append(
                # [key_team_request, team_request, timestap, country, liga, date_game, team_1, key_tim_1, team_2, key_tim_2])
                [key_team_request, timestap, country, liga, date_game])

    # print(result_list)
    return result_list


if __name__ == '__main__':
    fixtures('4jcj2zMd')
