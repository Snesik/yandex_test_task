import requests
import re


def take_news():
    last_news = requests.get('https://vc.ru/').text
    href_last_news = re.findall('<a class="content-header__item content-header-number" href=\"(.+?)\"', last_news)
    news = requests.get(href_last_news[0]).text
    text_news = re.findall('meta name=\"description\" content=\"(.+?)\"', news)
    return text_news

def token():
    with open('token.txt', 'r') as f:
        return f.readline()