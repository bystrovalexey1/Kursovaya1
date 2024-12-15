from src.reports import spending_by_category
from src.utils import excel_file_opening

result_read = excel_file_opening("./data/operations.xlsx")
result_spend = spending_by_category(result_read, "Косметика", date="17.12.2021")


def test_spending_by_category(category):
    assert spending_by_category(result_read, "Косметика", date="17.12.2021") == result_spend


def test_reports():
    assert spending_by_category(result_read, "Переводы") == []
    assert spending_by_category(result_read, "Красота") == []
    assert spending_by_category(result_read, "sdfsf") == []
