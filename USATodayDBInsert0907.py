from django.http import HttpResponse
from django.shortcuts import render
import operator
import requests
from bs4 import BeautifulSoup
import sqlite3

titles = []
links = []
dates = []
authors = []
contents = []


conn = sqlite3.connect("test.db")
cur = conn.cursor()

page = requests.get('https://www.usatoday.com/search/?q=Korea')
soup = BeautifulSoup(page.content, 'html.parser')

usatoday = soup.select('div.gnt_se_hl')
for title in usatoday:
    # 키워드 필터링
    # if('Korea' in title.text):
    if (title.parent.parent.get('href').find("/world/") != -1):
        print("Links:", title.parent.parent.get('href'))
        print("Title:", title.text)
        #titles.append(title.text)

    # 이 화면에서 저자, 날짜 빼오기
    #print("Source = ", title.parent)
    dtby = title.parent.find(attrs={"class": "gnt_se_dtby"})
    if (dtby != None):
        print("Author", dtby.get('data-c-by'))
        print("Date", dtby.get('data-c-dt'))

        Author = dtby.get('date-c-by')
        ArticleDate = dtby.get('data-c-dt')
        Articlelinks = title.parent.parent.get('href')



        #SQL = "INSERT INTO test8 (publisher, title) VALUES" \
        #     + "(" + "'USAToday'" + "," + "'" + title.text + "'" + ")"

        Noapostrophe = title.text.replace("'","")
        #repr(ArticleDate)
        #NocommaDate = ArticleDate.text.replace(",","")
        #print(NocommaDate)


        #SQL = "INSERT INTO test9 (publisher, title) VALUES" \
        #    + "(" + "'USAToday'" + "," + "'" + Noapostrophe + "'" + ")"
        #print(SQL)
        #SQL = "INSERT INTO test9 (title) VALUES ('TEST')"

        SQL = "INSERT INTO test9 (publisher, data, title, links) VALUES" \
             + "(" + "'USAToday'" + "," + "'" + ArticleDate + "'" + "," + "'" + Noapostrophe + "'" \
             + "," + "'" + Articlelinks + "'" + ")"

        #print(SQL)

        cur.execute(SQL)

cur.execute("select * from test9")

rows = cur.fetchall()
print(rows)

conn.commit()
conn.close()
