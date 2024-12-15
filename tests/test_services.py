import json

from src.services import find_numbers
from src.utils import excel_file_opening, xlcx_file

tr_list = excel_file_opening(xlcx_file)


def test_find_numbers(number):
    assert json.loads(find_numbers(tr_list))[0]["Описание"] == number["Описание"]
