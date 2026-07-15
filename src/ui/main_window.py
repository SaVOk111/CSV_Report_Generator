"""
Главное окно приложения.

Отвечает за создание главного окна и
размещение основных компонентов интерфейса.
"""

import customtkinter as ctk

from components.header import Header
from components.file_panel import FilePanel
from components.settings_panel import SettingsPanel
from components.analysis_panel import AnalysisPanel
from components.status_bar import StatusBar
from core.csv_loader import CSVLoader
from core.merger import Merger
from core.groupby_engine import GroupByEngine
from core.statistics_engine import StatisticsEngine
from core.sorter import Sorter
from core.exporter import Exporter
from core.ascii_chart_builder import ASCIIChartBuilder
from utils.logger import AppLogger
from tkinter import filedialog, messagebox, ttk



class MainWindow:

    def __init__(self):

        # ==========================================
        # Настройка внешнего вида приложения
        # ==========================================

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # ==========================================
        # Создание главного окна
        # ==========================================

        self.root = ctk.CTk()

        self.root.title("CSV Report Generator")

        self.root.geometry("1400x900")

        self.root.minsize(1200, 800)

        # Главное окно должно растягиваться
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.current_report = []

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):

        # ==========================================
        # Header
        # ==========================================

        self.header = Header(self.root)

        self.header.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        # ==========================================
        # Главный контейнер
        # ==========================================

        self.main_frame = ctk.CTkFrame(
            self.root,
            corner_radius=12
        )

        self.main_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=0)

        # ==========================================
        # Верхняя панель
        # ==========================================

        self.top_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.top_frame.grid(
            row=0,
            column=0,
            sticky="new",
            padx=15,
            pady=(10, 5)
        )


        self.top_frame.grid_columnconfigure(0, weight=2)
        self.top_frame.grid_columnconfigure(1, weight=3)

        # ==========================================
        # Панели
        # ==========================================

        self.file_panel = FilePanel(self.top_frame)
        self.settings_panel = SettingsPanel(self.top_frame)
        self.analysis_panel = AnalysisPanel(self.main_frame)
        self.status_bar = StatusBar(self.main_frame)

        self.settings_panel.build_button.configure(
            command=self.build_report
        )

        self.settings_panel.chart_combobox.configure(
            command=self.update_chart
        )

        self.settings_panel.export_csv_button.configure(
            command=self.export_csv
        )

        self.settings_panel.export_txt_button.configure(
            command=self.export_txt
        )

        # ==========================================
        # Размещение
        # ==========================================

        self.file_panel.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        self.settings_panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        self.analysis_panel.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=15,
            pady=(5, 10)
        )

        self.status_bar.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 10)
        )

    def build_report(self):
        """
        Формирует сводный отчет.
        """

        files = self.file_panel.get_files()

        if not files:
            AppLogger.warning("Попытка построить отчет без выбранных файлов.")

            messagebox.showwarning(
                "Внимание",
                "Сначала выберите CSV-файлы."
            )

            return

        loaded_data = []

        for file in files:

            try:

                loaded_data.append(
                    CSVLoader.load(file)
                )

            except Exception as error:

                AppLogger.error(
                    f"Ошибка загрузки файла {file}: {error}"
                )

                messagebox.showerror(
                    "Ошибка загрузки CSV",
                    str(error)
                )

                return
        try:

            merged = Merger.merge(loaded_data)


            if not merged:
                raise ValueError(
                    "После объединения CSV нет данных для анализа."
                )


            groups = GroupByEngine.group_by(
                merged,
                self.settings_panel.get_group_field()
            )


            report = StatisticsEngine.calculate(
                groups,
                self.settings_panel.get_value_field()
            )


            report = Sorter.sort(
                report,
                self.settings_panel.get_sort_field(),
                self.settings_panel.get_reverse_sort()
            )


        except Exception as error:

            AppLogger.error(
                f"Ошибка формирования отчета: {error}"
            )


            messagebox.showerror(
                "Ошибка анализа",
                str(error)
            )


            return
        
        self.current_report = report


        try:

            self.analysis_panel.result_panel.show_report(report)

            self.update_chart()


        except Exception as error:

            AppLogger.error(
                f"Ошибка построения диаграммы: {error}"
            )


            messagebox.showerror(
                "Ошибка диаграммы",
                str(error)
            )


            return


        AppLogger.info(
            f"Построен отчет ({len(report)} групп)."
        )  
    
    def export_csv(self):
        """
        Экспортирует отчет в CSV.
        """

        if not self.current_report:

            messagebox.showwarning(
                "Внимание",
                "Сначала сформируйте отчет."
            )

            return

        file_path = filedialog.asksaveasfilename(

            title="Сохранить CSV",

            defaultextension=".csv",

            filetypes=[
                ("CSV файл", "*.csv")
            ]
        )

        if not file_path:
            return

        try:

            Exporter.save_csv(
                self.current_report,
                file_path
            )

            messagebox.showinfo(
                "Успех",
                "CSV успешно сохранен."
            )


        except Exception as error:

            AppLogger.error(
                f"Ошибка экспорта CSV через интерфейс: {error}"
            )

            messagebox.showerror(
                "Ошибка экспорта",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Ошибка",
                str(error)
            )

            AppLogger.error(
                f"Ошибка экспорта CSV: {error}"
            )
        
    def export_txt(self):
        """
        Экспортирует отчет в TXT.
        """

        if not self.current_report:

            messagebox.showwarning(
                "Внимание",
                "Сначала сформируйте отчет."
            )

            return

        file_path = filedialog.asksaveasfilename(

            title="Сохранить TXT",

            defaultextension=".txt",

            filetypes=[
                ("Текстовый файл", "*.txt")
            ]
        )

        if not file_path:
            return

        try:

            Exporter.save_txt(
                self.current_report,
                file_path
            )

            messagebox.showinfo(
                "Успех",
                "TXT успешно сохранен."
            )


        except Exception as error:

            AppLogger.error(
                f"Ошибка экспорта TXT через интерфейс: {error}"
            )

            messagebox.showerror(
                "Ошибка экспорта",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Ошибка",
                str(error)
            )

            AppLogger.error(
                f"Ошибка экспорта TXT: {error}"
            )
    def update_chart(self, choice=None):
        """
        Перестроить диаграмму по текущему отчету.
        """

        if not self.current_report:
            return

        self.current_figure = ASCIIChartBuilder.build(
            self.current_report,
            self.settings_panel.get_chart_type()
        )

        self.analysis_panel.chart_panel.show_chart(
            self.current_figure
        )

        AppLogger.info(
            f"Изменен вид диаграммы: {self.settings_panel.get_chart_type()}"
        )

    def run(self):
        self.root.mainloop()