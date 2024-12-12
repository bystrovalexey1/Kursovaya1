import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", "a")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(filename)s %(funcName)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def find_numbers(list_transactions):
    """Функция возвращает JSON со всеми транзакциями, содержащими в описании мобильные номера"""
    current_transactions = []
    for transaction in list_transactions:
        if "+7" in transaction["Описание"]:
            current_transactions.append(transaction)
    logger.info("Возвращение списка со всеми транзакциями, содержащими в описании мобильные номера")
    current_transactions = json.dumps(current_transactions, ensure_ascii=False)
    return current_transactions
