"""
Хранение текущего состояния приложения.
"""


class ApplicationState:

    def __init__(self):

        # Пути к выбранным CSV
        self.files = []

        # Данные каждого CSV
        self.loaded_data = []

        # Объединённые данные
        self.merged_data = []

        # Группы после GroupBy
        self.groups = {}

        # Итоговый отчёт
        self.report = []