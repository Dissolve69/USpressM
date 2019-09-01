
from django.http import HttpResponse
from django.shortcuts import render
import operator
import requests
from bs4 import BeautifulSoup
import psycopg2

conn_string = "host='localhost' dbname ='uspressm' user='uspressm' password='codefair'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

page = requests.get('https://www.nytimes.com/section/world/asia')
soup = BeautifulSoup(page.content, 'html.parser')
nytimes = soup.select('div > div.css-4jyr1y > a > h2')

nytitles = list()

for title in nytimes:
    #SQL="INSERT INTO uspressmtable (title) VALUES" \
    #    + "(" + "'" + title.text + "'" + ")"
    SQL = "INSERT INTO uspressmtable2 (publisher, title) VALUES" \
          + "(" + "'NYtimes'" + "," + "'" +title.text + "'" + ")"

    cur.execute(SQL)

    print(title.text)


cur.execute("SELECT * FROM uspressmtable2;")
result = cur.fetchall()
print(result)

conn.commit()
conn.close()

