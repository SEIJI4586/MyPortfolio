import re

from pip._internal.commands import install
import numpy as np
from bs4 import BeautifulSoup
import requests #ライブラリWebサイトの情報取得
import time
import os
import pandas as pd #データ解析
import codecs
#標準的な Python codec (エンコーダとデコーダ) 用の基底クラスを定義し、
# codec とエラー処理検索プロセスを管理する内部のPythoncodecレジストリへのアクセスを提供
from urllib.parse import urljoin #URL解析
import collections as cl
import csv


def main():
    res = requests.get("サイト") #1回目のスクレイピング、URLが1回目だけ異なったから他とは別に
    res.raise_for_status() #
    html = BeautifulSoup(res.text, 'html.parser')
    table = html.find_all(class_="rankingTabledata")

    for row in table:
        Row = []
        for cell in html.find_all('td'):#リストに一ページ一気にいれる。html.find_allを繰り返す。
            if cell.get_text() == "掲示板":#掲示板の文字邪魔なので消し去る
                continue #飛ばす
            Row.append(cell.get_text())
    length = len(Row) #どのくらいの量
    n = 0
    s = 9
    kabulist = []
    for i in Row:
        print(Row[n:n+s:1])#上で一気にいれたのを企業ごとに分割
        kabulist.append(Row[n:n+s:1])#スライス
        n  += s
        if n >= length:
            break
    with open("パス\\kabu.csv", "w", encoding="Shift_JIS") as f:#ファイルの書き込みヘッダー設定
        fieldnames = ['順位', '銘柄コード', '証券', '企業名', '取引月日', '取引値', '上場年月日', '決算年月', '時価総額']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    with open("パス\\kabu.csv", "a", encoding="Shift_JIS") as f:#株のデータをCSVに記載していく
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(kabulist)

def continuous(x):#2回目以降はこちらのfor文で対応
    string = "サイト/?kd=41&tm=d&vl=a&mk=1&p="
    res = requests.get(string + str(x))
    res.raise_for_status()
    html = BeautifulSoup(res.text, 'html.parser')
    table = html.find_all(class_="rankingTabledata")
    for row in table:
        Row = []
        for cell in html.find_all('td'):
            if cell.get_text() == "掲示板":
                continue
            Row.append(cell.get_text())
    length = len(Row)
    stock = []
    n = 0
    s = 9
    for i in Row:
        #print(Row[n:n + s:1])
        stock.append(Row[n:n + s:1])
        n += s
        if n >= length:
            break
    print(stock)
    with open("パス\\kabu.csv", "a", encoding="Shift_JIS") as f:#データを記載していく
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(stock)




if __name__ == '__main__':
    main()
    for i in range(2, 84):#２ページ以降
        continuous(i)
        time.sleep(2)



