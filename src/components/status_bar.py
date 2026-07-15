import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            height=28,
            corner_radius=0
        )

        self.grid_propagate(False)

        self.label = ctk.CTkLabel(
            self,
            text="Готов к работе",
            anchor="w"
        )

        self.label.pack(
            side="left",
            padx=10
        )