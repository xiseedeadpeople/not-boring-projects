
import flet as ft
from flet_model import Model


class Homepage(Model):
    route = 'home'
    controls = [ft.Text('Homepage here', size=20), ft.ElevatedButton('second_page', on_click='second_page_to')]

    def second_page_to(self, e):
        self.page.go('second_page')
