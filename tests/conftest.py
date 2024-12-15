import pytest


@pytest.fixture
def top_transactions():
    """from 04.11.2021 23:50:17"""
    return [
        {
            "date": "01.11.2021",
            "amount": 525.0,
            "category": "Одежда и обувь",
            "description": "WILDBERRIES",
        },
        {
            "date": "01.11.2021",
            "amount": 228.0,
            "category": "Супермаркеты",
            "description": "Колхоз",
        },
        {
            "date": "01.11.2021",
            "amount": 110.0,
            "category": "Фастфуд",
            "description": "Mouse Tail",
        },
    ]


@pytest.fixture
def generate_all_transactions():
    """from 01.11.2021 23:50:17"""
    return [
        {
            "Дата операции": "01.11.2021 15:32:24",
            "Дата платежа": "01.11.2021",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": -228.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -228.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 11.0,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 11,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 228.0,
        },
        {
            "Дата операции": "01.11.2021 11:01:19",
            "Дата платежа": "01.11.2021",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": -110.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -110.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 1.0,
            "Категория": "Фастфуд",
            "MCC": 5814.0,
            "Описание": "Mouse Tail",
            "Бонусы (включая кэшбэк)": 1,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 110.0,
        },
        {
            "Дата операции": "31.10.2021 19:06:21",
            "Дата платежа": "01.11.2021",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": -525.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -525.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 26.0,
            "Категория": "Одежда и обувь",
            "MCC": 5651.0,
            "Описание": "WILDBERRIES",
            "Бонусы (включая кэшбэк)": 26,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 525.0,
        },
    ]


@pytest.fixture
def filtered_cards():
    return [
        {"last_digit": "*4556", "total_spent": -228.0, "cashback": -2.28},
        {"last_digit": "*4556", "total_spent": -110.0, "cashback": -1.1},
        {"last_digit": "*4556", "total_spent": -525.0, "cashback": -5.25},
    ]


@pytest.fixture
def get_excel_0():
    return {
        "Дата операции": "02.11.2021 10:05:06",
        "Дата платежа": "02.11.2021",
        "Номер карты": "*4556",
        "Статус": "OK",
        "Сумма операции": -69.99,
        "Валюта операции": "RUB",
        "Сумма платежа": -69.99,
        "Валюта платежа": "RUB",
        "Кэшбэк": 3.0,
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "Магнит",
        "Бонусы (включая кэшбэк)": 3,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 69.99,
    }


@pytest.fixture
def number():
    return {
        "Дата платежа": "19.11.2021",
        "Статус": "OK",
        "Сумма платежа": -200.0,
        "Валюта платежа": "RUB",
        "Категория": "Мобильная связь",
        "Описание": "Тинькофф Мобайл +7 995 555-55-55",
        "Номер карты": "nan",
    }


@pytest.fixture
def category():
    return [
        {
            "Дата платежа": "09.12.2021",
            "Статус": "OK",
            "Сумма платежа": -15.0,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "29.11.2021",
            "Статус": "OK",
            "Сумма платежа": -228.9,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "19.11.2021",
            "Статус": "OK",
            "Сумма платежа": -271.4,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Подружка",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "15.11.2021",
            "Статус": "OK",
            "Сумма платежа": -79.0,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "04.11.2021",
            "Статус": "OK",
            "Сумма платежа": -290.01,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Подружка",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "03.11.2021",
            "Статус": "OK",
            "Сумма платежа": -191.5,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "25.10.2021",
            "Статус": "OK",
            "Сумма платежа": -273.9,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*7197",
        },
        {
            "Дата платежа": "20.10.2021",
            "Статус": "OK",
            "Сумма платежа": -133.1,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*7197",
        },
        {
            "Дата платежа": "27.09.2021",
            "Статус": "OK",
            "Сумма платежа": -202.4,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "02.09.2021",
            "Статус": "OK",
            "Сумма платежа": -47.0,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "31.08.2021",
            "Статус": "OK",
            "Сумма платежа": -110.1,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "Улыбка радуги",
            "Номер карты": "*7197",
        },
        {
            "Дата платежа": "26.08.2021",
            "Статус": "OK",
            "Сумма платежа": -51.2,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "OOO Balid",
            "Номер карты": "*7197",
        },
        {
            "Дата платежа": "22.08.2021",
            "Статус": "OK",
            "Сумма платежа": -372.8,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "OOO Balid",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "05.08.2021",
            "Статус": "OK",
            "Сумма платежа": -9.5,
            "Валюта платежа": "RUB",
            "Категория": "Косметика",
            "Описание": "OOO Balid",
            "Номер карты": "*4556",
        },
    ]
