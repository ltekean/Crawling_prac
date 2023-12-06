from bs4 import BeautifulSoup
import requests
import re

def get_html_from_url(url):
    response = requests.get(url)
    html = response.text
    return html

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

def write_titles(titles, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for title in titles:
            if isinstance(title, list):
                title_str = ', '.join(map(str, title))
                file.write(title_str + '\n')
            else:
                file.write(str(title) + '\n')

def naver_news_titles_crawl(keyword):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}'
    html = get_html_from_url(url)
    titles = parse_article_titles(html=html)
    write_titles(titles=titles, filename=f'{keyword}.txt')

if __name__ == '__main__':
    naver_news_titles_crawl(keyword='트와이스')
