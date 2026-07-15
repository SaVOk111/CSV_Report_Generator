"""
Контроллер приложения.

Связывает интерфейс и алгоритмическое ядро.
"""

from tkinter import filedialog


class AppController:

    def __init__(self):
        pass

    def select_csv_file(self):
        """
        Открывает окно выбора CSV-файла.
        """

        filename = filedialog.askopenfilename(

            title="Выберите CSV-файл",

            filetypes=[
                ("CSV files", "*.csv"),
                ("Все файлы", "*.*")
            ]
        )

        return filename