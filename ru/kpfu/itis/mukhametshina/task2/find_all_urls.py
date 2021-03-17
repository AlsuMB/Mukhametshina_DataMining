import requests
from bs4 import BeautifulSoup

all_sites = set()

# HOST = 'https://www.random.org/'
URL = 'https://www.random.org/'
HEADERS = {
    'accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def change_set():
    all_sites.add('lox')


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_next_target(page):
    soup = BeautifulSoup(get_html(page).content, 'html.parser')
    return soup.find_all('a', href=True)


all_href = get_next_target(URL)
for i in all_href:
    print(i)