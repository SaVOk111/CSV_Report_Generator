"""
Header приложения.
"""

import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        # ==========================
        # Название программы
        # ==========================

        self.title = ctk.CTkLabel(
            self,
            text="CSV Report Generator",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=30,
                weight="bold"
            )
        )

        self.title.grid(
            row=0,
            column=0,
            pady=(20, 0)
        )

        # ==========================
        # Подзаголовок
        # ==========================

        self.subtitle = ctk.CTkLabel(
            self,
            text="Генератор сводных отчетов из CSV-файлов",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=15
            ),
            text_color="gray60"
        )

        self.subtitle.grid(
            row=1,
            column=0,
            pady=(5, 15)
        )

        # ==========================
        # Разделительная линия
        # ==========================

        self.separator = ctk.CTkFrame(
            self,
            height=2,
            corner_radius=0
        )

        self.separator.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20
        )