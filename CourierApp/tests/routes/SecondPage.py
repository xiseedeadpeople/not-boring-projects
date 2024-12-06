import flet as ft
from flet_model import Model


class Secondp(Model):
    route = 'home'
    controls = [ft.Text('2nd here here', size=20), ft.ElevatedButton('go gome', on_click='about_to')]

    def about_to(self, e):
        self.page.go('home')
