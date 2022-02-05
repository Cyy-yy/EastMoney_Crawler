# -*- coding: utf-8 -*-
# author: cyy

import requests

url = 'https://movie.douban.com/j/chart/top_list'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

# 爬取前100
for j in [0, 20, 40, 60, 80]:
    params = {
            'type': '20',
            'interval_id': '100:90',
            'action': '', 
            'start': j,
            'limit': '20'
    }

    response = requests.get(url=url, params=params, headers=headers)
    result_lst = response.json()

    for i in range(len(result_lst)):
        with open('豆瓣恐怖片排行.txt', 'a', encoding='utf-8') as fp:
            fp.write('No.' + str(j+i+1) + '\n' +
                     'Title: ' + result_lst[i]['title'] + '\n' +
                     'Score: ' + result_lst[i]['score'] + '\n' +
                     'Region: ' + str(result_lst[i]['regions']) + '\n' +
                     'Date: ' + result_lst[i]['release_date'] + '\n' +
                     'Actors: ' + str(result_lst[i]['actors'][:3]) + '\n' +
                     '=' * 50 + '\n')
            
response.close()