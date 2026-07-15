"""
Интеграционное тестирование формирования отчета.
"""

import os
import sys


sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)


from core.csv_loader import CSVLoader
from core.merger import Merger
from core.groupby_engine import GroupByEngine
from core.statistics_engine import StatisticsEngine



def test_report_generation():

    data1 = CSVLoader.load(
        "data/sales_june_part1.csv"
    )

    data2 = CSVLoader.load(
        "data/sales_june_part2.csv"
    )


    merged = Merger.merge(
        [
            data1,
            data2
        ]
    )


    groups = GroupByEngine.group_by(
        merged,
        "Категория"
    )


    report = StatisticsEngine.calculate(
        groups,
        "Сумма"
    )


    assert len(report) > 0


    first = report[0]


    assert "Группа" in first

    assert "Количество" in first

    assert "Сумма" in first

    assert "Среднее" in first

    assert "Медиана" in first

    assert "Минимум" in first

    assert "Максимум" in first