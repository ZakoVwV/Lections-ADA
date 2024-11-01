from bs4 import BeautifulSoup as BS
import requests
import json


URL = 'https://www.sulpak.kg/f/'

def get_html(category: str, page: int = 1):
    response = requests.get(f'{URL}{category}', params={'page':page})
    if response.status_code == 200:
        return response.text
    raise Exception('Пройзошла ошибка')


def get_cards(html: str):
    soup = BS(html, 'lxml')
    cards = soup.find_all('div', class_='product__item product__item-js tile-container')
    return cards

def parse_cards(cards: list) -> list:
    data = []
    try:
        for card in cards:
            data.append({
                'title':card.get('data-name'),
                'price':card.get('data-price'),
                'brand':card.get('data-brand'),
                'in_stock': card.find('div', class_='product__item-showcase').text if card.find('div', class_='product__item-showcase') else 'Нет в наличий',
                'product_link': 'https://www.sulpak.kg' + card.find('div', class_='product__item-name').find('a').get('href')
            })
        return data
    except Exception as e:
        print(e)
        return 'Что-то пошло не так'

def get_last_page(category: str) -> int:
    html = get_html(category)
    soup = BS(html, 'lxml')
    last_page = soup.find('div', class_='pagination').get('data-pagescount')
    return int(last_page)

def save_to_json(data: list, filename: str) -> None:
    with open (filename, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main(category: str) -> None:
    data = []
    last_page = get_last_page(category)

    for page in range(1, last_page + 1):
        html = get_html(category, page)
        cards = get_cards(html)
        data.extend(parse_cards(cards))
    save_to_json(data, f'{category}.json')


main('holodilniki')