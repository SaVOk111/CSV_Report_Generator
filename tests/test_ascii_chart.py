from src.core.ascii_chart_builder import ASCIIChartBuilder


def get_report():
    return [
        {
            "Группа": "Продукты",
            "Сумма": 2230
        },
        {
            "Группа": "Транспорт",
            "Сумма": 730
        },
        {
            "Группа": "Кафе",
            "Сумма": 860
        },
    ]


def test_horizontal_chart():
    result = ASCIIChartBuilder.build(
        get_report(),
        "Горизонтальная"
    )

    assert "ASCII REPORT CHART" in result
    assert "Продукты" in result
    assert "Транспорт" in result
    assert "2230.00" in result
    assert "#" in result


def test_percentage_chart():
    result = ASCIIChartBuilder.build(
        get_report(),
        "Процентная"
    )

    assert "ASCII PERCENTAGE CHART" in result
    assert "Продукты" in result
    assert "%" in result
    assert "Итого" in result


def test_empty_report():
    result = ASCIIChartBuilder.build(
        [],
        "Горизонтальная"
    )

    assert result == (
        "Нет данных для построения диаграммы."
    )


def test_unknown_chart_type():
    result = ASCIIChartBuilder.build(
        get_report(),
        "Неизвестная"
    )

    assert result == "Неизвестный тип диаграммы."