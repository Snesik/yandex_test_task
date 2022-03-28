import requests
import re


def take_news():
    last_news = requests.get('https://vc.ru/').text
    href_last_news = re.findall('<a class="content-header__item content-header-number" href=\"(.+?)\"', last_news)
    news = requests.get(href_last_news[0]).text
    text_news = re.findall('meta name=\"description\" content=\"(.+?)\"', news)
    return text_news


def take_token(path):
    with open(path) as f:
        return f.readline()


def send_telegram(text):
    url = "https://api.telegram.org/bot"
    channel_id = -1001625716305
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")


if __name__ == '__main__':
    token = take_token('token.txt')
    send_telegram(take_news())
