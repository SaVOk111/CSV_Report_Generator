"""
Модуль вычисления статистики по группам.
"""

from statistics import median

class StatisticsEngine:

    @staticmethod
    def calculate(groups, value_field):
        """
        Вычисляет статистику для каждой группы.

        Parameters
        ----------
        groups : dict
            Словарь групп.

        value_field : str
            Поле, по которому считается статистика.

        Returns
        -------
        list
            Список словарей с результатами.
        """

        result = []

        for group_name, rows in groups.items():

            values = []

            for row in rows:

                try:
                    values.append(float(row[value_field]))
                except (ValueError, KeyError):
                    continue

            if not values:
                continue

            report = {

                "Группа": group_name,

                "Количество": len(values),

                "Сумма": sum(values),

                "Среднее": sum(values) / len(values),
                
                "Медиана": median(values),

                "Минимум": min(values),

                "Максимум": max(values)

            }

            result.append(report)

        return result