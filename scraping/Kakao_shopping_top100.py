#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://store.kakao.com/home/best')


prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if(curr_height == prev_height):
        break
    else:
        prev_height = browser.execute_script("return document.body.scrollHeight")


html = browser.page_source


from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')
contents = soup.select('li.item-container')
#content = contents[0]

# rank = content.select('div > em.rank_info')[0]
# title = content.select('span.product_name')[0]

import sqlite3
connect = sqlite3.connect('../db.sqlite3')
cursor = connect.cursor()

for content in contents:
    # rank = str(rank).strip()
    # title = str(title).strip()
    rank = content.select('div > em.rank_info')[0]
    rank = rank.text.strip()
    title = content.select('span.product_name')[0]
    title = title.text.strip()

    try:
        cursor.execute(
            "insert into dbapp_kakaoshop(create_date, rank, title) values(datetime('now'), ?, ?)", (rank,title))
        print(rank, ' : ', title)
    except:
        pass

connect.commit()
connect.close()

browser.close()
browser.quit()
