from typing import Union

import customtkinter as ctk

import settings

from .button import Button, DisplayButton


class Page(ctk.CTkFrame):
    def __init__(
        self,
        master: Union[ctk.CTk, ctk.CTkFrame],
        buttons: dict[str, Button],
        width: int = 555,
        height: int = 555,
    ) -> None:
        self.master = master
        self.buttons = buttons
        self.width = width
        self.height = height
        self.display_button = None

        super().__init__(
            self.master, width, self.height, fg_color="green", bg_color="red"
        )

        self._set_display_button()
        self._initialize_buttons()

    def _set_display_button(self):
        self.display_button = DisplayButton(
            target_page=self, master=self.master
        )

    def _initialize_buttons(self) -> None:
        for button in self.buttons.values():
            button = button(master=self)

    def display(self) -> None:
        self.pack()
        for button in self.buttons.values():
            button.pack(self)

    def hide(self) -> None:
        self.pack_forget()

    def set_display_button(self, button: ctk.CTkButton) -> None:
        self.display_button = button
