import logging
import os
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY_CUR = os.getenv("API_KEY_CUR")

SP_500_API_KEY = os.getenv("SP_500_API_KEY")

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(filename)s %(funcName)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

BASE_DIR = Path(__file__).resolve().parent.parent
xlcx_file = BASE_DIR / "data" / "operations.xlsx"


def excel_file_opening(xlcx_file: str) -> list[dict]:
    """Функция принимает на вход путь до файла excel и возвращает список словарей с транзакциями"""
    try:
        logger.info(f"Выполняем поиск файла {xlcx_file}")
        data_frame = pd.read_excel(xlcx_file)
        logger.info(f"Открытие excel файла {xlcx_file}")
    except ValueError:
        logger.warning("Пустой файл или не верный тип, возвращаем пустой список")
        return []
    except FileNotFoundError:
        logger.warning("Файл не найден, возвращаем пустой список")
        return []
    else:
        logger.info("Конвертируем excel файл в python")
        operations = data_frame.apply(
            lambda row: {
                "Дата платежа": row["Дата платежа"],
                "Статус": row["Статус"],
                "Сумма платежа": row["Сумма платежа"],
                "Валюта платежа": row["Валюта платежа"],
                "Категория": row["Категория"],
                "Описание": row["Описание"],
                "Номер карты": row["Номер карты"],
            },
            axis=1,
        ).tolist()
        logger.info("Успешно! Возвращаем словарь с транзакциями")
        return operations


# print(excel_file_opening(xlcx_file))


def filtered_by_date(date: str, transactions_list: list):
    """Функция, возвращающая отфильтрованные по дате транзакции"""
    current_transactions = []
    for transaction in transactions_list:
        if str(transaction["Дата платежа"])[2:10] == date[2:10] and str(transaction["Дата платежа"])[:2] <= date[:2]:
            current_transactions.append(transaction)
    logger.debug("Correct data payment")
    return current_transactions


# cards = excel_file_opening(xlcx_file)
# print(filtered_by_date('02.05.2020', cards))


def filtered_each_cards(my_list: list) -> list:
    """Функция создания информации по каждой карте"""
    logger.info("Начало работы функции (for_each_card)")
    cards = {}
    result = []
    logger.info("Перебор транзакций")
    for i in my_list:
        if i["Номер карты"] == "nan" or type(i["Номер карты"]) is float:
            continue
        elif i["Сумма платежа"] == "nan":
            continue
        else:
            if i["Номер карты"][1:] in cards:
                cards[i["Номер карты"][1:]] += float(str(i["Сумма платежа"])[1:])
            else:
                cards[i["Номер карты"][1:]] = float(str(i["Сумма платежа"])[1:])
    for k, v in cards.items():
        result.append({"Последние цифры карты": k, "Всего потрачено": round(v, 2), "Кэшбек": round(v / 100, 2)})
    logger.info("Завершение работы функции (for_each_card)")
    return result


# cards = excel_file_opening(xlcx_file)
# print(for_each_card(cards))


def currency_rates(currency: list) -> list[dict]:
    """Функция запроса курса валют"""
    result = []
    logger.info("Начало работы функции (currency_rates)")
    for i in currency:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={i}&amount=1"
        headers = {"apikey": API_KEY_CUR}
        response = requests.request("GET", url, headers=headers)
        rates = response.json()["info"]["rate"]
        rates = round(rates, 2)
        result.append({"Валюта": i, "Курс": rates})
    logger.info("Создание списка словарей для функции - currency_rates")

    logger.info("Окончание работы функции - currency_rates")
    return result


# print(currency_rates(['USD','EUR', 'BTC', 'GBP']))


def top_five_transaction(transaction_list: list) -> list:
    """Функция для получения топ-5 транзакций по сумме платежа"""
    logger.info("Начало работы функции (top_five_transaction)")
    top_list = []
    sort_transaction_list = sorted(transaction_list, reverse=True, key=lambda x: abs(x["Сумма платежа"]))
    for transaction in sort_transaction_list:
        top = {
            "date": transaction["Дата платежа"],
            "amount": abs(transaction["Сумма платежа"]),
            "category": transaction["Категория"],
            "description": transaction["Описание"],
        }
        logger.info("Добавление операции в список")
        top_list.append(top)
        if len(top_list) == 5:
            break
    logger.info("Конец работы функции")
    return top_list


# tr_list = excel_file_opening(xlcx_file)
# print(top_five_transaction(tr_list))


def get_price_stock(stocks: list) -> list:
    """Функция для получения данных об акциях из списка S&P500"""
    logger.info("Начало работы функции (get_price_stock)")
    api_key = SP_500_API_KEY
    stock_prices = []
    logger.info("Функция обрабатывает данные транзакций.")
    for stock in stocks:
        logger.info("Перебор акций в списке 'stocks' в функции (get_price_stock)")
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}"
        response = requests.get(url, timeout=5, allow_redirects=False)
        result = response.json()

        stock_prices.append({"stock": stock, "price": round(float(result["Global Quote"]["05. price"]), 2)})
    logger.info("Функция get_price_stock успешно завершила свою работу")
    return stock_prices


# print(get_price_stock(["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]))
