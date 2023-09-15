# Парсер сайта аренды недвижимости krisha.kz

[![License: MIT](https://img.shields.io/github/license/andprov/krisha.kz?color=blueviolet)](https://github.com/andprov/krisha.kz/blob/main/LICENSE.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Описание

По заданным [параметрам](#params) осуществляет поиск и просмотр объявлений:
- Запрашивает данные со страниц предварительного просмотра объявлений. 
Находит ссылки на страницы с детальным описанием.
- Проходит по страницам с детальным описанием каждого объявления и собирает 
данные.
- После обхода двадцати объявлений на странице, сохраняет данные в SQLite базу, 
переходит на следующую страницу.

Реализован выбор параметров поиска, повторяющий функционал сайта.
Для указания параметров поиска, в корневом каталоге проекта находится 
файл `SEARCH_PARAMETERS.json`.


### 💡 Необходимо для работы
- [Python3.9 и выше](https://www.python.org/)
- [SQLite3](https://www.sqlite.org/index.html)

### Сторонние библиотеки используемые в проекте
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests](https://requests.readthedocs.io/en/latest/)


# Установка и запуск

Клонировать репозиторий:
```
git clone <https or SSH URL>
```

Перейти в папку проекта:
```
cd krisha.kz
```

Создать виртуальное окружение:
```
python3 -m venv venv
```

Активировать виртуальное окружение:
```
source venv/bin/activate
```

Установить зависимости:
```
pip install -r requirements.txt
```

Указать параметры поиска в фале `SEARCH_PARAMETERS.json`: [см. примеры](#examples)

Запустить скрипт:
```
python main.py
```

# Настройка запуска по расписанию

Отредактировать файл cron.sh, внести свой путь к проекту:
```
#!/bin/bash
cd /home/< user-name >/< dir-name >/krisha.kz
source venv/bin/activate
python main.py
```
Открыть настройки cron:
```
crontab -e
```
Внести запись с настройкой запуска:
```
# Ежедневный запуск в 12 часов.
0 12 * * * /home/< user-name >/< dir-name >/krisha.kz/cron.sh
```

# <a id="params">Параметры поиска</a>

- `city` - Город поиска от 0 до 20;
- `has_photo` - Наличие фото у объявления;
- `furniture` - Наличие мебели в квартире;
- `rooms` - Количество комнат от 1 до 5;
- `price_from` - Стоимость, нижний предел;
- `price_to` - Стоимость, верхний предел;
- `owner` - Объявление опубликовано собственником;

### Варианты значения `city`

- 0 - Весь Казахстан.
- 1 - Алматы.
- 2 - Астана.
- 3 - Шымкент.
- 4 - Абайская обл.
- 5 - Акмолинская обл.
- 6 - Актюбинская обл.
- 7 - Алматинская обл.
- 8 - Атырауская обл.
- 9 - Восточно-Казахстанская обл.
- 10 - Жамбылская обл.
- 11 - Жетысуская обл.
- 12 - Западно-Казахстанская обл.
- 13 - Карагандинская обл.
- 14 - Костанайская обл.
- 15 - Кызылординская обл.
- 16 - Мангистауская обл.
- 17 - Павлодарская обл.
- 18 - Северо-Казахстанская обл.
- 19 - Туркестанская обл.
- 20 - Улытауская обл.


### <a id="examples">Примеры указания параметров поиска:</a1>
1. Найти однокомнатные квартирами в Алматы.
Объявления с фотографиями.
Квартиры с мебелью.
Стоимость от 100000 до 300000.
Объявления от собственников.
```json
{
  "city": 1,
  "has_photo": true,
  "furniture": true,
  "rooms": [1],
  "price_from": 100000,
  "price_to": 300000,
  "owner": true
}
```

2. Найти двухкомнатные и трехкомнатные квартиры в Астане.
Объявления с фотографиями.
Квартиры без мебели.
Стоимость до 400000.
Объявления от собственников.
```json
{
  "city": 2,
  "has_photo": true,
  "rooms": [2, 3],
  "price_to": 400000,
  "owner": true
}
```

3. Найти квартиры с любым количеством комнат в Казахстане.
Объявления без фотографий.
Квартира без мебели.
Стоимость от 200000.
Объявления от собственников, агентств и частных риэлторов.
```json
{
  "price_from": 200000
}
```

Вернет такой же результат, как пример № 3.
```json
{
  "city": 0,
  "has_photo": false,
  "furniture": false,
  "rooms": [0],
  "price_from": 200000,
  "price_to": null,
  "owner": false
}
```