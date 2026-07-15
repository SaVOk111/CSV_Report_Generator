"""
Автоматическое тестирование Exporter.
"""

import os
import tempfile

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


from core.exporter import Exporter



def test_export_csv():

    report = [

        {
            "Группа": "Продукты",
            "Количество": 2,
            "Сумма": 300,
            "Среднее": 150,
            "Медиана": 150,
            "Минимум": 100,
            "Максимум": 200
        }

    ]


    with tempfile.TemporaryDirectory() as folder:

        file_path = os.path.join(
            folder,
            "test_report.csv"
        )


        Exporter.save_csv(
            report,
            file_path
        )


        assert os.path.exists(file_path)



def test_export_txt():

    report = [

        {
            "Группа": "Продукты",
            "Количество": 2,
            "Сумма": 300,
            "Среднее": 150,
            "Медиана": 150,
            "Минимум": 100,
            "Максимум": 200
        }

    ]


    with tempfile.TemporaryDirectory() as folder:

        file_path = os.path.join(
            folder,
            "test_report.txt"
        )


        Exporter.save_txt(
            report,
            file_path
        )


        assert os.path.exists(file_path)


        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()


        assert "ASCII" in content

        assert "Продукты" in content