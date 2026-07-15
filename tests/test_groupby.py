"""
Автоматическое тестирование GroupByEngine.
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


from core.groupby_engine import GroupByEngine



def test_group_by():

    data = [

        {
            "Категория": "Продукты",
            "Сумма": "100"
        },

        {
            "Категория": "Продукты",
            "Сумма": "200"
        },

        {
            "Категория": "Транспорт",
            "Сумма": "50"
        }

    ]


    result = GroupByEngine.group_by(
        data,
        "Категория"
    )


    assert len(result) == 2

    assert len(result["Продукты"]) == 2

    assert len(result["Транспорт"]) == 1



def test_group_by_missing_field():

    data = [

        {
            "Название": "Товар",
            "Сумма": "100"
        }

    ]


    try:

        GroupByEngine.group_by(
            data,
            "Категория"
        )

        assert False


    except ValueError:

        assert True