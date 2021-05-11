import re
from bs4 import BeautifulSoup as bs
import codecs
import parser
import requests
import lxml.html.clean

#https://clck.ru/UktRw

url = input('Введите URL сайта: ')
url = requests.get(url)
url.encoding = 'utf-8'
doc = bs(url.text, 'lxml')

# Извлечение данных из статьи
title = doc.select('b')[4].decode_contents().strip()
about = doc.select('a.username.u-concealed')[0].decode_contents().strip()
date = doc.select('time.u-dt')[0].decode_contents().strip()
rat = doc.select('span.t-rating-count')[0].decode_contents().strip()
last = doc.select('time.u-dt')[3].decode_contents().strip()

html = title
safe_attrs = lxml.html.clean.defs.safe_attrs
cleaner = lxml.html.clean.Cleaner(safe_attrs_only=True, safe_attrs=frozenset())
html = cleaner.clean_html(html)
html = html.replace("<p>","")
html = html.replace("</p>","")

# Вывод на экран
print('Название курса:', html)
print('Автор публикации:', about)
print('Дата публикации:', date)
print('Кол-во', rat)
print('Последнее редактирование:', last)

# Извлечение данных о комментариях
comments = []
for node in doc.select('article.message.message--post.js-post.js-inlineModContainer'):
    author = node.select('a.username')[0].decode_contents().strip()
    text = node.select('div.bbWrapper')[0].decode_contents().strip()
    comments.append({'text': text, 'author': author})

# Вывод информации по комментариям
print('Комментариев в статье:', len(comments))
print('Самый маленький комментарий:', sorted(comments, key=lambda x: len(x['text']))[0]['text'])

# Самый активный комментатор
commentators = {}
for comment in comments:
    if comment['author'] in commentators:
        commentators[comment['author']] += 1
    else:
        commentators[comment['author']] = 1
most_active = max(commentators, key=commentators.get)
print('\nСамый активный комментатор:', '\nНаиольшее кол-во комментариев:', commentators[most_active])
most_active = most_active.replace("<span class=\"username--style5\">","")
most_active = most_active.replace("</span>","")
print('Никнейм:', most_active)