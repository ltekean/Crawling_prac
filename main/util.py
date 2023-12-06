import requests

def get_html_from_url(url):
    response = requests.get(url)
    html = response.text
    return html


def write_titles(titles, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for title in titles:
            if isinstance(title, list):
                title_str = ', '.join(map(str, title))
                file.write(title_str + '\n')
            else:
                file.write(str(title) + '\n')