from dataclasses import dataclass
from typing import Protocol, Union

import customtkinter as ctk


@dataclass
class Page(Protocol):
    master: Union[ctk.CTk, ctk.CTkFrame]
    buttons: dict[str, ctk.CTkButton]

    def __post_init__(self) -> None:
        pass

    def display(self) -> None:
        pass
