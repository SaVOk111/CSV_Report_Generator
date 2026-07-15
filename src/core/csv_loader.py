"""
Модуль загрузки CSV-файлов.
"""

import csv
import os

from utils.logger import AppLogger


class CSVLoader:
    """
    Класс для чтения CSV-файлов.
    """

    @staticmethod
    def load(file_path):
        """
        Загружает CSV-файл и возвращает список словарей.

        Parameters
        ----------
        file_path : str
            Путь к CSV-файлу.

        Returns
        -------
        list
            Список строк CSV.
        """

        if not os.path.exists(file_path):

            AppLogger.error(
                f"Файл не найден: {file_path}"
            )

            raise FileNotFoundError(
                f"Файл не найден: {file_path}"
            )


        try:

            with open(
                file_path,
                "r",
                encoding="utf-8-sig",
                newline=""
            ) as file:


                sample = file.read(2048)

                file.seek(0)


                if not sample.strip():

                    AppLogger.warning(
                        f"Пустой CSV-файл: {file_path}"
                    )

                    raise ValueError(
                        "CSV-файл пуст."
                    )


                try:

                    dialect = csv.Sniffer().sniff(
                        sample,
                        delimiters=";,"
                    )

                except csv.Error:

                    dialect = csv.excel



                reader = csv.DictReader(
                    file,
                    dialect=dialect
                )


                if not reader.fieldnames:

                    AppLogger.error(
                        f"В файле отсутствуют заголовки: {file_path}"
                    )

                    raise ValueError(
                        "CSV-файл не содержит заголовков."
                    )


                data = list(reader)


                if not data:

                    AppLogger.warning(
                        f"CSV-файл не содержит данных: {file_path}"
                    )

                    raise ValueError(
                        "CSV-файл не содержит данных."
                    )


                AppLogger.info(
                    f"CSV загружен: {file_path} "
                    f"({len(data)} строк)"
                )


                return data


        except UnicodeDecodeError:

            AppLogger.error(
                f"Ошибка кодировки CSV: {file_path}"
            )

            raise ValueError(
                "Не удалось прочитать CSV. Проверьте кодировку файла."
            )


        except Exception as error:

            AppLogger.error(
                f"Ошибка загрузки CSV {file_path}: {error}"
            )

            raise