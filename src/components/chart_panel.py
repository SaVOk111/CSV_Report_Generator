import customtkinter as ctk


class ChartPanel(ctk.CTkFrame):
    """
    Панель отображения ASCII-диаграммы.
    """

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.chart_textbox = ctk.CTkTextbox(
            self,
            font=("Consolas", 13),
            wrap="none"
        )

        self.chart_textbox.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.chart_textbox.insert(
            "1.0",
            "Сначала сформируйте отчет."
        )

        self.chart_textbox.configure(
            state="disabled"
        )

    def show_chart(self, chart):
        """
        Отобразить ASCII-диаграмму.
        """

        self.chart_textbox.configure(state="normal")

        self.chart_textbox.delete(
            "1.0",
            "end"
        )

        self.chart_textbox.insert(
            "1.0",
            chart
        )

        self.chart_textbox.configure(state="disabled")

    def clear(self):
        """
        Очистить панель.
        """

        self.chart_textbox.configure(state="normal")

        self.chart_textbox.delete(
            "1.0",
            "end"
        )

        self.chart_textbox.insert(
            "1.0",
            "Сначала сформируйте отчет."
        )

        self.chart_textbox.configure(state="disabled")