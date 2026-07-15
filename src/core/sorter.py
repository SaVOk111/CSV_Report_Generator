"""
Модуль сортировки результатов.
"""


class Sorter:

    @staticmethod
    def sort(data, field, reverse=False):
        """
        Сортирует список словарей.

        Parameters
        ----------
        data : list
            Данные для сортировки.

        field : str
            Поле сортировки.

        reverse : bool
            Обратный порядок.

        Returns
        -------
        list
            Отсортированный список.
        """

        if not isinstance(data, list):
            raise TypeError("Ожидался список.")

        return sorted(
            data,
            key=lambda row: row[field],
            reverse=reverse
        )