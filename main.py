import requests
from bs4 import BeautifulSoup
import time
import sys


def get_wikipedia_info(query, language='en'):
    query = query.lower()

    # URL в зависимости от языка
    search_url = f"https://{language}.wikipedia.org/wiki/Special:Search"
    params = {"search": query}

    # Отправляем GET-запрос
    response = requests.get(search_url, params=params)

    # Проверяем статус ответа
    if response.status_code != 200:
        return f"Error: Unable to fetch the page. Status code: {response.status_code}"

    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Пытаемся найти основной контент
    content_div = soup.find("div", {"class": "mw-parser-output"})
    if not content_div:
        return "Error: Unable to find the main content on the page."

    # Извлекаем текст из найденного div
    paragraphs = content_div.find_all("p")
    if not paragraphs:
        return "Error: Unable to find any paragraphs in the main content."

    # Объединяем текст из всех <p>
    page_text = "\n".join([para.get_text() for para in paragraphs])

    return page_text.strip()


def slow_print(text, delay=0.03):
    # Цикл по каждому символу текста
    for char in text:
        # Печатаем букву
        sys.stdout.write(char)
        sys.stdout.flush()
        # Задержка печати
        time.sleep(delay)
    print() 

def main():
    slow_print('Введите запрос: ')
    query = input()
    response = get_wikipedia_info(query, language='ru')
    slow_print(response)


if __name__ ==  "__main__":
    main()
