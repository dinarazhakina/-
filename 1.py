# Импорт библиотеки BeautifulSoup для парсинга HTML-документов
from bs4 import BeautifulSoup
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Функция для получения заголовков новостей с веб-страницы
def get_news_titles(url):
    # Блок try-except для обработки возможных ошибок при выполнении запроса
    try:
        # Отправка GET-запроса к указанному URL
        response = requests.get(url)
        # Проверка статуса ответа: вызовет исключение, если статус не 200 (OK)
        response.raise_for_status()
    
    # Обработка исключений, которые могут возникнуть при запросе
    except requests.exceptions.RequestException as e:
        # Вывод сообщения об ошибке, если запрос не удался
        print(f"Ошибка при запросе: {e}")
        # Возврат пустого списка в случае ошибки
        return []

    # Создание объекта BeautifulSoup для парсинга HTML-содержимого страницы
    # response.text содержит HTML-код страницы, 'html.parser' - указание парсера
    soup = BeautifulSoup(response.text, "html.parser")

    # Поиск всех элементов <h3> с классом 'news-card__title' на странице
    # Эти элементы содержат заголовки новостей
    titles = soup.find_all('h3', "news-card__title")

    # Извлечение текста из каждого найденного заголовка и удаление лишних пробелов
    # Создание списка заголовков новостей
    news_titles = [title.text.strip() for title in titles]
    # Возврат списка заголовков
    return news_titles

# Функция для сохранения заголовков в текстовый файл
def save_titles_to_file(titles, filename):
    # Открытие файла для записи ('w') с указанием кодировки UTF-8
    with open(filename, 'w', encoding='utf-8') as file:
        # Запись каждого заголовка в файл с добавлением переноса строки
        for title in titles:
            file.write(title + '\n')

# Основной блок кода, который выполняется при запуске скрипта
if __name__ == '__main__':
    # URL страницы с новостями (все новости на одной странице благодаря SHOWALL_1=1)
    news_url = 'https://www.omgtu.ru/news/?SHOWALL_1=1'

    # Получение заголовков новостей с помощью функции get_news_titles
    titles = get_news_titles(news_url)

    # Проверка, были ли найдены заголовки
    if titles:
        # Если заголовки найдены, сохраняем их в файл
        save_titles_to_file(titles, 'news_titles.txt')
        # Вывод сообщения об успешном сохранении
        print(f"Заголовки новостей сохранены в файл 'news_titles.txt'")
    else:
        # Вывод сообщения, если заголовки не найдены
        print("Заголовки новостей не найдены.")
