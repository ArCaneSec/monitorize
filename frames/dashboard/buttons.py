from dataclasses import dataclass
from typing import Union

import customtkinter as ctk

from bases.button import Button


@dataclass
class RedButton(Button):
    master: Union[ctk.CTk, ctk.CTkFrame]
    width: int = 555
    height: int = 555

    def __post_init__(self):
        super().__init__(
            self.master,
            self.width,
            self.height,
            text="red button",
            fg_color="red",
        )


exported_buttons: dict[str, Button] = {RedButton.__name__: RedButton}
