# tests/test_filter.py
import pytest
import tempfile
from csv_processor.commands.filter import run_filter, parse_filter_condition, compare

@pytest.mark.parametrize("condition,expected", [
    ("price>500", ("price", ">", "500")),
    ("rating=4.5", ("rating", "=", "4.5")),
    ("name<iphone", ("name", "<", "iphone")),
])
def test_parse_filter_condition(condition, expected):
    assert parse_filter_condition(condition) == expected

@pytest.mark.parametrize("val,op,target,expected", [
    ("500", ">", "400", True),
    ("apple", "=", "apple", True),
    ("300", "<", "100", False),
    ("abc", "!=", "xyz", True),
    ("123", ">=", "123", True),
])
def test_compare(val, op, target, expected):
    assert compare(val, op, target) == expected

@pytest.fixture
def sample_csv():
    content = """name,brand,price,rating
iphone 15 pro,apple,999,4.9
redmi note 12,xiaomi,199,4.6
galaxy s23 ultra,samsung,1199,4.8
"""
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as f:
        f.write(content)
        return f.name

def test_run_filter_price_gt(sample_csv, capsys):
    run_filter(sample_csv, "price>1000")
    output = capsys.readouterr().out
    assert "galaxy s23 ultra" in output
    assert "redmi note" not in output

def test_run_filter_rating_eq(sample_csv, capsys):
    run_filter(sample_csv, "rating=4.6")
    output = capsys.readouterr().out
    assert "redmi note 12" in output

def test_invalid_column(sample_csv):
    with pytest.raises(ValueError, match="Колонки 'weight' нет в CSV."):
        run_filter(sample_csv, "weight>100")
