import json
import logging

from src.utils import excel_file_opening, xlcx_file

logger = logging.getLogger("services.log")
file_handler = logging.FileHandler("services.log", "w")
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


tr_list = excel_file_opening(xlcx_file)
# a = (find_numbers(tr_list))
print(json.loads(find_numbers(tr_list)))
