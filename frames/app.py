import customtkinter as ctk

import settings
from bases.frame import Page

from .buttons import DisplayPageButton
from .dashboard.page import Dashboard

page_with_display_button = dict[Page, DisplayPageButton]
pages_with_display_button = list[page_with_display_button]


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Monitorize")
        self.geometry(settings.RESOLUTION)
        self.pages: page_with_display_button = {}

    def create_page(self, pages: pages_with_display_button):
        for page_dicts in pages:
            for page, button in page_dicts.items():
                self.pages[page] = button
                button.pack()


app = App()

dashboard = Dashboard(app)
app.create_page(
    [dict(dashboard=DisplayPageButton(master=app, target_page=dashboard))]
)
