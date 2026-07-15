"""
Панель отображения результатов.
"""

import customtkinter as ctk
from tkinter import ttk


class ResultPanel(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, corner_radius=12)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):

        # ------------------------------
        # Заголовок панели
        # ------------------------------

        self.title = ctk.CTkLabel(
            self,
            text="📊 Результаты",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=18,
                weight="bold"
            )
        )

        self.title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 10)
        )

        # ------------------------------
        # Таблица
        # ------------------------------

        columns = (
            "Категория",
            "Количество",
            "Сумма",
            "Среднее",
            "Медиана",
            "Минимум",
            "Максимум"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=18
        )

        for column in columns:

            self.tree.heading(column, text=column)

            self.tree.column(
                column,
                anchor="center",
                width=120
            )

        self.tree.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.scrollbar.grid(
            row=1,
            column=1,
            sticky="ns",
            pady=(0, 20)
        )

    def clear_table(self):
        """
        Полностью очищает таблицу.
        """

        for item in self.tree.get_children():
            self.tree.delete(item)
    def show_report(self, report):
        """
        Отображает сводный отчёт в таблице.

        Parameters
        ----------
        report : list
            Список словарей со статистикой.
        """

        self.clear_table()

        for row in report:

            self.tree.insert(
                "",
                "end",
                values=(
                    row["Группа"],
                    row["Количество"],
                    f"{row['Сумма']:.2f}",
                    f"{row['Среднее']:.2f}",
                    f"{row['Медиана']:.2f}",
                    f"{row['Минимум']:.2f}",
                    f"{row['Максимум']:.2f}"
                )
            )