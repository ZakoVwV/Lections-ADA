import requests
from bs4 import BeautifulSoup as BS

URL = 'https://kaktus.media/?lable=8&date=2024-11-01&order=time'
dict_with_news = {}

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup


def get_list_news():
    html = get_html(URL)
    soup = get_soup(html)
    catalog = soup.find('div', class_='Tag--articles')
    news = catalog.find_all('div', class_='Tag--article')
    count = 1
    list_news = []
    for new in news:
        dict_with_news[count] = new
        title = f"{count}. {new.find('a', class_='ArticleItem--name').text.strip()}"
        list_news.append(title)
        count += 1
        if count == 21:
            break
    return '\n'.join(list_news)


def get_one_new(int_):
    url_one_new = dict_with_news[int_].find('a', class_='ArticleItem--name').get('href')
    html = get_html(url_one_new)
    soup = get_soup(html)
    all_about_new = soup.find('div', class_='BbCode').find('p').text
    return all_about_new

def get_photo(int_):
    photo = dict_with_news[int_].find('img', class_='ArticleItem--image-img lazyload').get('src')
    return photo