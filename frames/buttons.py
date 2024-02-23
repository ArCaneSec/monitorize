import customtkinter as ctk

from bases.frame import Page


class DisplayPageButton(ctk.CTkButton):

    def __init__(
        self,
        master: ctk.CTk,
        target_page: Page,
        width: int = 140,
        height: int = 28,
    ):
        self.master = master
        self.target_page = target_page
        self.width = width
        self.height = height

        super().__init__(
            self.master,
            self.width,
            self.height,
            text="red button",
            fg_color="red",
            command=self.command,
        )

    def command(self):
        self.target_page.display()
