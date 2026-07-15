from src.core.sorter import Sorter


def test_sort_ascending():
    data = [
        {"Группа": "Транспорт", "Сумма": 730},
        {"Группа": "Продукты", "Сумма": 2230},
        {"Группа": "Кафе", "Сумма": 860},
    ]

    result = Sorter.sort(data, "Сумма")

    assert result[0]["Сумма"] == 730
    assert result[1]["Сумма"] == 860
    assert result[2]["Сумма"] == 2230


def test_sort_descending():
    data = [
        {"Группа": "Транспорт", "Сумма": 730},
        {"Группа": "Продукты", "Сумма": 2230},
        {"Группа": "Кафе", "Сумма": 860},
    ]

    result = Sorter.sort(
        data,
        "Сумма",
        reverse=True
    )

    assert result[0]["Сумма"] == 2230
    assert result[1]["Сумма"] == 860
    assert result[2]["Сумма"] == 730


def test_sort_invalid_data():
    try:
        Sorter.sort("invalid", "Сумма")
        assert False
    except TypeError:
        assert True