# Курсовая работа по третьему модулю


## Описание:
В этом проекте разработано приложение для анализа транзакций, которые находятся в Excel-файле. 
Приложение генерирует JSON-данные для веб-страниц, формирует Excel-отчеты, а также предоставляет другие сервисы.


## Структура проекта
1. 'Отчеты' - это модуль 'reports' в котором реализованна функция
   'spending_by_category' возвращающая траты за последние
   3 месяца по заданной категории.
2. 'Сервисы' - это модуль 'services' в котором реализованна функция
   поиска по телефонным номерам 'find_numbers'.
3. 'Веб-страницы' этот модуль располагает свой функционал
   в двух модулях 'utils' - модуль отвечающий за вспомогательные функции,
   'views' - модуль для генерации основными функциями JSON-ответа.


## Инструкция
Клонируйте репозиторий:
```
git clone git@github.com:bystrovalexey1/Kursovaya1.git
```
Установите зависимости:
```
pip install -r requirements.txt
```

### Тестирование:
Тестами покрыто 80% кода.
Тесты нужны для того, чтобы все функции работали корректно.
Для запуска тестов введите команду:
```
pytest.exe
```
После успешного прохождения тестов можно пользоваться программой, иначе обратитесь к разработчику за помощью

## Источник
[SkyPro](https://my.sky.pro/)