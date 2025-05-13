from pathlib import Path
import pytest
from main import read_csv_manually, calculate_payout


@pytest.fixture
def csv_basic(tmp_path):
    file = tmp_path / "basic.csv"
    file.write_text("id,email,name,department,hours_worked,rate\n"
                    "1,a@x.com,Alice,HR,160,50\n"
                    "2,b@x.com,Bob,IT,150,40")
    return file

@pytest.fixture
def csv_with_salary(tmp_path):
    file = tmp_path / "with_salary.csv"
    file.write_text("email,name,department,hours_worked,salary,id\n"
                    "x@y.com,Carol,Sales,170,60,3")
    return file

def test_read_csv_basic(csv_basic):
    records = read_csv_manually(csv_basic)
    assert len(records) == 2
    assert records[0]["name"] == "Alice"
    assert records[1]["hours_worked"] == "150"

def test_read_csv_with_salary(csv_with_salary):
    records = read_csv_manually(csv_with_salary)
    assert records[0]["department"] == "Sales"
    assert records[0]["salary"] == "60"

def test_calculate_payout_with_rate():
    result = calculate_payout(160, 50)
    assert result == 8000

def test_calculate_payout_with_hourly_rate():
    result = calculate_payout(150, 40)
    assert result == 6000
