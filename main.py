import os

from dotenv import load_dotenv

from src.reports import spending_by_category
from src.services import find_numbers
from src.utils import excel_file_opening
from src.views import final_list, hello

load_dotenv()
API_KEY_CUR = os.getenv("API_KEY_CUR")
data_frame = excel_file_opening("data/operations.xlsx")
user_currencies = ["USD", "EUR"]
user_stocks = ["MSFT", "TSLA"]


hello()
user_data = input("Введите дату в формате DD.MM.YYYY: ")
print(final_list(user_data, data_frame, user_stocks, user_currencies))
print(find_numbers(data_frame))
category = input("Введите категорию поиска: ")
user_data_category = input("Введите дату в формате DD.MM.YYYY: ")
print(spending_by_category(data_frame, category, user_data_category))
