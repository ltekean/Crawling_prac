import unittest

import requests

from main import parsing
from main.parsing import parse_article_titles


class ParserTestCase(unittest.TestCase):
    def test_parse_article_titles(self):
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=트와이스'
        html = requests.get(url, 'lxml').text
        titles = parsing.parse_article_titles(html)
        print(titles)
        self.assertEqual(len(titles), 10)


if __name__ == '__main__':
    unittest.main()