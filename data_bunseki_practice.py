import requests
from bs4 import BeautifulSoup
import pandas as pd

target_url = 'https://www.amazon.co.jp/gp/bestsellers/books/466284/ref=pd_zg_hrsr_books' #スクレイピングしたいURL
r = requests.get(target_url)  #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml')

title = []
author = []
types = []
price = []

#題名の取得（img srcから）
for img in soup.select('a img'):
    title.append(img.attrs.get('alt', 'N').replace('\u3000', ' '))

#著者と形式の取得
for i, j in enumerate(soup.find_all('div', 'a-row a-size-small')):
    if i % 2 == 0:
        author.append(j.text)
    else:
        types.append(j.text)

#値段の取得
for k in soup.find_all('span', 'p13n-sc-price'):
    price.append(k.text.replace("￥", "").replace(',', ''))

#リストの結合
data = list(zip(title, author, types, price))

#DataFrameオブジェクトの生成（オプションでカラム名を追加）
df = pd.DataFrame(data, columns=['題名', '著者', '形式', '値段'])

#indexを1から始める
df.index = df.index + 1

#csvに書き込み
df.to_csv('bookranking.csv')