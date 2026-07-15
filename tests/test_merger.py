"""
Автоматическое тестирование Merger.
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



def test_merger():

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


    assert len(merged) == (
        len(data1)
        +
        len(data2)
    )


    assert isinstance(
        merged[0],
        dict
    )