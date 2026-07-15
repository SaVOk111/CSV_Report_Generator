"""
Модуль объединения данных из нескольких CSV-файлов.
"""


class Merger:
    """
    Класс для объединения данных,
    полученных из нескольких CSV-файлов.
    """

    @staticmethod
    def merge(data_sets):
        """
        Объединяет несколько списков строк
        в один общий список.

        Parameters
        ----------
        data_sets : list
            Список наборов данных.

        Returns
        -------
        list
            Общий список строк.
        """

        merged_data = []

        for data in data_sets:

            if not data:
                continue

            merged_data.extend(data)

        return merged_data