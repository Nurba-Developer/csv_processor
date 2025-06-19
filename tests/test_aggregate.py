# tests/test_aggregate.py
import pytest
import tempfile
from csv_processor.commands.aggregate import run_aggregate


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


@pytest.mark.parametrize("command,expected", [
    ("price avg", "799.0"),
    ("rating min", "4.6"),
    ("price max", "1199.0"),
])
def test_run_aggregate_valid(sample_csv, command, expected, capsys):
    run_aggregate(sample_csv, command)
    output = capsys.readouterr().out
    assert expected in output


def test_invalid_function(sample_csv):
    with pytest.raises(ValueError, match="Unsupported function"):
        run_aggregate(sample_csv, "price sum")


def test_invalid_column(sample_csv):
    with pytest.raises(ValueError, match="Column 'weight' not found"):
        run_aggregate(sample_csv, "weight max")


def test_non_numeric_column(sample_csv):
    with pytest.raises(ValueError, match="must contain numeric values only"):
        run_aggregate(sample_csv, "brand avg")
