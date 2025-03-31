from bs4 import BeautifulSoup
import requests

# Функция для получения заголовков новостей
def get_news_titles(url):
    try:
        # Отправляем GET-запрос
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []

    # Парсим HTML-страницу
    soup = BeautifulSoup(response.text, "html.parser")

    # Ищем все заголовки новостей (тег <h3> с классом 'news-card__title')
    titles = soup.find_all('h3', "news-card__title")

    # Извлекаем текст из заголовков
    news_titles = [title.text.strip() for title in titles]
    return news_titles

# Функция для записи заголовков в файл
def save_titles_to_file(titles, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(title + '\n')

# Основной код
if __name__ == '__main__':
    # URL страницы со всеми новостями
    news_url = 'https://www.omgtu.ru/news/?SHOWALL_1=1'

    # Получаем заголовки новостей
    titles = get_news_titles(news_url)

    # Если заголовки найдены, записываем их в файл
    if titles:
        save_titles_to_file(titles, 'news_titles.txt')
        print(f"Заголовки новостей сохранены в файл 'news_titles.txt'")
    else:
        print("Заголовки новостей не найдены.")