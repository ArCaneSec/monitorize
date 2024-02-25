import customtkinter as ctk
from bases.button import Button

from bases.frame import Page

from .buttons import RedButton


class Dashboard(Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
