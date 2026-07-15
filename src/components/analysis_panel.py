import customtkinter as ctk

from components.result_panel import ResultPanel
from components.chart_panel import ChartPanel


class AnalysisPanel(ctk.CTkFrame):
    """
    Панель анализа.
    """

    def __init__(self, master):

        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # =====================================
        # Верхняя панель
        # =====================================

        self.toolbar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.toolbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=5,
            pady=(5, 5)
        )

        self.report_button = ctk.CTkButton(
            self.toolbar,
            text="📋 Отчёт",
            width=170
        )

        self.report_button.pack(
            side="left",
            padx=5
        )

        self.chart_button = ctk.CTkButton(
            self.toolbar,
            text="📊 Диаграммы",
            width=170
        )

        self.chart_button.pack(
            side="left",
            padx=5
        )

        # =====================================
        # Таблица
        # =====================================

        self.result_panel = ResultPanel(self)

        self.result_panel.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=5,
            pady=(0, 5)
        )

        # =====================================
        # Диаграмма
        # =====================================

        self.chart_panel = ChartPanel(self)

        self.chart_panel.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=5,
            pady=(0, 5)
        )

        self.chart_panel.grid_remove()

        # =====================================
        # Кнопки
        # =====================================

        self.report_button.configure(
            command=self.show_report
        )

        self.chart_button.configure(
            command=self.show_chart
        )

    def show_report(self):

        self.chart_panel.grid_remove()
        self.result_panel.grid()

    def show_chart(self):

        self.result_panel.grid_remove()
        self.chart_panel.grid()