
from django.http import HttpResponse
from django.shortcuts import render
import operator
import requests
from bs4 import BeautifulSoup

def homepage(request):

    page = requests.get('https://www.nytimes.com/section/world/asia')
    soup = BeautifulSoup(page.content, 'html.parser')
    nytimes = soup.select('div > div.css-4jyr1y > a > h2')

    nytitles=list()

    # print (nytimes)
    for title in nytimes:
        nytitles.append(title.text)


    return render(request, 'home3.html',{'nytitles':nytitles})
