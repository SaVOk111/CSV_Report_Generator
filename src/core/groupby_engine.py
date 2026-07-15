"""
Модуль группировки данных.
"""


class GroupByEngine:
    """
    Выполняет группировку записей
    по указанному полю.
    """

    @staticmethod
    def group_by(data, key):

        if not isinstance(data, list):
            raise TypeError("Ожидался список записей.")

        if not data:
            raise ValueError(
                "Нет данных для группировки."
            )

        if not any(key in row for row in data):
            raise ValueError(
                f"Отсутствует поле группировки: {key}"
            )

        groups = {}

        for row in data:

            if key not in row:
                continue

            value = row[key]

            if value is None or str(value).strip() == "":
                continue

            if value not in groups:
                groups[value] = []

            groups[value].append(row)

        if not groups:
            raise ValueError(
                "Не удалось сформировать группы."
            )

        return groups