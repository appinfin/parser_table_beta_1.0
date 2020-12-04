import requests, lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent #fake User-Agent
ua = UserAgent().chrome #Mozilla/5.0

def get_soup(url: str, ua: str) -> object:
    """возвращает объект BeautifulSoup(html, 'lxml')"""
    head = {'User-Agent': ua}
    html = requests.get(url, headers=head).text # получить содержимое страницы (строка)
    soup = BeautifulSoup(html, 'lxml')  # вернуть в виде объекта BS
    return soup

def save_html():
    url = 'https://www.championat.com/football/_england/tournament/4013/table/' #input()
    soup = get_soup(url, ua)
    t_body = soup.find('tbody') #находим тег tbody
    list_tr = t_body.find_all('tr') #список строк таблицы
    with open('index.html','w+') as file:
        file.write(str(list_tr))
