from dataclasses import dataclass
from typing import Union

import customtkinter as ctk


@dataclass
class RedButton(ctk.CTkButton):
    master: Union[ctk.CTk, ctk.CTkFrame]
    width: int = 140
    height: int = 28

    def __post_init__(self):
        super().__init__(
            self.master,
            self.width,
            self.height,
            text="red button",
            fg_color="red",
        )
