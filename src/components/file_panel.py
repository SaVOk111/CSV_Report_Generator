"""
Панель загрузки CSV-файлов.
"""

import os
import customtkinter as ctk
from tkinter import filedialog


class FilePanel(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=12
        )

        self.grid_columnconfigure(0, weight=1)

        self.files = []

        self.create_widgets()

    def create_widgets(self):

        # ======================================
        # Заголовок
        # ======================================

        self.title = ctk.CTkLabel(
            self,
            text="📂 Загрузка CSV-файлов",
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
            pady=(12, 8)
        )

        # ======================================
        # Кнопки
        # ======================================

        self.button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.button_frame.grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=(0, 8)
        )

        self.add_button = ctk.CTkButton(
            self.button_frame,
            text="+ Добавить CSV",
            width=150,
            command=self.add_csv
        )

        self.add_button.pack(
            side="left",
            padx=(0, 8)
        )

        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="Очистить список",
            width=150,
            command=self.clear_files
        )

        self.clear_button.pack(
            side="left"
        )

        # ======================================
        # Список файлов
        # ======================================

        self.files_frame = ctk.CTkFrame(self)

        self.files_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 8)
        )

        self.files_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.empty_label = ctk.CTkLabel(
            self.files_frame,
            text="Пока файлов нет",
            text_color="gray60"
        )

        self.empty_label.grid(
            row=0,
            column=0,
            pady=15
        )

        # ======================================
        # Счетчик
        # ======================================

        self.counter_label = ctk.CTkLabel(
            self,
            text="Всего файлов: 0"
        )

        self.counter_label.grid(
            row=3,
            column=0,
            sticky="w",
            padx=20,
            pady=(0, 10)
        )

    def add_csv(self):

        filename = filedialog.askopenfilename(
            title="Выберите CSV-файл",
            filetypes=[
                ("CSV files", "*.csv"),
                ("Все файлы", "*.*")
            ]
        )

        if filename:
            self.files.append(filename)
            self.update_file_list()

    def update_file_list(self):

        for widget in self.files_frame.winfo_children():

            if widget != self.empty_label:
                widget.destroy()

        if not self.files:

            self.empty_label.grid()

            self.counter_label.configure(
                text="Всего файлов: 0"
            )

            return

        self.empty_label.grid_remove()

        for index, file in enumerate(self.files):

            label = ctk.CTkLabel(
                self.files_frame,
                text=os.path.basename(file),
                anchor="w"
            )

            label.grid(
                row=index,
                column=0,
                sticky="w",
                padx=10,
                pady=2
            )

        self.counter_label.configure(
            text=f"Всего файлов: {len(self.files)}"
        )

    def clear_files(self):

        self.files.clear()

        self.update_file_list()

    def get_files(self):

        return self.files.copy()