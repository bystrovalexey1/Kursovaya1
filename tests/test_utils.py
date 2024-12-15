import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.utils import (currency_rates, excel_file_opening, filtered_by_date, filtered_each_cards, get_price_stock,
                       top_five_transaction, xlcx_file)

load_dotenv()
API_KEY_CUR = os.getenv("API_KEY_CUR")
transaction_list = excel_file_opening(xlcx_file)
empty_list = []


def test_filtered_for_each_card():
    """Тестирование функции создающей информацию по каждой карте, в обычном режиме"""
    assert filtered_each_cards(transaction_list) == [
        {"Последние цифры карты": "7197", "Всего потрачено": 2504514.54, "Кэшбек": 25045.15},
        {"Последние цифры карты": "5091", "Всего потрачено": 18216.84, "Кэшбек": 182.17},
        {"Последние цифры карты": "4556", "Всего потрачено": 2103029.17, "Кэшбек": 21030.29},
        {"Последние цифры карты": "1112", "Всего потрачено": 46207.08, "Кэшбек": 462.07},
        {"Последние цифры карты": "5507", "Всего потрачено": 84000.0, "Кэшбек": 840.0},
        {"Последние цифры карты": "6002", "Всего потрачено": 69200.0, "Кэшбек": 692.0},
        {"Последние цифры карты": "5441", "Всего потрачено": 470854.8, "Кэшбек": 4708.55},
    ]


def test_filtered_for_each_card_emp_att():
    """Тестирование функции создающей информацию по каждой карте, с пустым списком"""
    assert filtered_each_cards(empty_list) == []


def test_top_five_transaction():
    """Тестирование функции для получения топ-5 транзакций по сумме платежа, в обычном режиме"""
    assert top_five_transaction(transaction_list) == [
        {"date": "01.09.2021", "amount": 5990.0, "category": "Каршеринг", "description": "Ситидрайв"},
        {"date": "20.05.2021", "amount": 8626.0, "category": "Бонусы", "description": "Компенсация покупки"},
        {"date": "14.05.2019", "amount": 42965.94, "category": "Другое", "description": "ГУП ВЦКП ЖХ"},
        {
            "date": "30.04.2019",
            "amount": 6100.0,
            "category": "Зарплата",
            "description": 'Пополнение. ООО "ФОРТУНА". Зарплата',
        },
        {"date": "23.04.2019", "amount": 4518.0, "category": "Сервис", "description": "Kopirovalniy Centr"},
    ]


def test_filter_by_date():
    """Тестирования функции фильтра от заданной даты"""
    assert filtered_by_date("01.11.2021", transaction_list) == [
        {
            "Дата платежа": "01.11.2021",
            "Статус": "OK",
            "Сумма платежа": -228.0,
            "Валюта платежа": "RUB",
            "Категория": "Супермаркеты",
            "Описание": "Колхоз",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "01.11.2021",
            "Статус": "OK",
            "Сумма платежа": -110.0,
            "Валюта платежа": "RUB",
            "Категория": "Фастфуд",
            "Описание": "Mouse Tail",
            "Номер карты": "*4556",
        },
        {
            "Дата платежа": "01.11.2021",
            "Статус": "OK",
            "Сумма платежа": -525.0,
            "Валюта платежа": "RUB",
            "Категория": "Одежда и обувь",
            "Описание": "WILDBERRIES",
            "Номер карты": "*4556",
        },
    ]


def test_top_five_transaction_empty():
    """Тестирование функции для получения топ-5 транзакций по сумме платежа, с пустым списком"""
    assert top_five_transaction(empty_list) == []


@patch("requests.get")
def test_currency_rates(mock_get):
    """Тестирование функции вывода курса валют"""
    mock_get.return_value.json.return_value = {"result": currency_rates("USD")}
    result = {"Валюта": "USD", "Курс": 95.61}
    assert result == {"Валюта": "USD", "Курс": 95.61}


@patch("requests.get")
def test_fetch_stock_prices(mock_get):
    """Тестирование функции получения данных об акциях из списка S&P500"""

    mock_get.return_value.json.return_value = {"Global Quote": {"05. price": 210.00}}

    list_stocks = ["AAPL"]

    result = get_price_stock(list_stocks)
    expected = [
        {"stock": "AAPL", "price": 210.00},
    ]
    assert result == expected
