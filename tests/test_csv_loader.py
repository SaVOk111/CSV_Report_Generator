"""
Автоматическое тестирование CSVLoader.
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



def test_csv_loader():

    file_path = "data/sales_june_part1.csv"


    rows = CSVLoader.load(
        file_path
    )


    assert rows is not None

    assert len(rows) > 0

    assert isinstance(
        rows,
        list
    )


    assert isinstance(
        rows[0],
        dict
    )



def test_csv_loader_file_not_found():

    try:

        CSVLoader.load(
            "data/not_exists.csv"
        )

        assert False


    except FileNotFoundError:

        assert True