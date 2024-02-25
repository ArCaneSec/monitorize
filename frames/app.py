"""
This module contains the main app (master frame) and initializations
of all pages and their display buttons

Any newly created page must be initialized in this module and then
included in app.create_page([]) list.
"""

from typing import Optional, Union

import customtkinter as ctk

import settings
from bases.button import DisplayButton
from bases.frame import Page

from .dashboard.buttons import exported_buttons
from .dashboard.page import Dashboard


class App(ctk.CTk):
    """
    Master frame which contains all other pages within it.

    Attributes:
        pages: dict of pages.
        active_page: the page which is currently being showed.
        display_button: display button for master frame.
    """

    def __init__(self):
        super().__init__()
        self.title("Monitorize")
        self.geometry(settings.RESOLUTION)
        self.pages: dict[str, Page] = {}
        self.active_page: Union[self, Page] = self
        self.display_button: Optional[DisplayButton] = None
        self._set_display_button()

    def _set_display_button(self):
        """
        Initializing master's display button and packing it.
        """

        self.display_button = DisplayButton(target_page=self, master=self)
        self.display_button.pack()
        self.display_button.configure(state=ctk.DISABLED)

    def create_page(self, pages: list[Page]):
        """
        Adding all pages into 'self.page' and packing their display button.
        """

        for page in pages:
            self.pages[page.__class__.__name__] = page
            page.display_button.pack()

    def _disable_current_page(self):
        """
        Unpacking currenct active page and then enabling it's display
        button so user can reactivate it again.

        If active page is the master itself, it doesn't required to unpack
        it, so we just enabling its display button.
        """

        self.active_page.display_button.configure(state=ctk.NORMAL)
        if self.active_page.__class__.__name__ != self.__class__.__name__:
            self.active_page.pack_forget()

    def change_active_page(self, page: Page):
        """
        Changing active page from current one to the 'page'.
        Then disabling its display button.
        """

        self._disable_current_page()
        self.active_page = page
        page.display_button.configure(state=ctk.DISABLED)


app = App()

dashboard = Dashboard(master=app, buttons=exported_buttons)

app.create_page([dashboard])
