import sys

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import pandas as pd
import csv


def main():
    df = pd.read_csv('パス//kabu.csv', index_col=1)
    codelist = df.index.values
    #print(codelist)
    #sample = ['a', 'b', 'c', 'd']
    complete = []
    for code in codelist:
        oncode = []
        stock = []
        wordlist = []
        strcode = str(code) #キャスト文字にする
        onlycode = 'パス//kabu.csv' + strcode
        driver = webdriver.Chrome()
        driver.get(onlycode)
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        oncode.append(strcode)
        stock.append(oncode)

        listuri1 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(2) > td:nth-child(2)')
        onlyuri1 = trim(listuri1)
        onlyuri11 = hantei(onlyuri1)
        stock.append(onlyuri11)
        listuri2 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(3) > td:nth-child(2)')
        onlyuri2 = trim(listuri2)
        onlyuri12 = hantei(onlyuri2)
        stock.append(onlyuri12)
        listuri3 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(4) > td:nth-child(2)')
        onlyuri3 = trim(listuri3)
        onlyuri13 = hantei(onlyuri3)
        stock.append(onlyuri13)

        listeigyo1 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(2) > td:nth-child(3)')
        onlyeigyo1 = trim(listeigyo1)
        onlyeigyo11 = hantei(onlyeigyo1)
        stock.append(onlyeigyo11)
        listeigyo2 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(3) > td:nth-child(3)')
        onlyeigyo2 = trim(listeigyo2)
        onlyeigyo12 = hantei(onlyeigyo2)
        stock.append(onlyeigyo12)
        listeigyo3 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(4) > td:nth-child(3)')
        onlyeigyo3 = trim(listeigyo3)
        onlyeigyo13 = hantei(onlyeigyo3)
        stock.append(onlyeigyo13)

        listrieki1 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(2) > td:nth-child(4)')
        onlyrieki1 = trim(listrieki1)
        onlyrieki11 = hantei(onlyrieki1)
        stock.append(onlyrieki11)
        listrieki2 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(3) > td:nth-child(4)')
        onlyrieki2 = trim(listrieki2)
        onlyrieki12 = hantei(onlyrieki2)
        stock.append(onlyrieki12)
        listrieki3 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(4) > td:nth-child(4)')
        onlyrieki3 = trim(listrieki3)
        onlyrieki13 = hantei(onlyrieki3)
        stock.append(onlyrieki13)

        listroe1 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(2) > td:nth-child(5)')
        onlyroe1 = trim(listroe1)
        onlyroe11 = hantei(onlyroe1)
        stock.append(onlyroe11)
        listroe2 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(3) > td:nth-child(5)')
        onlyroe2 = trim(listroe2)
        onlyroe12 = hantei(onlyroe2)
        stock.append(onlyroe12)
        listroe3 = soup.select('#finance_box > div.fin_f_t0_d.fin_f_t4_d.dispnone > table > tbody > tr:nth-child(4) > td:nth-child(5)')
        onlyroe3 = trim(listroe3)
        onlyroe13 = hantei(onlyroe3)
        stock.append(onlyroe13)
        driver.close()

        for i in range(0, 13):
            wordlist.append(stock[i][0])
        print(wordlist)
        complete.append(wordlist)
    #print(complete)
    datahead()
    datastoring(complete)

def trim(tag):
    tagnasi = [x.text for x in tag]
    return tagnasi

def hantei(arunasi):
    kaesi = arunasi
    if not arunasi:
        kaesi = '---'
    return kaesi


def datahead():
    with open("パス\\kabu.csv", "w", encoding="Shift_JIS") as f:#ファイルの書き込みヘッダー設定
        fieldnames = ['銘柄コード', '売り上げ高(2019)', '売り上げ高(2020)', '売り上げ高(2021)', '営業益(2019)', '営業益(2020)', '営業益(2021)', '営業利益率(2019)', '営業利益率(2020)', '営業利益率(2021)', 'ROE(2019)', 'ROE(2020)', 'ROE(2021)']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

def datastoring(complete):
    with open("パス\\kabu.csv", "a", encoding="utf-8") as f:#データを記載していく
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(complete)





if __name__ == '__main__':
    main()
