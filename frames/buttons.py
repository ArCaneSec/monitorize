# import settings
# from bases.button import Button
# from bases.frame import Page


# class DisplayButton(Button):
#     def __init__(self, target_page: Page, *args, **kwargs):
#         self.target_page = target_page
#         super().__init__(
#             command=self.command,
#             target_page=self.target_page,
#             text=self.target_page.__class__.__name__,
#             *args,
#             **kwargs,
#         )

#     def command(self):
#         if self.target_page != self.master:
#             self.target_page.display()

#         settings.DEBUG_MODE and print(
#             f"{self.target_page.__class__.__name__} displayed."
#         )
#         self.master.change_active_page(self.target_page)
