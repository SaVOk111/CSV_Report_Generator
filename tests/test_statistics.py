"""
Автоматическое тестирование StatisticsEngine.
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


from core.statistics_engine import StatisticsEngine



def test_statistics_calculation():

    groups = {

        "Продукты": [

            {
                "Сумма": "10"
            },

            {
                "Сумма": "20"
            },

            {
                "Сумма": "30"
            }

        ]

    }


    report = StatisticsEngine.calculate(
        groups,
        "Сумма"
    )


    result = report[0]


    assert result["Группа"] == "Продукты"

    assert result["Количество"] == 3

    assert result["Сумма"] == 60

    assert result["Среднее"] == 20

    assert result["Медиана"] == 20

    assert result["Минимум"] == 10

    assert result["Максимум"] == 30