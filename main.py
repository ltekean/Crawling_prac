from bs4 import BeautifulSoup
import requests

url = 'https://music.youtube.com/watch?v=JUzPQ0JalHE'
Response = requests.get(url)
html = Response.text
soup = BeautifulSoup(html, 'lxml')
articleContainer = soup.find('ul', class_='type01')
articles = articleContainer.findAll('li')
titles = []
for article in articles:
    dt = article.find('dt')
    if dt is not None:
        continue
    title = dt.find('a').text
    titles.append(title)
with open('result.txt', 'w') as result:
    for title in titles:
        result.write(title+'\n')