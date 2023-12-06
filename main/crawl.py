# crawl.py
from util import get_html_from_url, write_titles
from parsing import parse_article_titles

def naver_news_titles_crawl(keyword):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}'
    html = get_html_from_url(url)
    titles = parse_article_titles(html=html)
    write_titles(titles=titles, filename=f'{keyword}.txt')

if __name__ == '__main__':
    naver_news_titles_crawl(keyword='트와이스')


def naver_news_titles_crawl(keyword):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}'
    html = get_html_from_url(url)
    titles = parse_article_titles(html=html)
    write_titles(titles=titles, filename=f'{keyword}.txt')

if __name__ == '__main__':
    naver_news_titles_crawl(keyword='엑소')