"""
Панель настроек анализа.
"""

import customtkinter as ctk


class SettingsPanel(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, corner_radius=12)

        self.grid_columnconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):

        # -------------------------------------------------
        # Заголовок
        # -------------------------------------------------

        self.title = ctk.CTkLabel(
            self,
            text="⚙ Настройки анализа",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=18,
                weight="bold"
            )
        )

        self.title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=(15, 20)
        )

        # -------------------------------------------------
        # Поле группировки
        # -------------------------------------------------

        self.group_label = ctk.CTkLabel(
            self,
            text="Поле группировки:"
        )

        self.group_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=(20, 10),
            pady=5
        )

        self.group_combobox = ctk.CTkComboBox(
            self,
            values=["Категория"]
        )

        self.group_combobox.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=(0, 20),
            pady=5
        )

        self.group_combobox.set("Категория")

        # -------------------------------------------------
        # Поле значения
        # -------------------------------------------------

        self.value_label = ctk.CTkLabel(
            self,
            text="Поле значения:"
        )

        self.value_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=(20, 10),
            pady=5
        )

        self.value_combobox = ctk.CTkComboBox(
            self,
            values=["Сумма"]
        )

        self.value_combobox.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=(0, 20),
            pady=5
        )

        self.value_combobox.set("Сумма")

        # -------------------------------------------------
        # Поле сортировки
        # -------------------------------------------------

        self.sort_label = ctk.CTkLabel(
            self,
            text="Сортировать по:"
        )

        self.sort_label.grid(
            row=3,
            column=0,
            sticky="w",
            padx=(20, 10),
            pady=5
        )

        self.sort_combobox = ctk.CTkComboBox(
            self,
            values=[
                "Группа",
                "Количество",
                "Сумма",
                "Среднее",
                "Минимум",
                "Максимум"
            ]
        )

        self.sort_combobox.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=(0, 20),
            pady=5
        )

        self.sort_combobox.set("Группа")

        # -------------------------------------------------
        # Тип диаграммы
        # -------------------------------------------------

        self.chart_label = ctk.CTkLabel(
            self,
            text="Тип диаграммы:"
        )

        self.chart_label.grid(
            row=4,
            column=0,
            sticky="w",
            padx=(20, 10),
            pady=5
        )

        self.chart_combobox = ctk.CTkComboBox(
            self,
            values=[
                "Горизонтальная",
                "Процентная"
            ]
        )

        self.chart_combobox.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=(0, 20),
            pady=5
        )

        self.chart_combobox.set("Горизонтальная")

        # -------------------------------------------------
        # Сортировка по убыванию
        # -------------------------------------------------

        self.reverse_checkbox = ctk.CTkCheckBox(
            self,
            text="Сортировка по убыванию"
        )

        self.reverse_checkbox.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=(5, 10)
        )

        # -------------------------------------------------
        # Построить отчет
        # -------------------------------------------------

        self.build_button = ctk.CTkButton(
            self,
            text="Построить отчет"
        )

        self.build_button.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=20
        )

        # -------------------------------------------------
        # Экспорт
        # -------------------------------------------------

        self.export_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.export_frame.grid(
            row=7,
            column=0,
            columnspan=2,
            pady=(0, 20)
        )

        self.export_csv_button = ctk.CTkButton(
            self.export_frame,
            text="Экспорт CSV",
            width=150
        )

        self.export_csv_button.pack(
            side="left",
            padx=5
        )

        self.export_txt_button = ctk.CTkButton(
            self.export_frame,
            text="Экспорт TXT",
            width=150
        )

        self.export_txt_button.pack(
            side="left",
            padx=5
        )

    # ==============================
    # Методы получения настроек
    # ==============================

    def get_group_field(self):
        return self.group_combobox.get()

    def get_value_field(self):
        return self.value_combobox.get()

    def get_sort_field(self):
        return self.sort_combobox.get()

    def get_chart_type(self):
        return self.chart_combobox.get()

    def get_reverse_sort(self):
        return self.reverse_checkbox.get() == 1