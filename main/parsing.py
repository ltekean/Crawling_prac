from bs4 import BeautifulSoup
import re

def parse_article_titles(html):
    soup = BeautifulSoup(html, 'lxml')
    article_container = soup.find('ul', class_='list_news')
    articles = article_container.findAll('li')
    titles = []
    for article in articles:
        data_table = re.search(r'title="(.*?)"', str(article))
        if not data_table:
            continue
        dt = data_table.group(0)
        titles.append(dt)
    return titles