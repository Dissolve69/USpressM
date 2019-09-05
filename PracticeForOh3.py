import requests
from bs4 import BeautifulSoup

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
        
        #data /story/news/world/년도/월/일자/기사 data
		date = soup.select('div > span.asset-metabar-time.asset-metabar-item.nobyline')
        
		if (len(date)!=0):
			dates.append(date[0].text.strip())
		else:
			dates.append("ERROR")
			print("ERROR")
        #author = soup.find(attrs={"rel": "author"})
		author = soup.select('div > span.asset-metabar-author.asset-metabar-item > a')
		if (len(author)!=0):
			authors.append(author[0].text.strip())
			print(author[0].text.strip())
		else:
			author = soup.select('div > span.asset-metabar-author.asset-metabar-item')
			authors.append("ERROR")
			print(author[0].text.strip())
            
print(titles)
print(links)
print(dates)
print(authors)
