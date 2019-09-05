import requests
from bs4 import BeautifulSoup

#여기에 작성할게요

titles = []
links = []
dates = []
authors = []
contents = []

page = requests.get('https://www.usatoday.com/search/?q=Korea')
soup = BeautifulSoup(page.content, 'html.parser')
#헤드라인 따로, 부 기사 따로 추출. 셀렉터가 다름.
usatoday = soup.select('div.gnt_se_hl')
for title in usatoday:
	#키워드 필터링
	#if('Korea' in title.text):
    if (title.parent.parent.get('href').find("/world/")!=-1):
        print(title.parent.parent.get('href'))
        titles.append(title.text)
	    #깊게 탐색
        deeppage = 'https://usatoday.com'
        deeppage += title.parent.parent.get('href')
        page = requests.get(deeppage)
        links.append(deeppage)
        soup = BeautifulSoup(page.content, 'html.parser')
        date = soup.select('div > span.asset-metabar-time.asset-metabar-item.nobyline')
        dates.append(date[0].text.strip())
        #
        print(date[0].text.strip())
        #author = soup.find(attrs={"rel": "author"})
        author = soup.select('div > span.asset-metabar-author.asset-metabar-item')
        authors.append(author[0].text)
        #
        print(author[0].text)
        
print(titles)
print(links)
print(dates)
print(authors)
