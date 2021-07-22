#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000006')

html = browser.page_source


from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')
contents = soup.select('li._itemSection')

import sqlite3
connect = sqlite3.connect('../db.sqlite3')
cursor = connect.cursor()


for content in contents:
    #rank = content.select('div.best_rnk > em')[0]    순위가 1~9까지 잘나오다가 10부터 num1,num0 식으로 되어있음
    #rank = rank.text.strip()
    title = content.select('p.cont')[0]
    title = title.text.strip()

    try:
        cursor.execute(
            "insert into dbapp_navershop(create_date, title) values(datetime('now'), ?)", [title])
        print(title)
    except:
        pass

connect.commit()
connect.close()

browser.close()
browser.quit()



