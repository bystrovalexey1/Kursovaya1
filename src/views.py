import json
import logging
from datetime import datetime

from src.utils import (currency_rates, excel_file_opening, filtered_by_date, filtered_each_cards, get_price_stock,
                       top_five_transaction)

logger = logging.getLogger("views.log")
file_handler = logging.FileHandler("views.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

data_frame = excel_file_opening("../data/operations.xlsx")


def hello():
    """Функция приветствия"""
    user_time = datetime.now()
    if 6 <= user_time.hour <= 12:
        return "Доброе утро"
    elif 13 <= user_time.hour <= 18:
        return "Добрый день"
    elif 19 <= user_time.hour <= 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


print(hello())
# transaction_for_print = [{}]


def final_list(date: str, df_transactions, stocks: list, currency: list):
    """Функция, формирующая конечный список из готовых данных"""
    logger.info("Начало работы главной функции (main)")
    final_list = filtered_by_date(date, df_transactions)
    greeting = hello()
    cards = filtered_each_cards(final_list)
    top_transaction = top_five_transaction(final_list)
    stocks_prices = get_price_stock(stocks)
    currency_r = currency_rates(currency)
    logger.info("Создание JSON ответа")
    result = [
        {
            "greeting": greeting,
            "cards": cards,
            "top_transactions": top_transaction,
            "currency_rates": currency_r,
            "stock_prices": stocks_prices,
        }
    ]
    date_json = json.dumps(
        result,
        indent=4,
        ensure_ascii=False,
    )
    logger.info("Завершение работы главной функции (main)")
    return date_json


print(
    final_list("20.05.2021", data_frame, ["MSFT", "TSLA"], ["USD", "EUR"])
)
