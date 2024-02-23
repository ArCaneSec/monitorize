import customtkinter as ctk

import settings

from .buttons import RedButton


class Dashboard(ctk.CTkFrame):
    def __init__(
        self, main_window: ctk.CTk, buttons: dict[str, ctk.CTkButton] = {}
    ):
        self.main_window = main_window
        self.buttons = buttons
        super().__init__(self.main_window, settings.WIDTH, settings.HEIGHT)

    def display(self) -> None:
        self.pack()
        RedButton(self, 100, 100).pack()
